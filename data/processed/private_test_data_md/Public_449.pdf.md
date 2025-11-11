<!-- image -->

## VIETTEL AI RACE

## BÁO CÁO HỆ THỐNG &amp; LOG

TD449

Lần ban hành: 1

| Module   | Loại log       | Mức độ   | Hành động          | Mô tả chi tiết                                                                                        | Kết quả               | Ghi chú                   |
|----------|----------------|----------|--------------------|-------------------------------------------------------------------------------------------------------|-----------------------|---------------------------|
| RPA      | TransactionLog | Critical | Xuất log           | Hệ thống RPA Xuất log loại TransactionLog với mức Critical, dữ liệu lưu trữ tối thiểu 90 ngày.        | Có chỉ số thống kê    | Gửi log sang ELK          |
| CRM      | TransactionLog | Error    | Nén và lưu trữ log | Hệ thống CRM Nén và lưu trữ log loại TransactionLog với mức Error, dữ liệu lưu trữ tối thiểu 90 ngày. | Có chỉ số thống kê    | Theo chuẩn syslog RFC5424 |
| Billing  | PerformanceLog | Error    | Phân tích log      | Hệ thống Billing Phân tích log loại PerformanceLog với mức Error, dữ liệu lưu trữ tối thiểu 90 ngày.  | Không mất mát dữ liệu | Có dashboard Grafana      |
| Infra    | TransactionLog | Critical | Xóa log            | Hệ thống Infra Xóa log loại TransactionLog với mức Critical, dữ liệu lưu trữ tối thiểu 90 ngày.       | Không mất mát dữ liệu | Theo chuẩn syslog RFC5424 |
| QA       | AuditLog       | Warning  | Xuất               | Hệ thống QA Xuất                                                                                      | Không                 | Có dashboard              |

<!-- image -->

| VIETTEL AI RACE   | TD449   |
|-------------------|---------|

|         |                |         | log                | log loại AuditLog với mức Warning, dữ liệu lưu trữ tối thiểu 90 ngày.                                  | mất mát dữ liệu            | Grafana                      |
|---------|----------------|---------|--------------------|--------------------------------------------------------------------------------------------------------|----------------------------|------------------------------|
| IPCC    | PerformanceLog | Fatal   | Nén và lưu trữ log | Hệ thống IPCC Nén và lưu trữ log loại PerformanceLog với mức Fatal, dữ liệu lưu trữ tối thiểu 90 ngày. | Tích hợp cảnh báo realtime | Có dashboard Grafana         |
| IPCC    | ErrorLog       | Info    | Xóa log            | Hệ thống IPCC Xóa log loại ErrorLog với mức Info, dữ liệu lưu trữ tối thiểu 90 ngày.                   | Log được mã hóa AES- 256   | Có dashboard Grafana         |
| Billing | ErrorLog       | Warning | Xóa log            | Hệ thống Billing Xóa log loại ErrorLog với mức Warning, dữ liệu lưu trữ tối thiểu 90 ngày.             | Có thể truy xuất khi cần   | Tự động xóa log sau 180 ngày |
| CRM     | AuditLog       | Error   | Gửi log sang SIEM  | Hệ thống CRM Gửi log sang SIEM loại AuditLog với mức Error, dữ liệu lưu trữ tối thiểu 90 ngày.         | Tích hợp cảnh báo realtime | Theo chuẩn syslog RFC5424    |
| Infra   | AuditLog       | Error   | Gửi log            | Hệ thống Infra Gửi log sang SIEM loại                                                                  | Không mất mát              | Theo chuẩn syslog            |

<!-- image -->

| VIETTEL AI RACE   | TD449   |
|-------------------|---------|

|         |                |       | sang SIEM          | AuditLog với mức Error, dữ liệu lưu trữ tối thiểu 90 ngày.                                     | dữ liệu                  | RFC5424                      |
|---------|----------------|-------|--------------------|------------------------------------------------------------------------------------------------|--------------------------|------------------------------|
| RPA     | PerformanceLog | Fatal | Xuất log           | Hệ thống RPA Xuất log loại PerformanceLog với mức Fatal, dữ liệu lưu trữ tối thiểu 90 ngày.    | Có thể truy xuất khi cần | Tự động xóa log sau 180 ngày |
| QA      | AccessLog      | Info  | Nén và lưu trữ log | Hệ thống QA Nén và lưu trữ log loại AccessLog với mức Info, dữ liệu lưu trữ tối thiểu 90 ngày. | Log được mã hóa AES- 256 | Tự động xóa log sau 180 ngày |
| Billing | ErrorLog       | Info  | Xuất log           | Hệ thống Billing Xuất log loại ErrorLog với mức Info, dữ liệu lưu trữ tối thiểu 90 ngày.       | Có chỉ số thống kê       | Phân quyền chi tiết          |
| IVR     | TransactionLog | Fatal | Xóa log            | Hệ thống IVR Xóa log loại TransactionLog với mức Fatal, dữ liệu lưu trữ tối thiểu 90 ngày.     | Có chỉ số thống kê       | Phân quyền chi tiết          |
| IVR     | PerformanceLog | Error | Xóa log            | Hệ thống IVR Xóa log loại PerformanceLog                                                       | Có chỉ số thống          | Gửi log sang ELK             |

<!-- image -->

| VIETTEL AI RACE   | TD449   |
|-------------------|---------|

|       |           |          |                    | với mức Error, dữ liệu lưu trữ tối thiểu 90 ngày.                                                 | kê                         |                           |
|-------|-----------|----------|--------------------|---------------------------------------------------------------------------------------------------|----------------------------|---------------------------|
| IPCC  | AuditLog  | Error    | Nén và lưu trữ log | Hệ thống IPCC Nén và lưu trữ log loại AuditLog với mức Error, dữ liệu lưu trữ tối thiểu 90 ngày.  | Có thể truy xuất khi cần   | Theo chuẩn syslog RFC5424 |
| Infra | AccessLog | Warning  | Xuất log           | Hệ thống Infra Xuất log loại AccessLog với mức Warning, dữ liệu lưu trữ tối thiểu 90 ngày.        | Có chỉ số thống kê         | Gửi log sang ELK          |
| QA    | AccessLog | Warning  | Nén và lưu trữ log | Hệ thống QA Nén và lưu trữ log loại AccessLog với mức Warning, dữ liệu lưu trữ tối thiểu 90 ngày. | Tích hợp cảnh báo realtime | Phân quyền chi tiết       |
| Infra | ErrorLog  | Critical | Xuất log           | Hệ thống Infra Xuất log loại ErrorLog với mức Critical, dữ liệu lưu trữ tối thiểu 90 ngày.        | Có thể truy xuất khi cần   | Gửi log sang ELK          |
| QA    | AuditLog  | Error    | Xóa log            | Hệ thống QA Xóa log loại AuditLog với mức Error, dữ liệu lưu trữ tối                              | Tích hợp cảnh báo          | Phân quyền chi tiết       |

<!-- image -->

## VIETTEL AI RACE

## BÁO CÁO HỆ THỐNG &amp; LOG

TD449

Lần ban hành: 1

|       |                |          |                    | thiểu 90 ngày.                                                                                         | realtime                   |                              |
|-------|----------------|----------|--------------------|--------------------------------------------------------------------------------------------------------|----------------------------|------------------------------|
| CRM   | AuditLog       | Fatal    | Xóa log            | Hệ thống CRM Xóa log loại AuditLog với mức Fatal, dữ liệu lưu trữ tối thiểu 90 ngày.                   | Có chỉ số thống kê         | Phân quyền chi tiết          |
| CRM   | PerformanceLog | Warning  | Xuất log           | Hệ thống CRM Xuất log loại PerformanceLog với mức Warning, dữ liệu lưu trữ tối thiểu 90 ngày.          | Có chỉ số thống kê         | Theo chuẩn syslog RFC5424    |
| Infra | TransactionLog | Critical | Xuất log           | Hệ thống Infra Xuất log loại TransactionLog với mức Critical, dữ liệu lưu trữ tối thiểu 90 ngày.       | Tích hợp cảnh báo realtime | Tự động xóa log sau 180 ngày |
| IPCC  | TransactionLog | Error    | Nén và lưu trữ log | Hệ thống IPCC Nén và lưu trữ log loại TransactionLog với mức Error, dữ liệu lưu trữ tối thiểu 90 ngày. | Tích hợp cảnh báo realtime | Phân quyền chi tiết          |
| IPCC  | PerformanceLog | Fatal    | Xóa log            | Hệ thống IPCC Xóa log loại PerformanceLog với mức Fatal, dữ liệu lưu trữ tối                           | Có chỉ số thống kê         | Phân quyền chi tiết          |

<!-- image -->

## VIETTEL AI RACE

## BÁO CÁO HỆ THỐNG &amp; LOG

TD449

Lần ban hành: 1

|         |                |          |                   | thiểu 90 ngày.                                                                                  |                          |                              |
|---------|----------------|----------|-------------------|-------------------------------------------------------------------------------------------------|--------------------------|------------------------------|
| Billing | AccessLog      | Fatal    | Phân tích log     | Hệ thống Billing Phân tích log loại AccessLog với mức Fatal, dữ liệu lưu trữ tối thiểu 90 ngày. | Log được mã hóa AES- 256 | Tự động xóa log sau 180 ngày |
| RPA     | ErrorLog       | Fatal    | Xóa log           | Hệ thống RPA Xóa log loại ErrorLog với mức Fatal, dữ liệu lưu trữ tối thiểu 90 ngày.            | Log được mã hóa AES- 256 | Có dashboard Grafana         |
| Infra   | TransactionLog | Info     | Xuất log          | Hệ thống Infra Xuất log loại TransactionLog với mức Info, dữ liệu lưu trữ tối thiểu 90 ngày.    | Không mất mát dữ liệu    | Theo chuẩn syslog RFC5424    |
| IVR     | ErrorLog       | Warning  | Xuất log          | Hệ thống IVR Xuất log loại ErrorLog với mức Warning, dữ liệu lưu trữ tối thiểu 90 ngày.         | Log được mã hóa AES- 256 | Có dashboard Grafana         |
| QA      | AuditLog       | Warning  | Gửi log sang SIEM | Hệ thống QA Gửi log sang SIEM loại AuditLog với mức Warning, dữ liệu lưu trữ tối thiểu 90 ngày. | Có chỉ số thống kê       | Tự động xóa log sau 180 ngày |
| Infra   | PerformanceLog | Critical | Phân              | Hệ thống Infra                                                                                  | Có chỉ                   | Theo chuẩn                   |

<!-- image -->

| VIETTEL AI RACE   | TD449   |
|-------------------|---------|

|       |                |          | tích log           | Phân tích log loại PerformanceLog với mức Critical, dữ liệu lưu trữ tối thiểu 90 ngày.                 | số thống kê                | syslog RFC5424       |
|-------|----------------|----------|--------------------|--------------------------------------------------------------------------------------------------------|----------------------------|----------------------|
| QA    | AuditLog       | Critical | Xuất log           | Hệ thống QA Xuất log loại AuditLog với mức Critical, dữ liệu lưu trữ tối thiểu 90 ngày.                | Log được mã hóa AES- 256   | Gửi log sang ELK     |
| IPCC  | TransactionLog | Error    | Nén và lưu trữ log | Hệ thống IPCC Nén và lưu trữ log loại TransactionLog với mức Error, dữ liệu lưu trữ tối thiểu 90 ngày. | Tích hợp cảnh báo realtime | Gửi log sang ELK     |
| RPA   | PerformanceLog | Critical | Phân tích log      | Hệ thống RPA Phân tích log loại PerformanceLog với mức Critical, dữ liệu lưu trữ tối thiểu 90 ngày.    | Có chỉ số thống kê         | Có dashboard Grafana |
| Infra | AuditLog       | Info     | Xóa log            | Hệ thống Infra Xóa log loại AuditLog với mức Info, dữ liệu lưu trữ tối thiểu 90 ngày.                  | Log được mã hóa AES- 256   | Có dashboard Grafana |
| RPA   | ErrorLog       | Fatal    | Xóa log            | Hệ thống RPA Xóa log loại ErrorLog với mức Fatal, dữ                                                   | Tích hợp cảnh              | Phân quyền chi tiết  |

<!-- image -->

| VIETTEL AI RACE   | TD449   |
|-------------------|---------|

|         |                |          |                    | liệu lưu trữ tối thiểu 90 ngày.                                                                           | báo realtime               |                           |
|---------|----------------|----------|--------------------|-----------------------------------------------------------------------------------------------------------|----------------------------|---------------------------|
| Billing | ErrorLog       | Info     | Gửi log sang SIEM  | Hệ thống Billing Gửi log sang SIEM loại ErrorLog với mức Info, dữ liệu lưu trữ tối thiểu 90 ngày.         | Tích hợp cảnh báo realtime | Phân quyền chi tiết       |
| CRM     | PerformanceLog | Critical | Gửi log sang SIEM  | Hệ thống CRM Gửi log sang SIEM loại PerformanceLog với mức Critical, dữ liệu lưu trữ tối thiểu 90 ngày.   | Log được mã hóa AES- 256   | Gửi log sang ELK          |
| Billing | TransactionLog | Error    | Nén và lưu trữ log | Hệ thống Billing Nén và lưu trữ log loại TransactionLog với mức Error, dữ liệu lưu trữ tối thiểu 90 ngày. | Log được mã hóa AES- 256   | Gửi log sang ELK          |
| CRM     | TransactionLog | Error    | Phân tích log      | Hệ thống CRM Phân tích log loại TransactionLog với mức Error, dữ liệu lưu trữ tối thiểu 90 ngày.          | Tích hợp cảnh báo realtime | Theo chuẩn syslog RFC5424 |
| IVR     | AuditLog       | Critical | Xuất log           | Hệ thống IVR Xuất log loại AuditLog với mức Critical,                                                     | Không mất mát              | Gửi log sang ELK          |

<!-- image -->

| VIETTEL AI RACE   | TD449   |
|-------------------|---------|

|       |                |          |                    | dữ liệu lưu trữ tối thiểu 90 ngày.                                                                      | dữ liệu                  |                              |
|-------|----------------|----------|--------------------|---------------------------------------------------------------------------------------------------------|--------------------------|------------------------------|
| CRM   | ErrorLog       | Info     | Xuất log           | Hệ thống CRM Xuất log loại ErrorLog với mức Info, dữ liệu lưu trữ tối thiểu 90 ngày.                    | Không mất mát dữ liệu    | Tự động xóa log sau 180 ngày |
| IPCC  | ErrorLog       | Fatal    | Phân tích log      | Hệ thống IPCC Phân tích log loại ErrorLog với mức Fatal, dữ liệu lưu trữ tối thiểu 90 ngày.             | Không mất mát dữ liệu    | Tự động xóa log sau 180 ngày |
| QA    | AuditLog       | Error    | Nén và lưu trữ log | Hệ thống QA Nén và lưu trữ log loại AuditLog với mức Error, dữ liệu lưu trữ tối thiểu 90 ngày.          | Log được mã hóa AES- 256 | Tự động xóa log sau 180 ngày |
| CRM   | TransactionLog | Critical | Gửi log sang SIEM  | Hệ thống CRM Gửi log sang SIEM loại TransactionLog với mức Critical, dữ liệu lưu trữ tối thiểu 90 ngày. | Có thể truy xuất khi cần | Tự động xóa log sau 180 ngày |
| Infra | ErrorLog       | Warning  | Nén và lưu trữ     | Hệ thống Infra Nén và lưu trữ log loại ErrorLog với mức Warning, dữ liệu                                | Log được mã hóa AES-     | Theo chuẩn syslog RFC5424    |

<!-- image -->

## VIETTEL AI RACE

## BÁO CÁO HỆ THỐNG &amp; LOG

TD449

Lần ban hành: 1

|         |                |         | log                | lưu trữ tối thiểu 90 ngày.                                                                           | 256                        |                           |
|---------|----------------|---------|--------------------|------------------------------------------------------------------------------------------------------|----------------------------|---------------------------|
| RPA     | TransactionLog | Error   | Gửi log sang SIEM  | Hệ thống RPA Gửi log sang SIEM loại TransactionLog với mức Error, dữ liệu lưu trữ tối thiểu 90 ngày. | Có thể truy xuất khi cần   | Theo chuẩn syslog RFC5424 |
| QA      | ErrorLog       | Error   | Xuất log           | Hệ thống QA Xuất log loại ErrorLog với mức Error, dữ liệu lưu trữ tối thiểu 90 ngày.                 | Không mất mát dữ liệu      | Gửi log sang ELK          |
| QA      | AccessLog      | Info    | Xuất log           | Hệ thống QA Xuất log loại AccessLog với mức Info, dữ liệu lưu trữ tối thiểu 90 ngày.                 | Không mất mát dữ liệu      | Phân quyền chi tiết       |
| CRM     | AccessLog      | Fatal   | Gửi log sang SIEM  | Hệ thống CRM Gửi log sang SIEM loại AccessLog với mức Fatal, dữ liệu lưu trữ tối thiểu 90 ngày.      | Tích hợp cảnh báo realtime | Theo chuẩn syslog RFC5424 |
| Billing | PerformanceLog | Warning | Nén và lưu trữ log | Hệ thống Billing Nén và lưu trữ log loại PerformanceLog với mức Warning, dữ liệu lưu trữ tối         | Tích hợp cảnh báo realtime | Có dashboard Grafana      |

<!-- image -->

## VIETTEL AI RACE

## BÁO CÁO HỆ THỐNG &amp; LOG

TD449

Lần ban hành: 1

|         |           |         |                    | thiểu 90 ngày.                                                                                       |                            |                              |
|---------|-----------|---------|--------------------|------------------------------------------------------------------------------------------------------|----------------------------|------------------------------|
| IPCC    | AccessLog | Error   | Gửi log sang SIEM  | Hệ thống IPCC Gửi log sang SIEM loại AccessLog với mức Error, dữ liệu lưu trữ tối thiểu 90 ngày.     | Log được mã hóa AES- 256   | Có dashboard Grafana         |
| Billing | AuditLog  | Warning | Xuất log           | Hệ thống Billing Xuất log loại AuditLog với mức Warning, dữ liệu lưu trữ tối thiểu 90 ngày.          | Không mất mát dữ liệu      | Có dashboard Grafana         |
| Billing | AuditLog  | Error   | Xuất log           | Hệ thống Billing Xuất log loại AuditLog với mức Error, dữ liệu lưu trữ tối thiểu 90 ngày.            | Không mất mát dữ liệu      | Tự động xóa log sau 180 ngày |
| Billing | AccessLog | Fatal   | Nén và lưu trữ log | Hệ thống Billing Nén và lưu trữ log loại AccessLog với mức Fatal, dữ liệu lưu trữ tối thiểu 90 ngày. | Tích hợp cảnh báo realtime | Tự động xóa log sau 180 ngày |
| CRM     | AccessLog | Warning | Nén và lưu trữ log | Hệ thống CRM Nén và lưu trữ log loại AccessLog với mức Warning, dữ liệu lưu trữ tối                  | Tích hợp cảnh báo realtime | Tự động xóa log sau 180 ngày |

<!-- image -->

## VIETTEL AI RACE

## BÁO CÁO HỆ THỐNG &amp; LOG

TD449

Lần ban hành: 1

|       |                |          |                    | thiểu 90 ngày.                                                                                  |                            |                              |
|-------|----------------|----------|--------------------|-------------------------------------------------------------------------------------------------|----------------------------|------------------------------|
| Infra | AccessLog      | Fatal    | Phân tích log      | Hệ thống Infra Phân tích log loại AccessLog với mức Fatal, dữ liệu lưu trữ tối thiểu 90 ngày.   | Tích hợp cảnh báo realtime | Có dashboard Grafana         |
| IPCC  | TransactionLog | Info     | Xóa log            | Hệ thống IPCC Xóa log loại TransactionLog với mức Info, dữ liệu lưu trữ tối thiểu 90 ngày.      | Log được mã hóa AES- 256   | Tự động xóa log sau 180 ngày |
| QA    | AccessLog      | Error    | Nén và lưu trữ log | Hệ thống QA Nén và lưu trữ log loại AccessLog với mức Error, dữ liệu lưu trữ tối thiểu 90 ngày. | Có chỉ số thống kê         | Có dashboard Grafana         |
| IPCC  | ErrorLog       | Error    | Phân tích log      | Hệ thống IPCC Phân tích log loại ErrorLog với mức Error, dữ liệu lưu trữ tối thiểu 90 ngày.     | Tích hợp cảnh báo realtime | Gửi log sang ELK             |
| Infra | ErrorLog       | Critical | Phân tích log      | Hệ thống Infra Phân tích log loại ErrorLog với mức Critical, dữ liệu lưu trữ tối thiểu 90       | Không mất mát dữ liệu      | Phân quyền chi tiết          |

<!-- image -->

## VIETTEL AI RACE

## BÁO CÁO HỆ THỐNG &amp; LOG

TD449

Lần ban hành: 1

|         |                |         |                    | ngày.                                                                                                 |                          |                              |
|---------|----------------|---------|--------------------|-------------------------------------------------------------------------------------------------------|--------------------------|------------------------------|
| IVR     | AccessLog      | Warning | Phân tích log      | Hệ thống IVR Phân tích log loại AccessLog với mức Warning, dữ liệu lưu trữ tối thiểu 90 ngày.         | Không mất mát dữ liệu    | Có dashboard Grafana         |
| IVR     | TransactionLog | Error   | Nén và lưu trữ log | Hệ thống IVR Nén và lưu trữ log loại TransactionLog với mức Error, dữ liệu lưu trữ tối thiểu 90 ngày. | Có chỉ số thống kê       | Theo chuẩn syslog RFC5424    |
| QA      | ErrorLog       | Error   | Gửi log sang SIEM  | Hệ thống QA Gửi log sang SIEM loại ErrorLog với mức Error, dữ liệu lưu trữ tối thiểu 90 ngày.         | Log được mã hóa AES- 256 | Gửi log sang ELK             |
| RPA     | TransactionLog | Fatal   | Phân tích log      | Hệ thống RPA Phân tích log loại TransactionLog với mức Fatal, dữ liệu lưu trữ tối thiểu 90 ngày.      | Có chỉ số thống kê       | Tự động xóa log sau 180 ngày |
| Billing | AccessLog      | Fatal   | Gửi log sang SIEM  | Hệ thống Billing Gửi log sang SIEM loại AccessLog với mức Fatal, dữ liệu lưu trữ tối thiểu 90         | Không mất mát dữ liệu    | Tự động xóa log sau 180 ngày |

<!-- image -->

## VIETTEL AI RACE

## BÁO CÁO HỆ THỐNG &amp; LOG

TD449

Lần ban hành: 1

|         |                |       |                    | ngày.                                                                                                 |                          |                           |
|---------|----------------|-------|--------------------|-------------------------------------------------------------------------------------------------------|--------------------------|---------------------------|
| CRM     | TransactionLog | Info  | Phân tích log      | Hệ thống CRM Phân tích log loại TransactionLog với mức Info, dữ liệu lưu trữ tối thiểu 90 ngày.       | Có chỉ số thống kê       | Gửi log sang ELK          |
| Billing | ErrorLog       | Info  | Nén và lưu trữ log | Hệ thống Billing Nén và lưu trữ log loại ErrorLog với mức Info, dữ liệu lưu trữ tối thiểu 90 ngày.    | Có chỉ số thống kê       | Theo chuẩn syslog RFC5424 |
| RPA     | TransactionLog | Fatal | Nén và lưu trữ log | Hệ thống RPA Nén và lưu trữ log loại TransactionLog với mức Fatal, dữ liệu lưu trữ tối thiểu 90 ngày. | Có thể truy xuất khi cần | Gửi log sang ELK          |
| Infra   | ErrorLog       | Info  | Xóa log            | Hệ thống Infra Xóa log loại ErrorLog với mức Info, dữ liệu lưu trữ tối thiểu 90 ngày.                 | Log được mã hóa AES- 256 | Có dashboard Grafana      |
| IVR     | ErrorLog       | Info  | Nén và lưu trữ log | Hệ thống IVR Nén và lưu trữ log loại ErrorLog với mức Info, dữ liệu lưu trữ tối thiểu 90 ngày.        | Không mất mát dữ liệu    | Theo chuẩn syslog RFC5424 |

<!-- image -->

## VIETTEL AI RACE

## BÁO CÁO HỆ THỐNG &amp; LOG

TD449

Lần ban hành: 1

| IPCC   | AuditLog       | Error   | Gửi log sang SIEM   | Hệ thống IPCC Gửi log sang SIEM loại AuditLog với mức Error, dữ liệu lưu trữ tối thiểu 90 ngày.     | Tích hợp cảnh báo realtime   | Phân quyền chi tiết       |
|--------|----------------|---------|---------------------|-----------------------------------------------------------------------------------------------------|------------------------------|---------------------------|
| QA     | TransactionLog | Fatal   | Gửi log sang SIEM   | Hệ thống QA Gửi log sang SIEM loại TransactionLog với mức Fatal, dữ liệu lưu trữ tối thiểu 90 ngày. | Có thể truy xuất khi cần     | Có dashboard Grafana      |
| Infra  | AuditLog       | Warning | Xóa log             | Hệ thống Infra Xóa log loại AuditLog với mức Warning, dữ liệu lưu trữ tối thiểu 90 ngày.            | Có thể truy xuất khi cần     | Theo chuẩn syslog RFC5424 |
| IVR    | ErrorLog       | Warning | Gửi log sang SIEM   | Hệ thống IVR Gửi log sang SIEM loại ErrorLog với mức Warning, dữ liệu lưu trữ tối thiểu 90 ngày.    | Tích hợp cảnh báo realtime   | Theo chuẩn syslog RFC5424 |
| IVR    | AuditLog       | Fatal   | Xuất log            | Hệ thống IVR Xuất log loại AuditLog với mức Fatal, dữ liệu lưu trữ tối thiểu 90 ngày.               | Không mất mát dữ liệu        | Có dashboard Grafana      |
| Infra  | PerformanceLog | Info    | Nén và lưu          | Hệ thống Infra Nén và lưu trữ log loại PerformanceLog                                               | Không mất mát                | Phân quyền chi tiết       |

<!-- image -->

## VIETTEL AI RACE

## BÁO CÁO HỆ THỐNG &amp; LOG

TD449

Lần ban hành: 1

|         |                |          | trữ log            | với mức Info, dữ liệu lưu trữ tối thiểu 90 ngày.                                                        | dữ liệu                    |                              |
|---------|----------------|----------|--------------------|---------------------------------------------------------------------------------------------------------|----------------------------|------------------------------|
| Billing | PerformanceLog | Error    | Xuất log           | Hệ thống Billing Xuất log loại PerformanceLog với mức Error, dữ liệu lưu trữ tối thiểu 90 ngày.         | Log được mã hóa AES- 256   | Gửi log sang ELK             |
| CRM     | TransactionLog | Error    | Nén và lưu trữ log | Hệ thống CRM Nén và lưu trữ log loại TransactionLog với mức Error, dữ liệu lưu trữ tối thiểu 90 ngày.   | Có thể truy xuất khi cần   | Có dashboard Grafana         |
| QA      | TransactionLog | Fatal    | Xuất log           | Hệ thống QA Xuất log loại TransactionLog với mức Fatal, dữ liệu lưu trữ tối thiểu 90 ngày.              | Có chỉ số thống kê         | Phân quyền chi tiết          |
| RPA     | TransactionLog | Critical | Gửi log sang SIEM  | Hệ thống RPA Gửi log sang SIEM loại TransactionLog với mức Critical, dữ liệu lưu trữ tối thiểu 90 ngày. | Tích hợp cảnh báo realtime | Tự động xóa log sau 180 ngày |
| QA      | TransactionLog | Critical | Phân tích          | Hệ thống QA Phân tích log loại TransactionLog                                                           | Có chỉ số thống            | Theo chuẩn syslog            |

<!-- image -->

| VIETTEL AI RACE   | TD449   |
|-------------------|---------|

|         |                |          | log                | với mức Critical, dữ liệu lưu trữ tối thiểu 90 ngày.                                                         | kê                       | RFC5424                      |
|---------|----------------|----------|--------------------|--------------------------------------------------------------------------------------------------------------|--------------------------|------------------------------|
| CRM     | AccessLog      | Fatal    | Gửi log sang SIEM  | Hệ thống CRM Gửi log sang SIEM loại AccessLog với mức Fatal, dữ liệu lưu trữ tối thiểu 90 ngày.              | Log được mã hóa AES- 256 | Tự động xóa log sau 180 ngày |
| Billing | PerformanceLog | Critical | Nén và lưu trữ log | Hệ thống Billing Nén và lưu trữ log loại PerformanceLog với mức Critical, dữ liệu lưu trữ tối thiểu 90 ngày. | Có thể truy xuất khi cần | Phân quyền chi tiết          |
| QA      | TransactionLog | Error    | Xuất log           | Hệ thống QA Xuất log loại TransactionLog với mức Error, dữ liệu lưu trữ tối thiểu 90 ngày.                   | Có chỉ số thống kê       | Gửi log sang ELK             |
| Billing | AccessLog      | Info     | Xóa log            | Hệ thống Billing Xóa log loại AccessLog với mức Info, dữ liệu lưu trữ tối thiểu 90 ngày.                     | Không mất mát dữ liệu    | Có dashboard Grafana         |
| CRM     | AuditLog       | Warning  | Nén và lưu         | Hệ thống CRM Nén và lưu trữ log loại AuditLog với                                                            | Có chỉ số thống          | Phân quyền chi tiết          |

<!-- image -->

| VIETTEL AI RACE   | TD449   |
|-------------------|---------|

|         |                |       | trữ log            | mức Warning, dữ liệu lưu trữ tối thiểu 90 ngày.                                                          | kê                       |                              |
|---------|----------------|-------|--------------------|----------------------------------------------------------------------------------------------------------|--------------------------|------------------------------|
| Billing | AccessLog      | Info  | Xóa log            | Hệ thống Billing Xóa log loại AccessLog với mức Info, dữ liệu lưu trữ tối thiểu 90 ngày.                 | Có chỉ số thống kê       | Tự động xóa log sau 180 ngày |
| IVR     | AccessLog      | Error | Xóa log            | Hệ thống IVR Xóa log loại AccessLog với mức Error, dữ liệu lưu trữ tối thiểu 90 ngày.                    | Không mất mát dữ liệu    | Tự động xóa log sau 180 ngày |
| IVR     | AccessLog      | Error | Xóa log            | Hệ thống IVR Xóa log loại AccessLog với mức Error, dữ liệu lưu trữ tối thiểu 90 ngày.                    | Có thể truy xuất khi cần | Gửi log sang ELK             |
| Billing | TransactionLog | Info  | Nén và lưu trữ log | Hệ thống Billing Nén và lưu trữ log loại TransactionLog với mức Info, dữ liệu lưu trữ tối thiểu 90 ngày. | Không mất mát dữ liệu    | Gửi log sang ELK             |
| Billing | TransactionLog | Error | Xóa log            | Hệ thống Billing Xóa log loại TransactionLog với mức Error, dữ liệu lưu trữ tối                          | Log được mã hóa AES-     | Phân quyền chi tiết          |

<!-- image -->

## VIETTEL AI RACE

## BÁO CÁO HỆ THỐNG &amp; LOG

TD449

Lần ban hành: 1

|         |                |          |                    | thiểu 90 ngày.                                                                                              | 256                        |                           |
|---------|----------------|----------|--------------------|-------------------------------------------------------------------------------------------------------------|----------------------------|---------------------------|
| Infra   | AccessLog      | Info     | Xóa log            | Hệ thống Infra Xóa log loại AccessLog với mức Info, dữ liệu lưu trữ tối thiểu 90 ngày.                      | Có chỉ số thống kê         | Gửi log sang ELK          |
| RPA     | ErrorLog       | Critical | Xóa log            | Hệ thống RPA Xóa log loại ErrorLog với mức Critical, dữ liệu lưu trữ tối thiểu 90 ngày.                     | Log được mã hóa AES- 256   | Gửi log sang ELK          |
| Billing | TransactionLog | Warning  | Nén và lưu trữ log | Hệ thống Billing Nén và lưu trữ log loại TransactionLog với mức Warning, dữ liệu lưu trữ tối thiểu 90 ngày. | Tích hợp cảnh báo realtime | Theo chuẩn syslog RFC5424 |
| Infra   | PerformanceLog | Fatal    | Xóa log            | Hệ thống Infra Xóa log loại PerformanceLog với mức Fatal, dữ liệu lưu trữ tối thiểu 90 ngày.                | Có thể truy xuất khi cần   | Có dashboard Grafana      |
| Infra   | TransactionLog | Warning  | Gửi log sang SIEM  | Hệ thống Infra Gửi log sang SIEM loại TransactionLog với mức Warning, dữ liệu lưu trữ tối thiểu 90 ngày.    | Không mất mát dữ liệu      | Phân quyền chi tiết       |

<!-- image -->

## VIETTEL AI RACE

## BÁO CÁO HỆ THỐNG &amp; LOG

TD449

Lần ban hành: 1

| IPCC    | PerformanceLog   | Critical   | Nén và lưu trữ log   | Hệ thống IPCC Nén và lưu trữ log loại PerformanceLog với mức Critical, dữ liệu lưu trữ tối thiểu 90 ngày.   | Tích hợp cảnh báo realtime   | Phân quyền chi tiết   |
|---------|------------------|------------|----------------------|-------------------------------------------------------------------------------------------------------------|------------------------------|-----------------------|
| IPCC    | TransactionLog   | Error      | Gửi log sang SIEM    | Hệ thống IPCC Gửi log sang SIEM loại TransactionLog với mức Error, dữ liệu lưu trữ tối thiểu 90 ngày.       | Tích hợp cảnh báo realtime   | Có dashboard Grafana  |
| RPA     | AccessLog        | Fatal      | Gửi log sang SIEM    | Hệ thống RPA Gửi log sang SIEM loại AccessLog với mức Fatal, dữ liệu lưu trữ tối thiểu 90 ngày.             | Có chỉ số thống kê           | Gửi log sang ELK      |
| IVR     | AccessLog        | Critical   | Phân tích log        | Hệ thống IVR Phân tích log loại AccessLog với mức Critical, dữ liệu lưu trữ tối thiểu 90 ngày.              | Tích hợp cảnh báo realtime   | Phân quyền chi tiết   |
| Billing | AuditLog         | Critical   | Xóa log              | Hệ thống Billing Xóa log loại AuditLog với mức Critical, dữ liệu lưu trữ tối thiểu 90                       | Có chỉ số thống kê           | Gửi log sang ELK      |

<!-- image -->

## VIETTEL AI RACE

## BÁO CÁO HỆ THỐNG &amp; LOG

TD449

Lần ban hành: 1

|         |                |          |                    | ngày.                                                                                                   |                            |                              |
|---------|----------------|----------|--------------------|---------------------------------------------------------------------------------------------------------|----------------------------|------------------------------|
| QA      | AccessLog      | Fatal    | Gửi log sang SIEM  | Hệ thống QA Gửi log sang SIEM loại AccessLog với mức Fatal, dữ liệu lưu trữ tối thiểu 90 ngày.          | Tích hợp cảnh báo realtime | Có dashboard Grafana         |
| Billing | TransactionLog | Info     | Gửi log sang SIEM  | Hệ thống Billing Gửi log sang SIEM loại TransactionLog với mức Info, dữ liệu lưu trữ tối thiểu 90 ngày. | Có thể truy xuất khi cần   | Tự động xóa log sau 180 ngày |
| Billing | AccessLog      | Warning  | Nén và lưu trữ log | Hệ thống Billing Nén và lưu trữ log loại AccessLog với mức Warning, dữ liệu lưu trữ tối thiểu 90 ngày.  | Log được mã hóa AES- 256   | Phân quyền chi tiết          |
| IPCC    | ErrorLog       | Error    | Xóa log            | Hệ thống IPCC Xóa log loại ErrorLog với mức Error, dữ liệu lưu trữ tối thiểu 90 ngày.                   | Tích hợp cảnh báo realtime | Tự động xóa log sau 180 ngày |
| RPA     | TransactionLog | Critical | Phân tích log      | Hệ thống RPA Phân tích log loại TransactionLog với mức Critical, dữ liệu lưu trữ tối                    | Có thể truy xuất khi cần   | Gửi log sang ELK             |

<!-- image -->

## VIETTEL AI RACE

## BÁO CÁO HỆ THỐNG &amp; LOG

TD449

Lần ban hành: 1

|         |                |         |                    | thiểu 90 ngày.                                                                                      |                            |                              |
|---------|----------------|---------|--------------------|-----------------------------------------------------------------------------------------------------|----------------------------|------------------------------|
| Billing | AuditLog       | Error   | Phân tích log      | Hệ thống Billing Phân tích log loại AuditLog với mức Error, dữ liệu lưu trữ tối thiểu 90 ngày.      | Có chỉ số thống kê         | Phân quyền chi tiết          |
| QA      | TransactionLog | Info    | Nén và lưu trữ log | Hệ thống QA Nén và lưu trữ log loại TransactionLog với mức Info, dữ liệu lưu trữ tối thiểu 90 ngày. | Có chỉ số thống kê         | Tự động xóa log sau 180 ngày |
| CRM     | AuditLog       | Info    | Phân tích log      | Hệ thống CRM Phân tích log loại AuditLog với mức Info, dữ liệu lưu trữ tối thiểu 90 ngày.           | Có thể truy xuất khi cần   | Có dashboard Grafana         |
| QA      | TransactionLog | Warning | Phân tích log      | Hệ thống QA Phân tích log loại TransactionLog với mức Warning, dữ liệu lưu trữ tối thiểu 90 ngày.   | Tích hợp cảnh báo realtime | Phân quyền chi tiết          |
| Billing | TransactionLog | Fatal   | Xuất log           | Hệ thống Billing Xuất log loại TransactionLog với mức Fatal, dữ liệu lưu trữ tối                    | Tích hợp cảnh báo realtime | Gửi log sang ELK             |

<!-- image -->

## VIETTEL AI RACE

## BÁO CÁO HỆ THỐNG &amp; LOG

TD449

Lần ban hành: 1

|         |                |          |                    | thiểu 90 ngày.                                                                                          |                       |                              |
|---------|----------------|----------|--------------------|---------------------------------------------------------------------------------------------------------|-----------------------|------------------------------|
| Infra   | AccessLog      | Warning  | Xóa log            | Hệ thống Infra Xóa log loại AccessLog với mức Warning, dữ liệu lưu trữ tối thiểu 90 ngày.               | Có chỉ số thống kê    | Tự động xóa log sau 180 ngày |
| Billing | TransactionLog | Info     | Gửi log sang SIEM  | Hệ thống Billing Gửi log sang SIEM loại TransactionLog với mức Info, dữ liệu lưu trữ tối thiểu 90 ngày. | Không mất mát dữ liệu | Phân quyền chi tiết          |
| CRM     | AccessLog      | Critical | Nén và lưu trữ log | Hệ thống CRM Nén và lưu trữ log loại AccessLog với mức Critical, dữ liệu lưu trữ tối thiểu 90 ngày.     | Không mất mát dữ liệu | Tự động xóa log sau 180 ngày |
| QA      | ErrorLog       | Warning  | Xóa log            | Hệ thống QA Xóa log loại ErrorLog với mức Warning, dữ liệu lưu trữ tối thiểu 90 ngày.                   | Không mất mát dữ liệu | Tự động xóa log sau 180 ngày |
| Infra   | TransactionLog | Error    | Nén và lưu trữ log | Hệ thống Infra Nén và lưu trữ log loại TransactionLog với mức Error, dữ liệu lưu trữ tối thiểu 90 ngày. | Có chỉ số thống kê    | Tự động xóa log sau 180 ngày |

<!-- image -->

## VIETTEL AI RACE

## BÁO CÁO HỆ THỐNG &amp; LOG

TD449

Lần ban hành: 1

| IPCC   | AuditLog       | Error   | Nén và lưu trữ log   | Hệ thống IPCC Nén và lưu trữ log loại AuditLog với mức Error, dữ liệu lưu trữ tối thiểu 90 ngày.      | Có thể truy xuất khi cần   | Gửi log sang ELK             |
|--------|----------------|---------|----------------------|-------------------------------------------------------------------------------------------------------|----------------------------|------------------------------|
| QA     | AccessLog      | Fatal   | Nén và lưu trữ log   | Hệ thống QA Nén và lưu trữ log loại AccessLog với mức Fatal, dữ liệu lưu trữ tối thiểu 90 ngày.       | Có chỉ số thống kê         | Gửi log sang ELK             |
| CRM    | PerformanceLog | Error   | Gửi log sang SIEM    | Hệ thống CRM Gửi log sang SIEM loại PerformanceLog với mức Error, dữ liệu lưu trữ tối thiểu 90 ngày.  | Có chỉ số thống kê         | Theo chuẩn syslog RFC5424    |
| RPA    | TransactionLog | Fatal   | Nén và lưu trữ log   | Hệ thống RPA Nén và lưu trữ log loại TransactionLog với mức Fatal, dữ liệu lưu trữ tối thiểu 90 ngày. | Không mất mát dữ liệu      | Có dashboard Grafana         |
| CRM    | AuditLog       | Warning | Phân tích log        | Hệ thống CRM Phân tích log loại AuditLog với mức Warning, dữ liệu lưu trữ tối thiểu 90 ngày.          | Có thể truy xuất khi cần   | Tự động xóa log sau 180 ngày |

<!-- image -->

## VIETTEL AI RACE

## BÁO CÁO HỆ THỐNG &amp; LOG

TD449

Lần ban hành: 1

| Infra   | ErrorLog       | Critical   | Nén và lưu trữ log   | Hệ thống Infra Nén và lưu trữ log loại ErrorLog với mức Critical, dữ liệu lưu trữ tối thiểu 90 ngày.     | Không mất mát dữ liệu      | Gửi log sang ELK          |
|---------|----------------|------------|----------------------|----------------------------------------------------------------------------------------------------------|----------------------------|---------------------------|
| RPA     | PerformanceLog | Critical   | Nén và lưu trữ log   | Hệ thống RPA Nén và lưu trữ log loại PerformanceLog với mức Critical, dữ liệu lưu trữ tối thiểu 90 ngày. | Tích hợp cảnh báo realtime | Có dashboard Grafana      |
| IPCC    | AuditLog       | Warning    | Phân tích log        | Hệ thống IPCC Phân tích log loại AuditLog với mức Warning, dữ liệu lưu trữ tối thiểu 90 ngày.            | Có thể truy xuất khi cần   | Theo chuẩn syslog RFC5424 |
| Billing | AccessLog      | Info       | Xuất log             | Hệ thống Billing Xuất log loại AccessLog với mức Info, dữ liệu lưu trữ tối thiểu 90 ngày.                | Không mất mát dữ liệu      | Theo chuẩn syslog RFC5424 |
| Billing | AccessLog      | Warning    | Xuất log             | Hệ thống Billing Xuất log loại AccessLog với mức Warning, dữ liệu lưu trữ tối thiểu 90 ngày.             | Có thể truy xuất khi cần   | Theo chuẩn syslog RFC5424 |

<!-- image -->

| VIETTEL AI RACE   | TD449   |
|-------------------|---------|

| QA    | TransactionLog   | Warning   | Xuất log           | Hệ thống QA Xuất log loại TransactionLog với mức Warning, dữ liệu lưu trữ tối thiểu 90 ngày.            | Có chỉ số thống kê       | Tự động xóa log sau 180 ngày   |
|-------|------------------|-----------|--------------------|---------------------------------------------------------------------------------------------------------|--------------------------|--------------------------------|
| IVR   | AccessLog        | Warning   | Gửi log sang SIEM  | Hệ thống IVR Gửi log sang SIEM loại AccessLog với mức Warning, dữ liệu lưu trữ tối thiểu 90 ngày.       | Có thể truy xuất khi cần | Phân quyền chi tiết            |
| IVR   | ErrorLog         | Warning   | Xóa log            | Hệ thống IVR Xóa log loại ErrorLog với mức Warning, dữ liệu lưu trữ tối thiểu 90 ngày.                  | Có thể truy xuất khi cần | Tự động xóa log sau 180 ngày   |
| IPCC  | AuditLog         | Fatal     | Xóa log            | Hệ thống IPCC Xóa log loại AuditLog với mức Fatal, dữ liệu lưu trữ tối thiểu 90 ngày.                   | Có thể truy xuất khi cần | Có dashboard Grafana           |
| Infra | TransactionLog   | Error     | Nén và lưu trữ log | Hệ thống Infra Nén và lưu trữ log loại TransactionLog với mức Error, dữ liệu lưu trữ tối thiểu 90 ngày. | Không mất mát dữ liệu    | Phân quyền chi tiết            |
| Infra | AuditLog         | Error     | Nén và             | Hệ thống Infra Nén và lưu trữ log loại                                                                  | Tích hợp                 | Theo chuẩn syslog              |

<!-- image -->

| VIETTEL AI RACE   | TD449   |
|-------------------|---------|

|       |                |          | lưu trữ log       | AuditLog với mức Error, dữ liệu lưu trữ tối thiểu 90 ngày.                                               | cảnh báo realtime          | RFC5424                      |
|-------|----------------|----------|-------------------|----------------------------------------------------------------------------------------------------------|----------------------------|------------------------------|
| IPCC  | PerformanceLog | Critical | Gửi log sang SIEM | Hệ thống IPCC Gửi log sang SIEM loại PerformanceLog với mức Critical, dữ liệu lưu trữ tối thiểu 90 ngày. | Log được mã hóa AES- 256   | Tự động xóa log sau 180 ngày |
| Infra | PerformanceLog | Warning  | Phân tích log     | Hệ thống Infra Phân tích log loại PerformanceLog với mức Warning, dữ liệu lưu trữ tối thiểu 90 ngày.     | Tích hợp cảnh báo realtime | Tự động xóa log sau 180 ngày |
| Infra | AccessLog      | Fatal    | Xóa log           | Hệ thống Infra Xóa log loại AccessLog với mức Fatal, dữ liệu lưu trữ tối thiểu 90 ngày.                  | Có thể truy xuất khi cần   | Có dashboard Grafana         |
| QA    | PerformanceLog | Critical | Phân tích log     | Hệ thống QA Phân tích log loại PerformanceLog với mức Critical, dữ liệu lưu trữ tối thiểu 90 ngày.       | Không mất mát dữ liệu      | Theo chuẩn syslog RFC5424    |
| Infra | PerformanceLog | Critical | Xóa log           | Hệ thống Infra Xóa log loại PerformanceLog                                                               | Có thể truy xuất khi       | Theo chuẩn syslog            |

<!-- image -->

| VIETTEL AI RACE   | TD449   |
|-------------------|---------|

|      |                |          |                    | với mức Critical, dữ liệu lưu trữ tối thiểu 90 ngày.                                                 | cần                        | RFC5424                      |
|------|----------------|----------|--------------------|------------------------------------------------------------------------------------------------------|----------------------------|------------------------------|
| QA   | PerformanceLog | Fatal    | Nén và lưu trữ log | Hệ thống QA Nén và lưu trữ log loại PerformanceLog với mức Fatal, dữ liệu lưu trữ tối thiểu 90 ngày. | Có chỉ số thống kê         | Gửi log sang ELK             |
| RPA  | ErrorLog       | Warning  | Nén và lưu trữ log | Hệ thống RPA Nén và lưu trữ log loại ErrorLog với mức Warning, dữ liệu lưu trữ tối thiểu 90 ngày.    | Tích hợp cảnh báo realtime | Tự động xóa log sau 180 ngày |
| IPCC | ErrorLog       | Critical | Xóa log            | Hệ thống IPCC Xóa log loại ErrorLog với mức Critical, dữ liệu lưu trữ tối thiểu 90 ngày.             | Có thể truy xuất khi cần   | Phân quyền chi tiết          |
| QA   | AccessLog      | Fatal    | Xóa log            | Hệ thống QA Xóa log loại AccessLog với mức Fatal, dữ liệu lưu trữ tối thiểu 90 ngày.                 | Có chỉ số thống kê         | Theo chuẩn syslog RFC5424    |
| RPA  | AuditLog       | Warning  | Nén và lưu trữ     | Hệ thống RPA Nén và lưu trữ log loại AuditLog với mức Warning, dữ liệu lưu trữ tối thiểu 90          | Log được mã hóa AES-       | Theo chuẩn syslog RFC5424    |

<!-- image -->

## VIETTEL AI RACE

## BÁO CÁO HỆ THỐNG &amp; LOG

TD449

Lần ban hành: 1

|         |                |         | log                | ngày.                                                                                                  | 256                        |                              |
|---------|----------------|---------|--------------------|--------------------------------------------------------------------------------------------------------|----------------------------|------------------------------|
| QA      | AuditLog       | Fatal   | Gửi log sang SIEM  | Hệ thống QA Gửi log sang SIEM loại AuditLog với mức Fatal, dữ liệu lưu trữ tối thiểu 90 ngày.          | Có thể truy xuất khi cần   | Có dashboard Grafana         |
| CRM     | PerformanceLog | Warning | Gửi log sang SIEM  | Hệ thống CRM Gửi log sang SIEM loại PerformanceLog với mức Warning, dữ liệu lưu trữ tối thiểu 90 ngày. | Có thể truy xuất khi cần   | Có dashboard Grafana         |
| RPA     | TransactionLog | Fatal   | Gửi log sang SIEM  | Hệ thống RPA Gửi log sang SIEM loại TransactionLog với mức Fatal, dữ liệu lưu trữ tối thiểu 90 ngày.   | Tích hợp cảnh báo realtime | Tự động xóa log sau 180 ngày |
| Billing | AuditLog       | Warning | Nén và lưu trữ log | Hệ thống Billing Nén và lưu trữ log loại AuditLog với mức Warning, dữ liệu lưu trữ tối thiểu 90 ngày.  | Có chỉ số thống kê         | Tự động xóa log sau 180 ngày |
| IPCC    | AuditLog       | Error   | Nén và lưu trữ     | Hệ thống IPCC Nén và lưu trữ log loại AuditLog với mức Error, dữ liệu lưu trữ tối thiểu 90             | Log được mã hóa AES-       | Gửi log sang ELK             |

<!-- image -->

## VIETTEL AI RACE

## BÁO CÁO HỆ THỐNG &amp; LOG

TD449

Lần ban hành: 1

|         |                |          | log                | ngày.                                                                                                    | 256                        |                           |
|---------|----------------|----------|--------------------|----------------------------------------------------------------------------------------------------------|----------------------------|---------------------------|
| IPCC    | PerformanceLog | Warning  | Nén và lưu trữ log | Hệ thống IPCC Nén và lưu trữ log loại PerformanceLog với mức Warning, dữ liệu lưu trữ tối thiểu 90 ngày. | Log được mã hóa AES- 256   | Có dashboard Grafana      |
| IPCC    | TransactionLog | Warning  | Gửi log sang SIEM  | Hệ thống IPCC Gửi log sang SIEM loại TransactionLog với mức Warning, dữ liệu lưu trữ tối thiểu 90 ngày.  | Log được mã hóa AES- 256   | Gửi log sang ELK          |
| IVR     | PerformanceLog | Warning  | Phân tích log      | Hệ thống IVR Phân tích log loại PerformanceLog với mức Warning, dữ liệu lưu trữ tối thiểu 90 ngày.       | Có chỉ số thống kê         | Có dashboard Grafana      |
| Infra   | AccessLog      | Critical | Phân tích log      | Hệ thống Infra Phân tích log loại AccessLog với mức Critical, dữ liệu lưu trữ tối thiểu 90 ngày.         | Tích hợp cảnh báo realtime | Theo chuẩn syslog RFC5424 |
| Billing | PerformanceLog | Warning  | Nén và lưu trữ     | Hệ thống Billing Nén và lưu trữ log loại PerformanceLog                                                  | Có thể truy xuất khi       | Phân quyền chi tiết       |

<!-- image -->

## VIETTEL AI RACE

## BÁO CÁO HỆ THỐNG &amp; LOG

TD449

Lần ban hành: 1

|       |                |         | log               | với mức Warning, dữ liệu lưu trữ tối thiểu 90 ngày.                                                   | cần                   |                              |
|-------|----------------|---------|-------------------|-------------------------------------------------------------------------------------------------------|-----------------------|------------------------------|
| QA    | AccessLog      | Warning | Gửi log sang SIEM | Hệ thống QA Gửi log sang SIEM loại AccessLog với mức Warning, dữ liệu lưu trữ tối thiểu 90 ngày.      | Có chỉ số thống kê    | Theo chuẩn syslog RFC5424    |
| QA    | PerformanceLog | Warning | Gửi log sang SIEM | Hệ thống QA Gửi log sang SIEM loại PerformanceLog với mức Warning, dữ liệu lưu trữ tối thiểu 90 ngày. | Có chỉ số thống kê    | Có dashboard Grafana         |
| IPCC  | PerformanceLog | Fatal   | Xuất log          | Hệ thống IPCC Xuất log loại PerformanceLog với mức Fatal, dữ liệu lưu trữ tối thiểu 90 ngày.          | Không mất mát dữ liệu | Tự động xóa log sau 180 ngày |
| Infra | AccessLog      | Fatal   | Gửi log sang SIEM | Hệ thống Infra Gửi log sang SIEM loại AccessLog với mức Fatal, dữ liệu lưu trữ tối thiểu 90 ngày.     | Có chỉ số thống kê    | Gửi log sang ELK             |
| IPCC  | ErrorLog       | Error   | Gửi log sang      | Hệ thống IPCC Gửi log sang SIEM loại ErrorLog với mức Error, dữ liệu                                  | Có thể truy xuất khi  | Tự động xóa log sau 180 ngày |

<!-- image -->

## VIETTEL AI RACE

## BÁO CÁO HỆ THỐNG &amp; LOG

TD449

Lần ban hành: 1

|         |                |          | SIEM               | lưu trữ tối thiểu 90 ngày.                                                                                  | cần                        |                              |
|---------|----------------|----------|--------------------|-------------------------------------------------------------------------------------------------------------|----------------------------|------------------------------|
| IVR     | AuditLog       | Critical | Nén và lưu trữ log | Hệ thống IVR Nén và lưu trữ log loại AuditLog với mức Critical, dữ liệu lưu trữ tối thiểu 90 ngày.          | Log được mã hóa AES- 256   | Có dashboard Grafana         |
| Billing | TransactionLog | Critical | Gửi log sang SIEM  | Hệ thống Billing Gửi log sang SIEM loại TransactionLog với mức Critical, dữ liệu lưu trữ tối thiểu 90 ngày. | Có chỉ số thống kê         | Gửi log sang ELK             |
| RPA     | PerformanceLog | Critical | Phân tích log      | Hệ thống RPA Phân tích log loại PerformanceLog với mức Critical, dữ liệu lưu trữ tối thiểu 90 ngày.         | Có thể truy xuất khi cần   | Theo chuẩn syslog RFC5424    |
| IPCC    | AccessLog      | Fatal    | Gửi log sang SIEM  | Hệ thống IPCC Gửi log sang SIEM loại AccessLog với mức Fatal, dữ liệu lưu trữ tối thiểu 90 ngày.            | Tích hợp cảnh báo realtime | Phân quyền chi tiết          |
| Infra   | AuditLog       | Critical | Nén và lưu trữ     | Hệ thống Infra Nén và lưu trữ log loại AuditLog với mức Critical, dữ liệu lưu                               | Tích hợp cảnh báo          | Tự động xóa log sau 180 ngày |

<!-- image -->

## VIETTEL AI RACE

## BÁO CÁO HỆ THỐNG &amp; LOG

TD449

Lần ban hành: 1

|         |                |          | log               | trữ tối thiểu 90 ngày.                                                                                | realtime                   |                              |
|---------|----------------|----------|-------------------|-------------------------------------------------------------------------------------------------------|----------------------------|------------------------------|
| Billing | AccessLog      | Error    | Xóa log           | Hệ thống Billing Xóa log loại AccessLog với mức Error, dữ liệu lưu trữ tối thiểu 90 ngày.             | Không mất mát dữ liệu      | Phân quyền chi tiết          |
| QA      | AuditLog       | Critical | Xuất log          | Hệ thống QA Xuất log loại AuditLog với mức Critical, dữ liệu lưu trữ tối thiểu 90 ngày.               | Log được mã hóa AES- 256   | Theo chuẩn syslog RFC5424    |
| QA      | PerformanceLog | Warning  | Gửi log sang SIEM | Hệ thống QA Gửi log sang SIEM loại PerformanceLog với mức Warning, dữ liệu lưu trữ tối thiểu 90 ngày. | Có thể truy xuất khi cần   | Phân quyền chi tiết          |
| Infra   | ErrorLog       | Error    | Xóa log           | Hệ thống Infra Xóa log loại ErrorLog với mức Error, dữ liệu lưu trữ tối thiểu 90 ngày.                | Không mất mát dữ liệu      | Tự động xóa log sau 180 ngày |
| CRM     | AccessLog      | Info     | Xóa log           | Hệ thống CRM Xóa log loại AccessLog với mức Info, dữ liệu lưu trữ tối thiểu 90 ngày.                  | Tích hợp cảnh báo realtime | Tự động xóa log sau 180 ngày |

<!-- image -->

| VIETTEL AI RACE   | TD449   |
|-------------------|---------|

| IPCC   | AccessLog      | Fatal   | Gửi log sang SIEM   | Hệ thống IPCC Gửi log sang SIEM loại AccessLog với mức Fatal, dữ liệu lưu trữ tối thiểu 90 ngày.   | Tích hợp cảnh báo realtime   | Gửi log sang ELK             |
|--------|----------------|---------|---------------------|----------------------------------------------------------------------------------------------------|------------------------------|------------------------------|
| QA     | AuditLog       | Fatal   | Nén và lưu trữ log  | Hệ thống QA Nén và lưu trữ log loại AuditLog với mức Fatal, dữ liệu lưu trữ tối thiểu 90 ngày.     | Có thể truy xuất khi cần     | Tự động xóa log sau 180 ngày |
| RPA    | ErrorLog       | Fatal   | Xóa log             | Hệ thống RPA Xóa log loại ErrorLog với mức Fatal, dữ liệu lưu trữ tối thiểu 90 ngày.               | Log được mã hóa AES- 256     | Theo chuẩn syslog RFC5424    |
| CRM    | TransactionLog | Info    | Xuất log            | Hệ thống CRM Xuất log loại TransactionLog với mức Info, dữ liệu lưu trữ tối thiểu 90 ngày.         | Log được mã hóa AES- 256     | Gửi log sang ELK             |
| Infra  | PerformanceLog | Info    | Xuất log            | Hệ thống Infra Xuất log loại PerformanceLog với mức Info, dữ liệu lưu trữ tối thiểu 90 ngày.       | Log được mã hóa AES- 256     | Theo chuẩn syslog RFC5424    |
| Infra  | TransactionLog | Warning | Gửi log             | Hệ thống Infra Gửi log sang SIEM loại                                                              | Tích hợp                     | Theo chuẩn syslog            |

<!-- image -->

| VIETTEL AI RACE   | TD449   |
|-------------------|---------|

|         |                |          | sang SIEM          | TransactionLog với mức Warning, dữ liệu lưu trữ tối thiểu 90 ngày.                                   | cảnh báo realtime        | RFC5424                      |
|---------|----------------|----------|--------------------|------------------------------------------------------------------------------------------------------|--------------------------|------------------------------|
| IVR     | AuditLog       | Warning  | Xuất log           | Hệ thống IVR Xuất log loại AuditLog với mức Warning, dữ liệu lưu trữ tối thiểu 90 ngày.              | Có thể truy xuất khi cần | Tự động xóa log sau 180 ngày |
| Billing | ErrorLog       | Warning  | Xóa log            | Hệ thống Billing Xóa log loại ErrorLog với mức Warning, dữ liệu lưu trữ tối thiểu 90 ngày.           | Có thể truy xuất khi cần | Phân quyền chi tiết          |
| IPCC    | PerformanceLog | Critical | Phân tích log      | Hệ thống IPCC Phân tích log loại PerformanceLog với mức Critical, dữ liệu lưu trữ tối thiểu 90 ngày. | Không mất mát dữ liệu    | Tự động xóa log sau 180 ngày |
| RPA     | ErrorLog       | Error    | Nén và lưu trữ log | Hệ thống RPA Nén và lưu trữ log loại ErrorLog với mức Error, dữ liệu lưu trữ tối thiểu 90 ngày.      | Không mất mát dữ liệu    | Gửi log sang ELK             |
| RPA     | TransactionLog | Critical | Xuất log           | Hệ thống RPA Xuất log loại TransactionLog với mức Critical,                                          | Không mất mát dữ liệu    | Có dashboard Grafana         |

<!-- image -->

## VIETTEL AI RACE

## BÁO CÁO HỆ THỐNG &amp; LOG

TD449

Lần ban hành: 1

|     |                |          |                    | dữ liệu lưu trữ tối thiểu 90 ngày.                                                                   |                            |                              |
|-----|----------------|----------|--------------------|------------------------------------------------------------------------------------------------------|----------------------------|------------------------------|
| RPA | AuditLog       | Critical | Nén và lưu trữ log | Hệ thống RPA Nén và lưu trữ log loại AuditLog với mức Critical, dữ liệu lưu trữ tối thiểu 90 ngày.   | Có chỉ số thống kê         | Phân quyền chi tiết          |
| QA  | ErrorLog       | Fatal    | Phân tích log      | Hệ thống QA Phân tích log loại ErrorLog với mức Fatal, dữ liệu lưu trữ tối thiểu 90 ngày.            | Tích hợp cảnh báo realtime | Gửi log sang ELK             |
| RPA | TransactionLog | Error    | Gửi log sang SIEM  | Hệ thống RPA Gửi log sang SIEM loại TransactionLog với mức Error, dữ liệu lưu trữ tối thiểu 90 ngày. | Log được mã hóa AES- 256   | Gửi log sang ELK             |
| RPA | ErrorLog       | Warning  | Phân tích log      | Hệ thống RPA Phân tích log loại ErrorLog với mức Warning, dữ liệu lưu trữ tối thiểu 90 ngày.         | Có chỉ số thống kê         | Tự động xóa log sau 180 ngày |
| CRM | PerformanceLog | Info     | Xóa log            | Hệ thống CRM Xóa log loại PerformanceLog với mức Info, dữ liệu lưu trữ tối                           | Có chỉ số thống kê         | Phân quyền chi tiết          |

<!-- image -->

## VIETTEL AI RACE

## BÁO CÁO HỆ THỐNG &amp; LOG

TD449

Lần ban hành: 1

|       |                |          |                    | thiểu 90 ngày.                                                                                          |                          |                              |
|-------|----------------|----------|--------------------|---------------------------------------------------------------------------------------------------------|--------------------------|------------------------------|
| Infra | AccessLog      | Fatal    | Nén và lưu trữ log | Hệ thống Infra Nén và lưu trữ log loại AccessLog với mức Fatal, dữ liệu lưu trữ tối thiểu 90 ngày.      | Có chỉ số thống kê       | Theo chuẩn syslog RFC5424    |
| IVR   | ErrorLog       | Critical | Phân tích log      | Hệ thống IVR Phân tích log loại ErrorLog với mức Critical, dữ liệu lưu trữ tối thiểu 90 ngày.           | Có chỉ số thống kê       | Theo chuẩn syslog RFC5424    |
| Infra | PerformanceLog | Error    | Nén và lưu trữ log | Hệ thống Infra Nén và lưu trữ log loại PerformanceLog với mức Error, dữ liệu lưu trữ tối thiểu 90 ngày. | Có chỉ số thống kê       | Gửi log sang ELK             |
| IPCC  | TransactionLog | Info     | Gửi log sang SIEM  | Hệ thống IPCC Gửi log sang SIEM loại TransactionLog với mức Info, dữ liệu lưu trữ tối thiểu 90 ngày.    | Có thể truy xuất khi cần | Phân quyền chi tiết          |
| IPCC  | ErrorLog       | Error    | Nén và lưu trữ     | Hệ thống IPCC Nén và lưu trữ log loại ErrorLog với mức Error, dữ liệu lưu trữ tối thiểu 90              | Có chỉ số thống kê       | Tự động xóa log sau 180 ngày |

<!-- image -->

## VIETTEL AI RACE

## BÁO CÁO HỆ THỐNG &amp; LOG

TD449

Lần ban hành: 1

|       |                |          | log               | ngày.                                                                                                   |                            |                              |
|-------|----------------|----------|-------------------|---------------------------------------------------------------------------------------------------------|----------------------------|------------------------------|
| RPA   | PerformanceLog | Error    | Gửi log sang SIEM | Hệ thống RPA Gửi log sang SIEM loại PerformanceLog với mức Error, dữ liệu lưu trữ tối thiểu 90 ngày.    | Log được mã hóa AES- 256   | Tự động xóa log sau 180 ngày |
| Infra | ErrorLog       | Critical | Xóa log           | Hệ thống Infra Xóa log loại ErrorLog với mức Critical, dữ liệu lưu trữ tối thiểu 90 ngày.               | Tích hợp cảnh báo realtime | Gửi log sang ELK             |
| IVR   | PerformanceLog | Critical | Gửi log sang SIEM | Hệ thống IVR Gửi log sang SIEM loại PerformanceLog với mức Critical, dữ liệu lưu trữ tối thiểu 90 ngày. | Không mất mát dữ liệu      | Theo chuẩn syslog RFC5424    |
| Infra | AuditLog       | Error    | Gửi log sang SIEM | Hệ thống Infra Gửi log sang SIEM loại AuditLog với mức Error, dữ liệu lưu trữ tối thiểu 90 ngày.        | Log được mã hóa AES- 256   | Theo chuẩn syslog RFC5424    |
| IVR   | ErrorLog       | Critical | Xóa log           | Hệ thống IVR Xóa log loại ErrorLog với mức Critical, dữ liệu lưu trữ tối thiểu 90 ngày.                 | Không mất mát dữ liệu      | Phân quyền chi tiết          |
| QA    | PerformanceLog | Fatal    | Nén               | Hệ thống QA Nén                                                                                         | Có thể                     | Tự động xóa                  |

<!-- image -->

| VIETTEL AI RACE   | TD449   |
|-------------------|---------|

|         |                |          | và lưu trữ log   | và lưu trữ log loại PerformanceLog với mức Fatal, dữ liệu lưu trữ tối thiểu 90 ngày.                | truy xuất khi cần          | log sau 180 ngày             |
|---------|----------------|----------|------------------|-----------------------------------------------------------------------------------------------------|----------------------------|------------------------------|
| RPA     | TransactionLog | Critical | Phân tích log    | Hệ thống RPA Phân tích log loại TransactionLog với mức Critical, dữ liệu lưu trữ tối thiểu 90 ngày. | Không mất mát dữ liệu      | Gửi log sang ELK             |
| RPA     | PerformanceLog | Fatal    | Xóa log          | Hệ thống RPA Xóa log loại PerformanceLog với mức Fatal, dữ liệu lưu trữ tối thiểu 90 ngày.          | Không mất mát dữ liệu      | Phân quyền chi tiết          |
| Billing | ErrorLog       | Fatal    | Xóa log          | Hệ thống Billing Xóa log loại ErrorLog với mức Fatal, dữ liệu lưu trữ tối thiểu 90 ngày.            | Có chỉ số thống kê         | Phân quyền chi tiết          |
| RPA     | AccessLog      | Fatal    | Xóa log          | Hệ thống RPA Xóa log loại AccessLog với mức Fatal, dữ liệu lưu trữ tối thiểu 90 ngày.               | Tích hợp cảnh báo realtime | Tự động xóa log sau 180 ngày |
| CRM     | AccessLog      | Warning  | Xuất log         | Hệ thống CRM Xuất log loại AccessLog với                                                            | Có thể truy xuất khi       | Gửi log sang ELK             |

<!-- image -->

| VIETTEL AI RACE   | TD449   |
|-------------------|---------|

|      |                |         |                    | mức Warning, dữ liệu lưu trữ tối thiểu 90 ngày.                                                        | cần                      |                              |
|------|----------------|---------|--------------------|--------------------------------------------------------------------------------------------------------|--------------------------|------------------------------|
| IVR  | PerformanceLog | Warning | Gửi log sang SIEM  | Hệ thống IVR Gửi log sang SIEM loại PerformanceLog với mức Warning, dữ liệu lưu trữ tối thiểu 90 ngày. | Có thể truy xuất khi cần | Tự động xóa log sau 180 ngày |
| IPCC | PerformanceLog | Error   | Nén và lưu trữ log | Hệ thống IPCC Nén và lưu trữ log loại PerformanceLog với mức Error, dữ liệu lưu trữ tối thiểu 90 ngày. | Có thể truy xuất khi cần | Có dashboard Grafana         |
| QA   | TransactionLog | Error   | Nén và lưu trữ log | Hệ thống QA Nén và lưu trữ log loại TransactionLog với mức Error, dữ liệu lưu trữ tối thiểu 90 ngày.   | Có chỉ số thống kê       | Tự động xóa log sau 180 ngày |
| QA   | AccessLog      | Error   | Phân tích log      | Hệ thống QA Phân tích log loại AccessLog với mức Error, dữ liệu lưu trữ tối thiểu 90 ngày.             | Có chỉ số thống kê       | Gửi log sang ELK             |
| RPA  | AuditLog       | Info    | Phân tích          | Hệ thống RPA Phân tích log loại AuditLog với mức                                                       | Có thể truy xuất khi     | Phân quyền chi tiết          |

<!-- image -->

| VIETTEL AI RACE   | TD449   |
|-------------------|---------|

|         |                |         | log                | Info, dữ liệu lưu trữ tối thiểu 90 ngày.                                                             | cần                      |                      |
|---------|----------------|---------|--------------------|------------------------------------------------------------------------------------------------------|--------------------------|----------------------|
| Billing | ErrorLog       | Fatal   | Nén và lưu trữ log | Hệ thống Billing Nén và lưu trữ log loại ErrorLog với mức Fatal, dữ liệu lưu trữ tối thiểu 90 ngày.  | Không mất mát dữ liệu    | Có dashboard Grafana |
| CRM     | TransactionLog | Info    | Nén và lưu trữ log | Hệ thống CRM Nén và lưu trữ log loại TransactionLog với mức Info, dữ liệu lưu trữ tối thiểu 90 ngày. | Log được mã hóa AES- 256 | Gửi log sang ELK     |
| Billing | TransactionLog | Fatal   | Xóa log            | Hệ thống Billing Xóa log loại TransactionLog với mức Fatal, dữ liệu lưu trữ tối thiểu 90 ngày.       | Có chỉ số thống kê       | Gửi log sang ELK     |
| CRM     | TransactionLog | Error   | Xuất log           | Hệ thống CRM Xuất log loại TransactionLog với mức Error, dữ liệu lưu trữ tối thiểu 90 ngày.          | Có thể truy xuất khi cần | Gửi log sang ELK     |
| Infra   | AccessLog      | Warning | Gửi log sang       | Hệ thống Infra Gửi log sang SIEM loại AccessLog với                                                  | Có chỉ số thống          | Có dashboard Grafana |

<!-- image -->

| VIETTEL AI RACE   | TD449   |
|-------------------|---------|

|       |                |          | SIEM               | mức Warning, dữ liệu lưu trữ tối thiểu 90 ngày.                                                         | kê                         |                              |
|-------|----------------|----------|--------------------|---------------------------------------------------------------------------------------------------------|----------------------------|------------------------------|
| IPCC  | AuditLog       | Fatal    | Gửi log sang SIEM  | Hệ thống IPCC Gửi log sang SIEM loại AuditLog với mức Fatal, dữ liệu lưu trữ tối thiểu 90 ngày.         | Không mất mát dữ liệu      | Gửi log sang ELK             |
| CRM   | TransactionLog | Warning  | Nén và lưu trữ log | Hệ thống CRM Nén và lưu trữ log loại TransactionLog với mức Warning, dữ liệu lưu trữ tối thiểu 90 ngày. | Có chỉ số thống kê         | Gửi log sang ELK             |
| IVR   | AccessLog      | Error    | Xuất log           | Hệ thống IVR Xuất log loại AccessLog với mức Error, dữ liệu lưu trữ tối thiểu 90 ngày.                  | Có thể truy xuất khi cần   | Tự động xóa log sau 180 ngày |
| CRM   | TransactionLog | Critical | Xóa log            | Hệ thống CRM Xóa log loại TransactionLog với mức Critical, dữ liệu lưu trữ tối thiểu 90 ngày.           | Tích hợp cảnh báo realtime | Gửi log sang ELK             |
| Infra | TransactionLog | Fatal    | Nén và lưu trữ     | Hệ thống Infra Nén và lưu trữ log loại TransactionLog với mức Fatal, dữ                                 | Không mất mát dữ liệu      | Theo chuẩn syslog RFC5424    |

<!-- image -->

## VIETTEL AI RACE

## BÁO CÁO HỆ THỐNG &amp; LOG

TD449

Lần ban hành: 1

|         |                |          | log               | liệu lưu trữ tối thiểu 90 ngày.                                                                      |                          |                              |
|---------|----------------|----------|-------------------|------------------------------------------------------------------------------------------------------|--------------------------|------------------------------|
| IPCC    | PerformanceLog | Critical | Xuất log          | Hệ thống IPCC Xuất log loại PerformanceLog với mức Critical, dữ liệu lưu trữ tối thiểu 90 ngày.      | Log được mã hóa AES- 256 | Gửi log sang ELK             |
| Billing | TransactionLog | Fatal    | Xóa log           | Hệ thống Billing Xóa log loại TransactionLog với mức Fatal, dữ liệu lưu trữ tối thiểu 90 ngày.       | Có thể truy xuất khi cần | Gửi log sang ELK             |
| Infra   | AccessLog      | Fatal    | Xóa log           | Hệ thống Infra Xóa log loại AccessLog với mức Fatal, dữ liệu lưu trữ tối thiểu 90 ngày.              | Log được mã hóa AES- 256 | Tự động xóa log sau 180 ngày |
| IPCC    | TransactionLog | Info     | Gửi log sang SIEM | Hệ thống IPCC Gửi log sang SIEM loại TransactionLog với mức Info, dữ liệu lưu trữ tối thiểu 90 ngày. | Log được mã hóa AES- 256 | Gửi log sang ELK             |
| IPCC    | AccessLog      | Error    | Phân tích log     | Hệ thống IPCC Phân tích log loại AccessLog với mức Error, dữ liệu lưu trữ tối thiểu 90               | Có chỉ số thống kê       | Gửi log sang ELK             |

<!-- image -->

## VIETTEL AI RACE

## BÁO CÁO HỆ THỐNG &amp; LOG

TD449

Lần ban hành: 1

|         |                |         |                    | ngày.                                                                                                    |                            |                              |
|---------|----------------|---------|--------------------|----------------------------------------------------------------------------------------------------------|----------------------------|------------------------------|
| Infra   | PerformanceLog | Warning | Gửi log sang SIEM  | Hệ thống Infra Gửi log sang SIEM loại PerformanceLog với mức Warning, dữ liệu lưu trữ tối thiểu 90 ngày. | Log được mã hóa AES- 256   | Gửi log sang ELK             |
| IPCC    | PerformanceLog | Warning | Gửi log sang SIEM  | Hệ thống IPCC Gửi log sang SIEM loại PerformanceLog với mức Warning, dữ liệu lưu trữ tối thiểu 90 ngày.  | Không mất mát dữ liệu      | Tự động xóa log sau 180 ngày |
| Billing | AccessLog      | Error   | Nén và lưu trữ log | Hệ thống Billing Nén và lưu trữ log loại AccessLog với mức Error, dữ liệu lưu trữ tối thiểu 90 ngày.     | Tích hợp cảnh báo realtime | Tự động xóa log sau 180 ngày |
| Billing | PerformanceLog | Info    | Gửi log sang SIEM  | Hệ thống Billing Gửi log sang SIEM loại PerformanceLog với mức Info, dữ liệu lưu trữ tối thiểu 90 ngày.  | Tích hợp cảnh báo realtime | Có dashboard Grafana         |
| CRM     | ErrorLog       | Fatal   | Xuất log           | Hệ thống CRM Xuất log loại ErrorLog với mức Fatal, dữ liệu lưu                                           | Có chỉ số thống            | Theo chuẩn syslog RFC5424    |

<!-- image -->

## VIETTEL AI RACE

## BÁO CÁO HỆ THỐNG &amp; LOG

TD449

Lần ban hành: 1

|         |                |          |                    | trữ tối thiểu 90 ngày.                                                                                 | kê                       |                              |
|---------|----------------|----------|--------------------|--------------------------------------------------------------------------------------------------------|--------------------------|------------------------------|
| Billing | ErrorLog       | Critical | Nén và lưu trữ log | Hệ thống Billing Nén và lưu trữ log loại ErrorLog với mức Critical, dữ liệu lưu trữ tối thiểu 90 ngày. | Có thể truy xuất khi cần | Tự động xóa log sau 180 ngày |
| CRM     | ErrorLog       | Critical | Phân tích log      | Hệ thống CRM Phân tích log loại ErrorLog với mức Critical, dữ liệu lưu trữ tối thiểu 90 ngày.          | Có thể truy xuất khi cần | Có dashboard Grafana         |
| QA      | AuditLog       | Fatal    | Gửi log sang SIEM  | Hệ thống QA Gửi log sang SIEM loại AuditLog với mức Fatal, dữ liệu lưu trữ tối thiểu 90 ngày.          | Không mất mát dữ liệu    | Có dashboard Grafana         |
| QA      | PerformanceLog | Fatal    | Phân tích log      | Hệ thống QA Phân tích log loại PerformanceLog với mức Fatal, dữ liệu lưu trữ tối thiểu 90 ngày.        | Có chỉ số thống kê       | Tự động xóa log sau 180 ngày |
| Infra   | TransactionLog | Critical | Xuất log           | Hệ thống Infra Xuất log loại TransactionLog với mức Critical, dữ liệu lưu trữ tối                      | Có chỉ số thống kê       | Tự động xóa log sau 180 ngày |

<!-- image -->

## VIETTEL AI RACE

## BÁO CÁO HỆ THỐNG &amp; LOG

TD449

Lần ban hành: 1

|         |                |          |               | thiểu 90 ngày.                                                                                     |                            |                      |
|---------|----------------|----------|---------------|----------------------------------------------------------------------------------------------------|----------------------------|----------------------|
| CRM     | AuditLog       | Critical | Phân tích log | Hệ thống CRM Phân tích log loại AuditLog với mức Critical, dữ liệu lưu trữ tối thiểu 90 ngày.      | Có chỉ số thống kê         | Phân quyền chi tiết  |
| Billing | AuditLog       | Warning  | Xuất log      | Hệ thống Billing Xuất log loại AuditLog với mức Warning, dữ liệu lưu trữ tối thiểu 90 ngày.        | Log được mã hóa AES- 256   | Phân quyền chi tiết  |
| IPCC    | AccessLog      | Warning  | Phân tích log | Hệ thống IPCC Phân tích log loại AccessLog với mức Warning, dữ liệu lưu trữ tối thiểu 90 ngày.     | Có thể truy xuất khi cần   | Có dashboard Grafana |
| Billing | PerformanceLog | Critical | Xuất log      | Hệ thống Billing Xuất log loại PerformanceLog với mức Critical, dữ liệu lưu trữ tối thiểu 90 ngày. | Log được mã hóa AES- 256   | Gửi log sang ELK     |
| RPA     | AuditLog       | Critical | Xuất log      | Hệ thống RPA Xuất log loại AuditLog với mức Critical, dữ liệu lưu trữ tối thiểu 90                 | Tích hợp cảnh báo realtime | Có dashboard Grafana |

<!-- image -->

## VIETTEL AI RACE

## BÁO CÁO HỆ THỐNG &amp; LOG

TD449

Lần ban hành: 1

|     |          |          |                    | ngày.                                                                                              |                          |                              |
|-----|----------|----------|--------------------|----------------------------------------------------------------------------------------------------|--------------------------|------------------------------|
| CRM | AuditLog | Critical | Nén và lưu trữ log | Hệ thống CRM Nén và lưu trữ log loại AuditLog với mức Critical, dữ liệu lưu trữ tối thiểu 90 ngày. | Không mất mát dữ liệu    | Phân quyền chi tiết          |
| RPA | AuditLog | Info     | Xuất log           | Hệ thống RPA Xuất log loại AuditLog với mức Info, dữ liệu lưu trữ tối thiểu 90 ngày.               | Có thể truy xuất khi cần | Có dashboard Grafana         |
| RPA | ErrorLog | Critical | Xuất log           | Hệ thống RPA Xuất log loại ErrorLog với mức Critical, dữ liệu lưu trữ tối thiểu 90 ngày.           | Không mất mát dữ liệu    | Tự động xóa log sau 180 ngày |
| RPA | ErrorLog | Error    | Xuất log           | Hệ thống RPA Xuất log loại ErrorLog với mức Error, dữ liệu lưu trữ tối thiểu 90 ngày.              | Không mất mát dữ liệu    | Phân quyền chi tiết          |
| QA  | AuditLog | Critical | Xóa log            | Hệ thống QA Xóa log loại AuditLog với mức Critical, dữ liệu lưu trữ tối thiểu 90 ngày.             | Có thể truy xuất khi cần | Theo chuẩn syslog RFC5424    |

<!-- image -->

## VIETTEL AI RACE

## BÁO CÁO HỆ THỐNG &amp; LOG

TD449

Lần ban hành: 1

| IVR   | AccessLog      | Info     | Gửi log sang SIEM   | Hệ thống IVR Gửi log sang SIEM loại AccessLog với mức Info, dữ liệu lưu trữ tối thiểu 90 ngày.        | Có thể truy xuất khi cần   | Phân quyền chi tiết          |
|-------|----------------|----------|---------------------|-------------------------------------------------------------------------------------------------------|----------------------------|------------------------------|
| QA    | TransactionLog | Warning  | Gửi log sang SIEM   | Hệ thống QA Gửi log sang SIEM loại TransactionLog với mức Warning, dữ liệu lưu trữ tối thiểu 90 ngày. | Log được mã hóa AES- 256   | Tự động xóa log sau 180 ngày |
| Infra | AccessLog      | Critical | Phân tích log       | Hệ thống Infra Phân tích log loại AccessLog với mức Critical, dữ liệu lưu trữ tối thiểu 90 ngày.      | Có chỉ số thống kê         | Theo chuẩn syslog RFC5424    |
| RPA   | ErrorLog       | Info     | Gửi log sang SIEM   | Hệ thống RPA Gửi log sang SIEM loại ErrorLog với mức Info, dữ liệu lưu trữ tối thiểu 90 ngày.         | Có chỉ số thống kê         | Gửi log sang ELK             |
| CRM   | AccessLog      | Warning  | Gửi log sang SIEM   | Hệ thống CRM Gửi log sang SIEM loại AccessLog với mức Warning, dữ liệu lưu trữ tối thiểu 90 ngày.     | Có thể truy xuất khi cần   | Có dashboard Grafana         |

<!-- image -->

## VIETTEL AI RACE

## BÁO CÁO HỆ THỐNG &amp; LOG

TD449

Lần ban hành: 1

| RPA     | TransactionLog   | Error    | Xóa log            | Hệ thống RPA Xóa log loại TransactionLog với mức Error, dữ liệu lưu trữ tối thiểu 90 ngày.        | Không mất mát dữ liệu      | Phân quyền chi tiết          |
|---------|------------------|----------|--------------------|---------------------------------------------------------------------------------------------------|----------------------------|------------------------------|
| RPA     | ErrorLog         | Fatal    | Gửi log sang SIEM  | Hệ thống RPA Gửi log sang SIEM loại ErrorLog với mức Fatal, dữ liệu lưu trữ tối thiểu 90 ngày.    | Có thể truy xuất khi cần   | Theo chuẩn syslog RFC5424    |
| RPA     | AuditLog         | Critical | Xóa log            | Hệ thống RPA Xóa log loại AuditLog với mức Critical, dữ liệu lưu trữ tối thiểu 90 ngày.           | Tích hợp cảnh báo realtime | Tự động xóa log sau 180 ngày |
| CRM     | ErrorLog         | Warning  | Nén và lưu trữ log | Hệ thống CRM Nén và lưu trữ log loại ErrorLog với mức Warning, dữ liệu lưu trữ tối thiểu 90 ngày. | Không mất mát dữ liệu      | Có dashboard Grafana         |
| Infra   | TransactionLog   | Info     | Xóa log            | Hệ thống Infra Xóa log loại TransactionLog với mức Info, dữ liệu lưu trữ tối thiểu 90 ngày.       | Log được mã hóa AES- 256   | Gửi log sang ELK             |
| Billing | PerformanceLog   | Info     | Nén và             | Hệ thống Billing Nén và lưu trữ log                                                               | Không mất mát              | Gửi log sang                 |

<!-- image -->

| VIETTEL AI RACE   | TD449   |
|-------------------|---------|

|         |                |          | lưu trữ log   | loại PerformanceLog với mức Info, dữ liệu lưu trữ tối thiểu 90 ngày.                               | dữ liệu                    | ELK                          |
|---------|----------------|----------|---------------|----------------------------------------------------------------------------------------------------|----------------------------|------------------------------|
| Infra   | PerformanceLog | Fatal    | Phân tích log | Hệ thống Infra Phân tích log loại PerformanceLog với mức Fatal, dữ liệu lưu trữ tối thiểu 90 ngày. | Có thể truy xuất khi cần   | Phân quyền chi tiết          |
| IPCC    | TransactionLog | Critical | Xóa log       | Hệ thống IPCC Xóa log loại TransactionLog với mức Critical, dữ liệu lưu trữ tối thiểu 90 ngày.     | Log được mã hóa AES- 256   | Gửi log sang ELK             |
| IPCC    | PerformanceLog | Error    | Xóa log       | Hệ thống IPCC Xóa log loại PerformanceLog với mức Error, dữ liệu lưu trữ tối thiểu 90 ngày.        | Tích hợp cảnh báo realtime | Gửi log sang ELK             |
| Billing | ErrorLog       | Warning  | Xóa log       | Hệ thống Billing Xóa log loại ErrorLog với mức Warning, dữ liệu lưu trữ tối thiểu 90 ngày.         | Tích hợp cảnh báo realtime | Tự động xóa log sau 180 ngày |
| IVR     | ErrorLog       | Fatal    | Gửi log       | Hệ thống IVR Gửi log sang SIEM loại                                                                | Log được                   | Có dashboard                 |

<!-- image -->

| VIETTEL AI RACE   | TD449   |
|-------------------|---------|

|         |                |          | sang SIEM         | ErrorLog với mức Fatal, dữ liệu lưu trữ tối thiểu 90 ngày.                                        | mã hóa AES- 256            | Grafana                   |
|---------|----------------|----------|-------------------|---------------------------------------------------------------------------------------------------|----------------------------|---------------------------|
| CRM     | PerformanceLog | Error    | Xuất log          | Hệ thống CRM Xuất log loại PerformanceLog với mức Error, dữ liệu lưu trữ tối thiểu 90 ngày.       | Tích hợp cảnh báo realtime | Theo chuẩn syslog RFC5424 |
| Billing | TransactionLog | Critical | Xóa log           | Hệ thống Billing Xóa log loại TransactionLog với mức Critical, dữ liệu lưu trữ tối thiểu 90 ngày. | Log được mã hóa AES- 256   | Phân quyền chi tiết       |
| QA      | ErrorLog       | Fatal    | Phân tích log     | Hệ thống QA Phân tích log loại ErrorLog với mức Fatal, dữ liệu lưu trữ tối thiểu 90 ngày.         | Có chỉ số thống kê         | Có dashboard Grafana      |
| Infra   | AuditLog       | Fatal    | Gửi log sang SIEM | Hệ thống Infra Gửi log sang SIEM loại AuditLog với mức Fatal, dữ liệu lưu trữ tối thiểu 90 ngày.  | Log được mã hóa AES- 256   | Gửi log sang ELK          |
| QA      | AuditLog       | Critical | Xuất log          | Hệ thống QA Xuất log loại AuditLog với mức Critical,                                              | Có chỉ số thống            | Theo chuẩn syslog         |

<!-- image -->

## VIETTEL AI RACE

## BÁO CÁO HỆ THỐNG &amp; LOG

TD449

Lần ban hành: 1

|       |                |          |                    | dữ liệu lưu trữ tối thiểu 90 ngày.                                                                    | kê                         | RFC5424                      |
|-------|----------------|----------|--------------------|-------------------------------------------------------------------------------------------------------|----------------------------|------------------------------|
| QA    | PerformanceLog | Error    | Gửi log sang SIEM  | Hệ thống QA Gửi log sang SIEM loại PerformanceLog với mức Error, dữ liệu lưu trữ tối thiểu 90 ngày.   | Có chỉ số thống kê         | Tự động xóa log sau 180 ngày |
| Infra | TransactionLog | Info     | Xóa log            | Hệ thống Infra Xóa log loại TransactionLog với mức Info, dữ liệu lưu trữ tối thiểu 90 ngày.           | Không mất mát dữ liệu      | Tự động xóa log sau 180 ngày |
| IVR   | PerformanceLog | Fatal    | Nén và lưu trữ log | Hệ thống IVR Nén và lưu trữ log loại PerformanceLog với mức Fatal, dữ liệu lưu trữ tối thiểu 90 ngày. | Tích hợp cảnh báo realtime | Có dashboard Grafana         |
| CRM   | TransactionLog | Info     | Xóa log            | Hệ thống CRM Xóa log loại TransactionLog với mức Info, dữ liệu lưu trữ tối thiểu 90 ngày.             | Có thể truy xuất khi cần   | Gửi log sang ELK             |
| CRM   | AccessLog      | Critical | Phân tích log      | Hệ thống CRM Phân tích log loại AccessLog với mức Critical, dữ liệu lưu trữ tối                       | Log được mã hóa AES-       | Theo chuẩn syslog RFC5424    |

<!-- image -->

## VIETTEL AI RACE

## BÁO CÁO HỆ THỐNG &amp; LOG

TD449

Lần ban hành: 1

|         |                |         |                    | thiểu 90 ngày.                                                                                       | 256                        |                              |
|---------|----------------|---------|--------------------|------------------------------------------------------------------------------------------------------|----------------------------|------------------------------|
| RPA     | AccessLog      | Error   | Xóa log            | Hệ thống RPA Xóa log loại AccessLog với mức Error, dữ liệu lưu trữ tối thiểu 90 ngày.                | Không mất mát dữ liệu      | Có dashboard Grafana         |
| RPA     | AuditLog       | Info    | Xuất log           | Hệ thống RPA Xuất log loại AuditLog với mức Info, dữ liệu lưu trữ tối thiểu 90 ngày.                 | Có chỉ số thống kê         | Gửi log sang ELK             |
| Infra   | ErrorLog       | Warning | Phân tích log      | Hệ thống Infra Phân tích log loại ErrorLog với mức Warning, dữ liệu lưu trữ tối thiểu 90 ngày.       | Tích hợp cảnh báo realtime | Tự động xóa log sau 180 ngày |
| CRM     | PerformanceLog | Info    | Nén và lưu trữ log | Hệ thống CRM Nén và lưu trữ log loại PerformanceLog với mức Info, dữ liệu lưu trữ tối thiểu 90 ngày. | Có thể truy xuất khi cần   | Có dashboard Grafana         |
| Billing | AuditLog       | Error   | Nén và lưu trữ log | Hệ thống Billing Nén và lưu trữ log loại AuditLog với mức Error, dữ liệu lưu trữ tối thiểu 90        | Log được mã hóa AES- 256   | Phân quyền chi tiết          |

<!-- image -->

## VIETTEL AI RACE

## BÁO CÁO HỆ THỐNG &amp; LOG

TD449

Lần ban hành: 1

|       |                |          |                    | ngày.                                                                                                |                            |                              |
|-------|----------------|----------|--------------------|------------------------------------------------------------------------------------------------------|----------------------------|------------------------------|
| IVR   | TransactionLog | Error    | Phân tích log      | Hệ thống IVR Phân tích log loại TransactionLog với mức Error, dữ liệu lưu trữ tối thiểu 90 ngày.     | Không mất mát dữ liệu      | Tự động xóa log sau 180 ngày |
| QA    | TransactionLog | Fatal    | Nén và lưu trữ log | Hệ thống QA Nén và lưu trữ log loại TransactionLog với mức Fatal, dữ liệu lưu trữ tối thiểu 90 ngày. | Tích hợp cảnh báo realtime | Tự động xóa log sau 180 ngày |
| Infra | AuditLog       | Warning  | Xuất log           | Hệ thống Infra Xuất log loại AuditLog với mức Warning, dữ liệu lưu trữ tối thiểu 90 ngày.            | Không mất mát dữ liệu      | Phân quyền chi tiết          |
| IPCC  | PerformanceLog | Info     | Phân tích log      | Hệ thống IPCC Phân tích log loại PerformanceLog với mức Info, dữ liệu lưu trữ tối thiểu 90 ngày.     | Log được mã hóa AES- 256   | Tự động xóa log sau 180 ngày |
| IVR   | PerformanceLog | Critical | Phân tích log      | Hệ thống IVR Phân tích log loại PerformanceLog với mức Critical, dữ liệu lưu trữ tối                 | Có chỉ số thống kê         | Theo chuẩn syslog RFC5424    |

<!-- image -->

## VIETTEL AI RACE

## BÁO CÁO HỆ THỐNG &amp; LOG

TD449

Lần ban hành: 1

|         |                |          |                    | thiểu 90 ngày.                                                                                       |                            |                           |
|---------|----------------|----------|--------------------|------------------------------------------------------------------------------------------------------|----------------------------|---------------------------|
| Infra   | ErrorLog       | Critical | Nén và lưu trữ log | Hệ thống Infra Nén và lưu trữ log loại ErrorLog với mức Critical, dữ liệu lưu trữ tối thiểu 90 ngày. | Tích hợp cảnh báo realtime | Phân quyền chi tiết       |
| QA      | ErrorLog       | Info     | Gửi log sang SIEM  | Hệ thống QA Gửi log sang SIEM loại ErrorLog với mức Info, dữ liệu lưu trữ tối thiểu 90 ngày.         | Không mất mát dữ liệu      | Theo chuẩn syslog RFC5424 |
| IVR     | ErrorLog       | Fatal    | Xóa log            | Hệ thống IVR Xóa log loại ErrorLog với mức Fatal, dữ liệu lưu trữ tối thiểu 90 ngày.                 | Tích hợp cảnh báo realtime | Có dashboard Grafana      |
| Billing | ErrorLog       | Info     | Gửi log sang SIEM  | Hệ thống Billing Gửi log sang SIEM loại ErrorLog với mức Info, dữ liệu lưu trữ tối thiểu 90 ngày.    | Có thể truy xuất khi cần   | Theo chuẩn syslog RFC5424 |
| Infra   | TransactionLog | Fatal    | Xóa log            | Hệ thống Infra Xóa log loại TransactionLog với mức Fatal, dữ liệu lưu trữ tối thiểu 90 ngày.         | Log được mã hóa AES- 256   | Phân quyền chi tiết       |

<!-- image -->

## VIETTEL AI RACE

## BÁO CÁO HỆ THỐNG &amp; LOG

TD449

Lần ban hành: 1

| Billing   | TransactionLog   | Fatal   | Xuất log          | Hệ thống Billing Xuất log loại TransactionLog với mức Fatal, dữ liệu lưu trữ tối thiểu 90 ngày.    | Không mất mát dữ liệu      | Gửi log sang ELK          |
|-----------|------------------|---------|-------------------|----------------------------------------------------------------------------------------------------|----------------------------|---------------------------|
| IPCC      | ErrorLog         | Warning | Xóa log           | Hệ thống IPCC Xóa log loại ErrorLog với mức Warning, dữ liệu lưu trữ tối thiểu 90 ngày.            | Tích hợp cảnh báo realtime | Phân quyền chi tiết       |
| IVR       | AccessLog        | Error   | Gửi log sang SIEM | Hệ thống IVR Gửi log sang SIEM loại AccessLog với mức Error, dữ liệu lưu trữ tối thiểu 90 ngày.    | Log được mã hóa AES- 256   | Gửi log sang ELK          |
| Infra     | PerformanceLog   | Fatal   | Phân tích log     | Hệ thống Infra Phân tích log loại PerformanceLog với mức Fatal, dữ liệu lưu trữ tối thiểu 90 ngày. | Log được mã hóa AES- 256   | Theo chuẩn syslog RFC5424 |
| Infra     | AuditLog         | Error   | Gửi log sang SIEM | Hệ thống Infra Gửi log sang SIEM loại AuditLog với mức Error, dữ liệu lưu trữ tối thiểu 90 ngày.   | Log được mã hóa AES- 256   | Phân quyền chi tiết       |

<!-- image -->

## VIETTEL AI RACE

## BÁO CÁO HỆ THỐNG &amp; LOG

TD449

Lần ban hành: 1

| Infra   | AccessLog      | Warning   | Xóa log            | Hệ thống Infra Xóa log loại AccessLog với mức Warning, dữ liệu lưu trữ tối thiểu 90 ngày.            | Có chỉ số thống kê       | Gửi log sang ELK             |
|---------|----------------|-----------|--------------------|------------------------------------------------------------------------------------------------------|--------------------------|------------------------------|
| IVR     | ErrorLog       | Error     | Gửi log sang SIEM  | Hệ thống IVR Gửi log sang SIEM loại ErrorLog với mức Error, dữ liệu lưu trữ tối thiểu 90 ngày.       | Có chỉ số thống kê       | Gửi log sang ELK             |
| Infra   | ErrorLog       | Info      | Nén và lưu trữ log | Hệ thống Infra Nén và lưu trữ log loại ErrorLog với mức Info, dữ liệu lưu trữ tối thiểu 90 ngày.     | Không mất mát dữ liệu    | Theo chuẩn syslog RFC5424    |
| QA      | TransactionLog | Fatal     | Nén và lưu trữ log | Hệ thống QA Nén và lưu trữ log loại TransactionLog với mức Fatal, dữ liệu lưu trữ tối thiểu 90 ngày. | Log được mã hóa AES- 256 | Tự động xóa log sau 180 ngày |
| RPA     | AccessLog      | Info      | Xóa log            | Hệ thống RPA Xóa log loại AccessLog với mức Info, dữ liệu lưu trữ tối thiểu 90 ngày.                 | Không mất mát dữ liệu    | Có dashboard Grafana         |
| RPA     | ErrorLog       | Error     | Xuất log           | Hệ thống RPA Xuất log loại ErrorLog với mức                                                          | Có chỉ số thống          | Theo chuẩn syslog            |

<!-- image -->

| VIETTEL AI RACE   | TD449   |
|-------------------|---------|

|         |                |          |                    | Error, dữ liệu lưu trữ tối thiểu 90 ngày.                                                                | kê                       | RFC5424                      |
|---------|----------------|----------|--------------------|----------------------------------------------------------------------------------------------------------|--------------------------|------------------------------|
| Infra   | ErrorLog       | Critical | Nén và lưu trữ log | Hệ thống Infra Nén và lưu trữ log loại ErrorLog với mức Critical, dữ liệu lưu trữ tối thiểu 90 ngày.     | Log được mã hóa AES- 256 | Có dashboard Grafana         |
| IPCC    | TransactionLog | Critical | Gửi log sang SIEM  | Hệ thống IPCC Gửi log sang SIEM loại TransactionLog với mức Critical, dữ liệu lưu trữ tối thiểu 90 ngày. | Có chỉ số thống kê       | Theo chuẩn syslog RFC5424    |
| Infra   | PerformanceLog | Info     | Gửi log sang SIEM  | Hệ thống Infra Gửi log sang SIEM loại PerformanceLog với mức Info, dữ liệu lưu trữ tối thiểu 90 ngày.    | Log được mã hóa AES- 256 | Phân quyền chi tiết          |
| RPA     | PerformanceLog | Fatal    | Nén và lưu trữ log | Hệ thống RPA Nén và lưu trữ log loại PerformanceLog với mức Fatal, dữ liệu lưu trữ tối thiểu 90 ngày.    | Có chỉ số thống kê       | Tự động xóa log sau 180 ngày |
| Billing | AuditLog       | Critical | Xuất log           | Hệ thống Billing Xuất log loại AuditLog với mức                                                          | Có chỉ số thống          | Phân quyền chi tiết          |

<!-- image -->

| VIETTEL AI RACE   | TD449   |
|-------------------|---------|

|      |           |         |                   | Critical, dữ liệu lưu trữ tối thiểu 90 ngày.                                                  | kê                         |                           |
|------|-----------|---------|-------------------|-----------------------------------------------------------------------------------------------|----------------------------|---------------------------|
| IVR  | AuditLog  | Info    | Gửi log sang SIEM | Hệ thống IVR Gửi log sang SIEM loại AuditLog với mức Info, dữ liệu lưu trữ tối thiểu 90 ngày. | Tích hợp cảnh báo realtime | Gửi log sang ELK          |
| RPA  | AuditLog  | Warning | Xuất log          | Hệ thống RPA Xuất log loại AuditLog với mức Warning, dữ liệu lưu trữ tối thiểu 90 ngày.       | Log được mã hóa AES- 256   | Có dashboard Grafana      |
| IPCC | AuditLog  | Info    | Phân tích log     | Hệ thống IPCC Phân tích log loại AuditLog với mức Info, dữ liệu lưu trữ tối thiểu 90 ngày.    | Có chỉ số thống kê         | Theo chuẩn syslog RFC5424 |
| IVR  | AccessLog | Fatal   | Xuất log          | Hệ thống IVR Xuất log loại AccessLog với mức Fatal, dữ liệu lưu trữ tối thiểu 90 ngày.        | Không mất mát dữ liệu      | Theo chuẩn syslog RFC5424 |
| RPA  | ErrorLog  | Warning | Nén và lưu trữ    | Hệ thống RPA Nén và lưu trữ log loại ErrorLog với mức Warning, dữ liệu lưu trữ tối thiểu 90   | Tích hợp cảnh báo          | Gửi log sang ELK          |

<!-- image -->

## VIETTEL AI RACE

## BÁO CÁO HỆ THỐNG &amp; LOG

TD449

Lần ban hành: 1

|       |                |         | log               | ngày.                                                                                           | realtime                   |                              |
|-------|----------------|---------|-------------------|-------------------------------------------------------------------------------------------------|----------------------------|------------------------------|
| QA    | AuditLog       | Warning | Xóa log           | Hệ thống QA Xóa log loại AuditLog với mức Warning, dữ liệu lưu trữ tối thiểu 90 ngày.           | Có thể truy xuất khi cần   | Tự động xóa log sau 180 ngày |
| IPCC  | ErrorLog       | Info    | Phân tích log     | Hệ thống IPCC Phân tích log loại ErrorLog với mức Info, dữ liệu lưu trữ tối thiểu 90 ngày.      | Tích hợp cảnh báo realtime | Gửi log sang ELK             |
| IVR   | ErrorLog       | Warning | Phân tích log     | Hệ thống IVR Phân tích log loại ErrorLog với mức Warning, dữ liệu lưu trữ tối thiểu 90 ngày.    | Không mất mát dữ liệu      | Phân quyền chi tiết          |
| Infra | TransactionLog | Warning | Xuất log          | Hệ thống Infra Xuất log loại TransactionLog với mức Warning, dữ liệu lưu trữ tối thiểu 90 ngày. | Có chỉ số thống kê         | Theo chuẩn syslog RFC5424    |
| RPA   | AccessLog      | Fatal   | Gửi log sang SIEM | Hệ thống RPA Gửi log sang SIEM loại AccessLog với mức Fatal, dữ liệu lưu trữ tối thiểu 90 ngày. | Có thể truy xuất khi cần   | Gửi log sang ELK             |

<!-- image -->

## VIETTEL AI RACE

## BÁO CÁO HỆ THỐNG &amp; LOG

TD449

Lần ban hành: 1

| CRM     | ErrorLog       | Fatal    | Xóa log            | Hệ thống CRM Xóa log loại ErrorLog với mức Fatal, dữ liệu lưu trữ tối thiểu 90 ngày.                         | Log được mã hóa AES- 256   | Tự động xóa log sau 180 ngày   |
|---------|----------------|----------|--------------------|--------------------------------------------------------------------------------------------------------------|----------------------------|--------------------------------|
| IPCC    | ErrorLog       | Critical | Xuất log           | Hệ thống IPCC Xuất log loại ErrorLog với mức Critical, dữ liệu lưu trữ tối thiểu 90 ngày.                    | Không mất mát dữ liệu      | Theo chuẩn syslog RFC5424      |
| RPA     | AuditLog       | Info     | Nén và lưu trữ log | Hệ thống RPA Nén và lưu trữ log loại AuditLog với mức Info, dữ liệu lưu trữ tối thiểu 90 ngày.               | Có thể truy xuất khi cần   | Theo chuẩn syslog RFC5424      |
| Billing | PerformanceLog | Critical | Nén và lưu trữ log | Hệ thống Billing Nén và lưu trữ log loại PerformanceLog với mức Critical, dữ liệu lưu trữ tối thiểu 90 ngày. | Log được mã hóa AES- 256   | Gửi log sang ELK               |
| Infra   | AccessLog      | Critical | Xuất log           | Hệ thống Infra Xuất log loại AccessLog với mức Critical, dữ liệu lưu trữ tối thiểu 90 ngày.                  | Có chỉ số thống kê         | Phân quyền chi tiết            |

<!-- image -->

## VIETTEL AI RACE

## BÁO CÁO HỆ THỐNG &amp; LOG

TD449

Lần ban hành: 1

| IVR     | AccessLog      | Critical   | Xuất log           | Hệ thống IVR Xuất log loại AccessLog với mức Critical, dữ liệu lưu trữ tối thiểu 90 ngày.                | Không mất mát dữ liệu      | Gửi log sang ELK             |
|---------|----------------|------------|--------------------|----------------------------------------------------------------------------------------------------------|----------------------------|------------------------------|
| Billing | TransactionLog | Error      | Gửi log sang SIEM  | Hệ thống Billing Gửi log sang SIEM loại TransactionLog với mức Error, dữ liệu lưu trữ tối thiểu 90 ngày. | Log được mã hóa AES- 256   | Tự động xóa log sau 180 ngày |
| CRM     | AccessLog      | Info       | Xuất log           | Hệ thống CRM Xuất log loại AccessLog với mức Info, dữ liệu lưu trữ tối thiểu 90 ngày.                    | Tích hợp cảnh báo realtime | Tự động xóa log sau 180 ngày |
| CRM     | PerformanceLog | Critical   | Xóa log            | Hệ thống CRM Xóa log loại PerformanceLog với mức Critical, dữ liệu lưu trữ tối thiểu 90 ngày.            | Tích hợp cảnh báo realtime | Theo chuẩn syslog RFC5424    |
| CRM     | PerformanceLog | Fatal      | Nén và lưu trữ log | Hệ thống CRM Nén và lưu trữ log loại PerformanceLog với mức Fatal, dữ liệu lưu trữ tối thiểu 90 ngày.    | Có chỉ số thống kê         | Tự động xóa log sau 180 ngày |

<!-- image -->

## VIETTEL AI RACE

## BÁO CÁO HỆ THỐNG &amp; LOG

TD449

Lần ban hành: 1

| Billing   | TransactionLog   | Fatal   | Nén và lưu trữ log   | Hệ thống Billing Nén và lưu trữ log loại TransactionLog với mức Fatal, dữ liệu lưu trữ tối thiểu 90 ngày.   | Không mất mát dữ liệu      | Tự động xóa log sau 180 ngày   |
|-----------|------------------|---------|----------------------|-------------------------------------------------------------------------------------------------------------|----------------------------|--------------------------------|
| Infra     | AuditLog         | Fatal   | Gửi log sang SIEM    | Hệ thống Infra Gửi log sang SIEM loại AuditLog với mức Fatal, dữ liệu lưu trữ tối thiểu 90 ngày.            | Có chỉ số thống kê         | Có dashboard Grafana           |
| CRM       | PerformanceLog   | Error   | Nén và lưu trữ log   | Hệ thống CRM Nén và lưu trữ log loại PerformanceLog với mức Error, dữ liệu lưu trữ tối thiểu 90 ngày.       | Tích hợp cảnh báo realtime | Theo chuẩn syslog RFC5424      |