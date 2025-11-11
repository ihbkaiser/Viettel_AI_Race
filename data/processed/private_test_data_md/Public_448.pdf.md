<!-- image -->

## VIETTEL AI RACE

## QUẢN LÝ API &amp; LOG

TD448

Lần ban hành: 1

| API                       | Phương thức   | Hành động           | Mô tả chi tiết                                                                                                        | Kết quả                     | Ghi chú                          |
|---------------------------|---------------|---------------------|-----------------------------------------------------------------------------------------------------------------------|-----------------------------|----------------------------------|
| /customer/update          | PATCH         | Thêm bản ghi        | API /customer/update sử dụng phương thức PATCH để Thêm bản ghi, có xác thực OAuth2 và log giao dịch chi tiết.         | Rollback khi lỗi            | Giới hạn rate-limit 1000 req/min |
| /invoice/export           | PATCH         | Xóa thông tin       | API /invoice/export sử dụng phương thức PATCH để Xóa thông tin, có xác thực OAuth2 và log giao dịch chi tiết.         | Thông báo sự kiện qua Kafka | Tích hợp với API Gateway         |
| /security/firewall/config | GET           | Xóa thông tin       | API /security/firewall/config sử dụng phương thức GET để Xóa thông tin, có xác thực OAuth2 và log giao dịch chi tiết. | Thông báo sự kiện qua Kafka | Giới hạn rate-limit 1000 req/min |
| /ivr/callflow             | POST          | Kiểm tra trạng thái | API /ivr/callflow sử dụng phương thức POST để Kiểm tra trạng thái, có xác thực OAuth2 và log giao dịch chi tiết.      | Thông báo sự kiện qua Kafka | Có versioning v1/v2              |
| /crm/lead/import          | PUT           | Export dữ liệu      | API /crm/lead/import sử dụng phương thức PUT để Export dữ liệu, có xác thực OAuth2 và log giao dịch chi tiết.         | Thành công <1s              | Tích hợp với API Gateway         |

<!-- image -->

| VIETTEL AI RACE   | TD448   |
|-------------------|---------|

| /rpa/task/execute    | POST   | Cập nhật cấu hình   | API /rpa/task/execute sử dụng phương thức POST để Cập nhật cấu hình, có xác thực OAuth2 và log giao dịch chi tiết.      | Log đầy đủ                  | Tích hợp với API Gateway   |
|----------------------|--------|---------------------|-------------------------------------------------------------------------------------------------------------------------|-----------------------------|----------------------------|
| /customer/update     | GET    | Thêm bản ghi        | API /customer/update sử dụng phương thức GET để Thêm bản ghi, có xác thực OAuth2 và log giao dịch chi tiết.             | Retry tối đa 3 lần          | Hỗ trợ JSON và XML         |
| /network/qos/monitor | POST   | Kiểm tra trạng thái | API /network/qos/monitor sử dụng phương thức POST để Kiểm tra trạng thái, có xác thực OAuth2 và log giao dịch chi tiết. | Thông báo sự kiện qua Kafka | Tích hợp với API Gateway   |
| /invoice/export      | POST   | Cập nhật cấu hình   | API /invoice/export sử dụng phương thức POST để Cập nhật cấu hình, có xác thực OAuth2 và log giao dịch chi tiết.        | Rollback khi lỗi            | Theo chuẩn RESTful         |
| /network/qos/monitor | GET    | Export dữ liệu      | API /network/qos/monitor sử dụng phương thức GET để Export dữ liệu, có xác thực OAuth2 và log giao dịch chi tiết.       | Thông báo sự kiện qua Kafka | Hỗ trợ JSON và XML         |

<!-- image -->

| VIETTEL AI RACE   | TD448   |
|-------------------|---------|

| /rpa/task/execute         | POST   | Export dữ liệu      | API /rpa/task/execute sử dụng phương thức POST để Export dữ liệu, có xác thực OAuth2 và log giao dịch chi tiết.                | Log đầy đủ                  | Giới hạn rate-limit 1000 req/min   |
|---------------------------|--------|---------------------|--------------------------------------------------------------------------------------------------------------------------------|-----------------------------|------------------------------------|
| /crm/lead/import          | PATCH  | Export dữ liệu      | API /crm/lead/import sử dụng phương thức PATCH để Export dữ liệu, có xác thực OAuth2 và log giao dịch chi tiết.                | Rollback khi lỗi            | Giới hạn rate-limit 1000 req/min   |
| /invoice/export           | POST   | Cập nhật cấu hình   | API /invoice/export sử dụng phương thức POST để Cập nhật cấu hình, có xác thực OAuth2 và log giao dịch chi tiết.               | Thông báo sự kiện qua Kafka | Hỗ trợ JSON và XML                 |
| /ivr/callflow             | GET    | Xóa thông tin       | API /ivr/callflow sử dụng phương thức GET để Xóa thông tin, có xác thực OAuth2 và log giao dịch chi tiết.                      | Thông báo sự kiện qua Kafka | Giới hạn rate-limit 1000 req/min   |
| /security/firewall/config | DELETE | Kiểm tra trạng thái | API /security/firewall/config sử dụng phương thức DELETE để Kiểm tra trạng thái, có xác thực OAuth2 và log giao dịch chi tiết. | Log đầy đủ                  | Tích hợp với API Gateway           |

<!-- image -->

| VIETTEL AI RACE   | TD448   |
|-------------------|---------|

| /ivr/callflow             | POST   | Xóa thông tin       | API /ivr/callflow sử dụng phương thức POST để Xóa thông tin, có xác thực OAuth2 và log giao dịch chi tiết.                   | Thành công <1s     | Theo chuẩn RESTful               |
|---------------------------|--------|---------------------|------------------------------------------------------------------------------------------------------------------------------|--------------------|----------------------------------|
| /security/firewall/config | POST   | Kiểm tra trạng thái | API /security/firewall/config sử dụng phương thức POST để Kiểm tra trạng thái, có xác thực OAuth2 và log giao dịch chi tiết. | Retry tối đa 3 lần | Giới hạn rate-limit 1000 req/min |
| /invoice/export           | GET    | Thêm bản ghi        | API /invoice/export sử dụng phương thức GET để Thêm bản ghi, có xác thực OAuth2 và log giao dịch chi tiết.                   | Log đầy đủ         | Hỗ trợ JSON và XML               |
| /invoice/export           | PATCH  | Kiểm tra trạng thái | API /invoice/export sử dụng phương thức PATCH để Kiểm tra trạng thái, có xác thực OAuth2 và log giao dịch chi tiết.          | Log đầy đủ         | Hỗ trợ JSON và XML               |
| /crm/lead/import          | PUT    | Cập nhật cấu hình   | API /crm/lead/import sử dụng phương thức PUT để Cập nhật cấu hình, có xác thực OAuth2 và log giao dịch chi tiết.             | Thành công <1s     | Hỗ trợ JSON và XML               |
| /ivr/callflow             | PUT    | Thêm bản            | API /ivr/callflow sử dụng phương thức PUT                                                                                    | Log đầy            | Tích hợp với API                 |

<!-- image -->

| VIETTEL AI RACE   | TD448   |
|-------------------|---------|

|                      |        | ghi                 | để Thêm bản ghi, có xác thực OAuth2 và log giao dịch chi tiết.                                                         | đủ               | Gateway             |
|----------------------|--------|---------------------|------------------------------------------------------------------------------------------------------------------------|------------------|---------------------|
| /rpa/task/execute    | POST   | Thêm bản ghi        | API /rpa/task/execute sử dụng phương thức POST để Thêm bản ghi, có xác thực OAuth2 và log giao dịch chi tiết.          | Log đầy đủ       | Hỗ trợ JSON và XML  |
| /rpa/task/execute    | DELETE | Kiểm tra trạng thái | API /rpa/task/execute sử dụng phương thức DELETE để Kiểm tra trạng thái, có xác thực OAuth2 và log giao dịch chi tiết. | Rollback khi lỗi | Hỗ trợ JSON và XML  |
| /crm/lead/import     | PATCH  | Kiểm tra trạng thái | API /crm/lead/import sử dụng phương thức PATCH để Kiểm tra trạng thái, có xác thực OAuth2 và log giao dịch chi tiết.   | Thành công <1s   | Có versioning v1/v2 |
| /crm/lead/import     | DELETE | Cập nhật cấu hình   | API /crm/lead/import sử dụng phương thức DELETE để Cập nhật cấu hình, có xác thực OAuth2 và log giao dịch chi tiết.    | Rollback khi lỗi | Theo chuẩn RESTful  |
| /network/qos/monitor | DELETE | Thêm bản ghi        | API /network/qos/monitor sử dụng phương thức DELETE để Thêm bản                                                        | Thành công <1s   | Theo chuẩn RESTful  |

<!-- image -->

| VIETTEL AI RACE   | TD448   |
|-------------------|---------|

|                           |        |                     | ghi, có xác thực OAuth2 và log giao dịch chi tiết.                                                                           |                    |                                  |
|---------------------------|--------|---------------------|------------------------------------------------------------------------------------------------------------------------------|--------------------|----------------------------------|
| /crm/lead/import          | DELETE | Thêm bản ghi        | API /crm/lead/import sử dụng phương thức DELETE để Thêm bản ghi, có xác thực OAuth2 và log giao dịch chi tiết.               | Rollback khi lỗi   | Tích hợp với API Gateway         |
| /rpa/task/execute         | PATCH  | Cập nhật cấu hình   | API /rpa/task/execute sử dụng phương thức PATCH để Cập nhật cấu hình, có xác thực OAuth2 và log giao dịch chi tiết.          | Retry tối đa 3 lần | Có versioning v1/v2              |
| /invoice/export           | GET    | Export dữ liệu      | API /invoice/export sử dụng phương thức GET để Export dữ liệu, có xác thực OAuth2 và log giao dịch chi tiết.                 | Retry tối đa 3 lần | Giới hạn rate-limit 1000 req/min |
| /security/firewall/config | POST   | Kiểm tra trạng thái | API /security/firewall/config sử dụng phương thức POST để Kiểm tra trạng thái, có xác thực OAuth2 và log giao dịch chi tiết. | Retry tối đa 3 lần | Theo chuẩn RESTful               |
| /rpa/task/execute         | POST   | Kiểm tra trạng      | API /rpa/task/execute sử dụng phương thức POST để Kiểm tra trạng thái, có xác thực                                           | Log đầy đủ         | Có versioning v1/v2              |

<!-- image -->

| VIETTEL AI RACE   | TD448   |
|-------------------|---------|

|                           |        | thái                | OAuth2 và log giao dịch chi tiết.                                                                                           |                             |                                  |
|---------------------------|--------|---------------------|-----------------------------------------------------------------------------------------------------------------------------|-----------------------------|----------------------------------|
| /security/firewall/config | GET    | Kiểm tra trạng thái | API /security/firewall/config sử dụng phương thức GET để Kiểm tra trạng thái, có xác thực OAuth2 và log giao dịch chi tiết. | Retry tối đa 3 lần          | Giới hạn rate-limit 1000 req/min |
| /rpa/task/execute         | GET    | Thêm bản ghi        | API /rpa/task/execute sử dụng phương thức GET để Thêm bản ghi, có xác thực OAuth2 và log giao dịch chi tiết.                | Log đầy đủ                  | Tích hợp với API Gateway         |
| /crm/lead/import          | POST   | Cập nhật cấu hình   | API /crm/lead/import sử dụng phương thức POST để Cập nhật cấu hình, có xác thực OAuth2 và log giao dịch chi tiết.           | Rollback khi lỗi            | Theo chuẩn RESTful               |
| /ivr/callflow             | GET    | Export dữ liệu      | API /ivr/callflow sử dụng phương thức GET để Export dữ liệu, có xác thực OAuth2 và log giao dịch chi tiết.                  | Thông báo sự kiện qua Kafka | Giới hạn rate-limit 1000 req/min |
| /ivr/callflow             | DELETE | Thêm bản ghi        | API /ivr/callflow sử dụng phương thức DELETE để Thêm bản ghi, có xác thực OAuth2 và log giao                                | Thông báo sự kiện qua Kafka | Hỗ trợ JSON và XML               |

<!-- image -->

| VIETTEL AI RACE   | TD448   |
|-------------------|---------|

|                           |        |                     | dịch chi tiết.                                                                                                        |                    |                                  |
|---------------------------|--------|---------------------|-----------------------------------------------------------------------------------------------------------------------|--------------------|----------------------------------|
| /invoice/export           | PUT    | Export dữ liệu      | API /invoice/export sử dụng phương thức PUT để Export dữ liệu, có xác thực OAuth2 và log giao dịch chi tiết.          | Log đầy đủ         | Hỗ trợ JSON và XML               |
| /ivr/callflow             | PATCH  | Export dữ liệu      | API /ivr/callflow sử dụng phương thức PATCH để Export dữ liệu, có xác thực OAuth2 và log giao dịch chi tiết.          | Retry tối đa 3 lần | Có versioning v1/v2              |
| /invoice/export           | PUT    | Export dữ liệu      | API /invoice/export sử dụng phương thức PUT để Export dữ liệu, có xác thực OAuth2 và log giao dịch chi tiết.          | Log đầy đủ         | Giới hạn rate-limit 1000 req/min |
| /customer/update          | DELETE | Kiểm tra trạng thái | API /customer/update sử dụng phương thức DELETE để Kiểm tra trạng thái, có xác thực OAuth2 và log giao dịch chi tiết. | Rollback khi lỗi   | Có versioning v1/v2              |
| /rpa/task/execute         | DELETE | Cập nhật cấu hình   | API /rpa/task/execute sử dụng phương thức DELETE để Cập nhật cấu hình, có xác thực OAuth2 và log giao dịch chi tiết.  | Thành công <1s     | Theo chuẩn RESTful               |
| /security/firewall/config | PUT    | Export              | API                                                                                                                   | Rollback           | Tích hợp                         |

<!-- image -->

| VIETTEL AI RACE   | TD448   |
|-------------------|---------|

|                           |        | dữ liệu        | /security/firewall/config sử dụng phương thức PUT để Export dữ liệu, có xác thực OAuth2 và log giao dịch chi tiết.   | khi lỗi                     | với API Gateway                  |
|---------------------------|--------|----------------|----------------------------------------------------------------------------------------------------------------------|-----------------------------|----------------------------------|
| /rpa/task/execute         | PUT    | Export dữ liệu | API /rpa/task/execute sử dụng phương thức PUT để Export dữ liệu, có xác thực OAuth2 và log giao dịch chi tiết.       | Thông báo sự kiện qua Kafka | Theo chuẩn RESTful               |
| /security/firewall/config | PUT    | Thêm bản ghi   | API /security/firewall/config sử dụng phương thức PUT để Thêm bản ghi, có xác thực OAuth2 và log giao dịch chi tiết. | Thông báo sự kiện qua Kafka | Theo chuẩn RESTful               |
| /network/qos/monitor      | DELETE | Export dữ liệu | API /network/qos/monitor sử dụng phương thức DELETE để Export dữ liệu, có xác thực OAuth2 và log giao dịch chi tiết. | Log đầy đủ                  | Giới hạn rate-limit 1000 req/min |
| /rpa/task/execute         | PATCH  | Thêm bản ghi   | API /rpa/task/execute sử dụng phương thức PATCH để Thêm bản ghi, có xác thực OAuth2 và log giao dịch chi tiết.       | Rollback khi lỗi            | Giới hạn rate-limit 1000 req/min |
| /invoice/export           | GET    | Xóa thông      | API /invoice/export sử dụng phương thức GET                                                                          | Rollback                    | Giới hạn rate-limit              |

<!-- image -->

| VIETTEL AI RACE   | TD448   |
|-------------------|---------|

|                   |        | tin                 | để Xóa thông tin, có xác thực OAuth2 và log giao dịch chi tiết.                                                     | khi lỗi                     | 1000 req/min                     |
|-------------------|--------|---------------------|---------------------------------------------------------------------------------------------------------------------|-----------------------------|----------------------------------|
| /rpa/task/execute | PATCH  | Cập nhật cấu hình   | API /rpa/task/execute sử dụng phương thức PATCH để Cập nhật cấu hình, có xác thực OAuth2 và log giao dịch chi tiết. | Thành công <1s              | Giới hạn rate-limit 1000 req/min |
| /ivr/callflow     | DELETE | Kiểm tra trạng thái | API /ivr/callflow sử dụng phương thức DELETE để Kiểm tra trạng thái, có xác thực OAuth2 và log giao dịch chi tiết.  | Thông báo sự kiện qua Kafka | Giới hạn rate-limit 1000 req/min |
| /invoice/export   | DELETE | Thêm bản ghi        | API /invoice/export sử dụng phương thức DELETE để Thêm bản ghi, có xác thực OAuth2 và log giao dịch chi tiết.       | Thông báo sự kiện qua Kafka | Hỗ trợ JSON và XML               |
| /rpa/task/execute | GET    | Cập nhật cấu hình   | API /rpa/task/execute sử dụng phương thức GET để Cập nhật cấu hình, có xác thực OAuth2 và log giao dịch chi tiết.   | Thành công <1s              | Theo chuẩn RESTful               |
| /ivr/callflow     | DELETE | Cập nhật cấu        | API /ivr/callflow sử dụng phương thức DELETE để Cập nhật cấu hình, có xác thực                                      | Thành công <1s              | Theo chuẩn RESTful               |

<!-- image -->

| VIETTEL AI RACE   | TD448   |
|-------------------|---------|

|                      |       | hình                | OAuth2 và log giao dịch chi tiết.                                                                                        |                  |                                  |
|----------------------|-------|---------------------|--------------------------------------------------------------------------------------------------------------------------|------------------|----------------------------------|
| /crm/lead/import     | PUT   | Xóa thông tin       | API /crm/lead/import sử dụng phương thức PUT để Xóa thông tin, có xác thực OAuth2 và log giao dịch chi tiết.             | Thành công <1s   | Có versioning v1/v2              |
| /crm/lead/import     | POST  | Thêm bản ghi        | API /crm/lead/import sử dụng phương thức POST để Thêm bản ghi, có xác thực OAuth2 và log giao dịch chi tiết.             | Thành công <1s   | Giới hạn rate-limit 1000 req/min |
| /network/qos/monitor | PATCH | Kiểm tra trạng thái | API /network/qos/monitor sử dụng phương thức PATCH để Kiểm tra trạng thái, có xác thực OAuth2 và log giao dịch chi tiết. | Rollback khi lỗi | Hỗ trợ JSON và XML               |
| /customer/update     | PATCH | Xóa thông tin       | API /customer/update sử dụng phương thức PATCH để Xóa thông tin, có xác thực OAuth2 và log giao dịch chi tiết.           | Rollback khi lỗi | Hỗ trợ JSON và XML               |
| /crm/lead/import     | POST  | Export dữ liệu      | API /crm/lead/import sử dụng phương thức POST để Export dữ liệu, có xác thực OAuth2 và log giao                          | Log đầy đủ       | Giới hạn rate-limit 1000 req/min |

<!-- image -->

| VIETTEL AI RACE   | TD448   |
|-------------------|---------|

|                           |      |                     | dịch chi tiết.                                                                                                               |                             |                                  |
|---------------------------|------|---------------------|------------------------------------------------------------------------------------------------------------------------------|-----------------------------|----------------------------------|
| /security/firewall/config | PUT  | Thêm bản ghi        | API /security/firewall/config sử dụng phương thức PUT để Thêm bản ghi, có xác thực OAuth2 và log giao dịch chi tiết.         | Thông báo sự kiện qua Kafka | Tích hợp với API Gateway         |
| /invoice/export           | GET  | Export dữ liệu      | API /invoice/export sử dụng phương thức GET để Export dữ liệu, có xác thực OAuth2 và log giao dịch chi tiết.                 | Retry tối đa 3 lần          | Tích hợp với API Gateway         |
| /security/firewall/config | POST | Kiểm tra trạng thái | API /security/firewall/config sử dụng phương thức POST để Kiểm tra trạng thái, có xác thực OAuth2 và log giao dịch chi tiết. | Rollback khi lỗi            | Hỗ trợ JSON và XML               |
| /customer/update          | GET  | Cập nhật cấu hình   | API /customer/update sử dụng phương thức GET để Cập nhật cấu hình, có xác thực OAuth2 và log giao dịch chi tiết.             | Thành công <1s              | Tích hợp với API Gateway         |
| /customer/update          | POST | Xóa thông tin       | API /customer/update sử dụng phương thức POST để Xóa thông tin, có xác thực OAuth2 và log giao dịch chi tiết.                | Retry tối đa 3 lần          | Giới hạn rate-limit 1000 req/min |

<!-- image -->

| VIETTEL AI RACE   | TD448   |
|-------------------|---------|

| /network/qos/monitor      | PUT    | Thêm bản ghi   | API /network/qos/monitor sử dụng phương thức PUT để Thêm bản ghi, có xác thực OAuth2 và log giao dịch chi tiết.        | Retry tối đa 3 lần          | Có versioning v1/v2              |
|---------------------------|--------|----------------|------------------------------------------------------------------------------------------------------------------------|-----------------------------|----------------------------------|
| /ivr/callflow             | DELETE | Export dữ liệu | API /ivr/callflow sử dụng phương thức DELETE để Export dữ liệu, có xác thực OAuth2 và log giao dịch chi tiết.          | Log đầy đủ                  | Giới hạn rate-limit 1000 req/min |
| /invoice/export           | GET    | Xóa thông tin  | API /invoice/export sử dụng phương thức GET để Xóa thông tin, có xác thực OAuth2 và log giao dịch chi tiết.            | Thành công <1s              | Có versioning v1/v2              |
| /security/firewall/config | GET    | Export dữ liệu | API /security/firewall/config sử dụng phương thức GET để Export dữ liệu, có xác thực OAuth2 và log giao dịch chi tiết. | Thông báo sự kiện qua Kafka | Tích hợp với API Gateway         |
| /ivr/callflow             | POST   | Xóa thông tin  | API /ivr/callflow sử dụng phương thức POST để Xóa thông tin, có xác thực OAuth2 và log giao dịch chi tiết.             | Log đầy đủ                  | Hỗ trợ JSON và XML               |
| /customer/update          | DELETE | Xóa thông      | API /customer/update sử dụng phương thức DELETE để Xóa thông                                                           | Rollback khi lỗi            | Giới hạn rate-limit 1000         |

<!-- image -->

| VIETTEL AI RACE   | TD448   |
|-------------------|---------|

|                           |      | tin                 | tin, có xác thực OAuth2 và log giao dịch chi tiết.                                                                    |                  | req/min                  |
|---------------------------|------|---------------------|-----------------------------------------------------------------------------------------------------------------------|------------------|--------------------------|
| /security/firewall/config | POST | Thêm bản ghi        | API /security/firewall/config sử dụng phương thức POST để Thêm bản ghi, có xác thực OAuth2 và log giao dịch chi tiết. | Log đầy đủ       | Tích hợp với API Gateway |
| /invoice/export           | GET  | Thêm bản ghi        | API /invoice/export sử dụng phương thức GET để Thêm bản ghi, có xác thực OAuth2 và log giao dịch chi tiết.            | Thành công <1s   | Theo chuẩn RESTful       |
| /customer/update          | PUT  | Kiểm tra trạng thái | API /customer/update sử dụng phương thức PUT để Kiểm tra trạng thái, có xác thực OAuth2 và log giao dịch chi tiết.    | Rollback khi lỗi | Tích hợp với API Gateway |
| /customer/update          | POST | Kiểm tra trạng thái | API /customer/update sử dụng phương thức POST để Kiểm tra trạng thái, có xác thực OAuth2 và log giao dịch chi tiết.   | Log đầy đủ       | Theo chuẩn RESTful       |
| /ivr/callflow             | POST | Export dữ liệu      | API /ivr/callflow sử dụng phương thức POST để Export dữ liệu, có xác thực OAuth2 và log giao                          | Thành công <1s   | Có versioning v1/v2      |

<!-- image -->

| VIETTEL AI RACE   | TD448   |
|-------------------|---------|

|                           |        |                     | dịch chi tiết.                                                                                                          |                             |                                  |
|---------------------------|--------|---------------------|-------------------------------------------------------------------------------------------------------------------------|-----------------------------|----------------------------------|
| /invoice/export           | DELETE | Export dữ liệu      | API /invoice/export sử dụng phương thức DELETE để Export dữ liệu, có xác thực OAuth2 và log giao dịch chi tiết.         | Rollback khi lỗi            | Có versioning v1/v2              |
| /security/firewall/config | GET    | Export dữ liệu      | API /security/firewall/config sử dụng phương thức GET để Export dữ liệu, có xác thực OAuth2 và log giao dịch chi tiết.  | Retry tối đa 3 lần          | Hỗ trợ JSON và XML               |
| /crm/lead/import          | PATCH  | Xóa thông tin       | API /crm/lead/import sử dụng phương thức PATCH để Xóa thông tin, có xác thực OAuth2 và log giao dịch chi tiết.          | Thành công <1s              | Theo chuẩn RESTful               |
| /network/qos/monitor      | POST   | Kiểm tra trạng thái | API /network/qos/monitor sử dụng phương thức POST để Kiểm tra trạng thái, có xác thực OAuth2 và log giao dịch chi tiết. | Thông báo sự kiện qua Kafka | Giới hạn rate-limit 1000 req/min |
| /crm/lead/import          | DELETE | Thêm bản ghi        | API /crm/lead/import sử dụng phương thức DELETE để Thêm bản ghi, có xác thực OAuth2 và log giao                         | Log đầy đủ                  | Giới hạn rate-limit 1000 req/min |

<!-- image -->

| VIETTEL AI RACE   | TD448   |
|-------------------|---------|

|                      |      |                     | dịch chi tiết.                                                                                                       |                  |                                  |
|----------------------|------|---------------------|----------------------------------------------------------------------------------------------------------------------|------------------|----------------------------------|
| /crm/lead/import     | PUT  | Export dữ liệu      | API /crm/lead/import sử dụng phương thức PUT để Export dữ liệu, có xác thực OAuth2 và log giao dịch chi tiết.        | Rollback khi lỗi | Có versioning v1/v2              |
| /crm/lead/import     | POST | Kiểm tra trạng thái | API /crm/lead/import sử dụng phương thức POST để Kiểm tra trạng thái, có xác thực OAuth2 và log giao dịch chi tiết.  | Rollback khi lỗi | Theo chuẩn RESTful               |
| /customer/update     | GET  | Kiểm tra trạng thái | API /customer/update sử dụng phương thức GET để Kiểm tra trạng thái, có xác thực OAuth2 và log giao dịch chi tiết.   | Thành công <1s   | Giới hạn rate-limit 1000 req/min |
| /network/qos/monitor | PUT  | Cập nhật cấu hình   | API /network/qos/monitor sử dụng phương thức PUT để Cập nhật cấu hình, có xác thực OAuth2 và log giao dịch chi tiết. | Rollback khi lỗi | Theo chuẩn RESTful               |
| /network/qos/monitor | PUT  | Kiểm tra trạng thái | API /network/qos/monitor sử dụng phương thức PUT để Kiểm tra trạng thái, có xác thực OAuth2 và log giao              | Thành công <1s   | Theo chuẩn RESTful               |

<!-- image -->

| VIETTEL AI RACE   | TD448   |
|-------------------|---------|

|                           |        |                     | dịch chi tiết.                                                                                                                 |                    |                                  |
|---------------------------|--------|---------------------|--------------------------------------------------------------------------------------------------------------------------------|--------------------|----------------------------------|
| /security/firewall/config | GET    | Kiểm tra trạng thái | API /security/firewall/config sử dụng phương thức GET để Kiểm tra trạng thái, có xác thực OAuth2 và log giao dịch chi tiết.    | Rollback khi lỗi   | Hỗ trợ JSON và XML               |
| /security/firewall/config | GET    | Cập nhật cấu hình   | API /security/firewall/config sử dụng phương thức GET để Cập nhật cấu hình, có xác thực OAuth2 và log giao dịch chi tiết.      | Log đầy đủ         | Giới hạn rate-limit 1000 req/min |
| /invoice/export           | POST   | Thêm bản ghi        | API /invoice/export sử dụng phương thức POST để Thêm bản ghi, có xác thực OAuth2 và log giao dịch chi tiết.                    | Thành công <1s     | Hỗ trợ JSON và XML               |
| /security/firewall/config | DELETE | Kiểm tra trạng thái | API /security/firewall/config sử dụng phương thức DELETE để Kiểm tra trạng thái, có xác thực OAuth2 và log giao dịch chi tiết. | Retry tối đa 3 lần | Tích hợp với API Gateway         |
| /network/qos/monitor      | GET    | Cập nhật cấu        | API /network/qos/monitor sử dụng phương thức                                                                                   | Retry tối đa 3 lần | Tích hợp với API                 |

<!-- image -->

| VIETTEL AI RACE   | TD448   |
|-------------------|---------|

|                   |       | hình                | GET để Cập nhật cấu hình, có xác thực OAuth2 và log giao dịch chi tiết.                                          |                             | Gateway                          |
|-------------------|-------|---------------------|------------------------------------------------------------------------------------------------------------------|-----------------------------|----------------------------------|
| /rpa/task/execute | PATCH | Export dữ liệu      | API /rpa/task/execute sử dụng phương thức PATCH để Export dữ liệu, có xác thực OAuth2 và log giao dịch chi tiết. | Retry tối đa 3 lần          | Có versioning v1/v2              |
| /customer/update  | PUT   | Xóa thông tin       | API /customer/update sử dụng phương thức PUT để Xóa thông tin, có xác thực OAuth2 và log giao dịch chi tiết.     | Rollback khi lỗi            | Hỗ trợ JSON và XML               |
| /customer/update  | PUT   | Thêm bản ghi        | API /customer/update sử dụng phương thức PUT để Thêm bản ghi, có xác thực OAuth2 và log giao dịch chi tiết.      | Thành công <1s              | Có versioning v1/v2              |
| /ivr/callflow     | GET   | Kiểm tra trạng thái | API /ivr/callflow sử dụng phương thức GET để Kiểm tra trạng thái, có xác thực OAuth2 và log giao dịch chi tiết.  | Rollback khi lỗi            | Giới hạn rate-limit 1000 req/min |
| /invoice/export   | PUT   | Export dữ liệu      | API /invoice/export sử dụng phương thức PUT để Export dữ liệu, có xác thực OAuth2 và log giao dịch chi tiết.     | Thông báo sự kiện qua Kafka | Hỗ trợ JSON và XML               |

<!-- image -->

| VIETTEL AI RACE   | TD448   |
|-------------------|---------|

| /security/firewall/config   | DELETE   | Xóa thông tin     | API /security/firewall/config sử dụng phương thức DELETE để Xóa thông tin, có xác thực OAuth2 và log giao dịch chi tiết.   | Rollback khi lỗi   | Tích hợp với API Gateway   |
|-----------------------------|----------|-------------------|----------------------------------------------------------------------------------------------------------------------------|--------------------|----------------------------|
| /network/qos/monitor        | DELETE   | Export dữ liệu    | API /network/qos/monitor sử dụng phương thức DELETE để Export dữ liệu, có xác thực OAuth2 và log giao dịch chi tiết.       | Thành công <1s     | Theo chuẩn RESTful         |
| /crm/lead/import            | PATCH    | Xóa thông tin     | API /crm/lead/import sử dụng phương thức PATCH để Xóa thông tin, có xác thực OAuth2 và log giao dịch chi tiết.             | Thành công <1s     | Tích hợp với API Gateway   |
| /invoice/export             | POST     | Thêm bản ghi      | API /invoice/export sử dụng phương thức POST để Thêm bản ghi, có xác thực OAuth2 và log giao dịch chi tiết.                | Thành công <1s     | Theo chuẩn RESTful         |
| /rpa/task/execute           | POST     | Cập nhật cấu hình | API /rpa/task/execute sử dụng phương thức POST để Cập nhật cấu hình, có xác thực OAuth2 và log giao dịch chi tiết.         | Retry tối đa 3 lần | Tích hợp với API Gateway   |

<!-- image -->

| VIETTEL AI RACE   | TD448   |
|-------------------|---------|

| /crm/lead/import     | GET   | Kiểm tra trạng thái   | API /crm/lead/import sử dụng phương thức GET để Kiểm tra trạng thái, có xác thực OAuth2 và log giao dịch chi tiết.     | Retry tối đa 3 lần          | Theo chuẩn RESTful               |
|----------------------|-------|-----------------------|------------------------------------------------------------------------------------------------------------------------|-----------------------------|----------------------------------|
| /network/qos/monitor | PUT   | Kiểm tra trạng thái   | API /network/qos/monitor sử dụng phương thức PUT để Kiểm tra trạng thái, có xác thực OAuth2 và log giao dịch chi tiết. | Thành công <1s              | Tích hợp với API Gateway         |
| /customer/update     | POST  | Cập nhật cấu hình     | API /customer/update sử dụng phương thức POST để Cập nhật cấu hình, có xác thực OAuth2 và log giao dịch chi tiết.      | Thành công <1s              | Hỗ trợ JSON và XML               |
| /crm/lead/import     | PUT   | Thêm bản ghi          | API /crm/lead/import sử dụng phương thức PUT để Thêm bản ghi, có xác thực OAuth2 và log giao dịch chi tiết.            | Retry tối đa 3 lần          | Có versioning v1/v2              |
| /ivr/callflow        | POST  | Kiểm tra trạng thái   | API /ivr/callflow sử dụng phương thức POST để Kiểm tra trạng thái, có xác thực OAuth2 và log giao dịch chi tiết.       | Thông báo sự kiện qua Kafka | Giới hạn rate-limit 1000 req/min |

<!-- image -->

| VIETTEL AI RACE   | TD448   |
|-------------------|---------|

| /customer/update   | PATCH   | Cập nhật cấu hình   | API /customer/update sử dụng phương thức PATCH để Cập nhật cấu hình, có xác thực OAuth2 và log giao dịch chi tiết.   | Log đầy đủ                  | Tích hợp với API Gateway   |
|--------------------|---------|---------------------|----------------------------------------------------------------------------------------------------------------------|-----------------------------|----------------------------|
| /invoice/export    | POST    | Kiểm tra trạng thái | API /invoice/export sử dụng phương thức POST để Kiểm tra trạng thái, có xác thực OAuth2 và log giao dịch chi tiết.   | Thành công <1s              | Hỗ trợ JSON và XML         |
| /crm/lead/import   | PATCH   | Cập nhật cấu hình   | API /crm/lead/import sử dụng phương thức PATCH để Cập nhật cấu hình, có xác thực OAuth2 và log giao dịch chi tiết.   | Rollback khi lỗi            | Có versioning v1/v2        |
| /customer/update   | GET     | Kiểm tra trạng thái | API /customer/update sử dụng phương thức GET để Kiểm tra trạng thái, có xác thực OAuth2 và log giao dịch chi tiết.   | Thông báo sự kiện qua Kafka | Theo chuẩn RESTful         |
| /crm/lead/import   | PATCH   | Cập nhật cấu hình   | API /crm/lead/import sử dụng phương thức PATCH để Cập nhật cấu hình, có xác thực OAuth2 và log giao dịch chi tiết.   | Thành công <1s              | Tích hợp với API Gateway   |

<!-- image -->

| VIETTEL AI RACE   | TD448   |
|-------------------|---------|

| /crm/lead/import          | GET   | Thêm bản ghi        | API /crm/lead/import sử dụng phương thức GET để Thêm bản ghi, có xác thực OAuth2 và log giao dịch chi tiết.                 | Thành công <1s              | Tích hợp với API Gateway   |
|---------------------------|-------|---------------------|-----------------------------------------------------------------------------------------------------------------------------|-----------------------------|----------------------------|
| /security/firewall/config | GET   | Kiểm tra trạng thái | API /security/firewall/config sử dụng phương thức GET để Kiểm tra trạng thái, có xác thực OAuth2 và log giao dịch chi tiết. | Thông báo sự kiện qua Kafka | Có versioning v1/v2        |
| /crm/lead/import          | PATCH | Export dữ liệu      | API /crm/lead/import sử dụng phương thức PATCH để Export dữ liệu, có xác thực OAuth2 và log giao dịch chi tiết.             | Log đầy đủ                  | Theo chuẩn RESTful         |
| /network/qos/monitor      | GET   | Kiểm tra trạng thái | API /network/qos/monitor sử dụng phương thức GET để Kiểm tra trạng thái, có xác thực OAuth2 và log giao dịch chi tiết.      | Log đầy đủ                  | Tích hợp với API Gateway   |
| /security/firewall/config | POST  | Kiểm tra trạng thái | API /security/firewall/config sử dụng phương thức POST để Kiểm tra trạng thái, có xác thực OAuth2 và log giao               | Retry tối đa 3 lần          | Hỗ trợ JSON và XML         |

<!-- image -->

| VIETTEL AI RACE   | TD448   |
|-------------------|---------|

|                      |        |                     | dịch chi tiết.                                                                                                       |                             |                                  |
|----------------------|--------|---------------------|----------------------------------------------------------------------------------------------------------------------|-----------------------------|----------------------------------|
| /customer/update     | POST   | Export dữ liệu      | API /customer/update sử dụng phương thức POST để Export dữ liệu, có xác thực OAuth2 và log giao dịch chi tiết.       | Retry tối đa 3 lần          | Tích hợp với API Gateway         |
| /ivr/callflow        | DELETE | Kiểm tra trạng thái | API /ivr/callflow sử dụng phương thức DELETE để Kiểm tra trạng thái, có xác thực OAuth2 và log giao dịch chi tiết.   | Log đầy đủ                  | Có versioning v1/v2              |
| /network/qos/monitor | GET    | Cập nhật cấu hình   | API /network/qos/monitor sử dụng phương thức GET để Cập nhật cấu hình, có xác thực OAuth2 và log giao dịch chi tiết. | Rollback khi lỗi            | Giới hạn rate-limit 1000 req/min |
| /network/qos/monitor | PUT    | Export dữ liệu      | API /network/qos/monitor sử dụng phương thức PUT để Export dữ liệu, có xác thực OAuth2 và log giao dịch chi tiết.    | Thông báo sự kiện qua Kafka | Hỗ trợ JSON và XML               |
| /ivr/callflow        | PATCH  | Kiểm tra trạng thái | API /ivr/callflow sử dụng phương thức PATCH để Kiểm tra trạng thái, có xác thực OAuth2 và log giao                   | Rollback khi lỗi            | Theo chuẩn RESTful               |

<!-- image -->

| VIETTEL AI RACE   | TD448   |
|-------------------|---------|

|                      |       |                   | dịch chi tiết.                                                                                                      |                    |                                  |
|----------------------|-------|-------------------|---------------------------------------------------------------------------------------------------------------------|--------------------|----------------------------------|
| /crm/lead/import     | PUT   | Cập nhật cấu hình | API /crm/lead/import sử dụng phương thức PUT để Cập nhật cấu hình, có xác thực OAuth2 và log giao dịch chi tiết.    | Rollback khi lỗi   | Hỗ trợ JSON và XML               |
| /crm/lead/import     | POST  | Xóa thông tin     | API /crm/lead/import sử dụng phương thức POST để Xóa thông tin, có xác thực OAuth2 và log giao dịch chi tiết.       | Log đầy đủ         | Tích hợp với API Gateway         |
| /network/qos/monitor | PATCH | Export dữ liệu    | API /network/qos/monitor sử dụng phương thức PATCH để Export dữ liệu, có xác thực OAuth2 và log giao dịch chi tiết. | Retry tối đa 3 lần | Giới hạn rate-limit 1000 req/min |
| /ivr/callflow        | PUT   | Cập nhật cấu hình | API /ivr/callflow sử dụng phương thức PUT để Cập nhật cấu hình, có xác thực OAuth2 và log giao dịch chi tiết.       | Thành công <1s     | Giới hạn rate-limit 1000 req/min |
| /ivr/callflow        | GET   | Cập nhật cấu hình | API /ivr/callflow sử dụng phương thức GET để Cập nhật cấu hình, có xác thực OAuth2 và log giao dịch chi tiết.       | Log đầy đủ         | Hỗ trợ JSON và XML               |
| /crm/lead/import     | PATCH | Thêm              | API /crm/lead/import                                                                                                | Thông              | Theo                             |

<!-- image -->

| VIETTEL AI RACE   | TD448   |
|-------------------|---------|

|                      |        | bản ghi           | sử dụng phương thức PATCH để Thêm bản ghi, có xác thực OAuth2 và log giao dịch chi tiết.                             | báo sự kiện qua Kafka   | chuẩn RESTful                    |
|----------------------|--------|-------------------|----------------------------------------------------------------------------------------------------------------------|-------------------------|----------------------------------|
| /rpa/task/execute    | PATCH  | Thêm bản ghi      | API /rpa/task/execute sử dụng phương thức PATCH để Thêm bản ghi, có xác thực OAuth2 và log giao dịch chi tiết.       | Log đầy đủ              | Theo chuẩn RESTful               |
| /ivr/callflow        | PATCH  | Export dữ liệu    | API /ivr/callflow sử dụng phương thức PATCH để Export dữ liệu, có xác thực OAuth2 và log giao dịch chi tiết.         | Retry tối đa 3 lần      | Giới hạn rate-limit 1000 req/min |
| /invoice/export      | PUT    | Cập nhật cấu hình | API /invoice/export sử dụng phương thức PUT để Cập nhật cấu hình, có xác thực OAuth2 và log giao dịch chi tiết.      | Retry tối đa 3 lần      | Giới hạn rate-limit 1000 req/min |
| /network/qos/monitor | DELETE | Export dữ liệu    | API /network/qos/monitor sử dụng phương thức DELETE để Export dữ liệu, có xác thực OAuth2 và log giao dịch chi tiết. | Retry tối đa 3 lần      | Giới hạn rate-limit 1000 req/min |
| /crm/lead/import     | PUT    | Cập nhật          | API /crm/lead/import sử dụng phương thức                                                                             | Rollback                | Theo chuẩn                       |

<!-- image -->

| VIETTEL AI RACE   | TD448   |
|-------------------|---------|

|                      |        | cấu hình            | PUT để Cập nhật cấu hình, có xác thực OAuth2 và log giao dịch chi tiết.                                                 | khi lỗi                     | RESTful                          |
|----------------------|--------|---------------------|-------------------------------------------------------------------------------------------------------------------------|-----------------------------|----------------------------------|
| /rpa/task/execute    | POST   | Cập nhật cấu hình   | API /rpa/task/execute sử dụng phương thức POST để Cập nhật cấu hình, có xác thực OAuth2 và log giao dịch chi tiết.      | Thông báo sự kiện qua Kafka | Theo chuẩn RESTful               |
| /rpa/task/execute    | DELETE | Kiểm tra trạng thái | API /rpa/task/execute sử dụng phương thức DELETE để Kiểm tra trạng thái, có xác thực OAuth2 và log giao dịch chi tiết.  | Thành công <1s              | Hỗ trợ JSON và XML               |
| /network/qos/monitor | POST   | Kiểm tra trạng thái | API /network/qos/monitor sử dụng phương thức POST để Kiểm tra trạng thái, có xác thực OAuth2 và log giao dịch chi tiết. | Log đầy đủ                  | Có versioning v1/v2              |
| /customer/update     | GET    | Xóa thông tin       | API /customer/update sử dụng phương thức GET để Xóa thông tin, có xác thực OAuth2 và log giao dịch chi tiết.            | Thành công <1s              | Giới hạn rate-limit 1000 req/min |
| /rpa/task/execute    | POST   | Kiểm tra trạng      | API /rpa/task/execute sử dụng phương thức POST để Kiểm tra                                                              | Thành công                  | Giới hạn rate-limit 1000         |

<!-- image -->

| VIETTEL AI RACE   | TD448   |
|-------------------|---------|

|                           |        | thái              | trạng thái, có xác thực OAuth2 và log giao dịch chi tiết.                                                                   | <1s                | req/min             |
|---------------------------|--------|-------------------|-----------------------------------------------------------------------------------------------------------------------------|--------------------|---------------------|
| /security/firewall/config | DELETE | Thêm bản ghi      | API /security/firewall/config sử dụng phương thức DELETE để Thêm bản ghi, có xác thực OAuth2 và log giao dịch chi tiết.     | Rollback khi lỗi   | Có versioning v1/v2 |
| /security/firewall/config | DELETE | Xóa thông tin     | API /security/firewall/config sử dụng phương thức DELETE để Xóa thông tin, có xác thực OAuth2 và log giao dịch chi tiết.    | Log đầy đủ         | Theo chuẩn RESTful  |
| /customer/update          | PATCH  | Xóa thông tin     | API /customer/update sử dụng phương thức PATCH để Xóa thông tin, có xác thực OAuth2 và log giao dịch chi tiết.              | Retry tối đa 3 lần | Có versioning v1/v2 |
| /security/firewall/config | PATCH  | Cập nhật cấu hình | API /security/firewall/config sử dụng phương thức PATCH để Cập nhật cấu hình, có xác thực OAuth2 và log giao dịch chi tiết. | Rollback khi lỗi   | Có versioning v1/v2 |
| /network/qos/monitor      | GET    | Cập nhật cấu      | API /network/qos/monitor sử dụng phương thức                                                                                | Rollback khi lỗi   | Tích hợp với API    |

<!-- image -->

| VIETTEL AI RACE   | TD448   |
|-------------------|---------|

|                           |      | hình                | GET để Cập nhật cấu hình, có xác thực OAuth2 và log giao dịch chi tiết.                                                      |                  | Gateway                          |
|---------------------------|------|---------------------|------------------------------------------------------------------------------------------------------------------------------|------------------|----------------------------------|
| /customer/update          | PUT  | Kiểm tra trạng thái | API /customer/update sử dụng phương thức PUT để Kiểm tra trạng thái, có xác thực OAuth2 và log giao dịch chi tiết.           | Log đầy đủ       | Tích hợp với API Gateway         |
| /ivr/callflow             | POST | Cập nhật cấu hình   | API /ivr/callflow sử dụng phương thức POST để Cập nhật cấu hình, có xác thực OAuth2 và log giao dịch chi tiết.               | Rollback khi lỗi | Giới hạn rate-limit 1000 req/min |
| /security/firewall/config | POST | Kiểm tra trạng thái | API /security/firewall/config sử dụng phương thức POST để Kiểm tra trạng thái, có xác thực OAuth2 và log giao dịch chi tiết. | Log đầy đủ       | Theo chuẩn RESTful               |
| /invoice/export           | POST | Export dữ liệu      | API /invoice/export sử dụng phương thức POST để Export dữ liệu, có xác thực OAuth2 và log giao dịch chi tiết.                | Rollback khi lỗi | Giới hạn rate-limit 1000 req/min |
| /security/firewall/config | POST | Xóa thông           | API /security/firewall/config                                                                                                | Retry tối        | Hỗ trợ JSON và                   |

<!-- image -->

| VIETTEL AI RACE   | TD448   |
|-------------------|---------|

|                      |        | tin                 | sử dụng phương thức POST để Xóa thông tin, có xác thực OAuth2 và log giao dịch chi tiết.                            | đa 3 lần                    | XML                      |
|----------------------|--------|---------------------|---------------------------------------------------------------------------------------------------------------------|-----------------------------|--------------------------|
| /crm/lead/import     | POST   | Thêm bản ghi        | API /crm/lead/import sử dụng phương thức POST để Thêm bản ghi, có xác thực OAuth2 và log giao dịch chi tiết.        | Thành công <1s              | Hỗ trợ JSON và XML       |
| /network/qos/monitor | DELETE | Thêm bản ghi        | API /network/qos/monitor sử dụng phương thức DELETE để Thêm bản ghi, có xác thực OAuth2 và log giao dịch chi tiết.  | Thông báo sự kiện qua Kafka | Hỗ trợ JSON và XML       |
| /ivr/callflow        | DELETE | Kiểm tra trạng thái | API /ivr/callflow sử dụng phương thức DELETE để Kiểm tra trạng thái, có xác thực OAuth2 và log giao dịch chi tiết.  | Thành công <1s              | Có versioning v1/v2      |
| /network/qos/monitor | PATCH  | Export dữ liệu      | API /network/qos/monitor sử dụng phương thức PATCH để Export dữ liệu, có xác thực OAuth2 và log giao dịch chi tiết. | Retry tối đa 3 lần          | Tích hợp với API Gateway |

<!-- image -->

| VIETTEL AI RACE   | TD448   |
|-------------------|---------|

| /rpa/task/execute   | PATCH   | Cập nhật cấu hình   | API /rpa/task/execute sử dụng phương thức PATCH để Cập nhật cấu hình, có xác thực OAuth2 và log giao dịch chi tiết.   | Retry tối đa 3 lần   | Tích hợp với API Gateway   |
|---------------------|---------|---------------------|-----------------------------------------------------------------------------------------------------------------------|----------------------|----------------------------|
| /crm/lead/import    | GET     | Thêm bản ghi        | API /crm/lead/import sử dụng phương thức GET để Thêm bản ghi, có xác thực OAuth2 và log giao dịch chi tiết.           | Log đầy đủ           | Theo chuẩn RESTful         |
| /invoice/export     | DELETE  | Xóa thông tin       | API /invoice/export sử dụng phương thức DELETE để Xóa thông tin, có xác thực OAuth2 và log giao dịch chi tiết.        | Rollback khi lỗi     | Theo chuẩn RESTful         |
| /customer/update    | GET     | Kiểm tra trạng thái | API /customer/update sử dụng phương thức GET để Kiểm tra trạng thái, có xác thực OAuth2 và log giao dịch chi tiết.    | Log đầy đủ           | Có versioning v1/v2        |
| /rpa/task/execute   | POST    | Kiểm tra trạng thái | API /rpa/task/execute sử dụng phương thức POST để Kiểm tra trạng thái, có xác thực OAuth2 và log giao dịch chi tiết.  | Log đầy đủ           | Tích hợp với API Gateway   |
| /crm/lead/import    | POST    | Xóa thông           | API /crm/lead/import sử dụng phương thức POST để Xóa thông tin,                                                       | Thành công           | Tích hợp với API           |

<!-- image -->

| VIETTEL AI RACE   | TD448   |
|-------------------|---------|

|                      |       | tin            | có xác thực OAuth2 và log giao dịch chi tiết.                                                                     | <1s                | Gateway                          |
|----------------------|-------|----------------|-------------------------------------------------------------------------------------------------------------------|--------------------|----------------------------------|
| /network/qos/monitor | PATCH | Thêm bản ghi   | API /network/qos/monitor sử dụng phương thức PATCH để Thêm bản ghi, có xác thực OAuth2 và log giao dịch chi tiết. | Retry tối đa 3 lần | Giới hạn rate-limit 1000 req/min |
| /ivr/callflow        | GET   | Xóa thông tin  | API /ivr/callflow sử dụng phương thức GET để Xóa thông tin, có xác thực OAuth2 và log giao dịch chi tiết.         | Retry tối đa 3 lần | Có versioning v1/v2              |
| /customer/update     | PATCH | Export dữ liệu | API /customer/update sử dụng phương thức PATCH để Export dữ liệu, có xác thực OAuth2 và log giao dịch chi tiết.   | Retry tối đa 3 lần | Theo chuẩn RESTful               |
| /invoice/export      | POST  | Export dữ liệu | API /invoice/export sử dụng phương thức POST để Export dữ liệu, có xác thực OAuth2 và log giao dịch chi tiết.     | Thành công <1s     | Có versioning v1/v2              |
| /invoice/export      | PUT   | Xóa thông tin  | API /invoice/export sử dụng phương thức PUT để Xóa thông tin, có xác thực OAuth2 và log                           | Log đầy đủ         | Hỗ trợ JSON và XML               |

<!-- image -->

| VIETTEL AI RACE   | TD448   |
|-------------------|---------|

|                      |        |                     | giao dịch chi tiết.                                                                                                  |                             |                                  |
|----------------------|--------|---------------------|----------------------------------------------------------------------------------------------------------------------|-----------------------------|----------------------------------|
| /network/qos/monitor | PATCH  | Thêm bản ghi        | API /network/qos/monitor sử dụng phương thức PATCH để Thêm bản ghi, có xác thực OAuth2 và log giao dịch chi tiết.    | Log đầy đủ                  | Có versioning v1/v2              |
| /rpa/task/execute    | GET    | Kiểm tra trạng thái | API /rpa/task/execute sử dụng phương thức GET để Kiểm tra trạng thái, có xác thực OAuth2 và log giao dịch chi tiết.  | Log đầy đủ                  | Giới hạn rate-limit 1000 req/min |
| /customer/update     | PATCH  | Xóa thông tin       | API /customer/update sử dụng phương thức PATCH để Xóa thông tin, có xác thực OAuth2 và log giao dịch chi tiết.       | Thành công <1s              | Giới hạn rate-limit 1000 req/min |
| /invoice/export      | DELETE | Kiểm tra trạng thái | API /invoice/export sử dụng phương thức DELETE để Kiểm tra trạng thái, có xác thực OAuth2 và log giao dịch chi tiết. | Retry tối đa 3 lần          | Tích hợp với API Gateway         |
| /rpa/task/execute    | PUT    | Thêm bản ghi        | API /rpa/task/execute sử dụng phương thức PUT để Thêm bản ghi, có xác thực OAuth2 và log giao dịch chi tiết.         | Thông báo sự kiện qua Kafka | Có versioning v1/v2              |

<!-- image -->

| VIETTEL AI RACE   | TD448   |
|-------------------|---------|

| /invoice/export      | PATCH   | Xóa thông tin       | API /invoice/export sử dụng phương thức PATCH để Xóa thông tin, có xác thực OAuth2 và log giao dịch chi tiết.          | Thành công <1s     | Tích hợp với API Gateway         |
|----------------------|---------|---------------------|------------------------------------------------------------------------------------------------------------------------|--------------------|----------------------------------|
| /ivr/callflow        | DELETE  | Thêm bản ghi        | API /ivr/callflow sử dụng phương thức DELETE để Thêm bản ghi, có xác thực OAuth2 và log giao dịch chi tiết.            | Retry tối đa 3 lần | Hỗ trợ JSON và XML               |
| /crm/lead/import     | GET     | Cập nhật cấu hình   | API /crm/lead/import sử dụng phương thức GET để Cập nhật cấu hình, có xác thực OAuth2 và log giao dịch chi tiết.       | Rollback khi lỗi   | Hỗ trợ JSON và XML               |
| /rpa/task/execute    | DELETE  | Kiểm tra trạng thái | API /rpa/task/execute sử dụng phương thức DELETE để Kiểm tra trạng thái, có xác thực OAuth2 và log giao dịch chi tiết. | Retry tối đa 3 lần | Giới hạn rate-limit 1000 req/min |
| /network/qos/monitor | PATCH   | Cập nhật cấu hình   | API /network/qos/monitor sử dụng phương thức PATCH để Cập nhật cấu hình, có xác thực OAuth2 và log giao dịch chi tiết. | Retry tối đa 3 lần | Tích hợp với API Gateway         |

<!-- image -->

| VIETTEL AI RACE   | TD448   |
|-------------------|---------|

| /ivr/callflow     | POST   | Export dữ liệu    | API /ivr/callflow sử dụng phương thức POST để Export dữ liệu, có xác thực OAuth2 và log giao dịch chi tiết.      | Rollback khi lỗi            | Hỗ trợ JSON và XML               |
|-------------------|--------|-------------------|------------------------------------------------------------------------------------------------------------------|-----------------------------|----------------------------------|
| /ivr/callflow     | DELETE | Cập nhật cấu hình | API /ivr/callflow sử dụng phương thức DELETE để Cập nhật cấu hình, có xác thực OAuth2 và log giao dịch chi tiết. | Thông báo sự kiện qua Kafka | Hỗ trợ JSON và XML               |
| /crm/lead/import  | GET    | Xóa thông tin     | API /crm/lead/import sử dụng phương thức GET để Xóa thông tin, có xác thực OAuth2 và log giao dịch chi tiết.     | Log đầy đủ                  | Giới hạn rate-limit 1000 req/min |
| /rpa/task/execute | PUT    | Xóa thông tin     | API /rpa/task/execute sử dụng phương thức PUT để Xóa thông tin, có xác thực OAuth2 và log giao dịch chi tiết.    | Thành công <1s              | Theo chuẩn RESTful               |
| /crm/lead/import  | PATCH  | Thêm bản ghi      | API /crm/lead/import sử dụng phương thức PATCH để Thêm bản ghi, có xác thực OAuth2 và log giao dịch chi tiết.    | Log đầy đủ                  | Có versioning v1/v2              |
| /invoice/export   | PUT    | Kiểm tra trạng    | API /invoice/export sử dụng phương thức PUT để Kiểm tra trạng thái,                                              | Retry tối đa 3 lần          | Theo chuẩn                       |

<!-- image -->

| VIETTEL AI RACE   | TD448   |
|-------------------|---------|

|                      |       | thái                | có xác thực OAuth2 và log giao dịch chi tiết.                                                                       |                             | RESTful                          |
|----------------------|-------|---------------------|---------------------------------------------------------------------------------------------------------------------|-----------------------------|----------------------------------|
| /ivr/callflow        | PATCH | Kiểm tra trạng thái | API /ivr/callflow sử dụng phương thức PATCH để Kiểm tra trạng thái, có xác thực OAuth2 và log giao dịch chi tiết.   | Retry tối đa 3 lần          | Hỗ trợ JSON và XML               |
| /invoice/export      | GET   | Kiểm tra trạng thái | API /invoice/export sử dụng phương thức GET để Kiểm tra trạng thái, có xác thực OAuth2 và log giao dịch chi tiết.   | Thông báo sự kiện qua Kafka | Hỗ trợ JSON và XML               |
| /rpa/task/execute    | PATCH | Cập nhật cấu hình   | API /rpa/task/execute sử dụng phương thức PATCH để Cập nhật cấu hình, có xác thực OAuth2 và log giao dịch chi tiết. | Thông báo sự kiện qua Kafka | Giới hạn rate-limit 1000 req/min |
| /network/qos/monitor | GET   | Xóa thông tin       | API /network/qos/monitor sử dụng phương thức GET để Xóa thông tin, có xác thực OAuth2 và log giao dịch chi tiết.    | Thành công <1s              | Hỗ trợ JSON và XML               |
| /network/qos/monitor | POST  | Export dữ liệu      | API /network/qos/monitor sử dụng phương thức POST để Export dữ liệu, có xác thực OAuth2 và log giao                 | Thông báo sự kiện qua Kafka | Hỗ trợ JSON và XML               |

<!-- image -->

| VIETTEL AI RACE   | TD448   |
|-------------------|---------|

|                           |        |                     | dịch chi tiết.                                                                                                          |                             |                     |
|---------------------------|--------|---------------------|-------------------------------------------------------------------------------------------------------------------------|-----------------------------|---------------------|
| /invoice/export           | PUT    | Xóa thông tin       | API /invoice/export sử dụng phương thức PUT để Xóa thông tin, có xác thực OAuth2 và log giao dịch chi tiết.             | Rollback khi lỗi            | Có versioning v1/v2 |
| /security/firewall/config | DELETE | Thêm bản ghi        | API /security/firewall/config sử dụng phương thức DELETE để Thêm bản ghi, có xác thực OAuth2 và log giao dịch chi tiết. | Thông báo sự kiện qua Kafka | Theo chuẩn RESTful  |
| /invoice/export           | PATCH  | Kiểm tra trạng thái | API /invoice/export sử dụng phương thức PATCH để Kiểm tra trạng thái, có xác thực OAuth2 và log giao dịch chi tiết.     | Thông báo sự kiện qua Kafka | Có versioning v1/v2 |
| /network/qos/monitor      | DELETE | Export dữ liệu      | API /network/qos/monitor sử dụng phương thức DELETE để Export dữ liệu, có xác thực OAuth2 và log giao dịch chi tiết.    | Thông báo sự kiện qua Kafka | Hỗ trợ JSON và XML  |
| /ivr/callflow             | PATCH  | Export dữ liệu      | API /ivr/callflow sử dụng phương thức PATCH để Export dữ liệu, có xác thực OAuth2 và log giao                           | Thông báo sự kiện qua Kafka | Hỗ trợ JSON và XML  |

<!-- image -->

| VIETTEL AI RACE   | TD448   |
|-------------------|---------|

|                           |        |                     | dịch chi tiết.                                                                                                      |                  |                                  |
|---------------------------|--------|---------------------|---------------------------------------------------------------------------------------------------------------------|------------------|----------------------------------|
| /crm/lead/import          | PATCH  | Cập nhật cấu hình   | API /crm/lead/import sử dụng phương thức PATCH để Cập nhật cấu hình, có xác thực OAuth2 và log giao dịch chi tiết.  | Thành công <1s   | Có versioning v1/v2              |
| /ivr/callflow             | POST   | Kiểm tra trạng thái | API /ivr/callflow sử dụng phương thức POST để Kiểm tra trạng thái, có xác thực OAuth2 và log giao dịch chi tiết.    | Rollback khi lỗi | Tích hợp với API Gateway         |
| /ivr/callflow             | PATCH  | Xóa thông tin       | API /ivr/callflow sử dụng phương thức PATCH để Xóa thông tin, có xác thực OAuth2 và log giao dịch chi tiết.         | Thành công <1s   | Giới hạn rate-limit 1000 req/min |
| /network/qos/monitor      | DELETE | Xóa thông tin       | API /network/qos/monitor sử dụng phương thức DELETE để Xóa thông tin, có xác thực OAuth2 và log giao dịch chi tiết. | Log đầy đủ       | Giới hạn rate-limit 1000 req/min |
| /security/firewall/config | DELETE | Kiểm tra trạng thái | API /security/firewall/config sử dụng phương thức DELETE để Kiểm tra trạng thái, có xác thực OAuth2 và log giao     | Rollback khi lỗi | Hỗ trợ JSON và XML               |

<!-- image -->

| VIETTEL AI RACE   | TD448   |
|-------------------|---------|

|                           |        |                   | dịch chi tiết.                                                                                                         |                             |                                  |
|---------------------------|--------|-------------------|------------------------------------------------------------------------------------------------------------------------|-----------------------------|----------------------------------|
| /customer/update          | DELETE | Xóa thông tin     | API /customer/update sử dụng phương thức DELETE để Xóa thông tin, có xác thực OAuth2 và log giao dịch chi tiết.        | Thông báo sự kiện qua Kafka | Có versioning v1/v2              |
| /network/qos/monitor      | GET    | Thêm bản ghi      | API /network/qos/monitor sử dụng phương thức GET để Thêm bản ghi, có xác thực OAuth2 và log giao dịch chi tiết.        | Retry tối đa 3 lần          | Theo chuẩn RESTful               |
| /crm/lead/import          | DELETE | Export dữ liệu    | API /crm/lead/import sử dụng phương thức DELETE để Export dữ liệu, có xác thực OAuth2 và log giao dịch chi tiết.       | Thành công <1s              | Có versioning v1/v2              |
| /invoice/export           | POST   | Cập nhật cấu hình | API /invoice/export sử dụng phương thức POST để Cập nhật cấu hình, có xác thực OAuth2 và log giao dịch chi tiết.       | Log đầy đủ                  | Tích hợp với API Gateway         |
| /security/firewall/config | GET    | Export dữ liệu    | API /security/firewall/config sử dụng phương thức GET để Export dữ liệu, có xác thực OAuth2 và log giao dịch chi tiết. | Log đầy đủ                  | Giới hạn rate-limit 1000 req/min |

<!-- image -->

| VIETTEL AI RACE   | TD448   |
|-------------------|---------|

| /security/firewall/config   | PATCH   | Xóa thông tin       | API /security/firewall/config sử dụng phương thức PATCH để Xóa thông tin, có xác thực OAuth2 và log giao dịch chi tiết.   | Log đầy đủ                  | Hỗ trợ JSON và XML   |
|-----------------------------|---------|---------------------|---------------------------------------------------------------------------------------------------------------------------|-----------------------------|----------------------|
| /network/qos/monitor        | POST    | Export dữ liệu      | API /network/qos/monitor sử dụng phương thức POST để Export dữ liệu, có xác thực OAuth2 và log giao dịch chi tiết.        | Thông báo sự kiện qua Kafka | Theo chuẩn RESTful   |
| /rpa/task/execute           | DELETE  | Thêm bản ghi        | API /rpa/task/execute sử dụng phương thức DELETE để Thêm bản ghi, có xác thực OAuth2 và log giao dịch chi tiết.           | Thông báo sự kiện qua Kafka | Có versioning v1/v2  |
| /crm/lead/import            | PUT     | Kiểm tra trạng thái | API /crm/lead/import sử dụng phương thức PUT để Kiểm tra trạng thái, có xác thực OAuth2 và log giao dịch chi tiết.        | Thông báo sự kiện qua Kafka | Hỗ trợ JSON và XML   |
| /invoice/export             | PUT     | Thêm bản ghi        | API /invoice/export sử dụng phương thức PUT để Thêm bản ghi, có xác thực OAuth2 và log giao dịch chi tiết.                | Thành công <1s              | Theo chuẩn RESTful   |

<!-- image -->

| VIETTEL AI RACE   | TD448   |
|-------------------|---------|

| /ivr/callflow        | PATCH   | Cập nhật cấu hình   | API /ivr/callflow sử dụng phương thức PATCH để Cập nhật cấu hình, có xác thực OAuth2 và log giao dịch chi tiết.      | Retry tối đa 3 lần   | Giới hạn rate-limit 1000 req/min   |
|----------------------|---------|---------------------|----------------------------------------------------------------------------------------------------------------------|----------------------|------------------------------------|
| /network/qos/monitor | DELETE  | Export dữ liệu      | API /network/qos/monitor sử dụng phương thức DELETE để Export dữ liệu, có xác thực OAuth2 và log giao dịch chi tiết. | Rollback khi lỗi     | Tích hợp với API Gateway           |
| /customer/update     | PUT     | Xóa thông tin       | API /customer/update sử dụng phương thức PUT để Xóa thông tin, có xác thực OAuth2 và log giao dịch chi tiết.         | Thành công <1s       | Theo chuẩn RESTful                 |
| /network/qos/monitor | PATCH   | Xóa thông tin       | API /network/qos/monitor sử dụng phương thức PATCH để Xóa thông tin, có xác thực OAuth2 và log giao dịch chi tiết.   | Retry tối đa 3 lần   | Giới hạn rate-limit 1000 req/min   |
| /rpa/task/execute    | POST    | Xóa thông tin       | API /rpa/task/execute sử dụng phương thức POST để Xóa thông tin, có xác thực OAuth2 và log giao dịch chi tiết.       | Retry tối đa 3 lần   | Có versioning v1/v2                |
| /crm/lead/import     | PATCH   | Xóa thông           | API /crm/lead/import sử dụng phương thức                                                                             | Thông báo sự         | Theo chuẩn                         |

<!-- image -->

| VIETTEL AI RACE   | TD448   |
|-------------------|---------|

|                           |       | tin               | PATCH để Xóa thông tin, có xác thực OAuth2 và log giao dịch chi tiết.                                                       | kiện qua Kafka              | RESTful                          |
|---------------------------|-------|-------------------|-----------------------------------------------------------------------------------------------------------------------------|-----------------------------|----------------------------------|
| /crm/lead/import          | PATCH | Cập nhật cấu hình | API /crm/lead/import sử dụng phương thức PATCH để Cập nhật cấu hình, có xác thực OAuth2 và log giao dịch chi tiết.          | Thông báo sự kiện qua Kafka | Hỗ trợ JSON và XML               |
| /customer/update          | PUT   | Xóa thông tin     | API /customer/update sử dụng phương thức PUT để Xóa thông tin, có xác thực OAuth2 và log giao dịch chi tiết.                | Thông báo sự kiện qua Kafka | Giới hạn rate-limit 1000 req/min |
| /crm/lead/import          | POST  | Export dữ liệu    | API /crm/lead/import sử dụng phương thức POST để Export dữ liệu, có xác thực OAuth2 và log giao dịch chi tiết.              | Thông báo sự kiện qua Kafka | Theo chuẩn RESTful               |
| /security/firewall/config | PATCH | Cập nhật cấu hình | API /security/firewall/config sử dụng phương thức PATCH để Cập nhật cấu hình, có xác thực OAuth2 và log giao dịch chi tiết. | Retry tối đa 3 lần          | Giới hạn rate-limit 1000 req/min |
| /rpa/task/execute         | GET   | Thêm bản ghi      | API /rpa/task/execute sử dụng phương thức GET để Thêm bản ghi, có xác thực OAuth2 và                                        | Log đầy đủ                  | Có versioning v1/v2              |

<!-- image -->

| VIETTEL AI RACE   | TD448   |
|-------------------|---------|

|                      |       |                     | log giao dịch chi tiết.                                                                                             |                             |                                  |
|----------------------|-------|---------------------|---------------------------------------------------------------------------------------------------------------------|-----------------------------|----------------------------------|
| /network/qos/monitor | POST  | Xóa thông tin       | API /network/qos/monitor sử dụng phương thức POST để Xóa thông tin, có xác thực OAuth2 và log giao dịch chi tiết.   | Retry tối đa 3 lần          | Giới hạn rate-limit 1000 req/min |
| /customer/update     | POST  | Kiểm tra trạng thái | API /customer/update sử dụng phương thức POST để Kiểm tra trạng thái, có xác thực OAuth2 và log giao dịch chi tiết. | Thông báo sự kiện qua Kafka | Theo chuẩn RESTful               |
| /rpa/task/execute    | PATCH | Cập nhật cấu hình   | API /rpa/task/execute sử dụng phương thức PATCH để Cập nhật cấu hình, có xác thực OAuth2 và log giao dịch chi tiết. | Retry tối đa 3 lần          | Hỗ trợ JSON và XML               |
| /crm/lead/import     | PUT   | Thêm bản ghi        | API /crm/lead/import sử dụng phương thức PUT để Thêm bản ghi, có xác thực OAuth2 và log giao dịch chi tiết.         | Retry tối đa 3 lần          | Tích hợp với API Gateway         |
| /invoice/export      | GET   | Xóa thông tin       | API /invoice/export sử dụng phương thức GET để Xóa thông tin, có xác thực OAuth2 và log giao dịch chi tiết.         | Log đầy đủ                  | Hỗ trợ JSON và XML               |
| /ivr/callflow        | PUT   | Export              | API /ivr/callflow sử                                                                                                | Thông                       | Hỗ trợ                           |

<!-- image -->

| VIETTEL AI RACE   | TD448   |
|-------------------|---------|

|                           |        | dữ liệu           | dụng phương thức PUT để Export dữ liệu, có xác thực OAuth2 và log giao dịch chi tiết.                                     | báo sự kiện qua Kafka       | JSON và XML              |
|---------------------------|--------|-------------------|---------------------------------------------------------------------------------------------------------------------------|-----------------------------|--------------------------|
| /rpa/task/execute         | POST   | Xóa thông tin     | API /rpa/task/execute sử dụng phương thức POST để Xóa thông tin, có xác thực OAuth2 và log giao dịch chi tiết.            | Log đầy đủ                  | Theo chuẩn RESTful       |
| /crm/lead/import          | DELETE | Cập nhật cấu hình | API /crm/lead/import sử dụng phương thức DELETE để Cập nhật cấu hình, có xác thực OAuth2 và log giao dịch chi tiết.       | Rollback khi lỗi            | Có versioning v1/v2      |
| /invoice/export           | PATCH  | Thêm bản ghi      | API /invoice/export sử dụng phương thức PATCH để Thêm bản ghi, có xác thực OAuth2 và log giao dịch chi tiết.              | Retry tối đa 3 lần          | Theo chuẩn RESTful       |
| /security/firewall/config | PUT    | Cập nhật cấu hình | API /security/firewall/config sử dụng phương thức PUT để Cập nhật cấu hình, có xác thực OAuth2 và log giao dịch chi tiết. | Thông báo sự kiện qua Kafka | Tích hợp với API Gateway |
| /invoice/export           | POST   | Cập nhật cấu      | API /invoice/export sử dụng phương thức POST để Cập nhật cấu                                                              | Thông báo sự kiện qua       | Theo chuẩn               |

<!-- image -->

| VIETTEL AI RACE   | TD448   |
|-------------------|---------|

|                           |     | hình                | hình, có xác thực OAuth2 và log giao dịch chi tiết.                                                                  | Kafka                       | RESTful                          |
|---------------------------|-----|---------------------|----------------------------------------------------------------------------------------------------------------------|-----------------------------|----------------------------------|
| /rpa/task/execute         | PUT | Kiểm tra trạng thái | API /rpa/task/execute sử dụng phương thức PUT để Kiểm tra trạng thái, có xác thực OAuth2 và log giao dịch chi tiết.  | Rollback khi lỗi            | Tích hợp với API Gateway         |
| /network/qos/monitor      | PUT | Thêm bản ghi        | API /network/qos/monitor sử dụng phương thức PUT để Thêm bản ghi, có xác thực OAuth2 và log giao dịch chi tiết.      | Thông báo sự kiện qua Kafka | Hỗ trợ JSON và XML               |
| /security/firewall/config | PUT | Thêm bản ghi        | API /security/firewall/config sử dụng phương thức PUT để Thêm bản ghi, có xác thực OAuth2 và log giao dịch chi tiết. | Log đầy đủ                  | Tích hợp với API Gateway         |
| /crm/lead/import          | PUT | Cập nhật cấu hình   | API /crm/lead/import sử dụng phương thức PUT để Cập nhật cấu hình, có xác thực OAuth2 và log giao dịch chi tiết.     | Thành công <1s              | Giới hạn rate-limit 1000 req/min |
| /security/firewall/config | GET | Export dữ liệu      | API /security/firewall/config sử dụng phương thức GET để Export dữ liệu,                                             | Rollback khi lỗi            | Có versioning v1/v2              |

<!-- image -->

| VIETTEL AI RACE   | TD448   |
|-------------------|---------|

|                           |        |                     | có xác thực OAuth2 và log giao dịch chi tiết.                                                                          |                             |                                  |
|---------------------------|--------|---------------------|------------------------------------------------------------------------------------------------------------------------|-----------------------------|----------------------------------|
| /rpa/task/execute         | DELETE | Kiểm tra trạng thái | API /rpa/task/execute sử dụng phương thức DELETE để Kiểm tra trạng thái, có xác thực OAuth2 và log giao dịch chi tiết. | Rollback khi lỗi            | Giới hạn rate-limit 1000 req/min |
| /ivr/callflow             | POST   | Thêm bản ghi        | API /ivr/callflow sử dụng phương thức POST để Thêm bản ghi, có xác thực OAuth2 và log giao dịch chi tiết.              | Thành công <1s              | Hỗ trợ JSON và XML               |
| /ivr/callflow             | DELETE | Cập nhật cấu hình   | API /ivr/callflow sử dụng phương thức DELETE để Cập nhật cấu hình, có xác thực OAuth2 và log giao dịch chi tiết.       | Log đầy đủ                  | Có versioning v1/v2              |
| /rpa/task/execute         | DELETE | Export dữ liệu      | API /rpa/task/execute sử dụng phương thức DELETE để Export dữ liệu, có xác thực OAuth2 và log giao dịch chi tiết.      | Thông báo sự kiện qua Kafka | Theo chuẩn RESTful               |
| /security/firewall/config | PUT    | Export dữ liệu      | API /security/firewall/config sử dụng phương thức PUT để Export dữ liệu, có xác thực OAuth2 và                         | Thông báo sự kiện qua Kafka | Theo chuẩn RESTful               |

<!-- image -->

| VIETTEL AI RACE   | TD448   |
|-------------------|---------|

|                   |       |                     | log giao dịch chi tiết.                                                                                             |                             |                     |
|-------------------|-------|---------------------|---------------------------------------------------------------------------------------------------------------------|-----------------------------|---------------------|
| /crm/lead/import  | POST  | Cập nhật cấu hình   | API /crm/lead/import sử dụng phương thức POST để Cập nhật cấu hình, có xác thực OAuth2 và log giao dịch chi tiết.   | Thông báo sự kiện qua Kafka | Hỗ trợ JSON và XML  |
| /rpa/task/execute | PATCH | Xóa thông tin       | API /rpa/task/execute sử dụng phương thức PATCH để Xóa thông tin, có xác thực OAuth2 và log giao dịch chi tiết.     | Log đầy đủ                  | Theo chuẩn RESTful  |
| /invoice/export   | PATCH | Kiểm tra trạng thái | API /invoice/export sử dụng phương thức PATCH để Kiểm tra trạng thái, có xác thực OAuth2 và log giao dịch chi tiết. | Thành công <1s              | Hỗ trợ JSON và XML  |
| /crm/lead/import  | GET   | Cập nhật cấu hình   | API /crm/lead/import sử dụng phương thức GET để Cập nhật cấu hình, có xác thực OAuth2 và log giao dịch chi tiết.    | Retry tối đa 3 lần          | Có versioning v1/v2 |
| /customer/update  | GET   | Kiểm tra trạng thái | API /customer/update sử dụng phương thức GET để Kiểm tra trạng thái, có xác thực OAuth2 và log giao dịch chi tiết.  | Retry tối đa 3 lần          | Hỗ trợ JSON và XML  |

<!-- image -->

| VIETTEL AI RACE   | TD448   |
|-------------------|---------|

| /rpa/task/execute         | GET    | Thêm bản ghi        | API /rpa/task/execute sử dụng phương thức GET để Thêm bản ghi, có xác thực OAuth2 và log giao dịch chi tiết.                 | Rollback khi lỗi            | Theo chuẩn RESTful               |
|---------------------------|--------|---------------------|------------------------------------------------------------------------------------------------------------------------------|-----------------------------|----------------------------------|
| /invoice/export           | GET    | Kiểm tra trạng thái | API /invoice/export sử dụng phương thức GET để Kiểm tra trạng thái, có xác thực OAuth2 và log giao dịch chi tiết.            | Log đầy đủ                  | Có versioning v1/v2              |
| /invoice/export           | PATCH  | Thêm bản ghi        | API /invoice/export sử dụng phương thức PATCH để Thêm bản ghi, có xác thực OAuth2 và log giao dịch chi tiết.                 | Retry tối đa 3 lần          | Tích hợp với API Gateway         |
| /invoice/export           | DELETE | Thêm bản ghi        | API /invoice/export sử dụng phương thức DELETE để Thêm bản ghi, có xác thực OAuth2 và log giao dịch chi tiết.                | Thành công <1s              | Giới hạn rate-limit 1000 req/min |
| /security/firewall/config | DELETE | Cập nhật cấu hình   | API /security/firewall/config sử dụng phương thức DELETE để Cập nhật cấu hình, có xác thực OAuth2 và log giao dịch chi tiết. | Thông báo sự kiện qua Kafka | Giới hạn rate-limit 1000 req/min |
| /invoice/export           | PUT    | Xóa thông           | API /invoice/export sử dụng phương thức PUT                                                                                  | Retry tối                   | Theo chuẩn                       |

<!-- image -->

| VIETTEL AI RACE   | TD448   |
|-------------------|---------|

|                      |        | tin                 | để Xóa thông tin, có xác thực OAuth2 và log giao dịch chi tiết.                                                        | đa 3 lần                    | RESTful                          |
|----------------------|--------|---------------------|------------------------------------------------------------------------------------------------------------------------|-----------------------------|----------------------------------|
| /crm/lead/import     | POST   | Thêm bản ghi        | API /crm/lead/import sử dụng phương thức POST để Thêm bản ghi, có xác thực OAuth2 và log giao dịch chi tiết.           | Rollback khi lỗi            | Hỗ trợ JSON và XML               |
| /network/qos/monitor | GET    | Thêm bản ghi        | API /network/qos/monitor sử dụng phương thức GET để Thêm bản ghi, có xác thực OAuth2 và log giao dịch chi tiết.        | Thành công <1s              | Có versioning v1/v2              |
| /ivr/callflow        | PUT    | Cập nhật cấu hình   | API /ivr/callflow sử dụng phương thức PUT để Cập nhật cấu hình, có xác thực OAuth2 và log giao dịch chi tiết.          | Thông báo sự kiện qua Kafka | Theo chuẩn RESTful               |
| /rpa/task/execute    | DELETE | Kiểm tra trạng thái | API /rpa/task/execute sử dụng phương thức DELETE để Kiểm tra trạng thái, có xác thực OAuth2 và log giao dịch chi tiết. | Thông báo sự kiện qua Kafka | Hỗ trợ JSON và XML               |
| /rpa/task/execute    | PUT    | Thêm bản ghi        | API /rpa/task/execute sử dụng phương thức PUT để Thêm bản ghi, có xác thực OAuth2 và                                   | Thành công <1s              | Giới hạn rate-limit 1000 req/min |

<!-- image -->

| VIETTEL AI RACE   | TD448   |
|-------------------|---------|

|                      |        |                     | log giao dịch chi tiết.                                                                                              |                             |                                  |
|----------------------|--------|---------------------|----------------------------------------------------------------------------------------------------------------------|-----------------------------|----------------------------------|
| /crm/lead/import     | PATCH  | Kiểm tra trạng thái | API /crm/lead/import sử dụng phương thức PATCH để Kiểm tra trạng thái, có xác thực OAuth2 và log giao dịch chi tiết. | Rollback khi lỗi            | Tích hợp với API Gateway         |
| /customer/update     | PATCH  | Xóa thông tin       | API /customer/update sử dụng phương thức PATCH để Xóa thông tin, có xác thực OAuth2 và log giao dịch chi tiết.       | Retry tối đa 3 lần          | Theo chuẩn RESTful               |
| /ivr/callflow        | POST   | Kiểm tra trạng thái | API /ivr/callflow sử dụng phương thức POST để Kiểm tra trạng thái, có xác thực OAuth2 và log giao dịch chi tiết.     | Thành công <1s              | Giới hạn rate-limit 1000 req/min |
| /network/qos/monitor | GET    | Xóa thông tin       | API /network/qos/monitor sử dụng phương thức GET để Xóa thông tin, có xác thực OAuth2 và log giao dịch chi tiết.     | Thông báo sự kiện qua Kafka | Tích hợp với API Gateway         |
| /crm/lead/import     | DELETE | Xóa thông tin       | API /crm/lead/import sử dụng phương thức DELETE để Xóa thông tin, có xác thực OAuth2 và log giao dịch chi tiết.      | Thông báo sự kiện qua Kafka | Tích hợp với API Gateway         |
| /ivr/callflow        | PUT    | Export              | API /ivr/callflow sử                                                                                                 | Retry tối                   | Theo                             |

<!-- image -->

| VIETTEL AI RACE   | TD448   |
|-------------------|---------|

|                   |       | dữ liệu             | dụng phương thức PUT để Export dữ liệu, có xác thực OAuth2 và log giao dịch chi tiết.                                 | đa 3 lần           | chuẩn RESTful                    |
|-------------------|-------|---------------------|-----------------------------------------------------------------------------------------------------------------------|--------------------|----------------------------------|
| /rpa/task/execute | PATCH | Kiểm tra trạng thái | API /rpa/task/execute sử dụng phương thức PATCH để Kiểm tra trạng thái, có xác thực OAuth2 và log giao dịch chi tiết. | Retry tối đa 3 lần | Hỗ trợ JSON và XML               |
| /rpa/task/execute | PATCH | Export dữ liệu      | API /rpa/task/execute sử dụng phương thức PATCH để Export dữ liệu, có xác thực OAuth2 và log giao dịch chi tiết.      | Rollback khi lỗi   | Tích hợp với API Gateway         |
| /crm/lead/import  | PUT   | Xóa thông tin       | API /crm/lead/import sử dụng phương thức PUT để Xóa thông tin, có xác thực OAuth2 và log giao dịch chi tiết.          | Thành công <1s     | Theo chuẩn RESTful               |
| /rpa/task/execute | PATCH | Kiểm tra trạng thái | API /rpa/task/execute sử dụng phương thức PATCH để Kiểm tra trạng thái, có xác thực OAuth2 và log giao dịch chi tiết. | Retry tối đa 3 lần | Giới hạn rate-limit 1000 req/min |
| /crm/lead/import  | GET   | Export dữ liệu      | API /crm/lead/import sử dụng phương thức GET để Export dữ liệu, có xác thực OAuth2 và                                 | Log đầy đủ         | Có versioning v1/v2              |

<!-- image -->

| VIETTEL AI RACE   | TD448   |
|-------------------|---------|

|                           |        |                | log giao dịch chi tiết.                                                                                           |                             |                                  |
|---------------------------|--------|----------------|-------------------------------------------------------------------------------------------------------------------|-----------------------------|----------------------------------|
| /rpa/task/execute         | DELETE | Export dữ liệu | API /rpa/task/execute sử dụng phương thức DELETE để Export dữ liệu, có xác thực OAuth2 và log giao dịch chi tiết. | Thông báo sự kiện qua Kafka | Tích hợp với API Gateway         |
| /network/qos/monitor      | PATCH  | Thêm bản ghi   | API /network/qos/monitor sử dụng phương thức PATCH để Thêm bản ghi, có xác thực OAuth2 và log giao dịch chi tiết. | Log đầy đủ                  | Giới hạn rate-limit 1000 req/min |
| /invoice/export           | GET    | Export dữ liệu | API /invoice/export sử dụng phương thức GET để Export dữ liệu, có xác thực OAuth2 và log giao dịch chi tiết.      | Log đầy đủ                  | Theo chuẩn RESTful               |
| /rpa/task/execute         | DELETE | Export dữ liệu | API /rpa/task/execute sử dụng phương thức DELETE để Export dữ liệu, có xác thực OAuth2 và log giao dịch chi tiết. | Retry tối đa 3 lần          | Theo chuẩn RESTful               |
| /security/firewall/config | PATCH  | Xóa thông tin  | API /security/firewall/config sử dụng phương thức PATCH để Xóa thông tin, có xác thực OAuth2                      | Thông báo sự kiện qua Kafka | Theo chuẩn RESTful               |

<!-- image -->

| VIETTEL AI RACE   | TD448   |
|-------------------|---------|

|                      |        |                     | và log giao dịch chi tiết.                                                                                              |                    |                                  |
|----------------------|--------|---------------------|-------------------------------------------------------------------------------------------------------------------------|--------------------|----------------------------------|
| /customer/update     | PUT    | Cập nhật cấu hình   | API /customer/update sử dụng phương thức PUT để Cập nhật cấu hình, có xác thực OAuth2 và log giao dịch chi tiết.        | Thành công <1s     | Giới hạn rate-limit 1000 req/min |
| /invoice/export      | DELETE | Xóa thông tin       | API /invoice/export sử dụng phương thức DELETE để Xóa thông tin, có xác thực OAuth2 và log giao dịch chi tiết.          | Thành công <1s     | Tích hợp với API Gateway         |
| /customer/update     | PUT    | Export dữ liệu      | API /customer/update sử dụng phương thức PUT để Export dữ liệu, có xác thực OAuth2 và log giao dịch chi tiết.           | Thành công <1s     | Tích hợp với API Gateway         |
| /network/qos/monitor | POST   | Kiểm tra trạng thái | API /network/qos/monitor sử dụng phương thức POST để Kiểm tra trạng thái, có xác thực OAuth2 và log giao dịch chi tiết. | Log đầy đủ         | Tích hợp với API Gateway         |
| /invoice/export      | PUT    | Xóa thông tin       | API /invoice/export sử dụng phương thức PUT để Xóa thông tin, có xác thực OAuth2 và log giao dịch chi tiết.             | Retry tối đa 3 lần | Tích hợp với API Gateway         |
| /network/qos/monitor | GET    | Export              | API                                                                                                                     | Retry tối          | Tích hợp                         |

<!-- image -->

| VIETTEL AI RACE   | TD448   |
|-------------------|---------|

|                           |      | dữ liệu             | /network/qos/monitor sử dụng phương thức GET để Export dữ liệu, có xác thực OAuth2 và log giao dịch chi tiết.                | đa 3 lần           | với API Gateway                  |
|---------------------------|------|---------------------|------------------------------------------------------------------------------------------------------------------------------|--------------------|----------------------------------|
| /ivr/callflow             | GET  | Thêm bản ghi        | API /ivr/callflow sử dụng phương thức GET để Thêm bản ghi, có xác thực OAuth2 và log giao dịch chi tiết.                     | Retry tối đa 3 lần | Giới hạn rate-limit 1000 req/min |
| /security/firewall/config | POST | Kiểm tra trạng thái | API /security/firewall/config sử dụng phương thức POST để Kiểm tra trạng thái, có xác thực OAuth2 và log giao dịch chi tiết. | Thành công <1s     | Hỗ trợ JSON và XML               |
| /security/firewall/config | POST | Export dữ liệu      | API /security/firewall/config sử dụng phương thức POST để Export dữ liệu, có xác thực OAuth2 và log giao dịch chi tiết.      | Log đầy đủ         | Giới hạn rate-limit 1000 req/min |
| /invoice/export           | POST | Export dữ liệu      | API /invoice/export sử dụng phương thức POST để Export dữ liệu, có xác thực OAuth2 và log giao dịch chi tiết.                | Thành công <1s     | Theo chuẩn RESTful               |

<!-- image -->

| VIETTEL AI RACE   | TD448   |
|-------------------|---------|

| /crm/lead/import   | PATCH   | Kiểm tra trạng thái   | API /crm/lead/import sử dụng phương thức PATCH để Kiểm tra trạng thái, có xác thực OAuth2 và log giao dịch chi tiết.   | Retry tối đa 3 lần          | Hỗ trợ JSON và XML               |
|--------------------|---------|-----------------------|------------------------------------------------------------------------------------------------------------------------|-----------------------------|----------------------------------|
| /rpa/task/execute  | PUT     | Cập nhật cấu hình     | API /rpa/task/execute sử dụng phương thức PUT để Cập nhật cấu hình, có xác thực OAuth2 và log giao dịch chi tiết.      | Thông báo sự kiện qua Kafka | Hỗ trợ JSON và XML               |
| /invoice/export    | PUT     | Thêm bản ghi          | API /invoice/export sử dụng phương thức PUT để Thêm bản ghi, có xác thực OAuth2 và log giao dịch chi tiết.             | Log đầy đủ                  | Hỗ trợ JSON và XML               |
| /crm/lead/import   | DELETE  | Thêm bản ghi          | API /crm/lead/import sử dụng phương thức DELETE để Thêm bản ghi, có xác thực OAuth2 và log giao dịch chi tiết.         | Thông báo sự kiện qua Kafka | Tích hợp với API Gateway         |
| /ivr/callflow      | PUT     | Cập nhật cấu hình     | API /ivr/callflow sử dụng phương thức PUT để Cập nhật cấu hình, có xác thực OAuth2 và log giao dịch chi tiết.          | Retry tối đa 3 lần          | Giới hạn rate-limit 1000 req/min |
| /invoice/export    | PATCH   | Thêm bản              | API /invoice/export sử dụng phương thức PATCH để Thêm bản                                                              | Thành công                  | Có versioning                    |

<!-- image -->

| VIETTEL AI RACE   | TD448   |
|-------------------|---------|

|                   |        | ghi                 | ghi, có xác thực OAuth2 và log giao dịch chi tiết.                                                                 | <1s                         | v1/v2                            |
|-------------------|--------|---------------------|--------------------------------------------------------------------------------------------------------------------|-----------------------------|----------------------------------|
| /rpa/task/execute | PUT    | Export dữ liệu      | API /rpa/task/execute sử dụng phương thức PUT để Export dữ liệu, có xác thực OAuth2 và log giao dịch chi tiết.     | Retry tối đa 3 lần          | Có versioning v1/v2              |
| /invoice/export   | DELETE | Thêm bản ghi        | API /invoice/export sử dụng phương thức DELETE để Thêm bản ghi, có xác thực OAuth2 và log giao dịch chi tiết.      | Thành công <1s              | Tích hợp với API Gateway         |
| /invoice/export   | POST   | Kiểm tra trạng thái | API /invoice/export sử dụng phương thức POST để Kiểm tra trạng thái, có xác thực OAuth2 và log giao dịch chi tiết. | Log đầy đủ                  | Có versioning v1/v2              |
| /customer/update  | PUT    | Thêm bản ghi        | API /customer/update sử dụng phương thức PUT để Thêm bản ghi, có xác thực OAuth2 và log giao dịch chi tiết.        | Thành công <1s              | Giới hạn rate-limit 1000 req/min |
| /rpa/task/execute | PATCH  | Thêm bản ghi        | API /rpa/task/execute sử dụng phương thức PATCH để Thêm bản ghi, có xác thực OAuth2 và log giao                    | Thông báo sự kiện qua Kafka | Theo chuẩn RESTful               |

<!-- image -->

| VIETTEL AI RACE   | TD448   |
|-------------------|---------|

|                      |        |                     | dịch chi tiết.                                                                                                         |                  |                          |
|----------------------|--------|---------------------|------------------------------------------------------------------------------------------------------------------------|------------------|--------------------------|
| /network/qos/monitor | PUT    | Kiểm tra trạng thái | API /network/qos/monitor sử dụng phương thức PUT để Kiểm tra trạng thái, có xác thực OAuth2 và log giao dịch chi tiết. | Thành công <1s   | Có versioning v1/v2      |
| /invoice/export      | DELETE | Kiểm tra trạng thái | API /invoice/export sử dụng phương thức DELETE để Kiểm tra trạng thái, có xác thực OAuth2 và log giao dịch chi tiết.   | Rollback khi lỗi | Hỗ trợ JSON và XML       |
| /ivr/callflow        | PATCH  | Kiểm tra trạng thái | API /ivr/callflow sử dụng phương thức PATCH để Kiểm tra trạng thái, có xác thực OAuth2 và log giao dịch chi tiết.      | Log đầy đủ       | Hỗ trợ JSON và XML       |
| /customer/update     | PUT    | Thêm bản ghi        | API /customer/update sử dụng phương thức PUT để Thêm bản ghi, có xác thực OAuth2 và log giao dịch chi tiết.            | Rollback khi lỗi | Có versioning v1/v2      |
| /rpa/task/execute    | DELETE | Xóa thông tin       | API /rpa/task/execute sử dụng phương thức DELETE để Xóa thông tin, có xác thực OAuth2 và log giao dịch chi tiết.       | Log đầy đủ       | Tích hợp với API Gateway |

<!-- image -->

| VIETTEL AI RACE   | TD448   |
|-------------------|---------|

| /crm/lead/import          | DELETE   | Thêm bản ghi        | API /crm/lead/import sử dụng phương thức DELETE để Thêm bản ghi, có xác thực OAuth2 và log giao dịch chi tiết.               | Retry tối đa 3 lần          | Giới hạn rate-limit 1000 req/min   |
|---------------------------|----------|---------------------|------------------------------------------------------------------------------------------------------------------------------|-----------------------------|------------------------------------|
| /crm/lead/import          | PUT      | Export dữ liệu      | API /crm/lead/import sử dụng phương thức PUT để Export dữ liệu, có xác thực OAuth2 và log giao dịch chi tiết.                | Thành công <1s              | Giới hạn rate-limit 1000 req/min   |
| /network/qos/monitor      | POST     | Export dữ liệu      | API /network/qos/monitor sử dụng phương thức POST để Export dữ liệu, có xác thực OAuth2 và log giao dịch chi tiết.           | Rollback khi lỗi            | Theo chuẩn RESTful                 |
| /security/firewall/config | POST     | Kiểm tra trạng thái | API /security/firewall/config sử dụng phương thức POST để Kiểm tra trạng thái, có xác thực OAuth2 và log giao dịch chi tiết. | Thông báo sự kiện qua Kafka | Hỗ trợ JSON và XML                 |
| /ivr/callflow             | PUT      | Cập nhật cấu hình   | API /ivr/callflow sử dụng phương thức PUT để Cập nhật cấu hình, có xác thực OAuth2 và log giao dịch chi tiết.                | Retry tối đa 3 lần          | Theo chuẩn RESTful                 |

<!-- image -->

| VIETTEL AI RACE   | TD448   |
|-------------------|---------|

| /crm/lead/import          | DELETE   | Cập nhật cấu hình   | API /crm/lead/import sử dụng phương thức DELETE để Cập nhật cấu hình, có xác thực OAuth2 và log giao dịch chi tiết.      | Retry tối đa 3 lần   | Tích hợp với API Gateway   |
|---------------------------|----------|---------------------|--------------------------------------------------------------------------------------------------------------------------|----------------------|----------------------------|
| /ivr/callflow             | DELETE   | Cập nhật cấu hình   | API /ivr/callflow sử dụng phương thức DELETE để Cập nhật cấu hình, có xác thực OAuth2 và log giao dịch chi tiết.         | Rollback khi lỗi     | Tích hợp với API Gateway   |
| /crm/lead/import          | GET      | Thêm bản ghi        | API /crm/lead/import sử dụng phương thức GET để Thêm bản ghi, có xác thực OAuth2 và log giao dịch chi tiết.              | Rollback khi lỗi     | Theo chuẩn RESTful         |
| /security/firewall/config | PATCH    | Export dữ liệu      | API /security/firewall/config sử dụng phương thức PATCH để Export dữ liệu, có xác thực OAuth2 và log giao dịch chi tiết. | Log đầy đủ           | Có versioning v1/v2        |
| /ivr/callflow             | PUT      | Kiểm tra trạng thái | API /ivr/callflow sử dụng phương thức PUT để Kiểm tra trạng thái, có xác thực OAuth2 và log giao dịch chi tiết.          | Rollback khi lỗi     | Hỗ trợ JSON và XML         |
| /network/qos/monitor      | DELETE   | Kiểm tra            | API /network/qos/monitor                                                                                                 | Rollback             | Hỗ trợ JSON và             |

<!-- image -->

| VIETTEL AI RACE   | TD448   |
|-------------------|---------|

|                           |        | trạng thái        | sử dụng phương thức DELETE để Kiểm tra trạng thái, có xác thực OAuth2 và log giao dịch chi tiết.                         | khi lỗi                     | XML                              |
|---------------------------|--------|-------------------|--------------------------------------------------------------------------------------------------------------------------|-----------------------------|----------------------------------|
| /invoice/export           | DELETE | Xóa thông tin     | API /invoice/export sử dụng phương thức DELETE để Xóa thông tin, có xác thực OAuth2 và log giao dịch chi tiết.           | Retry tối đa 3 lần          | Có versioning v1/v2              |
| /network/qos/monitor      | POST   | Thêm bản ghi      | API /network/qos/monitor sử dụng phương thức POST để Thêm bản ghi, có xác thực OAuth2 và log giao dịch chi tiết.         | Retry tối đa 3 lần          | Giới hạn rate-limit 1000 req/min |
| /security/firewall/config | DELETE | Xóa thông tin     | API /security/firewall/config sử dụng phương thức DELETE để Xóa thông tin, có xác thực OAuth2 và log giao dịch chi tiết. | Thông báo sự kiện qua Kafka | Theo chuẩn RESTful               |
| /invoice/export           | DELETE | Cập nhật cấu hình | API /invoice/export sử dụng phương thức DELETE để Cập nhật cấu hình, có xác thực OAuth2 và log giao dịch chi tiết.       | Thành công <1s              | Theo chuẩn RESTful               |
| /customer/update          | PATCH  | Xóa thông         | API /customer/update sử dụng phương thức                                                                                 | Rollback                    | Tích hợp với API                 |

<!-- image -->

| VIETTEL AI RACE   | TD448   |
|-------------------|---------|

|                           |        | tin                 | PATCH để Xóa thông tin, có xác thực OAuth2 và log giao dịch chi tiết.                                                        | khi lỗi            | Gateway                  |
|---------------------------|--------|---------------------|------------------------------------------------------------------------------------------------------------------------------|--------------------|--------------------------|
| /ivr/callflow             | POST   | Cập nhật cấu hình   | API /ivr/callflow sử dụng phương thức POST để Cập nhật cấu hình, có xác thực OAuth2 và log giao dịch chi tiết.               | Retry tối đa 3 lần | Có versioning v1/v2      |
| /security/firewall/config | DELETE | Cập nhật cấu hình   | API /security/firewall/config sử dụng phương thức DELETE để Cập nhật cấu hình, có xác thực OAuth2 và log giao dịch chi tiết. | Retry tối đa 3 lần | Tích hợp với API Gateway |
| /customer/update          | DELETE | Kiểm tra trạng thái | API /customer/update sử dụng phương thức DELETE để Kiểm tra trạng thái, có xác thực OAuth2 và log giao dịch chi tiết.        | Retry tối đa 3 lần | Có versioning v1/v2      |
| /customer/update          | PATCH  | Kiểm tra trạng thái | API /customer/update sử dụng phương thức PATCH để Kiểm tra trạng thái, có xác thực OAuth2 và log giao dịch chi tiết.         | Log đầy đủ         | Theo chuẩn RESTful       |
| /security/firewall/config | POST   | Export dữ           | API /security/firewall/config sử dụng phương thức                                                                            | Log đầy đủ         | Tích hợp với API         |

<!-- image -->

| VIETTEL AI RACE   | TD448   |
|-------------------|---------|

|                  |        | liệu                | POST để Export dữ liệu, có xác thực OAuth2 và log giao dịch chi tiết.                                                 |                             | Gateway                          |
|------------------|--------|---------------------|-----------------------------------------------------------------------------------------------------------------------|-----------------------------|----------------------------------|
| /crm/lead/import | DELETE | Kiểm tra trạng thái | API /crm/lead/import sử dụng phương thức DELETE để Kiểm tra trạng thái, có xác thực OAuth2 và log giao dịch chi tiết. | Retry tối đa 3 lần          | Hỗ trợ JSON và XML               |
| /crm/lead/import | PATCH  | Kiểm tra trạng thái | API /crm/lead/import sử dụng phương thức PATCH để Kiểm tra trạng thái, có xác thực OAuth2 và log giao dịch chi tiết.  | Log đầy đủ                  | Có versioning v1/v2              |
| /customer/update | PUT    | Export dữ liệu      | API /customer/update sử dụng phương thức PUT để Export dữ liệu, có xác thực OAuth2 và log giao dịch chi tiết.         | Thông báo sự kiện qua Kafka | Tích hợp với API Gateway         |
| /invoice/export  | GET    | Export dữ liệu      | API /invoice/export sử dụng phương thức GET để Export dữ liệu, có xác thực OAuth2 và log giao dịch chi tiết.          | Thông báo sự kiện qua Kafka | Giới hạn rate-limit 1000 req/min |
| /customer/update | POST   | Thêm bản ghi        | API /customer/update sử dụng phương thức POST để Thêm bản ghi, có xác thực OAuth2 và log giao                         | Retry tối đa 3 lần          | Hỗ trợ JSON và XML               |

<!-- image -->

| VIETTEL AI RACE   | TD448   |
|-------------------|---------|

|                   |        |                     | dịch chi tiết.                                                                                                       |                    |                          |
|-------------------|--------|---------------------|----------------------------------------------------------------------------------------------------------------------|--------------------|--------------------------|
| /crm/lead/import  | DELETE | Xóa thông tin       | API /crm/lead/import sử dụng phương thức DELETE để Xóa thông tin, có xác thực OAuth2 và log giao dịch chi tiết.      | Thành công <1s     | Có versioning v1/v2      |
| /rpa/task/execute | GET    | Thêm bản ghi        | API /rpa/task/execute sử dụng phương thức GET để Thêm bản ghi, có xác thực OAuth2 và log giao dịch chi tiết.         | Retry tối đa 3 lần | Có versioning v1/v2      |
| /ivr/callflow     | POST   | Thêm bản ghi        | API /ivr/callflow sử dụng phương thức POST để Thêm bản ghi, có xác thực OAuth2 và log giao dịch chi tiết.            | Retry tối đa 3 lần | Tích hợp với API Gateway |
| /customer/update  | PATCH  | Kiểm tra trạng thái | API /customer/update sử dụng phương thức PATCH để Kiểm tra trạng thái, có xác thực OAuth2 và log giao dịch chi tiết. | Thành công <1s     | Hỗ trợ JSON và XML       |