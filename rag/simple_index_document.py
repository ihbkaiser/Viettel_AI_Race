from openai import OpenAI
from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm.auto import tqdm
from langchain_text_splitters import RecursiveCharacterTextSplitter
from glob import glob
import json

# Configuration
DEFAULT_MODEL = "gpt-4o-mini"
API_KEY = None
SERVER_HOST = "https://openrouter.ai/api"
TEMPERATURE = 0.0
TOP_P = 0.9
MAX_TOKENS = 2048
MARKDOWN_PATH = "data/processed/private_test_data_md/*.md"
OUTPUT_PATH = "data/processed/summary/private_test_data_summary.json"


def get_completion_vllm(
    input_prompt,
    system_prompt=None,
    model=DEFAULT_MODEL,
    temperature=TEMPERATURE,
    top_p=TOP_P,
    max_tokens=MAX_TOKENS,
    server_host=SERVER_HOST,
    api_key=API_KEY,
):
    client = OpenAI(
        api_key=api_key,
        base_url=f"{server_host}/v1",
    )
    messages = []
    if system_prompt is not None:
        messages.append({"role": "system", "content": system_prompt})
    messages.append({"role": "user", "content": input_prompt})
    try:
        response = client.chat.completions.create(
            model=model,
            messages=messages,
            seed=0,
            top_p=top_p,
            temperature=temperature,
            max_tokens=max_tokens,
        )
        return response.choices[0].message.content
    except Exception as e:
        print(e)
        return None


def multi_thread_task_dict(task_dictionary, num_workers=1, show_progress=True):
    final_results = {}
    futures = []

    with ThreadPoolExecutor(max_workers=num_workers) as executor:
        for id_, task in task_dictionary.items():
            futures.append(
                executor.submit(
                    lambda id_=id_, task=task: {"id": id_, "task_result": task()}
                )
            )

        if show_progress:
            with tqdm(total=len(futures)) as pbar:
                for future in as_completed(futures):
                    result = future.result()
                    final_results[result["id"]] = result["task_result"]
                    pbar.update(1)
        else:
            for future in as_completed(futures):
                result = future.result()
                final_results[result["id"]] = result["task_result"]

    return final_results


def parse_json(json_text):
    first = json_text.find("{")
    last = json_text.rfind("}")
    return json.loads(json_text[first:last+1])


def word_count(text):
    return len(text.split())


SUMMARIZE_CHUNK_PROMPT = """
Provide a short, one sentence summary in Vietnamese for this chunk of text. The summary should cover all aspects of the text chunk. Return only the Vietnamse summary without other information.
### Text chunk
{{chunk}}
""".strip()

SUMARIZE_WHOLE_DOCUMENT = """
You will be given a list of summarization for each paragraph in one larger document. Provide a short, one sentence summary in Vietnamese for the whole document based on the summarization from all smaller chunks.
The summary should cover all aspects gathered from text chunks. Return only the Vietnamse summary without other information.

### Summarization of chunks
{{chunk_summarziations}}
""".strip()


def get_summary(document, num_summaries=10, chunk_size=500, chunk_overlap=50):
    def preprocess_document(document):
        return "\n".join(document.split("\n\n"))
        
    document_dict = {}
    text_splitter = RecursiveCharacterTextSplitter(
        length_function=word_count,
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        separators=["\n##"]
    )
    document = preprocess_document(document)
    document_dict['document_content'] = document
    document_dict['chunks'] = []
    chunks = text_splitter.split_text(document)
    for chunk in chunks:
        prompt = SUMMARIZE_CHUNK_PROMPT.replace("{{chunk}}", chunk)
        try:    
            summary = get_completion_vllm(prompt)
            document_dict['chunks'].append({
                "chunk_content": chunk,
                "chunk_summary": summary
            })
        except Exception as e:
            document_dict['chunks'].append({
                "chunk_content": chunk,
                "chunk_summary": None
            })
    chunk_summarizations = "\n\n".join([f"{i}, {chunk}" for i, chunk in enumerate(chunks)])
    try:
        prompt = SUMARIZE_WHOLE_DOCUMENT.replace("{{chunk_summarziations}}", chunk_summarizations)
        document_dict['document_summary'] = get_completion_vllm(prompt)
    except Exception as e:
        document_dict['document_summary'] = None
    return document_dict


def task_summary(data_point):
    summary = get_summary(data_point['document_content'])
    data_point['chunks'] = summary['chunks']
    if not summary['document_summary']:
        data_point['document_summary'] = data_point['chunks'][0]['chunk_summary']
    data_point_index = f"Tóm tắt cho tài liệu {data_point['file_path'].split('/')[-1]}."
    data_point['document_summary'] = data_point_index + " " + summary['document_summary']
    return data_point


def index_documents(markdown_path=MARKDOWN_PATH, output_path=OUTPUT_PATH, num_workers=5):
    file_paths = glob(markdown_path)
    data = []
    for file_path in file_paths:
        with open(file_path) as f:
            data.append({
                "file_path": file_path,
                "document_content": f.read()
            })

    task_dict = {
        i: lambda point=point: task_summary(point)
        for i, point in enumerate(data)
    }
    task_results = multi_thread_task_dict(task_dict, num_workers=num_workers)
    with open(output_path, "w") as f:
        json.dump(list(task_results.values()), f, ensure_ascii=False)
    
    print(f"Indexed {len(task_results)} documents and saved to {output_path}")
    return task_results


if __name__ == "__main__":
    index_documents()