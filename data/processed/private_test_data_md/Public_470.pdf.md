<!-- image -->

## VIETTEL AI RACE

## HƯỚNG DẪN KHAI BÁO QOS CHO THIẾT BỊ TRUYỀN DẪN VIBA

## 1.  Cấu trúc dữ liệu đặc tả dùng cho lưu trữ dữ liệu

Dữ liệu đặc tả dùng cho lưu trữ dữ liệu liên quan đến:

- -  thông tinh hành chính về quá trình số hóa 3D: ngày tháng, thời gian, địa điểm, vật thể, chủng loại, cơ quan quét 3D,…
- -  các dữ liệu bao gồm các tài liệu tạo ra từ các phần mềm quét 3D, phần mềm mô hỉnh, xử lý thông tin, phân tích, xử lý đám mây điểm và hình ảnh 3D. Dữ liệu cũng có thể là tập hợp các trường dữ liệu trong một hệ thống cơ sở dữ liệu;
- -  tập hợp các dữ liệu bao gồm tập hợp các tệp tin (vật lý hoặc ảo), chuỗi các dữ liệu lưu trữ và hệ thống lưu trữ dữ liệu.

Các thuộc tính của dữ liệu đặc tả dùng cho lưu trữ dữ liệu với dữ liệu 3D dữ liệu được thể hiện trong bảng 1 dưới đây:

| Thuộc tính           | Đối chiếu TCVN 7980: 2008                                                  | Đối chiếu AGRMS         |
|----------------------|----------------------------------------------------------------------------|-------------------------|
| 1. Phân loại bề mặt  |                                                                            | Face Category           |
| 2. Phân loại vật thể |                                                                            | Category                |
| 3. Định danh         | Định danh (bổ sung thêm thuộc tính con chuỗi định danh, giá trị định danh) | Identifier              |
| 4. Tiêu đề           | Tiêu đề (tương thích toàn bộ)                                              | Name                    |
| 5. Tác giả           | Tác giả (tương thích toàn bộ)                                              |                         |
| 6. Chủ đề            | Chủ đề (tương thích toàn bộ)                                               | Keyword                 |
| 7. Mô tả             | Mô tả (tương thích toàn bộ)                                                | Description             |
| 8. Ngày              | Ngày tháng (bổ sung thêm thuộc tính con ngày bắt đầu, ngày kết thúc)       | Date Range              |
| 9. Loại bảo mật      | Security Classification                                                    | Security Classification |
| 10. Quyền            | Quyền  (bổ  sung  thêm thuộc tính con kiểu quyền, trạng thái quyền)        | Rights                  |

TD004

Lần ban hành: 1

<!-- image -->

TD004

Lần ban hành: 1

## VIETTEL AI RACE

## HƯỚNG DẪN KHAI BÁO QOS CHO THIẾT BỊ TRUYỀN DẪN VIBA

| 11. Ngôn ngữ            | Ngôn  ngữ  (tương  thích toàn bộ)                                                                                | Language      |
|-------------------------|------------------------------------------------------------------------------------------------------------------|---------------|
| 12. Phạm vi             | Phạm  vi  (bổ  sung  thêm thuộc  tính  con  phạm  vi thẩm quyền, phạm vi thời gian, phạm vi không gian)          | Coverage      |
| 13. Loại bỏ             | Disposal                                                                                                         | Disposal      |
| 14. Định dạng           | Định dạng (bổ sung thêm thuộc  tính  con  tên  định dạng, phiên bản định dạng, tên ứng dụng, phiên bản ứng dụng) | Format        |
| 15. Độ lớn              |                                                                                                                  | Extent        |
| 16. Phương tiện lưu trữ |                                                                                                                  | Medium        |
| 17. Vị trí              |                                                                                                                  | Location      |
| 18. Kiểu                | Kiểu (tương thích toàn bộ)                                                                                       | Document Form |
| 19. Loại máy quét 3D    |                                                                                                                  |               |
| 20.  Chất  liệu  đối    | tượng                                                                                                            | tượng         |

<!-- image -->

## VIETTEL AI RACE

## HƯỚNG DẪN KHAI BÁO QOS CHO THIẾT BỊ TRUYỀN DẪN VIBA

TD004

Lần ban hành: 1

<!-- image -->

2. 2.  Xác định dữ liệu đặc tả

<!-- image -->

TD004

Lần ban hành: 1

## VIETTEL AI RACE

## HƯỚNG DẪN KHAI BÁO QOS CHO THIẾT BỊ TRUYỀN DẪN VIBA

Dữ liệu đặc tả được sử dụng để mô tả các đối tượng, các thông tin cần thiết để lưu trữ.

Tất cả hình ảnh được số hóa 3D nên được chỉ định dữ liệu đặc tả cho quá trình số hóa tài liệu và hỗ trợ các quy trình nghiệp vụ đang diễn ra. Các tổ chức, cơ quan có thể đưa ra các yêu cầu cụ thể và để tối đa hóa sự kế thừa các giá trị dữ liệu từ các hệ thống và thiết bị hiện có. Quy trình quản lý dữ liệu đặc tả nên tối đa hóa tự động chụp dữ liệu đặc tả, giảm thiểu việc xử lý thủ công. Bất kỳ việc sử dụng, áp dụng dữ liệu đặc tả nên được thực hiện có sự tham khảo tiêu chuẩn ISO 23081-1: 2006.

Dữ liệu đặc tả kết hợp với hình ảnh là một thành phần thiết yếu trong việc quản lý và truy vấn các hình ảnh.

Hai loại dữ liệu đặc tả nên được bắt:

- -  dữ liệu đặc tả cụ thể cho các vật thể 3D, hình ảnh quét cụ thể và quá trình xử lý ảnh;
- -  dữ liệu đặc tả về dữ liệu 3D công việc đang được giao dịch và đại lý liên quan đến nghiệp vụ. Phần lớn các dữ liệu đặc tả này có thể được tự động sinh ra bởi các phần mềm phân tích đám mây điểm, xử lý mô hình 3D và các phần cứng như máy quét 3D được sử dụng để quản lý quá trình số hóa. Cần được giảm thiểu càng nhiều càng tốt việc xử lý thủ công.

Dữ liệu đặc tả có thể được nhúng với các nguồn tài nguyên tại thông tin tiêu đề, hoặc có thể được quản lý trong một hệ thống riêng biệt, hoặc cả hai, nhưng trong cả hai trường hợp đó phải có một mối quan hệ trực tiếp hoặc liên hệ giữa chúng; tức là khi dữ liệu đặc tả nằm trong một hệ thống riêng biệt, nó có liên kết trực tiếp đến các dữ liệu 3D. Dữ liệu đặc tả cũng có thể được đóng gói trong các định dạng hình ảnh 3D.

## 3.  Tạo lập dữ liệu đặc tả

Quá trình số hóa bao gồm bảy giai đoạn mà dữ liệu đặc tả phải được áp dụng. Các giai đoạn này là:

- -  lên kế hoạch;
- -  chuẩn bị
- -  quét đối tượng 3D;
- -  xử lý dữ liệu 3D;
- -  dung sai số hóa dữ liệu 3D;
- -  lập chỉ mục và dữ liệu đặc tả;
- -  quản lý, lưu trữ dữ liệu.

<!-- image -->

## VIETTEL AI RACE

## HƯỚNG DẪN KHAI BÁO QOS CHO THIẾT BỊ TRUYỀN DẪN VIBA

TD004

Lần ban hành: 1

Có hai loại thông tin đánh chỉ số: Thông tin tiểu sử và thông tin thư mục. Thông tin tiểu sử giao dịch với vòng đời của các tập tin dữ liệu 3D, các hình ảnh 3D và liên quan đến bối cảnh của các thuộc tính dữ liệu 3D và tập tin đó phải được giữ lại, đăng nhập và xác nhận trong quá trình số hóa 3D.

Các  định nghĩa về nghĩa vụ trong đánh chỉ số bao gồm:

- -  bắt buộc – thuộc tính phải có;
- -  bắt buộc nếu có - thuộc tính phải được cung cấp, nếu phù hợp với bối cảnh công việc và / hoặc các nguồn lực (đối tượng nghiệp vụ);
- -  đề nghị - nên được sử dụng nếu phù hợp với bối cảnh kinh doanh và / hoặc các nguồn lực (đối tượng kinh doanh) ;
- -  tùy chọn – tùy thuộc vào yêu cầu mà có lựa chọn cụ thể.

## 4.  Dữ liệu đặc tả về quy luật nghiệp vụ, chính sách và ủy nhiệm tại thời điểm quét 3D

Các thông tin liên quan đến số hóa nghiệp vụ, chính sách và ủy nhiệm được mô tả trong bảng 2.

Bảng 2 – Đánh chỉ số tiểu sử

| Nghĩa vụ   | Quá trình số hóa 3D                         | Các thuộc tính đánh chỉ số số hóa 3D                                                                                                                                                                                                                                                  |
|------------|---------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Bắt buộc   | Quét  dữ  liệu 3D                           | - Đối tượng, dữ liệu 3D liên quan; - Ngày và thời gian số hóa 3D (Lưu ý: thời gian được khuyến khích, nhưng không bắt buộc); - Số lượng vật thể được số hóa; - Người vận hành máy quét 3D và tên, nhãn hiệu, quốc gia sản xuất máy quét 3D; - Thông tin tham khảo chéo về dữ liệu 3D. |
| Bắt buộc   | Quét  lại  (nếu quá trình này là cần thiết) | - Đối tượng, dữ liệu 3D liên quan; - Ngày và thời gian số hóa 3D (Lưu ý: thời gian được khuyến khích, nhưng không bắt buộc); - Số lượng vật thể được số hóa; - Người vận hành máy quét 3D và tên, nhãn hiệu, quốc gia sản xuất máy quét 3D; - Thông tin tham khảo chéo về dữ liệu 3D. |
| Bắt buộc   | Đảm bảo chất lượng  (khi                    | - Tài liệu tham khảo hàng loạt (bắt buộc cho hàng loạt đầu vào);                                                                                                                                                                                                                      |

<!-- image -->

## TD004

Lần ban hành: 1

## VIETTEL AI RACE

## HƯỚNG DẪN KHAI BÁO QOS CHO THIẾT BỊ TRUYỀN DẪN VIBA

|                      | hoàn thành)       | - Người thực hiện đảm bảo chất lượng; - Ngày phê duyệt kiểm tra đảm bảo chất lượng.   |
|----------------------|-------------------|---------------------------------------------------------------------------------------|
| Bắt buộc nếu  có thể | Chuyển dữ liệu 3D | - Ngày chuyển - Tiêu đề chuyển - Chuyển mô tả - Lý do chuyển - Tiếp nhận chuyển       |

Một số hoặc tất cả các thông tin này có thể được lấy tự động bởi máy quét và phần mềm số hóa 3D. Trong trường hợp chuyển giao để đảm bảo lưu trữ, điều quan trọng là phải biết ngày chuyển giao để xác định bất kỳ sự chậm trễ nào đó có hợp lý không.Tổ chức cần thực hiện các thủ tục để ngăn chặn bất kỳ hình thức sửa đổi sau khi hình ảnh đã được lấy một cách phù hợp và lập chỉ mục.