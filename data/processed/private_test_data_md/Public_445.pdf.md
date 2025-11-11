<!-- image -->

| VIETTEL AI RACE   | TD445   |
|-------------------|---------|

| Nghiệp vụ   | Loại chỉ tiêu      | Hành động   | API/Action       | Mô tả chi tiết                                                                                                | Phương pháp đo     | Kết quả mong muốn                                                       | Ghi chú                                                     |
|-------------|--------------------|-------------|------------------|---------------------------------------------------------------------------------------------------------------|--------------------|-------------------------------------------------------------------------|-------------------------------------------------------------|
| Opportunity | Chỉ tiêu chức năng | Xóa         | /crm/lead/add    | Xóa dữ liệu Opportunity trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ. | Kiểm thử hiệu năng | Xuất báo cáo chi tiết dưới dạng CSV, có xác thực hai lớp trước khi tải. | Phải kiểm thử với ≥ 10.000 bản ghi để đảm bảo hiệu năng.    |
| Campaign    | Chỉ tiêu bảo mật   | Gắn thẻ     | /crm/lead/export | Gắn thẻ dữ liệu Campaign trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ                   | Kiểm thử hiệu năng | Xuất báo cáo chi tiết dưới dạng CSV, có xác thực hai lớp                | Yêu cầu tích hợp với hệ thống RPA để tự động hóa quy trình. |

<!-- image -->

| VIETTEL AI RACE   | TD445   |
|-------------------|---------|

|         |                    |          |                  | và ghi log đầy đủ.                                                                                            |                    | trước khi tải.                                                   |                                                           |
|---------|--------------------|----------|------------------|---------------------------------------------------------------------------------------------------------------|--------------------|------------------------------------------------------------------|-----------------------------------------------------------|
| Contact | Chỉ tiêu hiệu năng | Xóa      | /crm/lead/export | Xóa dữ liệu Contact trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ.     | Kiểm thử hiệu năng | Cảnh báo nếu thiếu trường bắt buộc, hệ thống rollback giao dịch. | Theo chuẩn ISO 27001 và quy định bảo mật Viettel.         |
| Contact | Chỉ tiêu chức năng | Gắn thẻ  | /crm/lead/export | Gắn thẻ dữ liệu Contact trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ. | Kiểm thử chức năng | Cảnh báo nếu thiếu trường bắt buộc, hệ thống rollback giao dịch. | Dữ liệu được backup hàng ngày, lưu giữ tối thiểu 30 ngày. |
| Contact | Chỉ tiêu hiệu năng | Cập nhật | /crm/lead/add    | Cập nhật dữ liệu Contact trong CRM, bao gồm                                                                   | Kiểm thử bảo mật   | Không lỗi, log đầy đủ trong                                      | Theo chuẩn ISO 27001 và quy định bảo mật Viettel.         |

<!-- image -->

| VIETTEL AI RACE   | TD445   |
|-------------------|---------|

|         |                    |            |                      | validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ.                                        |                    | AuditLog, SLA đáp ứng 99.99%.                                       |                                                           |
|---------|--------------------|------------|----------------------|-----------------------------------------------------------------------------------------------------------|--------------------|---------------------------------------------------------------------|-----------------------------------------------------------|
| Contact | Chỉ tiêu hiệu năng | Xóa        | /crm/campaign/import | Xóa dữ liệu Contact trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ. | Kiểm thử hiệu năng | Đồng bộ dữ liệu sang DataLake trong vòng 5s, tự động retry khi lỗi. | Kết quả được gửi mail và SMS cho quản trị viên phụ trách. |
| Contact | Chỉ tiêu chức năng | Chuyển đổi | /crm/lead/add        | Chuyển đổi dữ liệu Contact trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ             | Kiểm thử bảo mật   | Cảnh báo nếu thiếu trường bắt buộc, hệ thống rollback giao dịch.    | Theo chuẩn ISO 27001 và quy định bảo mật Viettel.         |

<!-- image -->

| VIETTEL AI RACE   | TD445   |
|-------------------|---------|

|             |                  |            |                      | và ghi log đầy đủ.                                                                                               |                    |                                                                         |                                                             |
|-------------|------------------|------------|----------------------|------------------------------------------------------------------------------------------------------------------|--------------------|-------------------------------------------------------------------------|-------------------------------------------------------------|
| Opportunity | Chỉ tiêu bảo mật | Import     | /crm/campaign/import | Import dữ liệu Opportunity trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ. | Kiểm thử bảo mật   | Xuất báo cáo chi tiết dưới dạng CSV, có xác thực hai lớp trước khi tải. | Theo chuẩn ISO 27001 và quy định bảo mật Viettel.           |
| Lead        | Chỉ tiêu bảo mật | Chuyển đổi | /crm/campaign/import | Chuyển đổi dữ liệu Lead trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ.    | Kiểm thử chức năng | Xuất báo cáo chi tiết dưới dạng CSV, có xác thực hai lớp trước khi tải. | Yêu cầu tích hợp với hệ thống RPA để tự động hóa quy trình. |

<!-- image -->

## VIETTEL AI RACE

## CHỈ TIÊU CRM - RPA

TD445

Lần ban hành: 1

| Lead     | Chỉ tiêu chức năng   | Chuyển đổi   | /crm/opportunity/delete   | Chuyển đổi dữ liệu Lead trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ.     | Kiểm thử chức năng   | Cảnh báo nếu thiếu trường bắt buộc, hệ thống rollback giao dịch.        | Phải kiểm thử với ≥ 10.000 bản ghi để đảm bảo hiệu năng.   |
|----------|----------------------|--------------|---------------------------|-------------------------------------------------------------------------------------------------------------------|----------------------|-------------------------------------------------------------------------|------------------------------------------------------------|
| Campaign | Chỉ tiêu chức năng   | Chuyển đổi   | /crm/campaign/import      | Chuyển đổi dữ liệu Campaign trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ. | Kiểm thử bảo mật     | Xuất báo cáo chi tiết dưới dạng CSV, có xác thực hai lớp trước khi tải. | Kết quả được gửi mail và SMS cho quản trị viên phụ trách.  |
| Campaign | Chỉ tiêu hiệu năng   | Export       | /crm/contact/update       | Export dữ liệu Campaign trong CRM, bao gồm validate dữ liệu đầu vào, xử lý                                        | Kiểm thử hiệu năng   | Thành công với thời gian xử lý < 1s, dữ liệu đồng                       | Theo chuẩn ISO 27001 và quy định bảo mật Viettel.          |

<!-- image -->

| VIETTEL AI RACE   | TD445   |
|-------------------|---------|

|             |                    |          |                     | logic nghiệp vụ và ghi log đầy đủ.                                                                                |                    | bộ sang hệ thống Billing.                                                   |                                                             |
|-------------|--------------------|----------|---------------------|-------------------------------------------------------------------------------------------------------------------|--------------------|-----------------------------------------------------------------------------|-------------------------------------------------------------|
| Opportunity | Chỉ tiêu hiệu năng | Gắn thẻ  | /crm/contact/update | Gắn thẻ dữ liệu Opportunity trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ. | Kiểm thử hiệu năng | Thành công với thời gian xử lý < 1s, dữ liệu đồng bộ sang hệ thống Billing. | Yêu cầu tích hợp với hệ thống RPA để tự động hóa quy trình. |
| Campaign    | Chỉ tiêu hiệu năng | Cập nhật | /crm/contact/update | Cập nhật dữ liệu Campaign trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ.   | Kiểm thử hiệu năng | Không lỗi, log đầy đủ trong AuditLog, SLA đáp ứng 99.99%.                   | Dữ liệu được backup hàng ngày, lưu giữ tối thiểu 30 ngày.   |

<!-- image -->

## VIETTEL AI RACE

## CHỈ TIÊU CRM - RPA

TD445

Lần ban hành: 1

| Lead        | Chỉ tiêu chức năng   | Chuyển đổi   | /crm/contact/update     | Chuyển đổi dữ liệu Lead trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ.    | Kiểm thử bảo mật   | Cảnh báo nếu thiếu trường bắt buộc, hệ thống rollback giao dịch.    | Phải kiểm thử với ≥ 10.000 bản ghi để đảm bảo hiệu năng.   |
|-------------|----------------------|--------------|-------------------------|------------------------------------------------------------------------------------------------------------------|--------------------|---------------------------------------------------------------------|------------------------------------------------------------|
| Contact     | Chỉ tiêu chức năng   | Chuyển đổi   | /crm/lead/add           | Chuyển đổi dữ liệu Contact trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ. | Kiểm thử bảo mật   | Đồng bộ dữ liệu sang DataLake trong vòng 5s, tự động retry khi lỗi. | Dữ liệu được backup hàng ngày, lưu giữ tối thiểu 30 ngày.  |
| Opportunity | Chỉ tiêu bảo mật     | Import       | /crm/opportunity/delete | Import dữ liệu Opportunity trong CRM, bao gồm validate dữ liệu đầu vào, xử lý                                    | Kiểm thử bảo mật   | Xuất báo cáo chi tiết dưới dạng CSV, có xác thực                    | Dữ liệu được backup hàng ngày, lưu giữ tối thiểu 30 ngày.  |

<!-- image -->

| VIETTEL AI RACE   | TD445   |
|-------------------|---------|

|          |                    |     |                     | logic nghiệp vụ và ghi log đầy đủ.                                                                         |                    | hai lớp trước khi tải.                                              |                                                           |
|----------|--------------------|-----|---------------------|------------------------------------------------------------------------------------------------------------|--------------------|---------------------------------------------------------------------|-----------------------------------------------------------|
| Campaign | Chỉ tiêu hiệu năng | Xóa | /crm/contact/update | Xóa dữ liệu Campaign trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ. | Kiểm thử hiệu năng | Đồng bộ dữ liệu sang DataLake trong vòng 5s, tự động retry khi lỗi. | Dữ liệu được backup hàng ngày, lưu giữ tối thiểu 30 ngày. |
| Campaign | Chỉ tiêu bảo mật   | Xóa | /crm/lead/export    | Xóa dữ liệu Campaign trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ. | Kiểm thử chức năng | Không lỗi, log đầy đủ trong AuditLog, SLA đáp ứng 99.99%.           | Theo chuẩn ISO 27001 và quy định bảo mật Viettel.         |

| VIETTEL AI RACE   | TD445   |
|-------------------|---------|

<!-- image -->

| Campaign    | Chỉ tiêu chức năng   | Xóa     | /crm/opportunity/delete   | Xóa dữ liệu Campaign trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ.       | Kiểm thử hiệu năng   | Xuất báo cáo chi tiết dưới dạng CSV, có xác thực hai lớp trước khi tải.   | Yêu cầu tích hợp với hệ thống RPA để tự động hóa quy trình.   |
|-------------|----------------------|---------|---------------------------|------------------------------------------------------------------------------------------------------------------|----------------------|---------------------------------------------------------------------------|---------------------------------------------------------------|
| Opportunity | Chỉ tiêu bảo mật     | Import  | /crm/lead/add             | Import dữ liệu Opportunity trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ. | Kiểm thử hiệu năng   | Xuất báo cáo chi tiết dưới dạng CSV, có xác thực hai lớp trước khi tải.   | Phải kiểm thử với ≥ 10.000 bản ghi để đảm bảo hiệu năng.      |
| Contact     | Chỉ tiêu chức năng   | Gắn thẻ | /crm/lead/add             | Gắn thẻ dữ liệu Contact trong CRM, bao gồm validate dữ liệu đầu vào, xử lý                                       | Kiểm thử hiệu năng   | Không lỗi, log đầy đủ trong AuditLog,                                     | Theo chuẩn ISO 27001 và quy định bảo mật Viettel.             |

<!-- image -->

| VIETTEL AI RACE   | TD445   |
|-------------------|---------|

|             |                    |            |                      | logic nghiệp vụ và ghi log đầy đủ.                                                                                   |                    | SLA đáp ứng 99.99%.                                                 |                                                             |
|-------------|--------------------|------------|----------------------|----------------------------------------------------------------------------------------------------------------------|--------------------|---------------------------------------------------------------------|-------------------------------------------------------------|
| Opportunity | Chỉ tiêu hiệu năng | Chuyển đổi | /crm/campaign/import | Chuyển đổi dữ liệu Opportunity trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ. | Kiểm thử bảo mật   | Đồng bộ dữ liệu sang DataLake trong vòng 5s, tự động retry khi lỗi. | Yêu cầu tích hợp với hệ thống RPA để tự động hóa quy trình. |
| Campaign    | Chỉ tiêu bảo mật   | Import     | /crm/campaign/import | Import dữ liệu Campaign trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ.        | Kiểm thử chức năng | Cảnh báo nếu thiếu trường bắt buộc, hệ thống rollback giao dịch.    | Yêu cầu tích hợp với hệ thống RPA để tự động hóa quy trình. |

<!-- image -->

## VIETTEL AI RACE

## CHỈ TIÊU CRM - RPA

TD445

Lần ban hành: 1

| Lead        | Chỉ tiêu hiệu năng   | Thêm mới   | /crm/contact/update     | Thêm mới dữ liệu Lead trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ.       | Kiểm thử hiệu năng   | Không lỗi, log đầy đủ trong AuditLog, SLA đáp ứng 99.99%.                   | Dữ liệu được backup hàng ngày, lưu giữ tối thiểu 30 ngày.   |
|-------------|----------------------|------------|-------------------------|-------------------------------------------------------------------------------------------------------------------|----------------------|-----------------------------------------------------------------------------|-------------------------------------------------------------|
| Campaign    | Chỉ tiêu hiệu năng   | Chuyển đổi | /crm/opportunity/delete | Chuyển đổi dữ liệu Campaign trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ. | Kiểm thử hiệu năng   | Thành công với thời gian xử lý < 1s, dữ liệu đồng bộ sang hệ thống Billing. | Phải kiểm thử với ≥ 10.000 bản ghi để đảm bảo hiệu năng.    |
| Opportunity | Chỉ tiêu bảo mật     | Cập nhật   | /crm/lead/export        | Cập nhật dữ liệu Opportunity trong CRM, bao gồm validate dữ liệu                                                  | Kiểm thử chức năng   | Không lỗi, log đầy đủ trong AuditLog, SLA đáp                               | Dữ liệu được backup hàng ngày, lưu giữ tối thiểu 30 ngày.   |

<!-- image -->

| VIETTEL AI RACE   | TD445   |
|-------------------|---------|

|          |                    |         |                  | đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ.                                                              |                    | ứng 99.99%.                                                             |                                                             |
|----------|--------------------|---------|------------------|----------------------------------------------------------------------------------------------------------------|--------------------|-------------------------------------------------------------------------|-------------------------------------------------------------|
| Lead     | Chỉ tiêu chức năng | Export  | /crm/lead/export | Export dữ liệu Lead trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ.      | Kiểm thử chức năng | Không lỗi, log đầy đủ trong AuditLog, SLA đáp ứng 99.99%.               | Dữ liệu được backup hàng ngày, lưu giữ tối thiểu 30 ngày.   |
| Campaign | Chỉ tiêu hiệu năng | Gắn thẻ | /crm/lead/export | Gắn thẻ dữ liệu Campaign trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ. | Kiểm thử chức năng | Xuất báo cáo chi tiết dưới dạng CSV, có xác thực hai lớp trước khi tải. | Yêu cầu tích hợp với hệ thống RPA để tự động hóa quy trình. |

<!-- image -->

## VIETTEL AI RACE

## CHỈ TIÊU CRM - RPA

TD445

Lần ban hành: 1

| Contact   | Chỉ tiêu chức năng   | Gắn thẻ   | /crm/contact/update   | Gắn thẻ dữ liệu Contact trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ.   | Kiểm thử chức năng   | Cảnh báo nếu thiếu trường bắt buộc, hệ thống rollback giao dịch.        | Yêu cầu tích hợp với hệ thống RPA để tự động hóa quy trình.   |
|-----------|----------------------|-----------|-----------------------|-----------------------------------------------------------------------------------------------------------------|----------------------|-------------------------------------------------------------------------|---------------------------------------------------------------|
| Lead      | Chỉ tiêu chức năng   | Gắn thẻ   | /crm/contact/update   | Gắn thẻ dữ liệu Lead trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ.      | Kiểm thử chức năng   | Xuất báo cáo chi tiết dưới dạng CSV, có xác thực hai lớp trước khi tải. | Theo chuẩn ISO 27001 và quy định bảo mật Viettel.             |
| Lead      | Chỉ tiêu bảo mật     | Xóa       | /crm/lead/add         | Xóa dữ liệu Lead trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ                             | Kiểm thử chức năng   | Đồng bộ dữ liệu sang DataLake trong vòng 5s,                            | Theo chuẩn ISO 27001 và quy định bảo mật Viettel.             |

<!-- image -->

| VIETTEL AI RACE   | TD445   |
|-------------------|---------|

|         |                    |          |                         | và ghi log đầy đủ.                                                                                             |                    | tự động retry khi lỗi.                                           |                                                             |
|---------|--------------------|----------|-------------------------|----------------------------------------------------------------------------------------------------------------|--------------------|------------------------------------------------------------------|-------------------------------------------------------------|
| Contact | Chỉ tiêu bảo mật   | Import   | /crm/opportunity/delete | Import dữ liệu Contact trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ.   | Kiểm thử hiệu năng | Cảnh báo nếu thiếu trường bắt buộc, hệ thống rollback giao dịch. | Dữ liệu được backup hàng ngày, lưu giữ tối thiểu 30 ngày.   |
| Contact | Chỉ tiêu hiệu năng | Cập nhật | /crm/lead/add           | Cập nhật dữ liệu Contact trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ. | Kiểm thử chức năng | Không lỗi, log đầy đủ trong AuditLog, SLA đáp ứng 99.99%.        | Yêu cầu tích hợp với hệ thống RPA để tự động hóa quy trình. |

<!-- image -->

## VIETTEL AI RACE

## CHỈ TIÊU CRM - RPA

TD445

Lần ban hành: 1

| Lead        | Chỉ tiêu bảo mật   | Chuyển đổi   | /crm/opportunity/delete   | Chuyển đổi dữ liệu Lead trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ.   | Kiểm thử chức năng   | Không lỗi, log đầy đủ trong AuditLog, SLA đáp ứng 99.99%.                   | Theo chuẩn ISO 27001 và quy định bảo mật Viettel.         |
|-------------|--------------------|--------------|---------------------------|-----------------------------------------------------------------------------------------------------------------|----------------------|-----------------------------------------------------------------------------|-----------------------------------------------------------|
| Lead        | Chỉ tiêu hiệu năng | Thêm mới     | /crm/lead/add             | Thêm mới dữ liệu Lead trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ.     | Kiểm thử chức năng   | Thành công với thời gian xử lý < 1s, dữ liệu đồng bộ sang hệ thống Billing. | Dữ liệu được backup hàng ngày, lưu giữ tối thiểu 30 ngày. |
| Opportunity | Chỉ tiêu chức năng | Export       | /crm/contact/update       | Export dữ liệu Opportunity trong CRM, bao gồm validate dữ liệu đầu vào, xử lý                                   | Kiểm thử hiệu năng   | Cảnh báo nếu thiếu trường bắt buộc, hệ thống                                | Kết quả được gửi mail và SMS cho quản trị viên phụ trách. |

<!-- image -->

| VIETTEL AI RACE   | TD445   |
|-------------------|---------|

|             |                    |            |                         | logic nghiệp vụ và ghi log đầy đủ.                                                                               |                    | rollback giao dịch.                                                         |                                                          |
|-------------|--------------------|------------|-------------------------|------------------------------------------------------------------------------------------------------------------|--------------------|-----------------------------------------------------------------------------|----------------------------------------------------------|
| Contact     | Chỉ tiêu bảo mật   | Chuyển đổi | /crm/lead/add           | Chuyển đổi dữ liệu Contact trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ. | Kiểm thử chức năng | Xuất báo cáo chi tiết dưới dạng CSV, có xác thực hai lớp trước khi tải.     | Theo chuẩn ISO 27001 và quy định bảo mật Viettel.        |
| Opportunity | Chỉ tiêu hiệu năng | Import     | /crm/opportunity/delete | Import dữ liệu Opportunity trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ. | Kiểm thử bảo mật   | Thành công với thời gian xử lý < 1s, dữ liệu đồng bộ sang hệ thống Billing. | Phải kiểm thử với ≥ 10.000 bản ghi để đảm bảo hiệu năng. |

<!-- image -->

## VIETTEL AI RACE

## CHỈ TIÊU CRM - RPA

TD445

Lần ban hành: 1

| Campaign   | Chỉ tiêu bảo mật   | Xóa        | /crm/campaign/import   | Xóa dữ liệu Campaign trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ.      | Kiểm thử bảo mật   | Đồng bộ dữ liệu sang DataLake trong vòng 5s, tự động retry khi lỗi.         | Kết quả được gửi mail và SMS cho quản trị viên phụ trách.   |
|------------|--------------------|------------|------------------------|-----------------------------------------------------------------------------------------------------------------|--------------------|-----------------------------------------------------------------------------|-------------------------------------------------------------|
| Campaign   | Chỉ tiêu hiệu năng | Cập nhật   | /crm/campaign/import   | Cập nhật dữ liệu Campaign trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ. | Kiểm thử bảo mật   | Thành công với thời gian xử lý < 1s, dữ liệu đồng bộ sang hệ thống Billing. | Yêu cầu tích hợp với hệ thống RPA để tự động hóa quy trình. |
| Campaign   | Chỉ tiêu bảo mật   | Chuyển đổi | /crm/lead/export       | Chuyển đổi dữ liệu Campaign trong CRM, bao gồm validate dữ liệu                                                 | Kiểm thử bảo mật   | Đồng bộ dữ liệu sang DataLake trong                                         | Phải kiểm thử với ≥ 10.000 bản ghi để đảm bảo hiệu năng.    |

<!-- image -->

| VIETTEL AI RACE   | TD445   |
|-------------------|---------|

|             |                    |            |                         | đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ.                                                                 |                  | vòng 5s, tự động retry khi lỗi.                                  |                                                             |
|-------------|--------------------|------------|-------------------------|-------------------------------------------------------------------------------------------------------------------|------------------|------------------------------------------------------------------|-------------------------------------------------------------|
| Campaign    | Chỉ tiêu hiệu năng | Chuyển đổi | /crm/opportunity/delete | Chuyển đổi dữ liệu Campaign trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ. | Kiểm thử bảo mật | Cảnh báo nếu thiếu trường bắt buộc, hệ thống rollback giao dịch. | Yêu cầu tích hợp với hệ thống RPA để tự động hóa quy trình. |
| Opportunity | Chỉ tiêu hiệu năng | Xóa        | /crm/campaign/import    | Xóa dữ liệu Opportunity trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ.     | Kiểm thử bảo mật | Không lỗi, log đầy đủ trong AuditLog, SLA đáp ứng 99.99%.        | Kết quả được gửi mail và SMS cho quản trị viên phụ trách.   |

<!-- image -->

| VIETTEL AI RACE   | TD445   |
|-------------------|---------|

| Contact     | Chỉ tiêu bảo mật   | Thêm mới   | /crm/lead/add           | Thêm mới dữ liệu Contact trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ.   | Kiểm thử bảo mật   | Không lỗi, log đầy đủ trong AuditLog, SLA đáp ứng 99.99%.                   | Theo chuẩn ISO 27001 và quy định bảo mật Viettel.           |
|-------------|--------------------|------------|-------------------------|------------------------------------------------------------------------------------------------------------------|--------------------|-----------------------------------------------------------------------------|-------------------------------------------------------------|
| Campaign    | Chỉ tiêu chức năng | Import     | /crm/opportunity/delete | Import dữ liệu Campaign trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ.    | Kiểm thử bảo mật   | Thành công với thời gian xử lý < 1s, dữ liệu đồng bộ sang hệ thống Billing. | Phải kiểm thử với ≥ 10.000 bản ghi để đảm bảo hiệu năng.    |
| Opportunity | Chỉ tiêu chức năng | Cập nhật   | /crm/lead/add           | Cập nhật dữ liệu Opportunity trong CRM, bao gồm                                                                  | Kiểm thử hiệu năng | Xuất báo cáo chi tiết dưới dạng CSV, có                                     | Yêu cầu tích hợp với hệ thống RPA để tự động hóa quy trình. |

<!-- image -->

| VIETTEL AI RACE   | TD445   |
|-------------------|---------|

|             |                    |        |                         | validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ.                                         |                    | xác thực hai lớp trước khi tải.                                  |                                                           |
|-------------|--------------------|--------|-------------------------|------------------------------------------------------------------------------------------------------------|--------------------|------------------------------------------------------------------|-----------------------------------------------------------|
| Campaign    | Chỉ tiêu chức năng | Xóa    | /crm/contact/update     | Xóa dữ liệu Campaign trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ. | Kiểm thử chức năng | Cảnh báo nếu thiếu trường bắt buộc, hệ thống rollback giao dịch. | Phải kiểm thử với ≥ 10.000 bản ghi để đảm bảo hiệu năng.  |
| Opportunity | Chỉ tiêu hiệu năng | Import | /crm/opportunity/delete | Import dữ liệu Opportunity trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ              | Kiểm thử chức năng | Cảnh báo nếu thiếu trường bắt buộc, hệ thống rollback giao dịch. | Kết quả được gửi mail và SMS cho quản trị viên phụ trách. |

<!-- image -->

## VIETTEL AI RACE

## CHỈ TIÊU CRM - RPA

TD445

Lần ban hành: 1

|             |                    |            |                         | và ghi log đầy đủ.                                                                                                   |                    |                                                                             |                                                           |
|-------------|--------------------|------------|-------------------------|----------------------------------------------------------------------------------------------------------------------|--------------------|-----------------------------------------------------------------------------|-----------------------------------------------------------|
| Contact     | Chỉ tiêu chức năng | Cập nhật   | /crm/campaign/import    | Cập nhật dữ liệu Contact trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ.       | Kiểm thử chức năng | Thành công với thời gian xử lý < 1s, dữ liệu đồng bộ sang hệ thống Billing. | Kết quả được gửi mail và SMS cho quản trị viên phụ trách. |
| Opportunity | Chỉ tiêu chức năng | Chuyển đổi | /crm/opportunity/delete | Chuyển đổi dữ liệu Opportunity trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ. | Kiểm thử chức năng | Cảnh báo nếu thiếu trường bắt buộc, hệ thống rollback giao dịch.            | Theo chuẩn ISO 27001 và quy định bảo mật Viettel.         |

<!-- image -->

## VIETTEL AI RACE

## CHỈ TIÊU CRM - RPA

TD445

Lần ban hành: 1

| Contact   | Chỉ tiêu hiệu năng   | Thêm mới   | /crm/campaign/import    | Thêm mới dữ liệu Contact trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ.   | Kiểm thử chức năng   | Cảnh báo nếu thiếu trường bắt buộc, hệ thống rollback giao dịch.   | Theo chuẩn ISO 27001 và quy định bảo mật Viettel.           |
|-----------|----------------------|------------|-------------------------|------------------------------------------------------------------------------------------------------------------|----------------------|--------------------------------------------------------------------|-------------------------------------------------------------|
| Contact   | Chỉ tiêu chức năng   | Thêm mới   | /crm/contact/update     | Thêm mới dữ liệu Contact trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ.   | Kiểm thử chức năng   | Không lỗi, log đầy đủ trong AuditLog, SLA đáp ứng 99.99%.          | Yêu cầu tích hợp với hệ thống RPA để tự động hóa quy trình. |
| Campaign  | Chỉ tiêu hiệu năng   | Xóa        | /crm/opportunity/delete | Xóa dữ liệu Campaign trong CRM, bao gồm validate dữ liệu                                                         | Kiểm thử hiệu năng   | Đồng bộ dữ liệu sang DataLake trong                                | Dữ liệu được backup hàng ngày, lưu giữ tối thiểu 30 ngày.   |

<!-- image -->

| VIETTEL AI RACE   | TD445   |
|-------------------|---------|

|         |                    |          |                      | đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ.                                                              |                    | vòng 5s, tự động retry khi lỗi.                                         |                                                           |
|---------|--------------------|----------|----------------------|----------------------------------------------------------------------------------------------------------------|--------------------|-------------------------------------------------------------------------|-----------------------------------------------------------|
| Contact | Chỉ tiêu chức năng | Gắn thẻ  | /crm/campaign/import | Gắn thẻ dữ liệu Contact trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ.  | Kiểm thử hiệu năng | Xuất báo cáo chi tiết dưới dạng CSV, có xác thực hai lớp trước khi tải. | Theo chuẩn ISO 27001 và quy định bảo mật Viettel.         |
| Contact | Chỉ tiêu bảo mật   | Cập nhật | /crm/campaign/import | Cập nhật dữ liệu Contact trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ. | Kiểm thử chức năng | Không lỗi, log đầy đủ trong AuditLog, SLA đáp ứng 99.99%.               | Dữ liệu được backup hàng ngày, lưu giữ tối thiểu 30 ngày. |

<!-- image -->

## VIETTEL AI RACE

## CHỈ TIÊU CRM - RPA

TD445

Lần ban hành: 1

| Opportunity   | Chỉ tiêu hiệu năng   | Gắn thẻ   | /crm/contact/update   | Gắn thẻ dữ liệu Opportunity trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ.   | Kiểm thử bảo mật   | Không lỗi, log đầy đủ trong AuditLog, SLA đáp ứng 99.99%.               | Theo chuẩn ISO 27001 và quy định bảo mật Viettel.           |
|---------------|----------------------|-----------|-----------------------|---------------------------------------------------------------------------------------------------------------------|--------------------|-------------------------------------------------------------------------|-------------------------------------------------------------|
| Lead          | Chỉ tiêu bảo mật     | Gắn thẻ   | /crm/campaign/import  | Gắn thẻ dữ liệu Lead trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ.          | Kiểm thử hiệu năng | Xuất báo cáo chi tiết dưới dạng CSV, có xác thực hai lớp trước khi tải. | Yêu cầu tích hợp với hệ thống RPA để tự động hóa quy trình. |
| Lead          | Chỉ tiêu hiệu năng   | Xóa       | /crm/lead/add         | Xóa dữ liệu Lead trong CRM, bao gồm validate dữ liệu đầu vào, xử lý                                                 | Kiểm thử bảo mật   | Cảnh báo nếu thiếu trường bắt buộc, hệ thống                            | Yêu cầu tích hợp với hệ thống RPA để tự động hóa quy trình. |

<!-- image -->

| VIETTEL AI RACE   | TD445   |
|-------------------|---------|

|          |                    |            |                         | logic nghiệp vụ và ghi log đầy đủ.                                                                            |                    | rollback giao dịch.                                              |                                                           |
|----------|--------------------|------------|-------------------------|---------------------------------------------------------------------------------------------------------------|--------------------|------------------------------------------------------------------|-----------------------------------------------------------|
| Lead     | Chỉ tiêu hiệu năng | Gắn thẻ    | /crm/contact/update     | Gắn thẻ dữ liệu Lead trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ.    | Kiểm thử hiệu năng | Không lỗi, log đầy đủ trong AuditLog, SLA đáp ứng 99.99%.        | Kết quả được gửi mail và SMS cho quản trị viên phụ trách. |
| Lead     | Chỉ tiêu chức năng | Chuyển đổi | /crm/opportunity/delete | Chuyển đổi dữ liệu Lead trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ. | Kiểm thử hiệu năng | Cảnh báo nếu thiếu trường bắt buộc, hệ thống rollback giao dịch. | Kết quả được gửi mail và SMS cho quản trị viên phụ trách. |
| Campaign | Chỉ tiêu hiệu năng | Gắn thẻ    | /crm/opportunity/delete | Gắn thẻ dữ liệu Campaign trong CRM,                                                                           | Kiểm thử           | Cảnh báo nếu thiếu trường                                        | Dữ liệu được backup hàng ngày,                            |

<!-- image -->

| VIETTEL AI RACE   | TD445   |
|-------------------|---------|

|          |                    |            |                         | bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ.                                        | hiệu năng          | bắt buộc, hệ thống rollback giao dịch.                                  | lưu giữ tối thiểu 30 ngày.                               |
|----------|--------------------|------------|-------------------------|-------------------------------------------------------------------------------------------------------------------|--------------------|-------------------------------------------------------------------------|----------------------------------------------------------|
| Campaign | Chỉ tiêu hiệu năng | Chuyển đổi | /crm/opportunity/delete | Chuyển đổi dữ liệu Campaign trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ. | Kiểm thử hiệu năng | Xuất báo cáo chi tiết dưới dạng CSV, có xác thực hai lớp trước khi tải. | Theo chuẩn ISO 27001 và quy định bảo mật Viettel.        |
| Campaign | Chỉ tiêu chức năng | Cập nhật   | /crm/lead/add           | Cập nhật dữ liệu Campaign trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ                      | Kiểm thử bảo mật   | Thành công với thời gian xử lý < 1s, dữ liệu đồng bộ sang               | Phải kiểm thử với ≥ 10.000 bản ghi để đảm bảo hiệu năng. |

<!-- image -->

| VIETTEL AI RACE   | TD445   |
|-------------------|---------|

|          |                    |          |                         | và ghi log đầy đủ.                                                                                             |                    | hệ thống Billing.                                                       |                                                           |
|----------|--------------------|----------|-------------------------|----------------------------------------------------------------------------------------------------------------|--------------------|-------------------------------------------------------------------------|-----------------------------------------------------------|
| Campaign | Chỉ tiêu hiệu năng | Xóa      | /crm/opportunity/delete | Xóa dữ liệu Campaign trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ.     | Kiểm thử bảo mật   | Xuất báo cáo chi tiết dưới dạng CSV, có xác thực hai lớp trước khi tải. | Theo chuẩn ISO 27001 và quy định bảo mật Viettel.         |
| Contact  | Chỉ tiêu hiệu năng | Cập nhật | /crm/lead/add           | Cập nhật dữ liệu Contact trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ. | Kiểm thử chức năng | Xuất báo cáo chi tiết dưới dạng CSV, có xác thực hai lớp trước khi tải. | Kết quả được gửi mail và SMS cho quản trị viên phụ trách. |

<!-- image -->

## VIETTEL AI RACE

## CHỈ TIÊU CRM - RPA

TD445

Lần ban hành: 1

| Contact   | Chỉ tiêu chức năng   | Xóa     | /crm/lead/export        | Xóa dữ liệu Contact trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ.     | Kiểm thử bảo mật   | Cảnh báo nếu thiếu trường bắt buộc, hệ thống rollback giao dịch.        | Theo chuẩn ISO 27001 và quy định bảo mật Viettel.         |
|-----------|----------------------|---------|-------------------------|---------------------------------------------------------------------------------------------------------------|--------------------|-------------------------------------------------------------------------|-----------------------------------------------------------|
| Contact   | Chỉ tiêu hiệu năng   | Gắn thẻ | /crm/lead/add           | Gắn thẻ dữ liệu Contact trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ. | Kiểm thử chức năng | Xuất báo cáo chi tiết dưới dạng CSV, có xác thực hai lớp trước khi tải. | Phải kiểm thử với ≥ 10.000 bản ghi để đảm bảo hiệu năng.  |
| Lead      | Chỉ tiêu chức năng   | Gắn thẻ | /crm/opportunity/delete | Gắn thẻ dữ liệu Lead trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ                       | Kiểm thử hiệu năng | Đồng bộ dữ liệu sang DataLake trong vòng 5s,                            | Kết quả được gửi mail và SMS cho quản trị viên phụ trách. |

<!-- image -->

| VIETTEL AI RACE   | TD445   |
|-------------------|---------|

|             |                    |          |                     | và ghi log đầy đủ.                                                                                                 |                  | tự động retry khi lỗi.                                                      |                                                             |
|-------------|--------------------|----------|---------------------|--------------------------------------------------------------------------------------------------------------------|------------------|-----------------------------------------------------------------------------|-------------------------------------------------------------|
| Opportunity | Chỉ tiêu hiệu năng | Thêm mới | /crm/contact/update | Thêm mới dữ liệu Opportunity trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ. | Kiểm thử bảo mật | Không lỗi, log đầy đủ trong AuditLog, SLA đáp ứng 99.99%.                   | Yêu cầu tích hợp với hệ thống RPA để tự động hóa quy trình. |
| Contact     | Chỉ tiêu chức năng | Cập nhật | /crm/lead/add       | Cập nhật dữ liệu Contact trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ.     | Kiểm thử bảo mật | Thành công với thời gian xử lý < 1s, dữ liệu đồng bộ sang hệ thống Billing. | Dữ liệu được backup hàng ngày, lưu giữ tối thiểu 30 ngày.   |

| VIETTEL AI RACE   | TD445   |
|-------------------|---------|

<!-- image -->

| Opportunity   | Chỉ tiêu bảo mật   | Export   | /crm/lead/export    | Export dữ liệu Opportunity trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ.   | Kiểm thử chức năng   | Đồng bộ dữ liệu sang DataLake trong vòng 5s, tự động retry khi lỗi.   | Phải kiểm thử với ≥ 10.000 bản ghi để đảm bảo hiệu năng.   |
|---------------|--------------------|----------|---------------------|--------------------------------------------------------------------------------------------------------------------|----------------------|-----------------------------------------------------------------------|------------------------------------------------------------|
| Opportunity   | Chỉ tiêu hiệu năng | Export   | /crm/lead/add       | Export dữ liệu Opportunity trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ.   | Kiểm thử hiệu năng   | Không lỗi, log đầy đủ trong AuditLog, SLA đáp ứng 99.99%.             | Theo chuẩn ISO 27001 và quy định bảo mật Viettel.          |
| Lead          | Chỉ tiêu chức năng | Thêm mới | /crm/contact/update | Thêm mới dữ liệu Lead trong CRM, bao gồm validate dữ liệu đầu vào, xử lý                                           | Kiểm thử hiệu năng   | Thành công với thời gian xử lý < 1s, dữ                               | Phải kiểm thử với ≥ 10.000 bản ghi để đảm bảo hiệu năng.   |

<!-- image -->

| VIETTEL AI RACE   | TD445   |
|-------------------|---------|

|      |                    |         |                      | logic nghiệp vụ và ghi log đầy đủ.                                                                         |                    | liệu đồng bộ sang hệ thống Billing.                                     |                                                           |
|------|--------------------|---------|----------------------|------------------------------------------------------------------------------------------------------------|--------------------|-------------------------------------------------------------------------|-----------------------------------------------------------|
| Lead | Chỉ tiêu bảo mật   | Gắn thẻ | /crm/campaign/import | Gắn thẻ dữ liệu Lead trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ. | Kiểm thử bảo mật   | Đồng bộ dữ liệu sang DataLake trong vòng 5s, tự động retry khi lỗi.     | Dữ liệu được backup hàng ngày, lưu giữ tối thiểu 30 ngày. |
| Lead | Chỉ tiêu chức năng | Export  | /crm/lead/export     | Export dữ liệu Lead trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ.  | Kiểm thử hiệu năng | Xuất báo cáo chi tiết dưới dạng CSV, có xác thực hai lớp trước khi tải. | Kết quả được gửi mail và SMS cho quản trị viên phụ trách. |

<!-- image -->

## VIETTEL AI RACE

## CHỈ TIÊU CRM - RPA

TD445

Lần ban hành: 1

| Contact     | Chỉ tiêu hiệu năng   | Cập nhật   | /crm/lead/export        | Cập nhật dữ liệu Contact trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ.   | Kiểm thử hiệu năng   | Thành công với thời gian xử lý < 1s, dữ liệu đồng bộ sang hệ thống Billing.   | Kết quả được gửi mail và SMS cho quản trị viên phụ trách.   |
|-------------|----------------------|------------|-------------------------|------------------------------------------------------------------------------------------------------------------|----------------------|-------------------------------------------------------------------------------|-------------------------------------------------------------|
| Opportunity | Chỉ tiêu hiệu năng   | Import     | /crm/lead/export        | Import dữ liệu Opportunity trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ. | Kiểm thử chức năng   | Thành công với thời gian xử lý < 1s, dữ liệu đồng bộ sang hệ thống Billing.   | Dữ liệu được backup hàng ngày, lưu giữ tối thiểu 30 ngày.   |
| Contact     | Chỉ tiêu chức năng   | Gắn thẻ    | /crm/opportunity/delete | Gắn thẻ dữ liệu Contact trong CRM, bao gồm validate dữ liệu đầu vào, xử lý                                       | Kiểm thử chức năng   | Không lỗi, log đầy đủ trong AuditLog,                                         | Kết quả được gửi mail và SMS cho quản trị viên phụ trách.   |

<!-- image -->

| VIETTEL AI RACE   | TD445   |
|-------------------|---------|

|      |                    |         |                         | logic nghiệp vụ và ghi log đầy đủ.                                                                         |                    | SLA đáp ứng 99.99%.                                                         |                                                          |
|------|--------------------|---------|-------------------------|------------------------------------------------------------------------------------------------------------|--------------------|-----------------------------------------------------------------------------|----------------------------------------------------------|
| Lead | Chỉ tiêu chức năng | Gắn thẻ | /crm/opportunity/delete | Gắn thẻ dữ liệu Lead trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ. | Kiểm thử chức năng | Thành công với thời gian xử lý < 1s, dữ liệu đồng bộ sang hệ thống Billing. | Phải kiểm thử với ≥ 10.000 bản ghi để đảm bảo hiệu năng. |
| Lead | Chỉ tiêu bảo mật   | Export  | /crm/lead/export        | Export dữ liệu Lead trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ.  | Kiểm thử hiệu năng | Xuất báo cáo chi tiết dưới dạng CSV, có xác thực hai lớp trước khi tải.     | Theo chuẩn ISO 27001 và quy định bảo mật Viettel.        |

<!-- image -->

## VIETTEL AI RACE

## CHỈ TIÊU CRM - RPA

TD445

Lần ban hành: 1

| Contact   | Chỉ tiêu chức năng   | Thêm mới   | /crm/campaign/import    | Thêm mới dữ liệu Contact trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ.   | Kiểm thử hiệu năng   | Đồng bộ dữ liệu sang DataLake trong vòng 5s, tự động retry khi lỗi.     | Kết quả được gửi mail và SMS cho quản trị viên phụ trách.   |
|-----------|----------------------|------------|-------------------------|------------------------------------------------------------------------------------------------------------------|----------------------|-------------------------------------------------------------------------|-------------------------------------------------------------|
| Lead      | Chỉ tiêu hiệu năng   | Xóa        | /crm/opportunity/delete | Xóa dữ liệu Lead trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ.           | Kiểm thử chức năng   | Xuất báo cáo chi tiết dưới dạng CSV, có xác thực hai lớp trước khi tải. | Yêu cầu tích hợp với hệ thống RPA để tự động hóa quy trình. |
| Campaign  | Chỉ tiêu hiệu năng   | Xóa        | /crm/lead/add           | Xóa dữ liệu Campaign trong CRM, bao gồm validate dữ liệu                                                         | Kiểm thử chức năng   | Đồng bộ dữ liệu sang DataLake trong                                     | Phải kiểm thử với ≥ 10.000 bản ghi để đảm bảo hiệu năng.    |

<!-- image -->

| VIETTEL AI RACE   | TD445   |
|-------------------|---------|

|          |                    |        |                      | đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ.                                                             |                    | vòng 5s, tự động retry khi lỗi.                                     |                                                             |
|----------|--------------------|--------|----------------------|---------------------------------------------------------------------------------------------------------------|--------------------|---------------------------------------------------------------------|-------------------------------------------------------------|
| Lead     | Chỉ tiêu hiệu năng | Export | /crm/campaign/import | Export dữ liệu Lead trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ.     | Kiểm thử hiệu năng | Cảnh báo nếu thiếu trường bắt buộc, hệ thống rollback giao dịch.    | Yêu cầu tích hợp với hệ thống RPA để tự động hóa quy trình. |
| Campaign | Chỉ tiêu hiệu năng | Import | /crm/contact/update  | Import dữ liệu Campaign trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ. | Kiểm thử chức năng | Đồng bộ dữ liệu sang DataLake trong vòng 5s, tự động retry khi lỗi. | Kết quả được gửi mail và SMS cho quản trị viên phụ trách.   |

<!-- image -->

| VIETTEL AI RACE   | TD445   |
|-------------------|---------|

| Opportunity   | Chỉ tiêu chức năng   | Thêm mới   | /crm/lead/export        | Thêm mới dữ liệu Opportunity trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ.   | Kiểm thử chức năng   | Thành công với thời gian xử lý < 1s, dữ liệu đồng bộ sang hệ thống Billing.   | Dữ liệu được backup hàng ngày, lưu giữ tối thiểu 30 ngày.   |
|---------------|----------------------|------------|-------------------------|----------------------------------------------------------------------------------------------------------------------|----------------------|-------------------------------------------------------------------------------|-------------------------------------------------------------|
| Opportunity   | Chỉ tiêu hiệu năng   | Xóa        | /crm/campaign/import    | Xóa dữ liệu Opportunity trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ.        | Kiểm thử hiệu năng   | Xuất báo cáo chi tiết dưới dạng CSV, có xác thực hai lớp trước khi tải.       | Yêu cầu tích hợp với hệ thống RPA để tự động hóa quy trình. |
| Contact       | Chỉ tiêu chức năng   | Xóa        | /crm/opportunity/delete | Xóa dữ liệu Contact trong CRM, bao gồm validate dữ liệu                                                              | Kiểm thử             | Thành công với thời gian xử lý <                                              | Dữ liệu được backup hàng ngày,                              |

<!-- image -->

| VIETTEL AI RACE   | TD445   |
|-------------------|---------|

|             |                  |        |                     | đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ.                                                            | hiệu năng        | 1s, dữ liệu đồng bộ sang hệ thống Billing.                              | lưu giữ tối thiểu 30 ngày.                                  |
|-------------|------------------|--------|---------------------|--------------------------------------------------------------------------------------------------------------|------------------|-------------------------------------------------------------------------|-------------------------------------------------------------|
| Contact     | Chỉ tiêu bảo mật | Import | /crm/lead/export    | Import dữ liệu Contact trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ. | Kiểm thử bảo mật | Xuất báo cáo chi tiết dưới dạng CSV, có xác thực hai lớp trước khi tải. | Kết quả được gửi mail và SMS cho quản trị viên phụ trách.   |
| Opportunity | Chỉ tiêu bảo mật | Import | /crm/contact/update | Import dữ liệu Opportunity trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ                | Kiểm thử bảo mật | Cảnh báo nếu thiếu trường bắt buộc, hệ thống rollback giao dịch.        | Yêu cầu tích hợp với hệ thống RPA để tự động hóa quy trình. |

<!-- image -->

| VIETTEL AI RACE   | TD445   |
|-------------------|---------|

|          |                    |          |                     | và ghi log đầy đủ.                                                                                              |                  |                                                                         |                                                           |
|----------|--------------------|----------|---------------------|-----------------------------------------------------------------------------------------------------------------|------------------|-------------------------------------------------------------------------|-----------------------------------------------------------|
| Lead     | Chỉ tiêu chức năng | Export   | /crm/contact/update | Export dữ liệu Lead trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ.       | Kiểm thử bảo mật | Xuất báo cáo chi tiết dưới dạng CSV, có xác thực hai lớp trước khi tải. | Phải kiểm thử với ≥ 10.000 bản ghi để đảm bảo hiệu năng.  |
| Campaign | Chỉ tiêu hiệu năng | Cập nhật | /crm/lead/export    | Cập nhật dữ liệu Campaign trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ. | Kiểm thử bảo mật | Cảnh báo nếu thiếu trường bắt buộc, hệ thống rollback giao dịch.        | Dữ liệu được backup hàng ngày, lưu giữ tối thiểu 30 ngày. |

<!-- image -->

## VIETTEL AI RACE

## CHỈ TIÊU CRM - RPA

TD445

Lần ban hành: 1

| Opportunity   | Chỉ tiêu chức năng   | Thêm mới   | /crm/contact/update     | Thêm mới dữ liệu Opportunity trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ.   | Kiểm thử hiệu năng   | Không lỗi, log đầy đủ trong AuditLog, SLA đáp ứng 99.99%.        | Kết quả được gửi mail và SMS cho quản trị viên phụ trách.   |
|---------------|----------------------|------------|-------------------------|----------------------------------------------------------------------------------------------------------------------|----------------------|------------------------------------------------------------------|-------------------------------------------------------------|
| Opportunity   | Chỉ tiêu chức năng   | Export     | /crm/contact/update     | Export dữ liệu Opportunity trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ.     | Kiểm thử hiệu năng   | Cảnh báo nếu thiếu trường bắt buộc, hệ thống rollback giao dịch. | Phải kiểm thử với ≥ 10.000 bản ghi để đảm bảo hiệu năng.    |
| Contact       | Chỉ tiêu hiệu năng   | Xóa        | /crm/opportunity/delete | Xóa dữ liệu Contact trong CRM, bao gồm validate dữ liệu                                                              | Kiểm thử             | Thành công với thời gian xử lý <                                 | Theo chuẩn ISO 27001 và quy định bảo mật Viettel.           |

<!-- image -->

| VIETTEL AI RACE   | TD445   |
|-------------------|---------|

|      |                    |            |                         | đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ.                                                             | chức năng          | 1s, dữ liệu đồng bộ sang hệ thống Billing.                          |                                                           |
|------|--------------------|------------|-------------------------|---------------------------------------------------------------------------------------------------------------|--------------------|---------------------------------------------------------------------|-----------------------------------------------------------|
| Lead | Chỉ tiêu hiệu năng | Cập nhật   | /crm/opportunity/delete | Cập nhật dữ liệu Lead trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ.   | Kiểm thử chức năng | Không lỗi, log đầy đủ trong AuditLog, SLA đáp ứng 99.99%.           | Kết quả được gửi mail và SMS cho quản trị viên phụ trách. |
| Lead | Chỉ tiêu bảo mật   | Chuyển đổi | /crm/lead/export        | Chuyển đổi dữ liệu Lead trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ. | Kiểm thử bảo mật   | Đồng bộ dữ liệu sang DataLake trong vòng 5s, tự động retry khi lỗi. | Theo chuẩn ISO 27001 và quy định bảo mật Viettel.         |

| VIETTEL AI RACE   | TD445   |
|-------------------|---------|

<!-- image -->

| Campaign    | Chỉ tiêu bảo mật   | Export   | /crm/lead/add           | Export dữ liệu Campaign trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ.   | Kiểm thử chức năng   | Xuất báo cáo chi tiết dưới dạng CSV, có xác thực hai lớp trước khi tải.   | Kết quả được gửi mail và SMS cho quản trị viên phụ trách.   |
|-------------|--------------------|----------|-------------------------|-----------------------------------------------------------------------------------------------------------------|----------------------|---------------------------------------------------------------------------|-------------------------------------------------------------|
| Contact     | Chỉ tiêu chức năng | Cập nhật | /crm/lead/export        | Cập nhật dữ liệu Contact trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ.  | Kiểm thử chức năng   | Cảnh báo nếu thiếu trường bắt buộc, hệ thống rollback giao dịch.          | Phải kiểm thử với ≥ 10.000 bản ghi để đảm bảo hiệu năng.    |
| Opportunity | Chỉ tiêu bảo mật   | Gắn thẻ  | /crm/opportunity/delete | Gắn thẻ dữ liệu Opportunity trong CRM, bao gồm validate dữ liệu                                                 | Kiểm thử hiệu năng   | Không lỗi, log đầy đủ trong AuditLog,                                     | Yêu cầu tích hợp với hệ thống RPA để tự động hóa quy trình. |

<!-- image -->

| VIETTEL AI RACE   | TD445   |
|-------------------|---------|

|          |                    |            |                         | đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ.                                                                 |                  | SLA đáp ứng 99.99%.                                                         |                                                           |
|----------|--------------------|------------|-------------------------|-------------------------------------------------------------------------------------------------------------------|------------------|-----------------------------------------------------------------------------|-----------------------------------------------------------|
| Campaign | Chỉ tiêu hiệu năng | Chuyển đổi | /crm/contact/update     | Chuyển đổi dữ liệu Campaign trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ. | Kiểm thử bảo mật | Thành công với thời gian xử lý < 1s, dữ liệu đồng bộ sang hệ thống Billing. | Theo chuẩn ISO 27001 và quy định bảo mật Viettel.         |
| Campaign | Chỉ tiêu bảo mật   | Import     | /crm/opportunity/delete | Import dữ liệu Campaign trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ.     | Kiểm thử bảo mật | Thành công với thời gian xử lý < 1s, dữ liệu đồng bộ sang hệ thống Billing. | Dữ liệu được backup hàng ngày, lưu giữ tối thiểu 30 ngày. |

<!-- image -->

## VIETTEL AI RACE

## CHỈ TIÊU CRM - RPA

TD445

Lần ban hành: 1

| Campaign   | Chỉ tiêu hiệu năng   | Thêm mới   | /crm/opportunity/delete   | Thêm mới dữ liệu Campaign trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ.   | Kiểm thử hiệu năng   | Cảnh báo nếu thiếu trường bắt buộc, hệ thống rollback giao dịch.    | Dữ liệu được backup hàng ngày, lưu giữ tối thiểu 30 ngày.   |
|------------|----------------------|------------|---------------------------|-------------------------------------------------------------------------------------------------------------------|----------------------|---------------------------------------------------------------------|-------------------------------------------------------------|
| Contact    | Chỉ tiêu hiệu năng   | Xóa        | /crm/campaign/import      | Xóa dữ liệu Contact trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ.         | Kiểm thử chức năng   | Đồng bộ dữ liệu sang DataLake trong vòng 5s, tự động retry khi lỗi. | Kết quả được gửi mail và SMS cho quản trị viên phụ trách.   |
| Campaign   | Chỉ tiêu bảo mật     | Export     | /crm/lead/export          | Export dữ liệu Campaign trong CRM, bao gồm validate dữ liệu                                                       | Kiểm thử hiệu năng   | Đồng bộ dữ liệu sang DataLake trong                                 | Phải kiểm thử với ≥ 10.000 bản ghi để đảm bảo hiệu năng.    |

<!-- image -->

| VIETTEL AI RACE   | TD445   |
|-------------------|---------|

|             |                    |         |                      | đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ.                                                                 |                    | vòng 5s, tự động retry khi lỗi.                                  |                                                           |
|-------------|--------------------|---------|----------------------|-------------------------------------------------------------------------------------------------------------------|--------------------|------------------------------------------------------------------|-----------------------------------------------------------|
| Opportunity | Chỉ tiêu chức năng | Gắn thẻ | /crm/lead/add        | Gắn thẻ dữ liệu Opportunity trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ. | Kiểm thử hiệu năng | Không lỗi, log đầy đủ trong AuditLog, SLA đáp ứng 99.99%.        | Dữ liệu được backup hàng ngày, lưu giữ tối thiểu 30 ngày. |
| Contact     | Chỉ tiêu bảo mật   | Gắn thẻ | /crm/campaign/import | Gắn thẻ dữ liệu Contact trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ.     | Kiểm thử chức năng | Cảnh báo nếu thiếu trường bắt buộc, hệ thống rollback giao dịch. | Phải kiểm thử với ≥ 10.000 bản ghi để đảm bảo hiệu năng.  |

<!-- image -->

## VIETTEL AI RACE

## CHỈ TIÊU CRM - RPA

TD445

Lần ban hành: 1

| Lead    | Chỉ tiêu hiệu năng   | Cập nhật   | /crm/contact/update     | Cập nhật dữ liệu Lead trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ.   | Kiểm thử hiệu năng   | Thành công với thời gian xử lý < 1s, dữ liệu đồng bộ sang hệ thống Billing.   | Dữ liệu được backup hàng ngày, lưu giữ tối thiểu 30 ngày.   |
|---------|----------------------|------------|-------------------------|---------------------------------------------------------------------------------------------------------------|----------------------|-------------------------------------------------------------------------------|-------------------------------------------------------------|
| Lead    | Chỉ tiêu hiệu năng   | Import     | /crm/lead/export        | Import dữ liệu Lead trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ.     | Kiểm thử bảo mật     | Xuất báo cáo chi tiết dưới dạng CSV, có xác thực hai lớp trước khi tải.       | Theo chuẩn ISO 27001 và quy định bảo mật Viettel.           |
| Contact | Chỉ tiêu chức năng   | Export     | /crm/opportunity/delete | Export dữ liệu Contact trong CRM, bao gồm validate dữ liệu đầu vào, xử lý                                     | Kiểm thử bảo mật     | Không lỗi, log đầy đủ trong AuditLog,                                         | Phải kiểm thử với ≥ 10.000 bản ghi để đảm bảo hiệu năng.    |

<!-- image -->

| VIETTEL AI RACE   | TD445   |
|-------------------|---------|

|         |                    |        |                  | logic nghiệp vụ và ghi log đầy đủ.                                                                        |                    | SLA đáp ứng 99.99%.                                                         |                                                             |
|---------|--------------------|--------|------------------|-----------------------------------------------------------------------------------------------------------|--------------------|-----------------------------------------------------------------------------|-------------------------------------------------------------|
| Contact | Chỉ tiêu bảo mật   | Xóa    | /crm/lead/add    | Xóa dữ liệu Contact trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ. | Kiểm thử hiệu năng | Xuất báo cáo chi tiết dưới dạng CSV, có xác thực hai lớp trước khi tải.     | Yêu cầu tích hợp với hệ thống RPA để tự động hóa quy trình. |
| Lead    | Chỉ tiêu chức năng | Export | /crm/lead/export | Export dữ liệu Lead trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ. | Kiểm thử bảo mật   | Thành công với thời gian xử lý < 1s, dữ liệu đồng bộ sang hệ thống Billing. | Phải kiểm thử với ≥ 10.000 bản ghi để đảm bảo hiệu năng.    |

<!-- image -->

## VIETTEL AI RACE

## CHỈ TIÊU CRM - RPA

TD445

Lần ban hành: 1

| Lead    | Chỉ tiêu bảo mật   | Cập nhật   | /crm/contact/update     | Cập nhật dữ liệu Lead trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ.   | Kiểm thử hiệu năng   | Đồng bộ dữ liệu sang DataLake trong vòng 5s, tự động retry khi lỗi.   | Phải kiểm thử với ≥ 10.000 bản ghi để đảm bảo hiệu năng.   |
|---------|--------------------|------------|-------------------------|---------------------------------------------------------------------------------------------------------------|----------------------|-----------------------------------------------------------------------|------------------------------------------------------------|
| Lead    | Chỉ tiêu bảo mật   | Cập nhật   | /crm/lead/add           | Cập nhật dữ liệu Lead trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ.   | Kiểm thử chức năng   | Cảnh báo nếu thiếu trường bắt buộc, hệ thống rollback giao dịch.      | Kết quả được gửi mail và SMS cho quản trị viên phụ trách.  |
| Contact | Chỉ tiêu bảo mật   | Thêm mới   | /crm/opportunity/delete | Thêm mới dữ liệu Contact trong CRM, bao gồm validate dữ liệu đầu vào, xử lý                                   | Kiểm thử chức năng   | Xuất báo cáo chi tiết dưới dạng CSV, có xác thực                      | Dữ liệu được backup hàng ngày, lưu giữ tối thiểu 30 ngày.  |

<!-- image -->

| VIETTEL AI RACE   | TD445   |
|-------------------|---------|

|          |                    |            |               | logic nghiệp vụ và ghi log đầy đủ.                                                                                |                    | hai lớp trước khi tải.                                           |                                                           |
|----------|--------------------|------------|---------------|-------------------------------------------------------------------------------------------------------------------|--------------------|------------------------------------------------------------------|-----------------------------------------------------------|
| Campaign | Chỉ tiêu hiệu năng | Chuyển đổi | /crm/lead/add | Chuyển đổi dữ liệu Campaign trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ. | Kiểm thử chức năng | Cảnh báo nếu thiếu trường bắt buộc, hệ thống rollback giao dịch. | Phải kiểm thử với ≥ 10.000 bản ghi để đảm bảo hiệu năng.  |
| Contact  | Chỉ tiêu hiệu năng | Thêm mới   | /crm/lead/add | Thêm mới dữ liệu Contact trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ.    | Kiểm thử bảo mật   | Cảnh báo nếu thiếu trường bắt buộc, hệ thống rollback giao dịch. | Kết quả được gửi mail và SMS cho quản trị viên phụ trách. |

<!-- image -->

## VIETTEL AI RACE

## CHỈ TIÊU CRM - RPA

TD445

Lần ban hành: 1

| Contact   | Chỉ tiêu chức năng   | Export     | /crm/opportunity/delete   | Export dữ liệu Contact trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ.   | Kiểm thử chức năng   | Cảnh báo nếu thiếu trường bắt buộc, hệ thống rollback giao dịch.            | Dữ liệu được backup hàng ngày, lưu giữ tối thiểu 30 ngày.   |
|-----------|----------------------|------------|---------------------------|----------------------------------------------------------------------------------------------------------------|----------------------|-----------------------------------------------------------------------------|-------------------------------------------------------------|
| Lead      | Chỉ tiêu bảo mật     | Import     | /crm/opportunity/delete   | Import dữ liệu Lead trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ.      | Kiểm thử chức năng   | Thành công với thời gian xử lý < 1s, dữ liệu đồng bộ sang hệ thống Billing. | Yêu cầu tích hợp với hệ thống RPA để tự động hóa quy trình. |
| Campaign  | Chỉ tiêu bảo mật     | Chuyển đổi | /crm/lead/add             | Chuyển đổi dữ liệu Campaign trong CRM, bao gồm validate dữ liệu đầu vào, xử lý                                 | Kiểm thử hiệu năng   | Thành công với thời gian xử lý < 1s, dữ liệu đồng                           | Kết quả được gửi mail và SMS cho quản trị viên phụ trách.   |

<!-- image -->

| VIETTEL AI RACE   | TD445   |
|-------------------|---------|

|          |                  |            |                      | logic nghiệp vụ và ghi log đầy đủ.                                                                               |                    | bộ sang hệ thống Billing.                                               |                                                           |
|----------|------------------|------------|----------------------|------------------------------------------------------------------------------------------------------------------|--------------------|-------------------------------------------------------------------------|-----------------------------------------------------------|
| Campaign | Chỉ tiêu bảo mật | Import     | /crm/campaign/import | Import dữ liệu Campaign trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ.    | Kiểm thử hiệu năng | Đồng bộ dữ liệu sang DataLake trong vòng 5s, tự động retry khi lỗi.     | Phải kiểm thử với ≥ 10.000 bản ghi để đảm bảo hiệu năng.  |
| Contact  | Chỉ tiêu bảo mật | Chuyển đổi | /crm/lead/add        | Chuyển đổi dữ liệu Contact trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ. | Kiểm thử hiệu năng | Xuất báo cáo chi tiết dưới dạng CSV, có xác thực hai lớp trước khi tải. | Dữ liệu được backup hàng ngày, lưu giữ tối thiểu 30 ngày. |

| VIETTEL AI RACE   | TD445   |
|-------------------|---------|

<!-- image -->

| Opportunity   | Chỉ tiêu chức năng   | Xóa      | /crm/lead/add       | Xóa dữ liệu Opportunity trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ.   | Kiểm thử chức năng   | Đồng bộ dữ liệu sang DataLake trong vòng 5s, tự động retry khi lỗi.   | Kết quả được gửi mail và SMS cho quản trị viên phụ trách.   |
|---------------|----------------------|----------|---------------------|-----------------------------------------------------------------------------------------------------------------|----------------------|-----------------------------------------------------------------------|-------------------------------------------------------------|
| Contact       | Chỉ tiêu hiệu năng   | Xóa      | /crm/contact/update | Xóa dữ liệu Contact trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ.       | Kiểm thử hiệu năng   | Cảnh báo nếu thiếu trường bắt buộc, hệ thống rollback giao dịch.      | Yêu cầu tích hợp với hệ thống RPA để tự động hóa quy trình. |
| Opportunity   | Chỉ tiêu hiệu năng   | Cập nhật | /crm/lead/export    | Cập nhật dữ liệu Opportunity trong CRM, bao gồm validate dữ liệu                                                | Kiểm thử chức năng   | Thành công với thời gian xử lý < 1s, dữ liệu đồng                     | Theo chuẩn ISO 27001 và quy định bảo mật Viettel.           |

<!-- image -->

| VIETTEL AI RACE   | TD445   |
|-------------------|---------|

|         |                    |        |                         | đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ.                                                            |                    | bộ sang hệ thống Billing.                                        |                                                   |
|---------|--------------------|--------|-------------------------|--------------------------------------------------------------------------------------------------------------|--------------------|------------------------------------------------------------------|---------------------------------------------------|
| Contact | Chỉ tiêu bảo mật   | Import | /crm/lead/export        | Import dữ liệu Contact trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ. | Kiểm thử bảo mật   | Cảnh báo nếu thiếu trường bắt buộc, hệ thống rollback giao dịch. | Theo chuẩn ISO 27001 và quy định bảo mật Viettel. |
| Lead    | Chỉ tiêu hiệu năng | Export | /crm/opportunity/delete | Export dữ liệu Lead trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ.    | Kiểm thử chức năng | Cảnh báo nếu thiếu trường bắt buộc, hệ thống rollback giao dịch. | Theo chuẩn ISO 27001 và quy định bảo mật Viettel. |

<!-- image -->

## VIETTEL AI RACE

## CHỈ TIÊU CRM - RPA

TD445

Lần ban hành: 1

| Lead        | Chỉ tiêu chức năng   | Thêm mới   | /crm/campaign/import    | Thêm mới dữ liệu Lead trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ.     | Kiểm thử hiệu năng   | Xuất báo cáo chi tiết dưới dạng CSV, có xác thực hai lớp trước khi tải.   | Kết quả được gửi mail và SMS cho quản trị viên phụ trách.   |
|-------------|----------------------|------------|-------------------------|-----------------------------------------------------------------------------------------------------------------|----------------------|---------------------------------------------------------------------------|-------------------------------------------------------------|
| Campaign    | Chỉ tiêu bảo mật     | Cập nhật   | /crm/campaign/import    | Cập nhật dữ liệu Campaign trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ. | Kiểm thử hiệu năng   | Không lỗi, log đầy đủ trong AuditLog, SLA đáp ứng 99.99%.                 | Kết quả được gửi mail và SMS cho quản trị viên phụ trách.   |
| Opportunity | Chỉ tiêu hiệu năng   | Export     | /crm/opportunity/delete | Export dữ liệu Opportunity trong CRM, bao gồm validate dữ liệu                                                  | Kiểm thử bảo mật     | Cảnh báo nếu thiếu trường bắt buộc, hệ thống                              | Kết quả được gửi mail và SMS cho quản trị viên phụ trách.   |

<!-- image -->

| VIETTEL AI RACE   | TD445   |
|-------------------|---------|

|         |                    |          |                      | đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ.                                                              |                    | rollback giao dịch.                                                         |                                                          |
|---------|--------------------|----------|----------------------|----------------------------------------------------------------------------------------------------------------|--------------------|-----------------------------------------------------------------------------|----------------------------------------------------------|
| Contact | Chỉ tiêu bảo mật   | Cập nhật | /crm/contact/update  | Cập nhật dữ liệu Contact trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ. | Kiểm thử chức năng | Cảnh báo nếu thiếu trường bắt buộc, hệ thống rollback giao dịch.            | Phải kiểm thử với ≥ 10.000 bản ghi để đảm bảo hiệu năng. |
| Contact | Chỉ tiêu chức năng | Import   | /crm/campaign/import | Import dữ liệu Contact trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ.   | Kiểm thử bảo mật   | Thành công với thời gian xử lý < 1s, dữ liệu đồng bộ sang hệ thống Billing. | Theo chuẩn ISO 27001 và quy định bảo mật Viettel.        |

<!-- image -->

| VIETTEL AI RACE   | TD445   |
|-------------------|---------|

| Campaign   | Chỉ tiêu hiệu năng   | Xóa      | /crm/campaign/import    | Xóa dữ liệu Campaign trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ.      | Kiểm thử chức năng   | Cảnh báo nếu thiếu trường bắt buộc, hệ thống rollback giao dịch.   | Kết quả được gửi mail và SMS cho quản trị viên phụ trách.   |
|------------|----------------------|----------|-------------------------|-----------------------------------------------------------------------------------------------------------------|----------------------|--------------------------------------------------------------------|-------------------------------------------------------------|
| Campaign   | Chỉ tiêu hiệu năng   | Thêm mới | /crm/lead/export        | Thêm mới dữ liệu Campaign trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ. | Kiểm thử chức năng   | Cảnh báo nếu thiếu trường bắt buộc, hệ thống rollback giao dịch.   | Theo chuẩn ISO 27001 và quy định bảo mật Viettel.           |
| Contact    | Chỉ tiêu hiệu năng   | Thêm mới | /crm/opportunity/delete | Thêm mới dữ liệu Contact trong CRM, bao gồm validate dữ liệu                                                    | Kiểm thử bảo mật     | Không lỗi, log đầy đủ trong AuditLog,                              | Dữ liệu được backup hàng ngày, lưu giữ tối thiểu 30 ngày.   |

<!-- image -->

| VIETTEL AI RACE   | TD445   |
|-------------------|---------|

|             |                    |            |                      | đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ.                                                                 |                  | SLA đáp ứng 99.99%.                                                     |                                                           |
|-------------|--------------------|------------|----------------------|-------------------------------------------------------------------------------------------------------------------|------------------|-------------------------------------------------------------------------|-----------------------------------------------------------|
| Opportunity | Chỉ tiêu hiệu năng | Import     | /crm/lead/add        | Import dữ liệu Opportunity trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ.  | Kiểm thử bảo mật | Xuất báo cáo chi tiết dưới dạng CSV, có xác thực hai lớp trước khi tải. | Kết quả được gửi mail và SMS cho quản trị viên phụ trách. |
| Campaign    | Chỉ tiêu chức năng | Chuyển đổi | /crm/campaign/import | Chuyển đổi dữ liệu Campaign trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ. | Kiểm thử bảo mật | Cảnh báo nếu thiếu trường bắt buộc, hệ thống rollback giao dịch.        | Dữ liệu được backup hàng ngày, lưu giữ tối thiểu 30 ngày. |

<!-- image -->

## VIETTEL AI RACE

## CHỈ TIÊU CRM - RPA

TD445

Lần ban hành: 1

| Lead        | Chỉ tiêu hiệu năng   | Cập nhật   | /crm/contact/update   | Cập nhật dữ liệu Lead trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ.      | Kiểm thử chức năng   | Cảnh báo nếu thiếu trường bắt buộc, hệ thống rollback giao dịch.    | Phải kiểm thử với ≥ 10.000 bản ghi để đảm bảo hiệu năng.   |
|-------------|----------------------|------------|-----------------------|------------------------------------------------------------------------------------------------------------------|----------------------|---------------------------------------------------------------------|------------------------------------------------------------|
| Contact     | Chỉ tiêu chức năng   | Chuyển đổi | /crm/lead/add         | Chuyển đổi dữ liệu Contact trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ. | Kiểm thử chức năng   | Đồng bộ dữ liệu sang DataLake trong vòng 5s, tự động retry khi lỗi. | Phải kiểm thử với ≥ 10.000 bản ghi để đảm bảo hiệu năng.   |
| Opportunity | Chỉ tiêu bảo mật     | Xóa        | /crm/campaign/import  | Xóa dữ liệu Opportunity trong CRM, bao gồm validate dữ liệu đầu vào, xử lý                                       | Kiểm thử bảo mật     | Xuất báo cáo chi tiết dưới dạng CSV, có xác thực                    | Kết quả được gửi mail và SMS cho quản trị viên phụ trách.  |

<!-- image -->

| VIETTEL AI RACE   | TD445   |
|-------------------|---------|

|          |                  |        |                         | logic nghiệp vụ và ghi log đầy đủ.                                                                            |                    | hai lớp trước khi tải.                                              |                                                             |
|----------|------------------|--------|-------------------------|---------------------------------------------------------------------------------------------------------------|--------------------|---------------------------------------------------------------------|-------------------------------------------------------------|
| Campaign | Chỉ tiêu bảo mật | Export | /crm/lead/add           | Export dữ liệu Campaign trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ. | Kiểm thử hiệu năng | Đồng bộ dữ liệu sang DataLake trong vòng 5s, tự động retry khi lỗi. | Yêu cầu tích hợp với hệ thống RPA để tự động hóa quy trình. |
| Contact  | Chỉ tiêu bảo mật | Export | /crm/opportunity/delete | Export dữ liệu Contact trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ.  | Kiểm thử hiệu năng | Đồng bộ dữ liệu sang DataLake trong vòng 5s, tự động retry khi lỗi. | Yêu cầu tích hợp với hệ thống RPA để tự động hóa quy trình. |

<!-- image -->

## VIETTEL AI RACE

## CHỈ TIÊU CRM - RPA

TD445

Lần ban hành: 1

| Opportunity   | Chỉ tiêu chức năng   | Xóa    | /crm/contact/update     | Xóa dữ liệu Opportunity trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ.   | Kiểm thử chức năng   | Đồng bộ dữ liệu sang DataLake trong vòng 5s, tự động retry khi lỗi.   | Kết quả được gửi mail và SMS cho quản trị viên phụ trách.   |
|---------------|----------------------|--------|-------------------------|-----------------------------------------------------------------------------------------------------------------|----------------------|-----------------------------------------------------------------------|-------------------------------------------------------------|
| Contact       | Chỉ tiêu hiệu năng   | Import | /crm/opportunity/delete | Import dữ liệu Contact trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ.    | Kiểm thử chức năng   | Đồng bộ dữ liệu sang DataLake trong vòng 5s, tự động retry khi lỗi.   | Phải kiểm thử với ≥ 10.000 bản ghi để đảm bảo hiệu năng.    |
| Contact       | Chỉ tiêu hiệu năng   | Xóa    | /crm/lead/export        | Xóa dữ liệu Contact trong CRM, bao gồm validate dữ liệu đầu vào, xử lý                                          | Kiểm thử chức năng   | Cảnh báo nếu thiếu trường bắt buộc, hệ thống                          | Phải kiểm thử với ≥ 10.000 bản ghi để đảm bảo hiệu năng.    |

<!-- image -->

| VIETTEL AI RACE   | TD445   |
|-------------------|---------|

|             |                    |          |                         | logic nghiệp vụ và ghi log đầy đủ.                                                                                 |                    | rollback giao dịch.                                                         |                                                          |
|-------------|--------------------|----------|-------------------------|--------------------------------------------------------------------------------------------------------------------|--------------------|-----------------------------------------------------------------------------|----------------------------------------------------------|
| Opportunity | Chỉ tiêu bảo mật   | Thêm mới | /crm/campaign/import    | Thêm mới dữ liệu Opportunity trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ. | Kiểm thử chức năng | Thành công với thời gian xử lý < 1s, dữ liệu đồng bộ sang hệ thống Billing. | Phải kiểm thử với ≥ 10.000 bản ghi để đảm bảo hiệu năng. |
| Contact     | Chỉ tiêu chức năng | Import   | /crm/opportunity/delete | Import dữ liệu Contact trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ.       | Kiểm thử bảo mật   | Đồng bộ dữ liệu sang DataLake trong vòng 5s, tự động retry khi lỗi.         | Phải kiểm thử với ≥ 10.000 bản ghi để đảm bảo hiệu năng. |

<!-- image -->

| VIETTEL AI RACE   | TD445   |
|-------------------|---------|

| Lead    | Chỉ tiêu hiệu năng   | Thêm mới   | /crm/lead/add    | Thêm mới dữ liệu Lead trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ.   | Kiểm thử bảo mật   | Thành công với thời gian xử lý < 1s, dữ liệu đồng bộ sang hệ thống Billing.   | Phải kiểm thử với ≥ 10.000 bản ghi để đảm bảo hiệu năng.   |
|---------|----------------------|------------|------------------|---------------------------------------------------------------------------------------------------------------|--------------------|-------------------------------------------------------------------------------|------------------------------------------------------------|
| Contact | Chỉ tiêu hiệu năng   | Gắn thẻ    | /crm/lead/add    | Gắn thẻ dữ liệu Contact trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ. | Kiểm thử chức năng | Cảnh báo nếu thiếu trường bắt buộc, hệ thống rollback giao dịch.              | Kết quả được gửi mail và SMS cho quản trị viên phụ trách.  |
| Contact | Chỉ tiêu hiệu năng   | Chuyển đổi | /crm/lead/export | Chuyển đổi dữ liệu Contact trong CRM, bao gồm validate dữ liệu đầu vào, xử lý                                 | Kiểm thử chức năng | Xuất báo cáo chi tiết dưới dạng CSV, có xác thực                              | Phải kiểm thử với ≥ 10.000 bản ghi để đảm bảo hiệu năng.   |

<!-- image -->

| VIETTEL AI RACE   | TD445   |
|-------------------|---------|

|          |                    |        |                         | logic nghiệp vụ và ghi log đầy đủ.                                                                            |                    | hai lớp trước khi tải.                                              |                                                           |
|----------|--------------------|--------|-------------------------|---------------------------------------------------------------------------------------------------------------|--------------------|---------------------------------------------------------------------|-----------------------------------------------------------|
| Campaign | Chỉ tiêu bảo mật   | Import | /crm/opportunity/delete | Import dữ liệu Campaign trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ. | Kiểm thử chức năng | Không lỗi, log đầy đủ trong AuditLog, SLA đáp ứng 99.99%.           | Kết quả được gửi mail và SMS cho quản trị viên phụ trách. |
| Lead     | Chỉ tiêu hiệu năng | Xóa    | /crm/lead/add           | Xóa dữ liệu Lead trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ.        | Kiểm thử bảo mật   | Đồng bộ dữ liệu sang DataLake trong vòng 5s, tự động retry khi lỗi. | Phải kiểm thử với ≥ 10.000 bản ghi để đảm bảo hiệu năng.  |

<!-- image -->

| VIETTEL AI RACE   | TD445   |
|-------------------|---------|

| Lead     | Chỉ tiêu bảo mật   | Chuyển đổi   | /crm/lead/add        | Chuyển đổi dữ liệu Lead trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ.   | Kiểm thử bảo mật   | Không lỗi, log đầy đủ trong AuditLog, SLA đáp ứng 99.99%.                   | Theo chuẩn ISO 27001 và quy định bảo mật Viettel.           |
|----------|--------------------|--------------|----------------------|-----------------------------------------------------------------------------------------------------------------|--------------------|-----------------------------------------------------------------------------|-------------------------------------------------------------|
| Lead     | Chỉ tiêu chức năng | Cập nhật     | /crm/campaign/import | Cập nhật dữ liệu Lead trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ.     | Kiểm thử bảo mật   | Thành công với thời gian xử lý < 1s, dữ liệu đồng bộ sang hệ thống Billing. | Phải kiểm thử với ≥ 10.000 bản ghi để đảm bảo hiệu năng.    |
| Campaign | Chỉ tiêu chức năng | Cập nhật     | /crm/contact/update  | Cập nhật dữ liệu Campaign trong CRM, bao gồm validate dữ liệu đầu vào, xử lý                                    | Kiểm thử hiệu năng | Không lỗi, log đầy đủ trong AuditLog, SLA đáp                               | Yêu cầu tích hợp với hệ thống RPA để tự động hóa quy trình. |

<!-- image -->

| VIETTEL AI RACE   | TD445   |
|-------------------|---------|

|             |                    |          |                     | logic nghiệp vụ và ghi log đầy đủ.                                                                                 |                    | ứng 99.99%.                                                             |                                                           |
|-------------|--------------------|----------|---------------------|--------------------------------------------------------------------------------------------------------------------|--------------------|-------------------------------------------------------------------------|-----------------------------------------------------------|
| Opportunity | Chỉ tiêu hiệu năng | Thêm mới | /crm/contact/update | Thêm mới dữ liệu Opportunity trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ. | Kiểm thử chức năng | Xuất báo cáo chi tiết dưới dạng CSV, có xác thực hai lớp trước khi tải. | Phải kiểm thử với ≥ 10.000 bản ghi để đảm bảo hiệu năng.  |
| Campaign    | Chỉ tiêu chức năng | Gắn thẻ  | /crm/lead/add       | Gắn thẻ dữ liệu Campaign trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ.     | Kiểm thử hiệu năng | Đồng bộ dữ liệu sang DataLake trong vòng 5s, tự động retry khi lỗi.     | Kết quả được gửi mail và SMS cho quản trị viên phụ trách. |

<!-- image -->

| VIETTEL AI RACE   | TD445   |
|-------------------|---------|

| Lead        | Chỉ tiêu bảo mật   | Xóa        | /crm/lead/export     | Xóa dữ liệu Lead trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ.         | Kiểm thử hiệu năng   | Xuất báo cáo chi tiết dưới dạng CSV, có xác thực hai lớp trước khi tải.   | Theo chuẩn ISO 27001 và quy định bảo mật Viettel.           |
|-------------|--------------------|------------|----------------------|----------------------------------------------------------------------------------------------------------------|----------------------|---------------------------------------------------------------------------|-------------------------------------------------------------|
| Contact     | Chỉ tiêu bảo mật   | Cập nhật   | /crm/campaign/import | Cập nhật dữ liệu Contact trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ. | Kiểm thử bảo mật     | Không lỗi, log đầy đủ trong AuditLog, SLA đáp ứng 99.99%.                 | Phải kiểm thử với ≥ 10.000 bản ghi để đảm bảo hiệu năng.    |
| Opportunity | Chỉ tiêu hiệu năng | Chuyển đổi | /crm/campaign/import | Chuyển đổi dữ liệu Opportunity trong CRM, bao gồm                                                              | Kiểm thử hiệu năng   | Đồng bộ dữ liệu sang DataLake trong                                       | Yêu cầu tích hợp với hệ thống RPA để tự động hóa quy trình. |

<!-- image -->

| VIETTEL AI RACE   | TD445   |
|-------------------|---------|

|      |                    |          |                      | validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ.                                          |                    | vòng 5s, tự động retry khi lỗi.                                     |                                                             |
|------|--------------------|----------|----------------------|-------------------------------------------------------------------------------------------------------------|--------------------|---------------------------------------------------------------------|-------------------------------------------------------------|
| Lead | Chỉ tiêu hiệu năng | Cập nhật | /crm/campaign/import | Cập nhật dữ liệu Lead trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ. | Kiểm thử chức năng | Đồng bộ dữ liệu sang DataLake trong vòng 5s, tự động retry khi lỗi. | Yêu cầu tích hợp với hệ thống RPA để tự động hóa quy trình. |
| Lead | Chỉ tiêu chức năng | Export   | /crm/lead/export     | Export dữ liệu Lead trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ.   | Kiểm thử bảo mật   | Đồng bộ dữ liệu sang DataLake trong vòng 5s, tự động                | Dữ liệu được backup hàng ngày, lưu giữ tối thiểu 30 ngày.   |

<!-- image -->

| VIETTEL AI RACE   | TD445   |
|-------------------|---------|

|          |                    |            |                      |                                                                                                               |                    | retry khi lỗi.                                                   |                                                             |
|----------|--------------------|------------|----------------------|---------------------------------------------------------------------------------------------------------------|--------------------|------------------------------------------------------------------|-------------------------------------------------------------|
| Contact  | Chỉ tiêu chức năng | Import     | /crm/campaign/import | Import dữ liệu Contact trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ.  | Kiểm thử chức năng | Không lỗi, log đầy đủ trong AuditLog, SLA đáp ứng 99.99%.        | Kết quả được gửi mail và SMS cho quản trị viên phụ trách.   |
| Campaign | Chỉ tiêu hiệu năng | Export     | /crm/lead/add        | Export dữ liệu Campaign trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ. | Kiểm thử hiệu năng | Cảnh báo nếu thiếu trường bắt buộc, hệ thống rollback giao dịch. | Yêu cầu tích hợp với hệ thống RPA để tự động hóa quy trình. |
| Lead     | Chỉ tiêu hiệu năng | Chuyển đổi | /crm/lead/add        | Chuyển đổi dữ liệu Lead trong CRM, bao gồm                                                                    | Kiểm thử           | Xuất báo cáo chi tiết dưới                                       | Theo chuẩn ISO 27001 và quy định bảo mật Viettel.           |

<!-- image -->

| VIETTEL AI RACE   | TD445   |
|-------------------|---------|

|             |                    |            |                         | validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ.                                                   | chức năng          | dạng CSV, có xác thực hai lớp trước khi tải.                            |                                                           |
|-------------|--------------------|------------|-------------------------|----------------------------------------------------------------------------------------------------------------------|--------------------|-------------------------------------------------------------------------|-----------------------------------------------------------|
| Opportunity | Chỉ tiêu hiệu năng | Chuyển đổi | /crm/opportunity/delete | Chuyển đổi dữ liệu Opportunity trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ. | Kiểm thử bảo mật   | Xuất báo cáo chi tiết dưới dạng CSV, có xác thực hai lớp trước khi tải. | Dữ liệu được backup hàng ngày, lưu giữ tối thiểu 30 ngày. |
| Campaign    | Chỉ tiêu chức năng | Xóa        | /crm/contact/update     | Xóa dữ liệu Campaign trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ                              | Kiểm thử chức năng | Thành công với thời gian xử lý < 1s, dữ liệu đồng bộ sang               | Theo chuẩn ISO 27001 và quy định bảo mật Viettel.         |

<!-- image -->

## VIETTEL AI RACE

## CHỈ TIÊU CRM - RPA

TD445

Lần ban hành: 1

|             |                  |            |                      | và ghi log đầy đủ.                                                                                                |                    | hệ thống Billing.                                                   |                                                           |
|-------------|------------------|------------|----------------------|-------------------------------------------------------------------------------------------------------------------|--------------------|---------------------------------------------------------------------|-----------------------------------------------------------|
| Contact     | Chỉ tiêu bảo mật | Chuyển đổi | /crm/campaign/import | Chuyển đổi dữ liệu Contact trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ.  | Kiểm thử bảo mật   | Đồng bộ dữ liệu sang DataLake trong vòng 5s, tự động retry khi lỗi. | Dữ liệu được backup hàng ngày, lưu giữ tối thiểu 30 ngày. |
| Opportunity | Chỉ tiêu bảo mật | Gắn thẻ    | /crm/contact/update  | Gắn thẻ dữ liệu Opportunity trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ. | Kiểm thử chức năng | Cảnh báo nếu thiếu trường bắt buộc, hệ thống rollback giao dịch.    | Phải kiểm thử với ≥ 10.000 bản ghi để đảm bảo hiệu năng.  |
| Contact     | Chỉ tiêu bảo mật | Thêm mới   | /crm/campaign/import | Thêm mới dữ liệu Contact                                                                                          | Kiểm thử           | Cảnh báo nếu thiếu                                                  | Dữ liệu được backup hàng ngày,                            |

<!-- image -->

| VIETTEL AI RACE   | TD445   |
|-------------------|---------|

|             |                  |          |                     | trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ.                          | hiệu năng          | trường bắt buộc, hệ thống rollback giao dịch.             | lưu giữ tối thiểu 30 ngày.                                  |
|-------------|------------------|----------|---------------------|----------------------------------------------------------------------------------------------------------------|--------------------|-----------------------------------------------------------|-------------------------------------------------------------|
| Contact     | Chỉ tiêu bảo mật | Thêm mới | /crm/contact/update | Thêm mới dữ liệu Contact trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ. | Kiểm thử chức năng | Không lỗi, log đầy đủ trong AuditLog, SLA đáp ứng 99.99%. | Kết quả được gửi mail và SMS cho quản trị viên phụ trách.   |
| Opportunity | Chỉ tiêu bảo mật | Export   | /crm/contact/update | Export dữ liệu Opportunity trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ                  | Kiểm thử bảo mật   | Thành công với thời gian xử lý < 1s, dữ liệu đồng bộ sang | Yêu cầu tích hợp với hệ thống RPA để tự động hóa quy trình. |

<!-- image -->

| VIETTEL AI RACE   | TD445   |
|-------------------|---------|

|          |                    |          |                         | và ghi log đầy đủ.                                                                                             |                    | hệ thống Billing.                                                       |                                                             |
|----------|--------------------|----------|-------------------------|----------------------------------------------------------------------------------------------------------------|--------------------|-------------------------------------------------------------------------|-------------------------------------------------------------|
| Contact  | Chỉ tiêu hiệu năng | Thêm mới | /crm/opportunity/delete | Thêm mới dữ liệu Contact trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ. | Kiểm thử hiệu năng | Xuất báo cáo chi tiết dưới dạng CSV, có xác thực hai lớp trước khi tải. | Yêu cầu tích hợp với hệ thống RPA để tự động hóa quy trình. |
| Campaign | Chỉ tiêu chức năng | Export   | /crm/lead/export        | Export dữ liệu Campaign trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ.  | Kiểm thử hiệu năng | Cảnh báo nếu thiếu trường bắt buộc, hệ thống rollback giao dịch.        | Yêu cầu tích hợp với hệ thống RPA để tự động hóa quy trình. |
| Lead     | Chỉ tiêu bảo mật   | Import   | /crm/contact/update     | Import dữ liệu Lead trong                                                                                      | Kiểm thử           | Cảnh báo nếu thiếu                                                      | Dữ liệu được backup hàng ngày,                              |

<!-- image -->

| VIETTEL AI RACE   | TD445   |
|-------------------|---------|

|      |                    |            |                  | CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ.                           | hiệu năng          | trường bắt buộc, hệ thống rollback giao dịch.                               | lưu giữ tối thiểu 30 ngày.                                |
|------|--------------------|------------|------------------|-----------------------------------------------------------------------------------------------------------|--------------------|-----------------------------------------------------------------------------|-----------------------------------------------------------|
| Lead | Chỉ tiêu hiệu năng | Import     | /crm/lead/export | Import dữ liệu Lead trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ. | Kiểm thử chức năng | Thành công với thời gian xử lý < 1s, dữ liệu đồng bộ sang hệ thống Billing. | Kết quả được gửi mail và SMS cho quản trị viên phụ trách. |
| Lead | Chỉ tiêu bảo mật   | Chuyển đổi | /crm/lead/export | Chuyển đổi dữ liệu Lead trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ                | Kiểm thử hiệu năng | Không lỗi, log đầy đủ trong AuditLog, SLA đáp                               | Theo chuẩn ISO 27001 và quy định bảo mật Viettel.         |

<!-- image -->

| VIETTEL AI RACE   | TD445   |
|-------------------|---------|

|      |                    |          |                         | và ghi log đầy đủ.                                                                                          |                    | ứng 99.99%.                                               |                                                             |
|------|--------------------|----------|-------------------------|-------------------------------------------------------------------------------------------------------------|--------------------|-----------------------------------------------------------|-------------------------------------------------------------|
| Lead | Chỉ tiêu hiệu năng | Gắn thẻ  | /crm/lead/add           | Gắn thẻ dữ liệu Lead trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ.  | Kiểm thử chức năng | Không lỗi, log đầy đủ trong AuditLog, SLA đáp ứng 99.99%. | Yêu cầu tích hợp với hệ thống RPA để tự động hóa quy trình. |
| Lead | Chỉ tiêu hiệu năng | Cập nhật | /crm/opportunity/delete | Cập nhật dữ liệu Lead trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ. | Kiểm thử bảo mật   | Không lỗi, log đầy đủ trong AuditLog, SLA đáp ứng 99.99%. | Kết quả được gửi mail và SMS cho quản trị viên phụ trách.   |
| Lead | Chỉ tiêu bảo mật   | Export   | /crm/lead/export        | Export dữ liệu Lead trong CRM, bao gồm validate dữ liệu                                                     | Kiểm thử hiệu năng | Cảnh báo nếu thiếu trường bắt buộc,                       | Phải kiểm thử với ≥ 10.000 bản ghi để đảm bảo hiệu năng.    |

<!-- image -->

| VIETTEL AI RACE   | TD445   |
|-------------------|---------|

|          |                    |        |                     | đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ.                                                             |                    | hệ thống rollback giao dịch.                                                |                                                           |
|----------|--------------------|--------|---------------------|---------------------------------------------------------------------------------------------------------------|--------------------|-----------------------------------------------------------------------------|-----------------------------------------------------------|
| Campaign | Chỉ tiêu bảo mật   | Xóa    | /crm/contact/update | Xóa dữ liệu Campaign trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ.    | Kiểm thử chức năng | Cảnh báo nếu thiếu trường bắt buộc, hệ thống rollback giao dịch.            | Theo chuẩn ISO 27001 và quy định bảo mật Viettel.         |
| Campaign | Chỉ tiêu chức năng | Export | /crm/lead/export    | Export dữ liệu Campaign trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ. | Kiểm thử chức năng | Thành công với thời gian xử lý < 1s, dữ liệu đồng bộ sang hệ thống Billing. | Kết quả được gửi mail và SMS cho quản trị viên phụ trách. |

<!-- image -->

## VIETTEL AI RACE

## CHỈ TIÊU CRM - RPA

TD445

Lần ban hành: 1

| Contact   | Chỉ tiêu chức năng   | Import   | /crm/campaign/import   | Import dữ liệu Contact trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ.   | Kiểm thử hiệu năng   | Cảnh báo nếu thiếu trường bắt buộc, hệ thống rollback giao dịch.    | Yêu cầu tích hợp với hệ thống RPA để tự động hóa quy trình.   |
|-----------|----------------------|----------|------------------------|----------------------------------------------------------------------------------------------------------------|----------------------|---------------------------------------------------------------------|---------------------------------------------------------------|
| Lead      | Chỉ tiêu hiệu năng   | Thêm mới | /crm/lead/export       | Thêm mới dữ liệu Lead trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ.    | Kiểm thử chức năng   | Đồng bộ dữ liệu sang DataLake trong vòng 5s, tự động retry khi lỗi. | Dữ liệu được backup hàng ngày, lưu giữ tối thiểu 30 ngày.     |
| Campaign  | Chỉ tiêu hiệu năng   | Gắn thẻ  | /crm/lead/export       | Gắn thẻ dữ liệu Campaign trong CRM, bao gồm validate dữ liệu đầu vào, xử lý                                    | Kiểm thử hiệu năng   | Cảnh báo nếu thiếu trường bắt buộc, hệ thống                        | Phải kiểm thử với ≥ 10.000 bản ghi để đảm bảo hiệu năng.      |

<!-- image -->

| VIETTEL AI RACE   | TD445   |
|-------------------|---------|

|          |                    |            |                      | logic nghiệp vụ và ghi log đầy đủ.                                                                                |                    | rollback giao dịch.                                                         |                                                          |
|----------|--------------------|------------|----------------------|-------------------------------------------------------------------------------------------------------------------|--------------------|-----------------------------------------------------------------------------|----------------------------------------------------------|
| Lead     | Chỉ tiêu chức năng | Export     | /crm/campaign/import | Export dữ liệu Lead trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ.         | Kiểm thử hiệu năng | Thành công với thời gian xử lý < 1s, dữ liệu đồng bộ sang hệ thống Billing. | Phải kiểm thử với ≥ 10.000 bản ghi để đảm bảo hiệu năng. |
| Campaign | Chỉ tiêu hiệu năng | Chuyển đổi | /crm/lead/export     | Chuyển đổi dữ liệu Campaign trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ. | Kiểm thử bảo mật   | Xuất báo cáo chi tiết dưới dạng CSV, có xác thực hai lớp trước khi tải.     | Phải kiểm thử với ≥ 10.000 bản ghi để đảm bảo hiệu năng. |

<!-- image -->

## VIETTEL AI RACE

## CHỈ TIÊU CRM - RPA

TD445

Lần ban hành: 1

| Contact     | Chỉ tiêu chức năng   | Thêm mới   | /crm/contact/update   | Thêm mới dữ liệu Contact trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ.     | Kiểm thử hiệu năng   | Xuất báo cáo chi tiết dưới dạng CSV, có xác thực hai lớp trước khi tải.     | Kết quả được gửi mail và SMS cho quản trị viên phụ trách.   |
|-------------|----------------------|------------|-----------------------|--------------------------------------------------------------------------------------------------------------------|----------------------|-----------------------------------------------------------------------------|-------------------------------------------------------------|
| Opportunity | Chỉ tiêu bảo mật     | Cập nhật   | /crm/contact/update   | Cập nhật dữ liệu Opportunity trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ. | Kiểm thử hiệu năng   | Thành công với thời gian xử lý < 1s, dữ liệu đồng bộ sang hệ thống Billing. | Theo chuẩn ISO 27001 và quy định bảo mật Viettel.           |
| Campaign    | Chỉ tiêu bảo mật     | Xóa        | /crm/lead/export      | Xóa dữ liệu Campaign trong CRM, bao gồm                                                                            | Kiểm thử bảo mật     | Đồng bộ dữ liệu sang DataLake                                               | Phải kiểm thử với ≥ 10.000 bản ghi để đảm bảo hiệu năng.    |

<!-- image -->

| VIETTEL AI RACE   | TD445   |
|-------------------|---------|

|          |                  |            |                      | validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ.                                        |                    | trong vòng 5s, tự động retry khi lỗi.                               |                                                           |
|----------|------------------|------------|----------------------|-----------------------------------------------------------------------------------------------------------|--------------------|---------------------------------------------------------------------|-----------------------------------------------------------|
| Contact  | Chỉ tiêu bảo mật | Xóa        | /crm/lead/export     | Xóa dữ liệu Contact trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ. | Kiểm thử chức năng | Đồng bộ dữ liệu sang DataLake trong vòng 5s, tự động retry khi lỗi. | Dữ liệu được backup hàng ngày, lưu giữ tối thiểu 30 ngày. |
| Campaign | Chỉ tiêu bảo mật | Chuyển đổi | /crm/campaign/import | Chuyển đổi dữ liệu Campaign trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ            | Kiểm thử bảo mật   | Thành công với thời gian xử lý < 1s, dữ liệu đồng bộ sang           | Phải kiểm thử với ≥ 10.000 bản ghi để đảm bảo hiệu năng.  |

<!-- image -->

| VIETTEL AI RACE   | TD445   |
|-------------------|---------|

|             |                    |          |                      | và ghi log đầy đủ.                                                                                                 |                    | hệ thống Billing.                                                           |                                                           |
|-------------|--------------------|----------|----------------------|--------------------------------------------------------------------------------------------------------------------|--------------------|-----------------------------------------------------------------------------|-----------------------------------------------------------|
| Campaign    | Chỉ tiêu bảo mật   | Thêm mới | /crm/campaign/import | Thêm mới dữ liệu Campaign trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ.    | Kiểm thử hiệu năng | Không lỗi, log đầy đủ trong AuditLog, SLA đáp ứng 99.99%.                   | Dữ liệu được backup hàng ngày, lưu giữ tối thiểu 30 ngày. |
| Opportunity | Chỉ tiêu hiệu năng | Cập nhật | /crm/campaign/import | Cập nhật dữ liệu Opportunity trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ. | Kiểm thử chức năng | Thành công với thời gian xử lý < 1s, dữ liệu đồng bộ sang hệ thống Billing. | Dữ liệu được backup hàng ngày, lưu giữ tối thiểu 30 ngày. |

<!-- image -->

## VIETTEL AI RACE

## CHỈ TIÊU CRM - RPA

TD445

Lần ban hành: 1

| Contact   | Chỉ tiêu chức năng   | Cập nhật   | /crm/opportunity/delete   | Cập nhật dữ liệu Contact trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ.   | Kiểm thử hiệu năng   | Đồng bộ dữ liệu sang DataLake trong vòng 5s, tự động retry khi lỗi.     | Dữ liệu được backup hàng ngày, lưu giữ tối thiểu 30 ngày.   |
|-----------|----------------------|------------|---------------------------|------------------------------------------------------------------------------------------------------------------|----------------------|-------------------------------------------------------------------------|-------------------------------------------------------------|
| Campaign  | Chỉ tiêu chức năng   | Xóa        | /crm/campaign/import      | Xóa dữ liệu Campaign trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ.       | Kiểm thử bảo mật     | Xuất báo cáo chi tiết dưới dạng CSV, có xác thực hai lớp trước khi tải. | Yêu cầu tích hợp với hệ thống RPA để tự động hóa quy trình. |
| Campaign  | Chỉ tiêu hiệu năng   | Gắn thẻ    | /crm/lead/export          | Gắn thẻ dữ liệu Campaign trong CRM, bao gồm validate dữ liệu                                                     | Kiểm thử hiệu năng   | Thành công với thời gian xử lý < 1s, dữ                                 | Yêu cầu tích hợp với hệ thống RPA để tự động hóa quy trình. |

<!-- image -->

| VIETTEL AI RACE   | TD445   |
|-------------------|---------|

|             |                    |            |               | đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ.                                                                 |                    | liệu đồng bộ sang hệ thống Billing.                              |                                                   |
|-------------|--------------------|------------|---------------|-------------------------------------------------------------------------------------------------------------------|--------------------|------------------------------------------------------------------|---------------------------------------------------|
| Campaign    | Chỉ tiêu chức năng | Chuyển đổi | /crm/lead/add | Chuyển đổi dữ liệu Campaign trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ. | Kiểm thử hiệu năng | Cảnh báo nếu thiếu trường bắt buộc, hệ thống rollback giao dịch. | Theo chuẩn ISO 27001 và quy định bảo mật Viettel. |
| Opportunity | Chỉ tiêu hiệu năng | Gắn thẻ    | /crm/lead/add | Gắn thẻ dữ liệu Opportunity trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ. | Kiểm thử chức năng | Cảnh báo nếu thiếu trường bắt buộc, hệ thống rollback giao dịch. | Theo chuẩn ISO 27001 và quy định bảo mật Viettel. |

<!-- image -->

## VIETTEL AI RACE

## CHỈ TIÊU CRM - RPA

TD445

Lần ban hành: 1

| Contact   | Chỉ tiêu bảo mật   | Import   | /crm/lead/add        | Import dữ liệu Contact trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ.    | Kiểm thử bảo mật   | Thành công với thời gian xử lý < 1s, dữ liệu đồng bộ sang hệ thống Billing.   | Kết quả được gửi mail và SMS cho quản trị viên phụ trách.   |
|-----------|--------------------|----------|----------------------|-----------------------------------------------------------------------------------------------------------------|--------------------|-------------------------------------------------------------------------------|-------------------------------------------------------------|
| Campaign  | Chỉ tiêu bảo mật   | Thêm mới | /crm/campaign/import | Thêm mới dữ liệu Campaign trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ. | Kiểm thử hiệu năng | Không lỗi, log đầy đủ trong AuditLog, SLA đáp ứng 99.99%.                     | Kết quả được gửi mail và SMS cho quản trị viên phụ trách.   |
| Contact   | Chỉ tiêu hiệu năng | Xóa      | /crm/lead/add        | Xóa dữ liệu Contact trong CRM, bao gồm validate dữ liệu đầu vào, xử lý                                          | Kiểm thử bảo mật   | Đồng bộ dữ liệu sang DataLake trong                                           | Yêu cầu tích hợp với hệ thống RPA để tự động hóa quy trình. |

<!-- image -->

| VIETTEL AI RACE   | TD445   |
|-------------------|---------|

|          |                    |            |                      | logic nghiệp vụ và ghi log đầy đủ.                                                                                |                    | vòng 5s, tự động retry khi lỗi.                                             |                                                           |
|----------|--------------------|------------|----------------------|-------------------------------------------------------------------------------------------------------------------|--------------------|-----------------------------------------------------------------------------|-----------------------------------------------------------|
| Campaign | Chỉ tiêu chức năng | Chuyển đổi | /crm/lead/export     | Chuyển đổi dữ liệu Campaign trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ. | Kiểm thử chức năng | Xuất báo cáo chi tiết dưới dạng CSV, có xác thực hai lớp trước khi tải.     | Dữ liệu được backup hàng ngày, lưu giữ tối thiểu 30 ngày. |
| Lead     | Chỉ tiêu hiệu năng | Xóa        | /crm/campaign/import | Xóa dữ liệu Lead trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ.            | Kiểm thử chức năng | Thành công với thời gian xử lý < 1s, dữ liệu đồng bộ sang hệ thống Billing. | Kết quả được gửi mail và SMS cho quản trị viên phụ trách. |

<!-- image -->

| VIETTEL AI RACE   | TD445   |
|-------------------|---------|

| Lead     | Chỉ tiêu hiệu năng   | Xóa    | /crm/contact/update   | Xóa dữ liệu Lead trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ.        | Kiểm thử chức năng   | Đồng bộ dữ liệu sang DataLake trong vòng 5s, tự động retry khi lỗi.         | Dữ liệu được backup hàng ngày, lưu giữ tối thiểu 30 ngày.   |
|----------|----------------------|--------|-----------------------|---------------------------------------------------------------------------------------------------------------|----------------------|-----------------------------------------------------------------------------|-------------------------------------------------------------|
| Campaign | Chỉ tiêu hiệu năng   | Export | /crm/lead/add         | Export dữ liệu Campaign trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ. | Kiểm thử bảo mật     | Thành công với thời gian xử lý < 1s, dữ liệu đồng bộ sang hệ thống Billing. | Dữ liệu được backup hàng ngày, lưu giữ tối thiểu 30 ngày.   |
| Lead     | Chỉ tiêu chức năng   | Export | /crm/lead/add         | Export dữ liệu Lead trong CRM, bao gồm validate dữ liệu đầu vào, xử lý                                        | Kiểm thử bảo mật     | Thành công với thời gian xử lý < 1s, dữ                                     | Phải kiểm thử với ≥ 10.000 bản ghi để đảm bảo hiệu năng.    |

<!-- image -->

| VIETTEL AI RACE   | TD445   |
|-------------------|---------|

|             |                    |            |                      | logic nghiệp vụ và ghi log đầy đủ.                                                                                |                    | liệu đồng bộ sang hệ thống Billing.                                     |                                                             |
|-------------|--------------------|------------|----------------------|-------------------------------------------------------------------------------------------------------------------|--------------------|-------------------------------------------------------------------------|-------------------------------------------------------------|
| Campaign    | Chỉ tiêu chức năng | Chuyển đổi | /crm/lead/add        | Chuyển đổi dữ liệu Campaign trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ. | Kiểm thử hiệu năng | Không lỗi, log đầy đủ trong AuditLog, SLA đáp ứng 99.99%.               | Yêu cầu tích hợp với hệ thống RPA để tự động hóa quy trình. |
| Opportunity | Chỉ tiêu chức năng | Chuyển đổi | /crm/campaign/import | Chuyển đổi dữ liệu Opportunity trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ                 | Kiểm thử bảo mật   | Xuất báo cáo chi tiết dưới dạng CSV, có xác thực hai lớp trước khi tải. | Theo chuẩn ISO 27001 và quy định bảo mật Viettel.           |

<!-- image -->

| VIETTEL AI RACE   | TD445   |
|-------------------|---------|

|             |                  |          |                         | và ghi log đầy đủ.                                                                                                 |                    |                                                                     |                                                           |
|-------------|------------------|----------|-------------------------|--------------------------------------------------------------------------------------------------------------------|--------------------|---------------------------------------------------------------------|-----------------------------------------------------------|
| Opportunity | Chỉ tiêu bảo mật | Cập nhật | /crm/opportunity/delete | Cập nhật dữ liệu Opportunity trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ. | Kiểm thử chức năng | Đồng bộ dữ liệu sang DataLake trong vòng 5s, tự động retry khi lỗi. | Phải kiểm thử với ≥ 10.000 bản ghi để đảm bảo hiệu năng.  |
| Campaign    | Chỉ tiêu bảo mật | Gắn thẻ  | /crm/campaign/import    | Gắn thẻ dữ liệu Campaign trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ.     | Kiểm thử bảo mật   | Không lỗi, log đầy đủ trong AuditLog, SLA đáp ứng 99.99%.           | Kết quả được gửi mail và SMS cho quản trị viên phụ trách. |

<!-- image -->

## VIETTEL AI RACE

## CHỈ TIÊU CRM - RPA

TD445

Lần ban hành: 1

| Campaign   | Chỉ tiêu hiệu năng   | Cập nhật   | /crm/campaign/import   | Cập nhật dữ liệu Campaign trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ.   | Kiểm thử bảo mật   | Đồng bộ dữ liệu sang DataLake trong vòng 5s, tự động retry khi lỗi.   | Kết quả được gửi mail và SMS cho quản trị viên phụ trách.   |
|------------|----------------------|------------|------------------------|-------------------------------------------------------------------------------------------------------------------|--------------------|-----------------------------------------------------------------------|-------------------------------------------------------------|
| Lead       | Chỉ tiêu chức năng   | Import     | /crm/campaign/import   | Import dữ liệu Lead trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ.         | Kiểm thử chức năng | Không lỗi, log đầy đủ trong AuditLog, SLA đáp ứng 99.99%.             | Theo chuẩn ISO 27001 và quy định bảo mật Viettel.           |
| Contact    | Chỉ tiêu bảo mật     | Import     | /crm/lead/export       | Import dữ liệu Contact trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ                         | Kiểm thử hiệu năng | Xuất báo cáo chi tiết dưới dạng CSV, có xác thực                      | Kết quả được gửi mail và SMS cho quản trị viên phụ trách.   |

<!-- image -->

| VIETTEL AI RACE   | TD445   |
|-------------------|---------|

|      |                    |          |                  | và ghi log đầy đủ.                                                                                          |                    | hai lớp trước khi tải.                                                  |                                                             |
|------|--------------------|----------|------------------|-------------------------------------------------------------------------------------------------------------|--------------------|-------------------------------------------------------------------------|-------------------------------------------------------------|
| Lead | Chỉ tiêu hiệu năng | Thêm mới | /crm/lead/add    | Thêm mới dữ liệu Lead trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ. | Kiểm thử hiệu năng | Xuất báo cáo chi tiết dưới dạng CSV, có xác thực hai lớp trước khi tải. | Yêu cầu tích hợp với hệ thống RPA để tự động hóa quy trình. |
| Lead | Chỉ tiêu chức năng | Cập nhật | /crm/lead/export | Cập nhật dữ liệu Lead trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ. | Kiểm thử hiệu năng | Cảnh báo nếu thiếu trường bắt buộc, hệ thống rollback giao dịch.        | Dữ liệu được backup hàng ngày, lưu giữ tối thiểu 30 ngày.   |

<!-- image -->

## VIETTEL AI RACE

## CHỈ TIÊU CRM - RPA

TD445

Lần ban hành: 1

| Lead        | Chỉ tiêu chức năng   | Gắn thẻ   | /crm/contact/update   | Gắn thẻ dữ liệu Lead trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ.      | Kiểm thử hiệu năng   | Cảnh báo nếu thiếu trường bắt buộc, hệ thống rollback giao dịch.            | Dữ liệu được backup hàng ngày, lưu giữ tối thiểu 30 ngày.   |
|-------------|----------------------|-----------|-----------------------|-----------------------------------------------------------------------------------------------------------------|----------------------|-----------------------------------------------------------------------------|-------------------------------------------------------------|
| Campaign    | Chỉ tiêu bảo mật     | Thêm mới  | /crm/lead/export      | Thêm mới dữ liệu Campaign trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ. | Kiểm thử chức năng   | Thành công với thời gian xử lý < 1s, dữ liệu đồng bộ sang hệ thống Billing. | Theo chuẩn ISO 27001 và quy định bảo mật Viettel.           |
| Opportunity | Chỉ tiêu chức năng   | Export    | /crm/lead/add         | Export dữ liệu Opportunity trong CRM, bao gồm validate dữ liệu đầu vào, xử lý                                   | Kiểm thử chức năng   | Đồng bộ dữ liệu sang DataLake trong vòng 5s,                                | Theo chuẩn ISO 27001 và quy định bảo mật Viettel.           |

<!-- image -->

| VIETTEL AI RACE   | TD445   |
|-------------------|---------|

|          |                    |          |                         | logic nghiệp vụ và ghi log đầy đủ.                                                                          |                    | tự động retry khi lỗi.                                                      |                                                           |
|----------|--------------------|----------|-------------------------|-------------------------------------------------------------------------------------------------------------|--------------------|-----------------------------------------------------------------------------|-----------------------------------------------------------|
| Campaign | Chỉ tiêu hiệu năng | Xóa      | /crm/opportunity/delete | Xóa dữ liệu Campaign trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ.  | Kiểm thử hiệu năng | Thành công với thời gian xử lý < 1s, dữ liệu đồng bộ sang hệ thống Billing. | Kết quả được gửi mail và SMS cho quản trị viên phụ trách. |
| Lead     | Chỉ tiêu chức năng | Thêm mới | /crm/lead/add           | Thêm mới dữ liệu Lead trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ. | Kiểm thử bảo mật   | Xuất báo cáo chi tiết dưới dạng CSV, có xác thực hai lớp trước khi tải.     | Phải kiểm thử với ≥ 10.000 bản ghi để đảm bảo hiệu năng.  |

<!-- image -->

## VIETTEL AI RACE

## CHỈ TIÊU CRM - RPA

TD445

Lần ban hành: 1

| Campaign   | Chỉ tiêu bảo mật   | Export     | /crm/contact/update   | Export dữ liệu Campaign trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ.   | Kiểm thử chức năng   | Không lỗi, log đầy đủ trong AuditLog, SLA đáp ứng 99.99%.               | Kết quả được gửi mail và SMS cho quản trị viên phụ trách.   |
|------------|--------------------|------------|-----------------------|-----------------------------------------------------------------------------------------------------------------|----------------------|-------------------------------------------------------------------------|-------------------------------------------------------------|
| Lead       | Chỉ tiêu bảo mật   | Chuyển đổi | /crm/contact/update   | Chuyển đổi dữ liệu Lead trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ.   | Kiểm thử hiệu năng   | Xuất báo cáo chi tiết dưới dạng CSV, có xác thực hai lớp trước khi tải. | Phải kiểm thử với ≥ 10.000 bản ghi để đảm bảo hiệu năng.    |
| Campaign   | Chỉ tiêu chức năng | Xóa        | /crm/lead/export      | Xóa dữ liệu Campaign trong CRM, bao gồm validate dữ liệu                                                        | Kiểm thử hiệu năng   | Xuất báo cáo chi tiết dưới dạng CSV, có                                 | Phải kiểm thử với ≥ 10.000 bản ghi để đảm bảo hiệu năng.    |

<!-- image -->

| VIETTEL AI RACE   | TD445   |
|-------------------|---------|

|         |                    |         |                         | đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ.                                                             |                  | xác thực hai lớp trước khi tải.                                         |                                                          |
|---------|--------------------|---------|-------------------------|---------------------------------------------------------------------------------------------------------------|------------------|-------------------------------------------------------------------------|----------------------------------------------------------|
| Contact | Chỉ tiêu hiệu năng | Gắn thẻ | /crm/opportunity/delete | Gắn thẻ dữ liệu Contact trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ. | Kiểm thử bảo mật | Xuất báo cáo chi tiết dưới dạng CSV, có xác thực hai lớp trước khi tải. | Theo chuẩn ISO 27001 và quy định bảo mật Viettel.        |
| Lead    | Chỉ tiêu chức năng | Import  | /crm/campaign/import    | Import dữ liệu Lead trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ.     | Kiểm thử bảo mật | Cảnh báo nếu thiếu trường bắt buộc, hệ thống rollback giao dịch.        | Phải kiểm thử với ≥ 10.000 bản ghi để đảm bảo hiệu năng. |

<!-- image -->

## VIETTEL AI RACE

## CHỈ TIÊU CRM - RPA

TD445

Lần ban hành: 1

| Contact   | Chỉ tiêu bảo mật   | Gắn thẻ   | /crm/campaign/import    | Gắn thẻ dữ liệu Contact trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ.   | Kiểm thử chức năng   | Không lỗi, log đầy đủ trong AuditLog, SLA đáp ứng 99.99%.                   | Theo chuẩn ISO 27001 và quy định bảo mật Viettel.           |
|-----------|--------------------|-----------|-------------------------|-----------------------------------------------------------------------------------------------------------------|----------------------|-----------------------------------------------------------------------------|-------------------------------------------------------------|
| Lead      | Chỉ tiêu hiệu năng | Cập nhật  | /crm/opportunity/delete | Cập nhật dữ liệu Lead trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ.     | Kiểm thử chức năng   | Thành công với thời gian xử lý < 1s, dữ liệu đồng bộ sang hệ thống Billing. | Yêu cầu tích hợp với hệ thống RPA để tự động hóa quy trình. |
| Lead      | Chỉ tiêu hiệu năng | Export    | /crm/opportunity/delete | Export dữ liệu Lead trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ                          | Kiểm thử bảo mật     | Xuất báo cáo chi tiết dưới dạng CSV, có xác thực                            | Theo chuẩn ISO 27001 và quy định bảo mật Viettel.           |

<!-- image -->

| VIETTEL AI RACE   | TD445   |
|-------------------|---------|

|             |                    |          |                         | và ghi log đầy đủ.                                                                                                 |                    | hai lớp trước khi tải.                                                  |                                                             |
|-------------|--------------------|----------|-------------------------|--------------------------------------------------------------------------------------------------------------------|--------------------|-------------------------------------------------------------------------|-------------------------------------------------------------|
| Contact     | Chỉ tiêu hiệu năng | Thêm mới | /crm/opportunity/delete | Thêm mới dữ liệu Contact trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ.     | Kiểm thử bảo mật   | Xuất báo cáo chi tiết dưới dạng CSV, có xác thực hai lớp trước khi tải. | Yêu cầu tích hợp với hệ thống RPA để tự động hóa quy trình. |
| Opportunity | Chỉ tiêu bảo mật   | Thêm mới | /crm/lead/export        | Thêm mới dữ liệu Opportunity trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ. | Kiểm thử hiệu năng | Đồng bộ dữ liệu sang DataLake trong vòng 5s, tự động retry khi lỗi.     | Phải kiểm thử với ≥ 10.000 bản ghi để đảm bảo hiệu năng.    |

<!-- image -->

## VIETTEL AI RACE

## CHỈ TIÊU CRM - RPA

TD445

Lần ban hành: 1

| Contact   | Chỉ tiêu chức năng   | Cập nhật   | /crm/lead/add        | Cập nhật dữ liệu Contact trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ.   | Kiểm thử chức năng   | Thành công với thời gian xử lý < 1s, dữ liệu đồng bộ sang hệ thống Billing.   | Yêu cầu tích hợp với hệ thống RPA để tự động hóa quy trình.   |
|-----------|----------------------|------------|----------------------|------------------------------------------------------------------------------------------------------------------|----------------------|-------------------------------------------------------------------------------|---------------------------------------------------------------|
| Lead      | Chỉ tiêu chức năng   | Chuyển đổi | /crm/campaign/import | Chuyển đổi dữ liệu Lead trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ.    | Kiểm thử chức năng   | Không lỗi, log đầy đủ trong AuditLog, SLA đáp ứng 99.99%.                     | Theo chuẩn ISO 27001 và quy định bảo mật Viettel.             |
| Lead      | Chỉ tiêu chức năng   | Import     | /crm/lead/export     | Import dữ liệu Lead trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ                           | Kiểm thử bảo mật     | Cảnh báo nếu thiếu trường bắt buộc, hệ thống                                  | Yêu cầu tích hợp với hệ thống RPA để tự động hóa quy trình.   |

<!-- image -->

| VIETTEL AI RACE   | TD445   |
|-------------------|---------|

|             |                    |          |                      | và ghi log đầy đủ.                                                                                          |                    | rollback giao dịch.                                              |                                                             |
|-------------|--------------------|----------|----------------------|-------------------------------------------------------------------------------------------------------------|--------------------|------------------------------------------------------------------|-------------------------------------------------------------|
| Lead        | Chỉ tiêu bảo mật   | Cập nhật | /crm/contact/update  | Cập nhật dữ liệu Lead trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ. | Kiểm thử chức năng | Cảnh báo nếu thiếu trường bắt buộc, hệ thống rollback giao dịch. | Yêu cầu tích hợp với hệ thống RPA để tự động hóa quy trình. |
| Lead        | Chỉ tiêu hiệu năng | Export   | /crm/lead/add        | Export dữ liệu Lead trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ.   | Kiểm thử chức năng | Không lỗi, log đầy đủ trong AuditLog, SLA đáp ứng 99.99%.        | Phải kiểm thử với ≥ 10.000 bản ghi để đảm bảo hiệu năng.    |
| Opportunity | Chỉ tiêu hiệu năng | Gắn thẻ  | /crm/campaign/import | Gắn thẻ dữ liệu Opportunity trong CRM, bao gồm                                                              | Kiểm thử bảo mật   | Thành công với thời gian xử lý <                                 | Yêu cầu tích hợp với hệ thống RPA để tự động hóa quy trình. |

<!-- image -->

| VIETTEL AI RACE   | TD445   |
|-------------------|---------|

|             |                    |        |                         | validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ.                                        |                  | 1s, dữ liệu đồng bộ sang hệ thống Billing.                                  |                                                           |
|-------------|--------------------|--------|-------------------------|-----------------------------------------------------------------------------------------------------------|------------------|-----------------------------------------------------------------------------|-----------------------------------------------------------|
| Lead        | Chỉ tiêu bảo mật   | Export | /crm/opportunity/delete | Export dữ liệu Lead trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ. | Kiểm thử bảo mật | Thành công với thời gian xử lý < 1s, dữ liệu đồng bộ sang hệ thống Billing. | Dữ liệu được backup hàng ngày, lưu giữ tối thiểu 30 ngày. |
| Opportunity | Chỉ tiêu hiệu năng | Xóa    | /crm/opportunity/delete | Xóa dữ liệu Opportunity trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ                | Kiểm thử bảo mật | Thành công với thời gian xử lý < 1s, dữ liệu đồng bộ sang                   | Dữ liệu được backup hàng ngày, lưu giữ tối thiểu 30 ngày. |

<!-- image -->

| VIETTEL AI RACE   | TD445   |
|-------------------|---------|

|          |                    |          |                         | và ghi log đầy đủ.                                                                                              |                    | hệ thống Billing.                                         |                                                           |
|----------|--------------------|----------|-------------------------|-----------------------------------------------------------------------------------------------------------------|--------------------|-----------------------------------------------------------|-----------------------------------------------------------|
| Campaign | Chỉ tiêu hiệu năng | Thêm mới | /crm/opportunity/delete | Thêm mới dữ liệu Campaign trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ. | Kiểm thử chức năng | Không lỗi, log đầy đủ trong AuditLog, SLA đáp ứng 99.99%. | Phải kiểm thử với ≥ 10.000 bản ghi để đảm bảo hiệu năng.  |
| Campaign | Chỉ tiêu hiệu năng | Gắn thẻ  | /crm/lead/export        | Gắn thẻ dữ liệu Campaign trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ.  | Kiểm thử bảo mật   | Không lỗi, log đầy đủ trong AuditLog, SLA đáp ứng 99.99%. | Dữ liệu được backup hàng ngày, lưu giữ tối thiểu 30 ngày. |

<!-- image -->

## VIETTEL AI RACE

## CHỈ TIÊU CRM - RPA

TD445

Lần ban hành: 1

| Opportunity   | Chỉ tiêu bảo mật   | Thêm mới   | /crm/contact/update     | Thêm mới dữ liệu Opportunity trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ.   | Kiểm thử chức năng   | Xuất báo cáo chi tiết dưới dạng CSV, có xác thực hai lớp trước khi tải.   | Theo chuẩn ISO 27001 và quy định bảo mật Viettel.           |
|---------------|--------------------|------------|-------------------------|----------------------------------------------------------------------------------------------------------------------|----------------------|---------------------------------------------------------------------------|-------------------------------------------------------------|
| Opportunity   | Chỉ tiêu bảo mật   | Chuyển đổi | /crm/opportunity/delete | Chuyển đổi dữ liệu Opportunity trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ. | Kiểm thử chức năng   | Xuất báo cáo chi tiết dưới dạng CSV, có xác thực hai lớp trước khi tải.   | Yêu cầu tích hợp với hệ thống RPA để tự động hóa quy trình. |
| Campaign      | Chỉ tiêu bảo mật   | Cập nhật   | /crm/lead/export        | Cập nhật dữ liệu Campaign trong CRM,                                                                                 | Kiểm thử             | Đồng bộ dữ liệu sang                                                      | Yêu cầu tích hợp với hệ thống RPA                           |

<!-- image -->

| VIETTEL AI RACE   | TD445   |
|-------------------|---------|

|          |                    |         |                     | bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ.                                     | hiệu năng          | DataLake trong vòng 5s, tự động retry khi lỗi.                              | để tự động hóa quy trình.                                 |
|----------|--------------------|---------|---------------------|----------------------------------------------------------------------------------------------------------------|--------------------|-----------------------------------------------------------------------------|-----------------------------------------------------------|
| Campaign | Chỉ tiêu chức năng | Gắn thẻ | /crm/lead/add       | Gắn thẻ dữ liệu Campaign trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ. | Kiểm thử bảo mật   | Thành công với thời gian xử lý < 1s, dữ liệu đồng bộ sang hệ thống Billing. | Phải kiểm thử với ≥ 10.000 bản ghi để đảm bảo hiệu năng.  |
| Campaign | Chỉ tiêu hiệu năng | Xóa     | /crm/contact/update | Xóa dữ liệu Campaign trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ                        | Kiểm thử chức năng | Không lỗi, log đầy đủ trong AuditLog, SLA đáp                               | Kết quả được gửi mail và SMS cho quản trị viên phụ trách. |

<!-- image -->

| VIETTEL AI RACE   | TD445   |
|-------------------|---------|

|          |                    |         |                         | và ghi log đầy đủ.                                                                                           |                    | ứng 99.99%.                                                      |                                                             |
|----------|--------------------|---------|-------------------------|--------------------------------------------------------------------------------------------------------------|--------------------|------------------------------------------------------------------|-------------------------------------------------------------|
| Lead     | Chỉ tiêu bảo mật   | Gắn thẻ | /crm/contact/update     | Gắn thẻ dữ liệu Lead trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ.   | Kiểm thử chức năng | Cảnh báo nếu thiếu trường bắt buộc, hệ thống rollback giao dịch. | Yêu cầu tích hợp với hệ thống RPA để tự động hóa quy trình. |
| Contact  | Chỉ tiêu hiệu năng | Import  | /crm/opportunity/delete | Import dữ liệu Contact trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ. | Kiểm thử hiệu năng | Không lỗi, log đầy đủ trong AuditLog, SLA đáp ứng 99.99%.        | Dữ liệu được backup hàng ngày, lưu giữ tối thiểu 30 ngày.   |
| Campaign | Chỉ tiêu hiệu năng | Xóa     | /crm/opportunity/delete | Xóa dữ liệu Campaign trong CRM, bao gồm                                                                      | Kiểm thử hiệu năng | Cảnh báo nếu thiếu trường bắt buộc,                              | Yêu cầu tích hợp với hệ thống RPA để tự động hóa quy trình. |

<!-- image -->

| VIETTEL AI RACE   | TD445   |
|-------------------|---------|

|         |                    |          |                  | validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ.                                          |                  | hệ thống rollback giao dịch.                                                |                                                           |
|---------|--------------------|----------|------------------|-------------------------------------------------------------------------------------------------------------|------------------|-----------------------------------------------------------------------------|-----------------------------------------------------------|
| Contact | Chỉ tiêu chức năng | Xóa      | /crm/lead/export | Xóa dữ liệu Contact trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ.   | Kiểm thử bảo mật | Thành công với thời gian xử lý < 1s, dữ liệu đồng bộ sang hệ thống Billing. | Kết quả được gửi mail và SMS cho quản trị viên phụ trách. |
| Lead    | Chỉ tiêu chức năng | Thêm mới | /crm/lead/export | Thêm mới dữ liệu Lead trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ. | Kiểm thử bảo mật | Không lỗi, log đầy đủ trong AuditLog, SLA đáp ứng 99.99%.                   | Theo chuẩn ISO 27001 và quy định bảo mật Viettel.         |

<!-- image -->

## VIETTEL AI RACE

## CHỈ TIÊU CRM - RPA

TD445

Lần ban hành: 1

| Contact   | Chỉ tiêu hiệu năng   | Thêm mới   | /crm/contact/update   | Thêm mới dữ liệu Contact trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ.   | Kiểm thử bảo mật   | Cảnh báo nếu thiếu trường bắt buộc, hệ thống rollback giao dịch.   | Phải kiểm thử với ≥ 10.000 bản ghi để đảm bảo hiệu năng.   |
|-----------|----------------------|------------|-----------------------|------------------------------------------------------------------------------------------------------------------|--------------------|--------------------------------------------------------------------|------------------------------------------------------------|
| Contact   | Chỉ tiêu hiệu năng   | Xóa        | /crm/lead/add         | Xóa dữ liệu Contact trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ.        | Kiểm thử chức năng | Cảnh báo nếu thiếu trường bắt buộc, hệ thống rollback giao dịch.   | Dữ liệu được backup hàng ngày, lưu giữ tối thiểu 30 ngày.  |
| Campaign  | Chỉ tiêu chức năng   | Import     | /crm/contact/update   | Import dữ liệu Campaign trong CRM, bao gồm validate dữ liệu đầu vào, xử lý                                       | Kiểm thử chức năng | Xuất báo cáo chi tiết dưới dạng CSV, có xác thực                   | Kết quả được gửi mail và SMS cho quản trị viên phụ trách.  |

<!-- image -->

| VIETTEL AI RACE   | TD445   |
|-------------------|---------|

|          |                    |          |                     | logic nghiệp vụ và ghi log đầy đủ.                                                                             |                    | hai lớp trước khi tải.                                                      |                                                             |
|----------|--------------------|----------|---------------------|----------------------------------------------------------------------------------------------------------------|--------------------|-----------------------------------------------------------------------------|-------------------------------------------------------------|
| Campaign | Chỉ tiêu chức năng | Import   | /crm/contact/update | Import dữ liệu Campaign trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ.  | Kiểm thử chức năng | Thành công với thời gian xử lý < 1s, dữ liệu đồng bộ sang hệ thống Billing. | Yêu cầu tích hợp với hệ thống RPA để tự động hóa quy trình. |
| Contact  | Chỉ tiêu bảo mật   | Cập nhật | /crm/lead/add       | Cập nhật dữ liệu Contact trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ. | Kiểm thử hiệu năng | Đồng bộ dữ liệu sang DataLake trong vòng 5s, tự động retry khi lỗi.         | Dữ liệu được backup hàng ngày, lưu giữ tối thiểu 30 ngày.   |

<!-- image -->

## VIETTEL AI RACE

## CHỈ TIÊU CRM - RPA

TD445

Lần ban hành: 1

| Contact   | Chỉ tiêu chức năng   | Gắn thẻ   | /crm/lead/export        | Gắn thẻ dữ liệu Contact trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ.   | Kiểm thử bảo mật   | Đồng bộ dữ liệu sang DataLake trong vòng 5s, tự động retry khi lỗi.     | Phải kiểm thử với ≥ 10.000 bản ghi để đảm bảo hiệu năng.    |
|-----------|----------------------|-----------|-------------------------|-----------------------------------------------------------------------------------------------------------------|--------------------|-------------------------------------------------------------------------|-------------------------------------------------------------|
| Lead      | Chỉ tiêu hiệu năng   | Gắn thẻ   | /crm/contact/update     | Gắn thẻ dữ liệu Lead trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ.      | Kiểm thử chức năng | Xuất báo cáo chi tiết dưới dạng CSV, có xác thực hai lớp trước khi tải. | Dữ liệu được backup hàng ngày, lưu giữ tối thiểu 30 ngày.   |
| Lead      | Chỉ tiêu chức năng   | Xóa       | /crm/opportunity/delete | Xóa dữ liệu Lead trong CRM, bao gồm validate dữ liệu đầu vào, xử lý                                             | Kiểm thử chức năng | Cảnh báo nếu thiếu trường bắt buộc, hệ thống                            | Yêu cầu tích hợp với hệ thống RPA để tự động hóa quy trình. |

<!-- image -->

| VIETTEL AI RACE   | TD445   |
|-------------------|---------|

|             |                    |          |                         | logic nghiệp vụ và ghi log đầy đủ.                                                                                 |                    | rollback giao dịch.                                              |                                                             |
|-------------|--------------------|----------|-------------------------|--------------------------------------------------------------------------------------------------------------------|--------------------|------------------------------------------------------------------|-------------------------------------------------------------|
| Opportunity | Chỉ tiêu bảo mật   | Cập nhật | /crm/campaign/import    | Cập nhật dữ liệu Opportunity trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ. | Kiểm thử bảo mật   | Cảnh báo nếu thiếu trường bắt buộc, hệ thống rollback giao dịch. | Yêu cầu tích hợp với hệ thống RPA để tự động hóa quy trình. |
| Lead        | Chỉ tiêu chức năng | Export   | /crm/opportunity/delete | Export dữ liệu Lead trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ.          | Kiểm thử hiệu năng | Không lỗi, log đầy đủ trong AuditLog, SLA đáp ứng 99.99%.        | Kết quả được gửi mail và SMS cho quản trị viên phụ trách.   |

<!-- image -->

| VIETTEL AI RACE   | TD445   |
|-------------------|---------|

| Lead     | Chỉ tiêu hiệu năng   | Xóa    | /crm/opportunity/delete   | Xóa dữ liệu Lead trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ.        | Kiểm thử chức năng   | Đồng bộ dữ liệu sang DataLake trong vòng 5s, tự động retry khi lỗi.   | Yêu cầu tích hợp với hệ thống RPA để tự động hóa quy trình.   |
|----------|----------------------|--------|---------------------------|---------------------------------------------------------------------------------------------------------------|----------------------|-----------------------------------------------------------------------|---------------------------------------------------------------|
| Campaign | Chỉ tiêu chức năng   | Import | /crm/lead/export          | Import dữ liệu Campaign trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ. | Kiểm thử chức năng   | Cảnh báo nếu thiếu trường bắt buộc, hệ thống rollback giao dịch.      | Kết quả được gửi mail và SMS cho quản trị viên phụ trách.     |
| Contact  | Chỉ tiêu chức năng   | Import | /crm/contact/update       | Import dữ liệu Contact trong CRM, bao gồm validate dữ liệu đầu vào, xử lý                                     | Kiểm thử chức năng   | Cảnh báo nếu thiếu trường bắt buộc, hệ thống                          | Theo chuẩn ISO 27001 và quy định bảo mật Viettel.             |

<!-- image -->

| VIETTEL AI RACE   | TD445   |
|-------------------|---------|

|         |                    |          |                         | logic nghiệp vụ và ghi log đầy đủ.                                                                             |                    | rollback giao dịch.                                       |                                                           |
|---------|--------------------|----------|-------------------------|----------------------------------------------------------------------------------------------------------------|--------------------|-----------------------------------------------------------|-----------------------------------------------------------|
| Contact | Chỉ tiêu hiệu năng | Thêm mới | /crm/opportunity/delete | Thêm mới dữ liệu Contact trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ. | Kiểm thử chức năng | Không lỗi, log đầy đủ trong AuditLog, SLA đáp ứng 99.99%. | Phải kiểm thử với ≥ 10.000 bản ghi để đảm bảo hiệu năng.  |
| Lead    | Chỉ tiêu hiệu năng | Export   | /crm/lead/add           | Export dữ liệu Lead trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ.      | Kiểm thử hiệu năng | Không lỗi, log đầy đủ trong AuditLog, SLA đáp ứng 99.99%. | Dữ liệu được backup hàng ngày, lưu giữ tối thiểu 30 ngày. |

<!-- image -->

## VIETTEL AI RACE

## CHỈ TIÊU CRM - RPA

TD445

Lần ban hành: 1

| Contact     | Chỉ tiêu hiệu năng   | Xóa      | /crm/contact/update     | Xóa dữ liệu Contact trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ.   | Kiểm thử bảo mật   | Không lỗi, log đầy đủ trong AuditLog, SLA đáp ứng 99.99%.           | Phải kiểm thử với ≥ 10.000 bản ghi để đảm bảo hiệu năng.   |
|-------------|----------------------|----------|-------------------------|-------------------------------------------------------------------------------------------------------------|--------------------|---------------------------------------------------------------------|------------------------------------------------------------|
| Lead        | Chỉ tiêu chức năng   | Export   | /crm/opportunity/delete | Export dữ liệu Lead trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ.   | Kiểm thử chức năng | Đồng bộ dữ liệu sang DataLake trong vòng 5s, tự động retry khi lỗi. | Phải kiểm thử với ≥ 10.000 bản ghi để đảm bảo hiệu năng.   |
| Opportunity | Chỉ tiêu bảo mật     | Cập nhật | /crm/lead/add           | Cập nhật dữ liệu Opportunity trong CRM, bao gồm validate dữ liệu                                            | Kiểm thử chức năng | Cảnh báo nếu thiếu trường bắt buộc, hệ thống                        | Phải kiểm thử với ≥ 10.000 bản ghi để đảm bảo hiệu năng.   |

<!-- image -->

| VIETTEL AI RACE   | TD445   |
|-------------------|---------|

|             |                    |        |                         | đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ.                                                             |                    | rollback giao dịch.                                                     |                                                           |
|-------------|--------------------|--------|-------------------------|---------------------------------------------------------------------------------------------------------------|--------------------|-------------------------------------------------------------------------|-----------------------------------------------------------|
| Campaign    | Chỉ tiêu hiệu năng | Import | /crm/opportunity/delete | Import dữ liệu Campaign trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ. | Kiểm thử bảo mật   | Không lỗi, log đầy đủ trong AuditLog, SLA đáp ứng 99.99%.               | Theo chuẩn ISO 27001 và quy định bảo mật Viettel.         |
| Opportunity | Chỉ tiêu bảo mật   | Xóa    | /crm/lead/add           | Xóa dữ liệu Opportunity trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ. | Kiểm thử chức năng | Xuất báo cáo chi tiết dưới dạng CSV, có xác thực hai lớp trước khi tải. | Kết quả được gửi mail và SMS cho quản trị viên phụ trách. |

| VIETTEL AI RACE   | TD445   |
|-------------------|---------|

<!-- image -->

| Campaign   | Chỉ tiêu bảo mật   | Thêm mới   | /crm/lead/add        | Thêm mới dữ liệu Campaign trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ.   | Kiểm thử hiệu năng   | Thành công với thời gian xử lý < 1s, dữ liệu đồng bộ sang hệ thống Billing.   | Dữ liệu được backup hàng ngày, lưu giữ tối thiểu 30 ngày.   |
|------------|--------------------|------------|----------------------|-------------------------------------------------------------------------------------------------------------------|----------------------|-------------------------------------------------------------------------------|-------------------------------------------------------------|
| Lead       | Chỉ tiêu chức năng | Thêm mới   | /crm/campaign/import | Thêm mới dữ liệu Lead trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ.       | Kiểm thử bảo mật     | Không lỗi, log đầy đủ trong AuditLog, SLA đáp ứng 99.99%.                     | Yêu cầu tích hợp với hệ thống RPA để tự động hóa quy trình. |
| Lead       | Chỉ tiêu hiệu năng | Thêm mới   | /crm/campaign/import | Thêm mới dữ liệu Lead trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ                          | Kiểm thử bảo mật     | Đồng bộ dữ liệu sang DataLake trong vòng 5s,                                  | Dữ liệu được backup hàng ngày, lưu giữ tối thiểu 30 ngày.   |

<!-- image -->

| VIETTEL AI RACE   | TD445   |
|-------------------|---------|

|             |                    |            |                  | và ghi log đầy đủ.                                                                                                   |                    | tự động retry khi lỗi.                                                  |                                                   |
|-------------|--------------------|------------|------------------|----------------------------------------------------------------------------------------------------------------------|--------------------|-------------------------------------------------------------------------|---------------------------------------------------|
| Opportunity | Chỉ tiêu chức năng | Chuyển đổi | /crm/lead/export | Chuyển đổi dữ liệu Opportunity trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ. | Kiểm thử hiệu năng | Cảnh báo nếu thiếu trường bắt buộc, hệ thống rollback giao dịch.        | Theo chuẩn ISO 27001 và quy định bảo mật Viettel. |
| Opportunity | Chỉ tiêu chức năng | Xóa        | /crm/lead/add    | Xóa dữ liệu Opportunity trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ.        | Kiểm thử hiệu năng | Xuất báo cáo chi tiết dưới dạng CSV, có xác thực hai lớp trước khi tải. | Theo chuẩn ISO 27001 và quy định bảo mật Viettel. |

<!-- image -->

| VIETTEL AI RACE   | TD445   |
|-------------------|---------|

| Opportunity   | Chỉ tiêu hiệu năng   | Chuyển đổi   | /crm/lead/add    | Chuyển đổi dữ liệu Opportunity trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ.   | Kiểm thử chức năng   | Thành công với thời gian xử lý < 1s, dữ liệu đồng bộ sang hệ thống Billing.   | Dữ liệu được backup hàng ngày, lưu giữ tối thiểu 30 ngày.   |
|---------------|----------------------|--------------|------------------|------------------------------------------------------------------------------------------------------------------------|----------------------|-------------------------------------------------------------------------------|-------------------------------------------------------------|
| Contact       | Chỉ tiêu bảo mật     | Cập nhật     | /crm/lead/add    | Cập nhật dữ liệu Contact trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ.         | Kiểm thử hiệu năng   | Không lỗi, log đầy đủ trong AuditLog, SLA đáp ứng 99.99%.                     | Yêu cầu tích hợp với hệ thống RPA để tự động hóa quy trình. |
| Opportunity   | Chỉ tiêu hiệu năng   | Export       | /crm/lead/export | Export dữ liệu Opportunity trong CRM, bao gồm                                                                          | Kiểm thử             | Không lỗi, log đầy đủ trong                                                   | Theo chuẩn ISO 27001 và quy định bảo mật Viettel.           |

<!-- image -->

| VIETTEL AI RACE   | TD445   |
|-------------------|---------|

|         |                    |            |                         | validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ.                                             | hiệu năng          | AuditLog, SLA đáp ứng 99.99%.                                               |                                                           |
|---------|--------------------|------------|-------------------------|----------------------------------------------------------------------------------------------------------------|--------------------|-----------------------------------------------------------------------------|-----------------------------------------------------------|
| Contact | Chỉ tiêu bảo mật   | Cập nhật   | /crm/contact/update     | Cập nhật dữ liệu Contact trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ. | Kiểm thử hiệu năng | Thành công với thời gian xử lý < 1s, dữ liệu đồng bộ sang hệ thống Billing. | Theo chuẩn ISO 27001 và quy định bảo mật Viettel.         |
| Lead    | Chỉ tiêu hiệu năng | Chuyển đổi | /crm/opportunity/delete | Chuyển đổi dữ liệu Lead trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ.  | Kiểm thử bảo mật   | Đồng bộ dữ liệu sang DataLake trong vòng 5s, tự động                        | Kết quả được gửi mail và SMS cho quản trị viên phụ trách. |

<!-- image -->

| VIETTEL AI RACE   | TD445   |
|-------------------|---------|

|             |                  |          |                      |                                                                                                                    |                    | retry khi lỗi.                                                      |                                                             |
|-------------|------------------|----------|----------------------|--------------------------------------------------------------------------------------------------------------------|--------------------|---------------------------------------------------------------------|-------------------------------------------------------------|
| Opportunity | Chỉ tiêu bảo mật | Xóa      | /crm/campaign/import | Xóa dữ liệu Opportunity trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ.      | Kiểm thử chức năng | Không lỗi, log đầy đủ trong AuditLog, SLA đáp ứng 99.99%.           | Yêu cầu tích hợp với hệ thống RPA để tự động hóa quy trình. |
| Opportunity | Chỉ tiêu bảo mật | Thêm mới | /crm/lead/export     | Thêm mới dữ liệu Opportunity trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ. | Kiểm thử hiệu năng | Đồng bộ dữ liệu sang DataLake trong vòng 5s, tự động retry khi lỗi. | Kết quả được gửi mail và SMS cho quản trị viên phụ trách.   |

<!-- image -->

## VIETTEL AI RACE

## CHỈ TIÊU CRM - RPA

TD445

Lần ban hành: 1

| Lead        | Chỉ tiêu hiệu năng   | Xóa        | /crm/contact/update     | Xóa dữ liệu Lead trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ.               | Kiểm thử chức năng   | Thành công với thời gian xử lý < 1s, dữ liệu đồng bộ sang hệ thống Billing.   | Yêu cầu tích hợp với hệ thống RPA để tự động hóa quy trình.   |
|-------------|----------------------|------------|-------------------------|----------------------------------------------------------------------------------------------------------------------|----------------------|-------------------------------------------------------------------------------|---------------------------------------------------------------|
| Opportunity | Chỉ tiêu bảo mật     | Chuyển đổi | /crm/opportunity/delete | Chuyển đổi dữ liệu Opportunity trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ. | Kiểm thử chức năng   | Cảnh báo nếu thiếu trường bắt buộc, hệ thống rollback giao dịch.              | Dữ liệu được backup hàng ngày, lưu giữ tối thiểu 30 ngày.     |
| Campaign    | Chỉ tiêu hiệu năng   | Cập nhật   | /crm/lead/add           | Cập nhật dữ liệu Campaign trong CRM, bao gồm                                                                         | Kiểm thử             | Đồng bộ dữ liệu sang DataLake                                                 | Phải kiểm thử với ≥ 10.000 bản ghi để đảm bảo hiệu năng.      |

<!-- image -->

| VIETTEL AI RACE   | TD445   |
|-------------------|---------|

|             |                    |         |                  | validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ.                                               | hiệu năng          | trong vòng 5s, tự động retry khi lỗi.                     |                                                           |
|-------------|--------------------|---------|------------------|------------------------------------------------------------------------------------------------------------------|--------------------|-----------------------------------------------------------|-----------------------------------------------------------|
| Opportunity | Chỉ tiêu hiệu năng | Import  | /crm/lead/add    | Import dữ liệu Opportunity trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ. | Kiểm thử hiệu năng | Không lỗi, log đầy đủ trong AuditLog, SLA đáp ứng 99.99%. | Kết quả được gửi mail và SMS cho quản trị viên phụ trách. |
| Opportunity | Chỉ tiêu hiệu năng | Gắn thẻ | /crm/lead/export | Gắn thẻ dữ liệu Opportunity trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ                   | Kiểm thử bảo mật   | Không lỗi, log đầy đủ trong AuditLog, SLA đáp ứng 99.99%. | Dữ liệu được backup hàng ngày, lưu giữ tối thiểu 30 ngày. |

<!-- image -->

| VIETTEL AI RACE   | TD445   |
|-------------------|---------|

|             |                    |          |                     | và ghi log đầy đủ.                                                                                               |                    |                                                                             |                                                           |
|-------------|--------------------|----------|---------------------|------------------------------------------------------------------------------------------------------------------|--------------------|-----------------------------------------------------------------------------|-----------------------------------------------------------|
| Lead        | Chỉ tiêu chức năng | Cập nhật | /crm/lead/add       | Cập nhật dữ liệu Lead trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ.      | Kiểm thử chức năng | Thành công với thời gian xử lý < 1s, dữ liệu đồng bộ sang hệ thống Billing. | Theo chuẩn ISO 27001 và quy định bảo mật Viettel.         |
| Opportunity | Chỉ tiêu hiệu năng | Import   | /crm/lead/export    | Import dữ liệu Opportunity trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ. | Kiểm thử hiệu năng | Xuất báo cáo chi tiết dưới dạng CSV, có xác thực hai lớp trước khi tải.     | Dữ liệu được backup hàng ngày, lưu giữ tối thiểu 30 ngày. |
| Contact     | Chỉ tiêu bảo mật   | Xóa      | /crm/contact/update | Xóa dữ liệu Contact trong                                                                                        | Kiểm thử           | Cảnh báo nếu thiếu                                                          | Kết quả được gửi mail và SMS cho                          |

<!-- image -->

| VIETTEL AI RACE   | TD445   |
|-------------------|---------|

|      |                  |         |                         | CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ.                           | hiệu năng          | trường bắt buộc, hệ thống rollback giao dịch.                       | quản trị viên phụ trách.                                  |
|------|------------------|---------|-------------------------|-----------------------------------------------------------------------------------------------------------|--------------------|---------------------------------------------------------------------|-----------------------------------------------------------|
| Lead | Chỉ tiêu bảo mật | Import  | /crm/opportunity/delete | Import dữ liệu Lead trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ. | Kiểm thử hiệu năng | Đồng bộ dữ liệu sang DataLake trong vòng 5s, tự động retry khi lỗi. | Dữ liệu được backup hàng ngày, lưu giữ tối thiểu 30 ngày. |
| Lead | Chỉ tiêu bảo mật | Gắn thẻ | /crm/lead/add           | Gắn thẻ dữ liệu Lead trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ                   | Kiểm thử bảo mật   | Thành công với thời gian xử lý < 1s, dữ liệu đồng bộ sang           | Dữ liệu được backup hàng ngày, lưu giữ tối thiểu 30 ngày. |

<!-- image -->

| VIETTEL AI RACE   | TD445   |
|-------------------|---------|

|          |                    |          |                      | và ghi log đầy đủ.                                                                                              |                    | hệ thống Billing.                                                       |                                                           |
|----------|--------------------|----------|----------------------|-----------------------------------------------------------------------------------------------------------------|--------------------|-------------------------------------------------------------------------|-----------------------------------------------------------|
| Lead     | Chỉ tiêu hiệu năng | Gắn thẻ  | /crm/lead/export     | Gắn thẻ dữ liệu Lead trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ.      | Kiểm thử hiệu năng | Xuất báo cáo chi tiết dưới dạng CSV, có xác thực hai lớp trước khi tải. | Kết quả được gửi mail và SMS cho quản trị viên phụ trách. |
| Campaign | Chỉ tiêu chức năng | Thêm mới | /crm/campaign/import | Thêm mới dữ liệu Campaign trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ. | Kiểm thử chức năng | Xuất báo cáo chi tiết dưới dạng CSV, có xác thực hai lớp trước khi tải. | Theo chuẩn ISO 27001 và quy định bảo mật Viettel.         |

<!-- image -->

## VIETTEL AI RACE

## CHỈ TIÊU CRM - RPA

TD445

Lần ban hành: 1

| Opportunity   | Chỉ tiêu bảo mật   | Chuyển đổi   | /crm/opportunity/delete   | Chuyển đổi dữ liệu Opportunity trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ.   | Kiểm thử bảo mật   | Cảnh báo nếu thiếu trường bắt buộc, hệ thống rollback giao dịch.   | Phải kiểm thử với ≥ 10.000 bản ghi để đảm bảo hiệu năng.   |
|---------------|--------------------|--------------|---------------------------|------------------------------------------------------------------------------------------------------------------------|--------------------|--------------------------------------------------------------------|------------------------------------------------------------|
| Opportunity   | Chỉ tiêu bảo mật   | Export       | /crm/opportunity/delete   | Export dữ liệu Opportunity trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ.       | Kiểm thử chức năng | Cảnh báo nếu thiếu trường bắt buộc, hệ thống rollback giao dịch.   | Dữ liệu được backup hàng ngày, lưu giữ tối thiểu 30 ngày.  |
| Opportunity   | Chỉ tiêu bảo mật   | Xóa          | /crm/campaign/import      | Xóa dữ liệu Opportunity trong CRM, bao gồm                                                                             | Kiểm thử bảo mật   | Đồng bộ dữ liệu sang DataLake                                      | Kết quả được gửi mail và SMS cho                           |

<!-- image -->

| VIETTEL AI RACE   | TD445   |
|-------------------|---------|

|          |                    |        |                     | validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ.                                            |                    | trong vòng 5s, tự động retry khi lỗi.                                   | quản trị viên phụ trách.                                  |
|----------|--------------------|--------|---------------------|---------------------------------------------------------------------------------------------------------------|--------------------|-------------------------------------------------------------------------|-----------------------------------------------------------|
| Lead     | Chỉ tiêu hiệu năng | Xóa    | /crm/lead/add       | Xóa dữ liệu Lead trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ.        | Kiểm thử hiệu năng | Cảnh báo nếu thiếu trường bắt buộc, hệ thống rollback giao dịch.        | Phải kiểm thử với ≥ 10.000 bản ghi để đảm bảo hiệu năng.  |
| Campaign | Chỉ tiêu bảo mật   | Export | /crm/contact/update | Export dữ liệu Campaign trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ. | Kiểm thử bảo mật   | Xuất báo cáo chi tiết dưới dạng CSV, có xác thực hai lớp trước khi tải. | Dữ liệu được backup hàng ngày, lưu giữ tối thiểu 30 ngày. |

<!-- image -->

## VIETTEL AI RACE

## CHỈ TIÊU CRM - RPA

TD445

Lần ban hành: 1

| Campaign    | Chỉ tiêu chức năng   | Chuyển đổi   | /crm/contact/update   | Chuyển đổi dữ liệu Campaign trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ.    | Kiểm thử bảo mật   | Đồng bộ dữ liệu sang DataLake trong vòng 5s, tự động retry khi lỗi.   | Yêu cầu tích hợp với hệ thống RPA để tự động hóa quy trình.   |
|-------------|----------------------|--------------|-----------------------|----------------------------------------------------------------------------------------------------------------------|--------------------|-----------------------------------------------------------------------|---------------------------------------------------------------|
| Opportunity | Chỉ tiêu hiệu năng   | Chuyển đổi   | /crm/lead/export      | Chuyển đổi dữ liệu Opportunity trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ. | Kiểm thử hiệu năng | Không lỗi, log đầy đủ trong AuditLog, SLA đáp ứng 99.99%.             | Phải kiểm thử với ≥ 10.000 bản ghi để đảm bảo hiệu năng.      |
| Campaign    | Chỉ tiêu chức năng   | Thêm mới     | /crm/lead/add         | Thêm mới dữ liệu Campaign trong CRM, bao gồm                                                                         | Kiểm thử           | Đồng bộ dữ liệu sang DataLake                                         | Kết quả được gửi mail và SMS cho                              |

<!-- image -->

| VIETTEL AI RACE   | TD445   |
|-------------------|---------|

|          |                    |         |                     | validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ.                                             | chức năng          | trong vòng 5s, tự động retry khi lỗi.                               | quản trị viên phụ trách.                                 |
|----------|--------------------|---------|---------------------|----------------------------------------------------------------------------------------------------------------|--------------------|---------------------------------------------------------------------|----------------------------------------------------------|
| Lead     | Chỉ tiêu chức năng | Export  | /crm/contact/update | Export dữ liệu Lead trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ.      | Kiểm thử hiệu năng | Cảnh báo nếu thiếu trường bắt buộc, hệ thống rollback giao dịch.    | Phải kiểm thử với ≥ 10.000 bản ghi để đảm bảo hiệu năng. |
| Campaign | Chỉ tiêu hiệu năng | Gắn thẻ | /crm/contact/update | Gắn thẻ dữ liệu Campaign trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ. | Kiểm thử chức năng | Đồng bộ dữ liệu sang DataLake trong vòng 5s, tự động retry khi lỗi. | Theo chuẩn ISO 27001 và quy định bảo mật Viettel.        |

<!-- image -->

## VIETTEL AI RACE

## CHỈ TIÊU CRM - RPA

TD445

Lần ban hành: 1

| Contact   | Chỉ tiêu chức năng   | Xóa    | /crm/lead/add        | Xóa dữ liệu Contact trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ.    | Kiểm thử bảo mật   | Thành công với thời gian xử lý < 1s, dữ liệu đồng bộ sang hệ thống Billing.   | Theo chuẩn ISO 27001 và quy định bảo mật Viettel.           |
|-----------|----------------------|--------|----------------------|--------------------------------------------------------------------------------------------------------------|--------------------|-------------------------------------------------------------------------------|-------------------------------------------------------------|
| Contact   | Chỉ tiêu hiệu năng   | Import | /crm/campaign/import | Import dữ liệu Contact trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ. | Kiểm thử chức năng | Đồng bộ dữ liệu sang DataLake trong vòng 5s, tự động retry khi lỗi.           | Yêu cầu tích hợp với hệ thống RPA để tự động hóa quy trình. |
| Contact   | Chỉ tiêu hiệu năng   | Export | /crm/lead/export     | Export dữ liệu Contact trong CRM, bao gồm validate dữ liệu đầu vào, xử lý                                    | Kiểm thử hiệu năng | Xuất báo cáo chi tiết dưới dạng CSV, có                                       | Yêu cầu tích hợp với hệ thống RPA để tự động hóa quy trình. |

<!-- image -->

| VIETTEL AI RACE   | TD445   |
|-------------------|---------|

|             |                    |         |                     | logic nghiệp vụ và ghi log đầy đủ.                                                                                |                    | xác thực hai lớp trước khi tải.                                             |                                                           |
|-------------|--------------------|---------|---------------------|-------------------------------------------------------------------------------------------------------------------|--------------------|-----------------------------------------------------------------------------|-----------------------------------------------------------|
| Opportunity | Chỉ tiêu bảo mật   | Gắn thẻ | /crm/contact/update | Gắn thẻ dữ liệu Opportunity trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ. | Kiểm thử hiệu năng | Thành công với thời gian xử lý < 1s, dữ liệu đồng bộ sang hệ thống Billing. | Theo chuẩn ISO 27001 và quy định bảo mật Viettel.         |
| Lead        | Chỉ tiêu chức năng | Import  | /crm/lead/export    | Import dữ liệu Lead trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ.         | Kiểm thử bảo mật   | Không lỗi, log đầy đủ trong AuditLog, SLA đáp ứng 99.99%.                   | Kết quả được gửi mail và SMS cho quản trị viên phụ trách. |

<!-- image -->

## VIETTEL AI RACE

## CHỈ TIÊU CRM - RPA

TD445

Lần ban hành: 1

| Contact     | Chỉ tiêu hiệu năng   | Xóa      | /crm/opportunity/delete   | Xóa dữ liệu Contact trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ.          | Kiểm thử chức năng   | Cảnh báo nếu thiếu trường bắt buộc, hệ thống rollback giao dịch.   | Dữ liệu được backup hàng ngày, lưu giữ tối thiểu 30 ngày.   |
|-------------|----------------------|----------|---------------------------|--------------------------------------------------------------------------------------------------------------------|----------------------|--------------------------------------------------------------------|-------------------------------------------------------------|
| Opportunity | Chỉ tiêu hiệu năng   | Thêm mới | /crm/lead/export          | Thêm mới dữ liệu Opportunity trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ. | Kiểm thử chức năng   | Cảnh báo nếu thiếu trường bắt buộc, hệ thống rollback giao dịch.   | Dữ liệu được backup hàng ngày, lưu giữ tối thiểu 30 ngày.   |
| Campaign    | Chỉ tiêu bảo mật     | Thêm mới | /crm/opportunity/delete   | Thêm mới dữ liệu Campaign trong CRM, bao gồm validate dữ liệu                                                      | Kiểm thử hiệu năng   | Đồng bộ dữ liệu sang DataLake trong                                | Kết quả được gửi mail và SMS cho quản trị viên phụ trách.   |

<!-- image -->

| VIETTEL AI RACE   | TD445   |
|-------------------|---------|

|             |                    |          |                         | đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ.                                                                  |                    | vòng 5s, tự động retry khi lỗi.                                             |                                                           |
|-------------|--------------------|----------|-------------------------|--------------------------------------------------------------------------------------------------------------------|--------------------|-----------------------------------------------------------------------------|-----------------------------------------------------------|
| Opportunity | Chỉ tiêu bảo mật   | Thêm mới | /crm/lead/export        | Thêm mới dữ liệu Opportunity trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ. | Kiểm thử chức năng | Thành công với thời gian xử lý < 1s, dữ liệu đồng bộ sang hệ thống Billing. | Dữ liệu được backup hàng ngày, lưu giữ tối thiểu 30 ngày. |
| Lead        | Chỉ tiêu hiệu năng | Export   | /crm/opportunity/delete | Export dữ liệu Lead trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ.          | Kiểm thử chức năng | Thành công với thời gian xử lý < 1s, dữ liệu đồng bộ sang                   | Kết quả được gửi mail và SMS cho quản trị viên phụ trách. |

<!-- image -->

| VIETTEL AI RACE   | TD445   |
|-------------------|---------|

|          |                    |            |                         |                                                                                                                   |                    | hệ thống Billing.                                         |                                                           |
|----------|--------------------|------------|-------------------------|-------------------------------------------------------------------------------------------------------------------|--------------------|-----------------------------------------------------------|-----------------------------------------------------------|
| Campaign | Chỉ tiêu bảo mật   | Xóa        | /crm/lead/add           | Xóa dữ liệu Campaign trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ.        | Kiểm thử chức năng | Không lỗi, log đầy đủ trong AuditLog, SLA đáp ứng 99.99%. | Kết quả được gửi mail và SMS cho quản trị viên phụ trách. |
| Campaign | Chỉ tiêu chức năng | Chuyển đổi | /crm/opportunity/delete | Chuyển đổi dữ liệu Campaign trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ. | Kiểm thử chức năng | Không lỗi, log đầy đủ trong AuditLog, SLA đáp ứng 99.99%. | Theo chuẩn ISO 27001 và quy định bảo mật Viettel.         |

<!-- image -->

| VIETTEL AI RACE   | TD445   |
|-------------------|---------|

| Contact     | Chỉ tiêu hiệu năng   | Export   | /crm/lead/add    | Export dữ liệu Contact trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ.       | Kiểm thử bảo mật   | Cảnh báo nếu thiếu trường bắt buộc, hệ thống rollback giao dịch.   | Yêu cầu tích hợp với hệ thống RPA để tự động hóa quy trình.   |
|-------------|----------------------|----------|------------------|--------------------------------------------------------------------------------------------------------------------|--------------------|--------------------------------------------------------------------|---------------------------------------------------------------|
| Opportunity | Chỉ tiêu hiệu năng   | Thêm mới | /crm/lead/export | Thêm mới dữ liệu Opportunity trong CRM, bao gồm validate dữ liệu đầu vào, xử lý logic nghiệp vụ và ghi log đầy đủ. | Kiểm thử hiệu năng | Cảnh báo nếu thiếu trường bắt buộc, hệ thống rollback giao dịch.   | Yêu cầu tích hợp với hệ thống RPA để tự động hóa quy trình.   |