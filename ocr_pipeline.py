from docling.document_converter import DocumentConverter
import pdfplumber
from typing import List, Tuple, Any, Dict
import os
from glob import glob
from tqdm import tqdm

def _reconstruct_text_from_chars(chars, y_line_thresh=2.0, x_gap_factor=0.45):
    """
    Rebuild lines from pdfplumber chars.
    - y_line_thresh: ngưỡng gộp cùng 1 dòng theo |y_mid - y_mid_prev|
    - x_gap_factor:  hệ số * size trung bình để quyết định chèn khoảng trắng
    """
    if not chars:
        return ""

    for c in chars:
        c["y_mid"] = (c["top"] + c["bottom"]) / 2.0

    chars.sort(key=lambda c: (c["y_mid"], c["x0"]))

    lines = []
    cur = [chars[0]]
    for ch in chars[1:]:
        if abs(ch["y_mid"] - cur[-1]["y_mid"]) <= y_line_thresh:
            cur.append(ch)
        else:
            lines.append(cur)
            cur = [ch]
    lines.append(cur)

    out_lines = []
    for line in lines:
        line.sort(key=lambda c: c["x0"])

        sizes = [c.get("size", 10.0) for c in line]
        avg_size = sum(sizes) / len(sizes) if sizes else 10.0
        x_gap_thresh = avg_size * x_gap_factor
        buf = []
        for i, ch in enumerate(line):
            if i == 0:
                buf.append(ch["text"])
            else:
                prev = line[i-1]
                gap = ch["x0"] - prev["x1"]
                if gap > x_gap_thresh:
                    buf.append(" ")
                buf.append(ch["text"])
        s = "".join(buf).strip()
        if s:
            out_lines.append(s)

    return " ".join(out_lines).strip()

def refine_docling_texts_with_pdfplumber(
    pdf_path: str,
    docling_text_items: List[Any],   
) -> List[Tuple[int, str, str]]:
    """
    Duyệt toàn bộ items trong result.document.texts, dùng pdfplumber để refine text theo bbox.
    Trả về list (index, old_text, refined_text). Không sửa in-place để an toàn.
    """
    results = []

    with pdfplumber.open(pdf_path) as pdf:
        for i, item in enumerate(docling_text_items):
            try:

                if not getattr(item, "prov", None):
                    continue

                prov = None
                for p in item.prov:
                    if getattr(p, "bbox", None) and getattr(p, "page_no", None):
                        prov = p
                        break
                if prov is None:
                    continue
                page_no = int(prov.page_no)  
                bbox = prov.bbox             
                l, t, r, b = float(bbox.l), float(bbox.t), float(bbox.r), float(bbox.b)

                page = pdf.pages[page_no - 1]
                H = float(page.height)

                if getattr(page, "rotation", 0) in (90, 180, 270):
                    page = page.rotate(360 - page.rotation)
                    H = float(page.height)

                origin = str(getattr(bbox, "coord_origin", ""))
                if "BOTTOMLEFT" in origin:
                    plumber_bbox = (l, H - t, r, H - b)
                elif "TOPLEFT" in origin:
                    plumber_bbox = (l, t, r, b)
                else:
                    continue  

                cropped = page.crop(plumber_bbox)
                chars = cropped.chars
                if not chars:

                    results.append((i, getattr(item, "text", ""), getattr(item, "text", "")))
                    continue
                refined = _reconstruct_text_from_chars(chars)

                old_text = getattr(item, "text", "")
                results.append((i, old_text, refined))
            except Exception as e:

                results.append((i, getattr(item, "text", ""), getattr(item, "text", "")))
    return results

def refine_docling_table_cells_with_pdfplumber(
    pdf_path: str,
    tables: List[Any],
) -> List[Tuple[int, int, str, str]]:
    """
    Duyệt toàn bộ tables, refine text của từng cell dùng pdfplumber theo bbox.
    Trả về list (table_idx, cell_idx, old_text, refined_text).
    """
    results = []

    with pdfplumber.open(pdf_path) as pdf:
        for table_idx, table in enumerate(tables):
            try:

                if not getattr(table, "prov", None):
                    continue
                prov = None
                for p in table.prov:
                    if getattr(p, "page_no", None):
                        prov = p
                        break
                if prov is None:
                    continue
                page_no = int(prov.page_no)

                if hasattr(table, '_data'):
                    table_data = table._data
                elif hasattr(table, 'data'):
                    table_data = table.data
                else:
                    continue
                cells = getattr(table_data, 'table_cells', [])
                if not cells:
                    continue

                page = pdf.pages[page_no - 1]
                H = float(page.height)

                if getattr(page, "rotation", 0) in (90, 180, 270):
                    page = page.rotate(360 - page.rotation)
                    H = float(page.height)
                for cell_idx, cell in enumerate(cells):
                    try:
                        if not getattr(cell, "bbox", None):
                            continue
                        bbox = cell.bbox
                        l, t, r, b = float(bbox.l), float(bbox.t), float(bbox.r), float(bbox.b)

                        origin = str(getattr(bbox, "coord_origin", ""))
                        if "BOTTOMLEFT" in origin:
                            plumber_bbox = (l, H - t, r, H - b)
                        elif "TOPLEFT" in origin:
                            plumber_bbox = (l, t, r, b)
                        else:
                            continue

                        cropped = page.crop(plumber_bbox)
                        chars = cropped.chars
                        if not chars:
                            results.append((table_idx, cell_idx, getattr(cell, "text", ""), getattr(cell, "text", "")))
                            continue
                        refined = _reconstruct_text_from_chars(chars)
                        old_text = getattr(cell, "text", "")
                        results.append((table_idx, cell_idx, old_text, refined))
                    except Exception as e:
                        results.append((table_idx, cell_idx, getattr(cell, "text", ""), getattr(cell, "text", "")))
            except Exception as e:
                pass  
    return results

def process_pdf_to_markdown(input_path: str, output_dir: str) -> None:
    """
    Process a PDF file using Docling, refine texts and tables with pdfplumber,
    export to Markdown, and save to the specified output directory.
    """

    os.makedirs(output_dir, exist_ok=True)

    converter = DocumentConverter()
    result = converter.convert(input_path)

    texts = result.document.texts
    fixed_texts = refine_docling_texts_with_pdfplumber(
        pdf_path=input_path,
        docling_text_items=texts
    )

    for idx, old, new in fixed_texts:
        if new and new != old:
            try:
                texts[idx].text = new
            except Exception:
                pass

    tables = result.document.tables
    fixed_tables = refine_docling_table_cells_with_pdfplumber(
        pdf_path=input_path,
        tables=tables
    )

    for table_idx, cell_idx, old, new in fixed_tables:
        if new and new != old:
            try:
                table = tables[table_idx]
                if hasattr(table, '_data'):
                    table._data.table_cells[cell_idx].text = new
                elif hasattr(table, 'data'):
                    table.data.table_cells[cell_idx].text = new
            except Exception:
                pass

    markdown = result.document.export_to_markdown()

    output_file = os.path.join(output_dir, os.path.basename(input_path) + ".md")
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(markdown)
    print(f"Markdown saved to {output_file}")
    

if __name__ == "__main__":
    file_paths = glob("input_test_data_final/*.pdf") 
    output_directory = "output_markdown_final"
    for input_pdf in tqdm(file_paths, desc="Processing PDFs"):
        if os.path.exists(os.path.join(output_directory, os.path.basename(input_pdf) + ".md")):
            continue
        process_pdf_to_markdown(input_pdf, output_directory)

