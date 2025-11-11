<!-- image -->

## VIETTEL AI RACE

## KỊCH BẢN KIỂM THỬ QA

TD447

Lần ban hành: 1

| Test case              | Mô tả                                                                                                                      | Input                       | Expected Output                              | Phương pháp      | Ghi chú                             |
|------------------------|----------------------------------------------------------------------------------------------------------------------------|-----------------------------|----------------------------------------------|------------------|-------------------------------------|
| Login test             | Thực hiện Login test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.             | API call batch 1000 request | User login thành công trong <1s              | JMeter script    | Test môi trường Pre- Prod           |
| Load test              | Thực hiện Load test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.              | stress load > 10k TPS       | User login thành công trong <1s              | Manual test plan | Phải log toàn bộ kết quả            |
| Database recovery test | Thực hiện Database recovery test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại. | network disconnect          | Không phát hiện lỗ hổng bảo mật OWASP Top 10 | Manual test plan | So sánh benchmark với release trước |
| Database recovery test | Thực hiện Database recovery test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại. | stress load > 10k TPS       | Cluster failover tự động trong 5s            | Manual test plan | Theo chuẩn ISTQB                    |

<!-- image -->

## VIETTEL AI RACE

## KỊCH BẢN KIỂM THỬ QA

TD447

Lần ban hành: 1

| Security scan          | Thực hiện Security scan để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.          | API call batch 1000 request   | User login thành công trong <1s              | Manual test plan   | Gửi báo cáo PDF hàng ngày           |
|------------------------|----------------------------------------------------------------------------------------------------------------------------|-------------------------------|----------------------------------------------|--------------------|-------------------------------------|
| Security scan          | Thực hiện Security scan để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.          | DB corruption                 | Dữ liệu được khôi phục toàn vẹn sau sự cố    | Kịch bản Ansible   | Test môi trường Pre- Prod           |
| API stress test        | Thực hiện API stress test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.        | valid data                    | User login thành công trong <1s              | Manual test plan   | So sánh benchmark với release trước |
| Database recovery test | Thực hiện Database recovery test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại. | valid data                    | Không phát hiện lỗ hổng bảo mật OWASP Top 10 | Manual test plan   | Test môi trường Pre- Prod           |
| Failover test          | Thực hiện Failover test để kiểm thử chức năng và hiệu năng của hệ thống,                                                   | network disconnect            | Dữ liệu được khôi phục toàn vẹn sau          | Manual test plan   | So sánh benchmark với release trước |

<!-- image -->

## VIETTEL AI RACE

## KỊCH BẢN KIỂM THỬ QA

TD447

Lần ban hành: 1

|                        | bao gồm kịch bản thành công và thất bại.                                                                                   |                       | sự cố                                        |                  |                                     |
|------------------------|----------------------------------------------------------------------------------------------------------------------------|-----------------------|----------------------------------------------|------------------|-------------------------------------|
| API stress test        | Thực hiện API stress test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.        | DB corruption         | Không phát hiện lỗ hổng bảo mật OWASP Top 10 | Kịch bản Ansible | Test môi trường Pre- Prod           |
| Data consistency test  | Thực hiện Data consistency test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.  | stress load > 10k TPS | Cluster failover tự động trong 5s            | Kịch bản Ansible | So sánh benchmark với release trước |
| Database recovery test | Thực hiện Database recovery test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại. | stress load > 10k TPS | User login thành công trong <1s              | Kịch bản Ansible | Gửi báo cáo PDF hàng ngày           |
| Failover test          | Thực hiện Failover test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.          | stress load > 10k TPS | Dữ liệu được khôi phục toàn vẹn sau sự cố    | JMeter script    | Phải log toàn bộ kết quả            |

<!-- image -->

## VIETTEL AI RACE

## KỊCH BẢN KIỂM THỬ QA

TD447

Lần ban hành: 1

| API stress test   | Thực hiện API stress test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.   | invalid data       | Dữ liệu được khôi phục toàn vẹn sau sự cố    | Automation Selenium   | Phải log toàn bộ kết quả            |
|-------------------|-----------------------------------------------------------------------------------------------------------------------|--------------------|----------------------------------------------|-----------------------|-------------------------------------|
| Load test         | Thực hiện Load test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.         | network disconnect | Cluster failover tự động trong 5s            | JMeter script         | Phải log toàn bộ kết quả            |
| Security scan     | Thực hiện Security scan để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.     | invalid data       | User login thành công trong <1s              | JMeter script         | So sánh benchmark với release trước |
| Failover test     | Thực hiện Failover test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.     | valid data         | Không phát hiện lỗ hổng bảo mật OWASP Top 10 | Kịch bản Ansible      | Theo chuẩn ISTQB                    |
| Failover test     | Thực hiện Failover test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản                             | network disconnect | User login thành công                        | Kịch bản Ansible      | Test môi trường Pre- Prod           |

<!-- image -->

## VIETTEL AI RACE

## KỊCH BẢN KIỂM THỬ QA

TD447

Lần ban hành: 1

|                       | thành công và thất bại.                                                                                                   |                    | trong <1s                                 |                     |                                     |
|-----------------------|---------------------------------------------------------------------------------------------------------------------------|--------------------|-------------------------------------------|---------------------|-------------------------------------|
| Failover test         | Thực hiện Failover test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.         | invalid data       | User login thành công trong <1s           | Manual test plan    | Gửi báo cáo PDF hàng ngày           |
| API stress test       | Thực hiện API stress test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.       | valid data         | Hệ thống chịu tải 20k TPS không gián đoạn | Automation Selenium | Test môi trường Pre- Prod           |
| Data consistency test | Thực hiện Data consistency test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại. | network disconnect | Cluster failover tự động trong 5s         | JMeter script       | So sánh benchmark với release trước |
| Load test             | Thực hiện Load test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.             | valid data         | User login thành công trong <1s           | Manual test plan    | Phải log toàn bộ kết quả            |
| API stress            | Thực hiện API stress test để kiểm thử                                                                                     | invalid            | User login                                | JMeter              | Gửi báo cáo                         |

<!-- image -->

## VIETTEL AI RACE

## KỊCH BẢN KIỂM THỬ QA

TD447

Lần ban hành: 1

| test                   | chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.                                              | data               | thành công trong <1s              | script              | PDF hàng ngày             |
|------------------------|----------------------------------------------------------------------------------------------------------------------------|--------------------|-----------------------------------|---------------------|---------------------------|
| Database recovery test | Thực hiện Database recovery test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại. | invalid data       | Cluster failover tự động trong 5s | Automation Selenium | Test môi trường Pre- Prod |
| Security scan          | Thực hiện Security scan để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.          | valid data         | User login thành công trong <1s   | JMeter script       | Gửi báo cáo PDF hàng ngày |
| Security scan          | Thực hiện Security scan để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.          | network disconnect | Cluster failover tự động trong 5s | Manual test plan    | Gửi báo cáo PDF hàng ngày |
| Login test             | Thực hiện Login test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành                               | invalid data       | User login thành công trong <1s   | Manual test plan    | Theo chuẩn ISTQB          |

<!-- image -->

## VIETTEL AI RACE

## KỊCH BẢN KIỂM THỬ QA

TD447

Lần ban hành: 1

|                       | công và thất bại.                                                                                                   |                             |                                           |                     |                                     |
|-----------------------|---------------------------------------------------------------------------------------------------------------------|-----------------------------|-------------------------------------------|---------------------|-------------------------------------|
| Load test             | Thực hiện Load test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.       | stress load > 10k TPS       | User login thành công trong <1s           | Automation Selenium | Phải log toàn bộ kết quả            |
| API stress test       | Thực hiện API stress test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại. | API call batch 1000 request | Cluster failover tự động trong 5s         | Kịch bản Ansible    | Phải log toàn bộ kết quả            |
| Load test             | Thực hiện Load test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.       | stress load > 10k TPS       | Cluster failover tự động trong 5s         | Kịch bản Ansible    | Test môi trường Pre- Prod           |
| API stress test       | Thực hiện API stress test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại. | network disconnect          | Hệ thống chịu tải 20k TPS không gián đoạn | Manual test plan    | Phải log toàn bộ kết quả            |
| Data consistency test | Thực hiện Data consistency test để kiểm thử chức năng và hiệu năng của hệ                                           | network disconnect          | Hệ thống chịu tải 20k TPS không           | Kịch bản Ansible    | So sánh benchmark với release trước |

<!-- image -->

## VIETTEL AI RACE

## KỊCH BẢN KIỂM THỬ QA

TD447

Lần ban hành: 1

|                        | thống, bao gồm kịch bản thành công và thất bại.                                                                            |                    | gián đoạn                                    |                  |                                     |
|------------------------|----------------------------------------------------------------------------------------------------------------------------|--------------------|----------------------------------------------|------------------|-------------------------------------|
| Load test              | Thực hiện Load test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.              | DB corruption      | Dữ liệu được khôi phục toàn vẹn sau sự cố    | Kịch bản Ansible | Test môi trường Pre- Prod           |
| Data consistency test  | Thực hiện Data consistency test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.  | network disconnect | User login thành công trong <1s              | Manual test plan | Theo chuẩn ISTQB                    |
| Database recovery test | Thực hiện Database recovery test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại. | DB corruption      | Không phát hiện lỗ hổng bảo mật OWASP Top 10 | JMeter script    | So sánh benchmark với release trước |
| Database recovery test | Thực hiện Database recovery test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại. | network disconnect | Không phát hiện lỗ hổng bảo mật OWASP Top 10 | JMeter script    | Test môi trường Pre- Prod           |
| Database               | Thực hiện Database                                                                                                         | DB                 | Hệ thống                                     | Automation       | So sánh                             |

<!-- image -->

## VIETTEL AI RACE

## KỊCH BẢN KIỂM THỬ QA

TD447

Lần ban hành: 1

| recovery test          | recovery test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.                    | corruption            | chịu tải 20k TPS không gián đoạn          | Selenium            | benchmark với release trước   |
|------------------------|----------------------------------------------------------------------------------------------------------------------------|-----------------------|-------------------------------------------|---------------------|-------------------------------|
| Data consistency test  | Thực hiện Data consistency test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.  | valid data            | Dữ liệu được khôi phục toàn vẹn sau sự cố | Manual test plan    | Phải log toàn bộ kết quả      |
| Database recovery test | Thực hiện Database recovery test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại. | stress load > 10k TPS | Dữ liệu được khôi phục toàn vẹn sau sự cố | JMeter script       | Gửi báo cáo PDF hàng ngày     |
| Database recovery test | Thực hiện Database recovery test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại. | valid data            | Cluster failover tự động trong 5s         | Automation Selenium | Phải log toàn bộ kết quả      |
| Data consistency test  | Thực hiện Data consistency test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch                              | invalid data          | User login thành công                     | Manual test plan    | Test môi trường Pre- Prod     |

<!-- image -->

## VIETTEL AI RACE

## KỊCH BẢN KIỂM THỬ QA

TD447

Lần ban hành: 1

|                       | bản thành công và thất bại.                                                                                       |                       | trong <1s                                    |                     |                           |
|-----------------------|-------------------------------------------------------------------------------------------------------------------|-----------------------|----------------------------------------------|---------------------|---------------------------|
| Failover test         | Thực hiện Failover test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại. | stress load > 10k TPS | Không phát hiện lỗ hổng bảo mật OWASP Top 10 | JMeter script       | Gửi báo cáo PDF hàng ngày |
| Login test            | Thực hiện Login test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.    | stress load > 10k TPS | Không phát hiện lỗ hổng bảo mật OWASP Top 10 | JMeter script       | Theo chuẩn ISTQB          |
| Login test            | Thực hiện Login test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.    | invalid data          | Không phát hiện lỗ hổng bảo mật OWASP Top 10 | Automation Selenium | Test môi trường Pre- Prod |
| Login test            | Thực hiện Login test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.    | valid data            | Hệ thống chịu tải 20k TPS không gián đoạn    | Manual test plan    | Theo chuẩn ISTQB          |
| Data consistency test | Thực hiện Data consistency test để kiểm thử chức năng và hiệu năng của hệ                                         | network disconnect    | Dữ liệu được khôi phục toàn vẹn sau          | Kịch bản Ansible    | Gửi báo cáo PDF hàng ngày |

<!-- image -->

## VIETTEL AI RACE

## KỊCH BẢN KIỂM THỬ QA

TD447

Lần ban hành: 1

|                 | thống, bao gồm kịch bản thành công và thất bại.                                                                     |                             | sự cố                                        |                     |                                     |
|-----------------|---------------------------------------------------------------------------------------------------------------------|-----------------------------|----------------------------------------------|---------------------|-------------------------------------|
| Login test      | Thực hiện Login test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.      | network disconnect          | Hệ thống chịu tải 20k TPS không gián đoạn    | Automation Selenium | So sánh benchmark với release trước |
| API stress test | Thực hiện API stress test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại. | network disconnect          | Cluster failover tự động trong 5s            | Kịch bản Ansible    | Test môi trường Pre- Prod           |
| Failover test   | Thực hiện Failover test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.   | API call batch 1000 request | Không phát hiện lỗ hổng bảo mật OWASP Top 10 | Automation Selenium | Test môi trường Pre- Prod           |
| API stress test | Thực hiện API stress test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại. | invalid data                | Không phát hiện lỗ hổng bảo mật OWASP Top 10 | Automation Selenium | Test môi trường Pre- Prod           |
| API stress      | Thực hiện API stress                                                                                                | network                     | Không                                        | JMeter              | Theo chuẩn                          |

<!-- image -->

## VIETTEL AI RACE

## KỊCH BẢN KIỂM THỬ QA

TD447

Lần ban hành: 1

| test                   | test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.                             | disconnect   | phát hiện lỗ hổng bảo mật OWASP Top 10    | script              | ISTQB                               |
|------------------------|----------------------------------------------------------------------------------------------------------------------------|--------------|-------------------------------------------|---------------------|-------------------------------------|
| Data consistency test  | Thực hiện Data consistency test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.  | invalid data | Cluster failover tự động trong 5s         | Manual test plan    | So sánh benchmark với release trước |
| Failover test          | Thực hiện Failover test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.          | valid data   | Dữ liệu được khôi phục toàn vẹn sau sự cố | Automation Selenium | So sánh benchmark với release trước |
| Database recovery test | Thực hiện Database recovery test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại. | valid data   | Hệ thống chịu tải 20k TPS không gián đoạn | Manual test plan    | So sánh benchmark với release trước |
| Data consistency test  | Thực hiện Data consistency test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch                              | invalid data | Cluster failover tự động trong 5s         | Automation Selenium | So sánh benchmark với release trước |

<!-- image -->

## VIETTEL AI RACE

## KỊCH BẢN KIỂM THỬ QA

TD447

Lần ban hành: 1

|                        | bản thành công và thất bại.                                                                                                |                       |                                           |                  |                                     |
|------------------------|----------------------------------------------------------------------------------------------------------------------------|-----------------------|-------------------------------------------|------------------|-------------------------------------|
| Load test              | Thực hiện Load test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.              | DB corruption         | User login thành công trong <1s           | Manual test plan | So sánh benchmark với release trước |
| API stress test        | Thực hiện API stress test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.        | DB corruption         | Hệ thống chịu tải 20k TPS không gián đoạn | Kịch bản Ansible | So sánh benchmark với release trước |
| Database recovery test | Thực hiện Database recovery test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại. | stress load > 10k TPS | User login thành công trong <1s           | JMeter script    | Theo chuẩn ISTQB                    |
| Database recovery test | Thực hiện Database recovery test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại. | valid data            | Cluster failover tự động trong 5s         | Manual test plan | Test môi trường Pre- Prod           |
| Data consistency       | Thực hiện Data consistency test để                                                                                         | network               | Hệ thống chịu tải                         | Manual test      | Phải log toàn                       |

<!-- image -->

## VIETTEL AI RACE

## KỊCH BẢN KIỂM THỬ QA

TD447

Lần ban hành: 1

| test          | kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.                            | disconnect         | 20k TPS không gián đoạn                   | plan                | bộ kết quả                          |
|---------------|-------------------------------------------------------------------------------------------------------------------|--------------------|-------------------------------------------|---------------------|-------------------------------------|
| Failover test | Thực hiện Failover test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại. | network disconnect | Cluster failover tự động trong 5s         | JMeter script       | Theo chuẩn ISTQB                    |
| Failover test | Thực hiện Failover test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại. | valid data         | Cluster failover tự động trong 5s         | Automation Selenium | So sánh benchmark với release trước |
| Load test     | Thực hiện Load test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.     | invalid data       | User login thành công trong <1s           | Automation Selenium | Theo chuẩn ISTQB                    |
| Login test    | Thực hiện Login test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.    | valid data         | Hệ thống chịu tải 20k TPS không gián đoạn | Automation Selenium | Theo chuẩn ISTQB                    |

<!-- image -->

## VIETTEL AI RACE

## KỊCH BẢN KIỂM THỬ QA

TD447

Lần ban hành: 1

| Load test             | Thực hiện Load test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.             | network disconnect    | Dữ liệu được khôi phục toàn vẹn sau sự cố    | JMeter script       | Gửi báo cáo PDF hàng ngày   |
|-----------------------|---------------------------------------------------------------------------------------------------------------------------|-----------------------|----------------------------------------------|---------------------|-----------------------------|
| Login test            | Thực hiện Login test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.            | valid data            | Không phát hiện lỗ hổng bảo mật OWASP Top 10 | Automation Selenium | Theo chuẩn ISTQB            |
| API stress test       | Thực hiện API stress test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.       | DB corruption         | Dữ liệu được khôi phục toàn vẹn sau sự cố    | Manual test plan    | Phải log toàn bộ kết quả    |
| Data consistency test | Thực hiện Data consistency test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại. | stress load > 10k TPS | User login thành công trong <1s              | Automation Selenium | Test môi trường Pre- Prod   |
| Security scan         | Thực hiện Security scan để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất              | stress load > 10k TPS | Hệ thống chịu tải 20k TPS không gián đoạn    | Kịch bản Ansible    | Theo chuẩn ISTQB            |

<!-- image -->

## VIETTEL AI RACE

## KỊCH BẢN KIỂM THỬ QA

TD447

Lần ban hành: 1

|                       | bại.                                                                                                                      |                             |                                           |                     |                                     |
|-----------------------|---------------------------------------------------------------------------------------------------------------------------|-----------------------------|-------------------------------------------|---------------------|-------------------------------------|
| Data consistency test | Thực hiện Data consistency test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại. | DB corruption               | User login thành công trong <1s           | Kịch bản Ansible    | Phải log toàn bộ kết quả            |
| Data consistency test | Thực hiện Data consistency test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại. | API call batch 1000 request | Hệ thống chịu tải 20k TPS không gián đoạn | Automation Selenium | Gửi báo cáo PDF hàng ngày           |
| Failover test         | Thực hiện Failover test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.         | API call batch 1000 request | User login thành công trong <1s           | Kịch bản Ansible    | So sánh benchmark với release trước |
| API stress test       | Thực hiện API stress test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.       | API call batch 1000 request | Cluster failover tự động trong 5s         | JMeter script       | Theo chuẩn ISTQB                    |
| Security              | Thực hiện Security scan để kiểm thử                                                                                       | valid data                  | Dữ liệu được khôi                         | Manual test         | Test môi trường Pre-                |

<!-- image -->

## VIETTEL AI RACE

## KỊCH BẢN KIỂM THỬ QA

TD447

Lần ban hành: 1

| scan          | chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.                                     |                             | phục toàn vẹn sau sự cố                      | plan                | Prod                                |
|---------------|-------------------------------------------------------------------------------------------------------------------|-----------------------------|----------------------------------------------|---------------------|-------------------------------------|
| Failover test | Thực hiện Failover test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại. | network disconnect          | Không phát hiện lỗ hổng bảo mật OWASP Top 10 | Kịch bản Ansible    | Phải log toàn bộ kết quả            |
| Load test     | Thực hiện Load test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.     | DB corruption               | Dữ liệu được khôi phục toàn vẹn sau sự cố    | Manual test plan    | Test môi trường Pre- Prod           |
| Failover test | Thực hiện Failover test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại. | API call batch 1000 request | Cluster failover tự động trong 5s            | Kịch bản Ansible    | So sánh benchmark với release trước |
| Load test     | Thực hiện Load test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.     | DB corruption               | User login thành công trong <1s              | Automation Selenium | So sánh benchmark với release trước |

<!-- image -->

## VIETTEL AI RACE

## KỊCH BẢN KIỂM THỬ QA

TD447

Lần ban hành: 1

| Failover test          | Thực hiện Failover test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.          | DB corruption      | User login thành công trong <1s           | Manual test plan    | Test môi trường Pre- Prod           |
|------------------------|----------------------------------------------------------------------------------------------------------------------------|--------------------|-------------------------------------------|---------------------|-------------------------------------|
| Database recovery test | Thực hiện Database recovery test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại. | network disconnect | Hệ thống chịu tải 20k TPS không gián đoạn | JMeter script       | So sánh benchmark với release trước |
| Login test             | Thực hiện Login test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.             | network disconnect | Dữ liệu được khôi phục toàn vẹn sau sự cố | JMeter script       | Test môi trường Pre- Prod           |
| Database recovery test | Thực hiện Database recovery test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại. | valid data         | Cluster failover tự động trong 5s         | Automation Selenium | Test môi trường Pre- Prod           |
| Login test             | Thực hiện Login test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành                               | invalid data       | Dữ liệu được khôi phục toàn vẹn sau       | Manual test plan    | Gửi báo cáo PDF hàng ngày           |

<!-- image -->

## VIETTEL AI RACE

## KỊCH BẢN KIỂM THỬ QA

TD447

Lần ban hành: 1

|                        | công và thất bại.                                                                                                          |               | sự cố                                        |                     |                                     |
|------------------------|----------------------------------------------------------------------------------------------------------------------------|---------------|----------------------------------------------|---------------------|-------------------------------------|
| Security scan          | Thực hiện Security scan để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.          | DB corruption | Không phát hiện lỗ hổng bảo mật OWASP Top 10 | Automation Selenium | Test môi trường Pre- Prod           |
| Failover test          | Thực hiện Failover test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.          | invalid data  | Dữ liệu được khôi phục toàn vẹn sau sự cố    | Manual test plan    | Test môi trường Pre- Prod           |
| Database recovery test | Thực hiện Database recovery test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại. | valid data    | User login thành công trong <1s              | Kịch bản Ansible    | Test môi trường Pre- Prod           |
| API stress test        | Thực hiện API stress test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.        | invalid data  | Hệ thống chịu tải 20k TPS không gián đoạn    | Manual test plan    | So sánh benchmark với release trước |
| Database recovery      | Thực hiện Database recovery test để                                                                                        | valid data    | User login                                   | JMeter              | Theo chuẩn                          |

<!-- image -->

## VIETTEL AI RACE

## KỊCH BẢN KIỂM THỬ QA

TD447

Lần ban hành: 1

| test            | kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.                              |                             | thành công trong <1s                      | script              | ISTQB                               |
|-----------------|---------------------------------------------------------------------------------------------------------------------|-----------------------------|-------------------------------------------|---------------------|-------------------------------------|
| Failover test   | Thực hiện Failover test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.   | API call batch 1000 request | Hệ thống chịu tải 20k TPS không gián đoạn | Automation Selenium | So sánh benchmark với release trước |
| Load test       | Thực hiện Load test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.       | API call batch 1000 request | Dữ liệu được khôi phục toàn vẹn sau sự cố | Automation Selenium | So sánh benchmark với release trước |
| Load test       | Thực hiện Load test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.       | API call batch 1000 request | Dữ liệu được khôi phục toàn vẹn sau sự cố | JMeter script       | Gửi báo cáo PDF hàng ngày           |
| API stress test | Thực hiện API stress test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại. | network disconnect          | Cluster failover tự động trong 5s         | Kịch bản Ansible    | Phải log toàn bộ kết quả            |

<!-- image -->

## VIETTEL AI RACE

## KỊCH BẢN KIỂM THỬ QA

TD447

Lần ban hành: 1

| Failover test   | Thực hiện Failover test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.   | DB corruption               | Cluster failover tự động trong 5s         | Automation Selenium   | Gửi báo cáo PDF hàng ngày           |
|-----------------|---------------------------------------------------------------------------------------------------------------------|-----------------------------|-------------------------------------------|-----------------------|-------------------------------------|
| Security scan   | Thực hiện Security scan để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.   | DB corruption               | User login thành công trong <1s           | JMeter script         | Gửi báo cáo PDF hàng ngày           |
| Security scan   | Thực hiện Security scan để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.   | API call batch 1000 request | User login thành công trong <1s           | Automation Selenium   | So sánh benchmark với release trước |
| API stress test | Thực hiện API stress test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại. | invalid data                | Dữ liệu được khôi phục toàn vẹn sau sự cố | Manual test plan      | So sánh benchmark với release trước |
| Failover test   | Thực hiện Failover test để kiểm thử chức năng và hiệu năng của hệ thống,                                            | valid data                  | User login thành công                     | Automation Selenium   | Theo chuẩn ISTQB                    |

<!-- image -->

## VIETTEL AI RACE

## KỊCH BẢN KIỂM THỬ QA

TD447

Lần ban hành: 1

|                       | bao gồm kịch bản thành công và thất bại.                                                                                  |                       | trong <1s                                 |                  |                           |
|-----------------------|---------------------------------------------------------------------------------------------------------------------------|-----------------------|-------------------------------------------|------------------|---------------------------|
| API stress test       | Thực hiện API stress test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.       | invalid data          | Dữ liệu được khôi phục toàn vẹn sau sự cố | Manual test plan | Gửi báo cáo PDF hàng ngày |
| Data consistency test | Thực hiện Data consistency test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại. | network disconnect    | Cluster failover tự động trong 5s         | Kịch bản Ansible | Gửi báo cáo PDF hàng ngày |
| API stress test       | Thực hiện API stress test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.       | stress load > 10k TPS | Dữ liệu được khôi phục toàn vẹn sau sự cố | JMeter script    | Test môi trường Pre- Prod |
| Login test            | Thực hiện Login test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.            | stress load > 10k TPS | Hệ thống chịu tải 20k TPS không gián đoạn | Manual test plan | Test môi trường Pre- Prod |
| Data                  | Thực hiện Data                                                                                                            | DB                    | User                                      | Kịch bản         | Test môi                  |

<!-- image -->

## VIETTEL AI RACE

## KỊCH BẢN KIỂM THỬ QA

TD447

Lần ban hành: 1

| consistency test       | consistency test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.                 | corruption                  | login thành công trong <1s                | Ansible             | trường Pre- Prod          |
|------------------------|----------------------------------------------------------------------------------------------------------------------------|-----------------------------|-------------------------------------------|---------------------|---------------------------|
| Database recovery test | Thực hiện Database recovery test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại. | API call batch 1000 request | Dữ liệu được khôi phục toàn vẹn sau sự cố | Manual test plan    | Gửi báo cáo PDF hàng ngày |
| API stress test        | Thực hiện API stress test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.        | valid data                  | Dữ liệu được khôi phục toàn vẹn sau sự cố | Automation Selenium | Theo chuẩn ISTQB          |
| Data consistency test  | Thực hiện Data consistency test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.  | network disconnect          | Dữ liệu được khôi phục toàn vẹn sau sự cố | Automation Selenium | Gửi báo cáo PDF hàng ngày |
| Login test             | Thực hiện Login test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành                               | network disconnect          | Không phát hiện lỗ hổng bảo mật OWASP     | Kịch bản Ansible    | Phải log toàn bộ kết quả  |

<!-- image -->

## VIETTEL AI RACE

## KỊCH BẢN KIỂM THỬ QA

TD447

Lần ban hành: 1

|               | công và thất bại.                                                                                                 |                             | Top 10                                    |                  |                                     |
|---------------|-------------------------------------------------------------------------------------------------------------------|-----------------------------|-------------------------------------------|------------------|-------------------------------------|
| Load test     | Thực hiện Load test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.     | DB corruption               | Dữ liệu được khôi phục toàn vẹn sau sự cố | JMeter script    | Phải log toàn bộ kết quả            |
| Load test     | Thực hiện Load test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.     | valid data                  | Dữ liệu được khôi phục toàn vẹn sau sự cố | Kịch bản Ansible | Phải log toàn bộ kết quả            |
| Load test     | Thực hiện Load test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.     | stress load > 10k TPS       | User login thành công trong <1s           | Manual test plan | So sánh benchmark với release trước |
| Security scan | Thực hiện Security scan để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại. | API call batch 1000 request | Cluster failover tự động trong 5s         | Kịch bản Ansible | Test môi trường Pre- Prod           |
| Load test     | Thực hiện Load test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành                       | valid data                  | Không phát hiện lỗ hổng bảo mật OWASP     | Manual test plan | Test môi trường Pre- Prod           |

<!-- image -->

## VIETTEL AI RACE

## KỊCH BẢN KIỂM THỬ QA

TD447

Lần ban hành: 1

|                 | công và thất bại.                                                                                                   |                       | Top 10                            |                     |                           |
|-----------------|---------------------------------------------------------------------------------------------------------------------|-----------------------|-----------------------------------|---------------------|---------------------------|
| Failover test   | Thực hiện Failover test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.   | valid data            | User login thành công trong <1s   | Kịch bản Ansible    | Phải log toàn bộ kết quả  |
| API stress test | Thực hiện API stress test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại. | network disconnect    | Cluster failover tự động trong 5s | Kịch bản Ansible    | Gửi báo cáo PDF hàng ngày |
| Login test      | Thực hiện Login test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.      | invalid data          | Cluster failover tự động trong 5s | Automation Selenium | Phải log toàn bộ kết quả  |
| Load test       | Thực hiện Load test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.       | valid data            | User login thành công trong <1s   | JMeter script       | Phải log toàn bộ kết quả  |
| Load test       | Thực hiện Load test để kiểm thử chức năng và hiệu năng của hệ thống, bao                                            | stress load > 10k TPS | User login thành công             | JMeter script       | Gửi báo cáo PDF hàng ngày |

<!-- image -->

## VIETTEL AI RACE

## KỊCH BẢN KIỂM THỬ QA

TD447

Lần ban hành: 1

|                        | gồm kịch bản thành công và thất bại.                                                                                       |                   | trong <1s                                    |                  |                           |
|------------------------|----------------------------------------------------------------------------------------------------------------------------|-------------------|----------------------------------------------|------------------|---------------------------|
| Login test             | Thực hiện Login test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.             | valid data        | Hệ thống chịu tải 20k TPS không gián đoạn    | JMeter script    | Theo chuẩn ISTQB          |
| Data consistency test  | Thực hiện Data consistency test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.  | DB corruption     | Không phát hiện lỗ hổng bảo mật OWASP Top 10 | JMeter script    | Gửi báo cáo PDF hàng ngày |
| Database recovery test | Thực hiện Database recovery test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại. | DB corruption     | Hệ thống chịu tải 20k TPS không gián đoạn    | JMeter script    | Theo chuẩn ISTQB          |
| Load test              | Thực hiện Load test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.              | valid data        | Cluster failover tự động trong 5s            | Kịch bản Ansible | Phải log toàn bộ kết quả  |
| Load test              | Thực hiện Load test để kiểm thử chức năng và hiệu năng                                                                     | stress load > 10k | Không phát hiện lỗ hổng                      | JMeter script    | So sánh benchmark với     |

<!-- image -->

## VIETTEL AI RACE

## KỊCH BẢN KIỂM THỬ QA

TD447

Lần ban hành: 1

|                       | của hệ thống, bao gồm kịch bản thành công và thất bại.                                                                    | TPS                         | bảo mật OWASP Top 10                      |                     | release trước                       |
|-----------------------|---------------------------------------------------------------------------------------------------------------------------|-----------------------------|-------------------------------------------|---------------------|-------------------------------------|
| Security scan         | Thực hiện Security scan để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.         | API call batch 1000 request | User login thành công trong <1s           | JMeter script       | Test môi trường Pre- Prod           |
| Data consistency test | Thực hiện Data consistency test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại. | API call batch 1000 request | User login thành công trong <1s           | Kịch bản Ansible    | Gửi báo cáo PDF hàng ngày           |
| Load test             | Thực hiện Load test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.             | valid data                  | User login thành công trong <1s           | Manual test plan    | So sánh benchmark với release trước |
| Security scan         | Thực hiện Security scan để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.         | stress load > 10k TPS       | Dữ liệu được khôi phục toàn vẹn sau sự cố | Automation Selenium | So sánh benchmark với release trước |
| Data                  | Thực hiện Data                                                                                                            | invalid                     | User                                      | Automation          | So sánh                             |

<!-- image -->

## VIETTEL AI RACE

## KỊCH BẢN KIỂM THỬ QA

TD447

Lần ban hành: 1

| consistency test      | consistency test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.                | data                  | login thành công trong <1s                | Selenium            | benchmark với release trước         |
|-----------------------|---------------------------------------------------------------------------------------------------------------------------|-----------------------|-------------------------------------------|---------------------|-------------------------------------|
| Data consistency test | Thực hiện Data consistency test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại. | valid data            | User login thành công trong <1s           | Manual test plan    | Phải log toàn bộ kết quả            |
| Data consistency test | Thực hiện Data consistency test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại. | invalid data          | Hệ thống chịu tải 20k TPS không gián đoạn | Automation Selenium | Phải log toàn bộ kết quả            |
| Failover test         | Thực hiện Failover test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.         | DB corruption         | Dữ liệu được khôi phục toàn vẹn sau sự cố | JMeter script       | Gửi báo cáo PDF hàng ngày           |
| Login test            | Thực hiện Login test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành                              | stress load > 10k TPS | Không phát hiện lỗ hổng bảo mật OWASP     | Manual test plan    | So sánh benchmark với release trước |

<!-- image -->

## VIETTEL AI RACE

## KỊCH BẢN KIỂM THỬ QA

TD447

Lần ban hành: 1

|                       | công và thất bại.                                                                                                         |                             | Top 10                                    |                  |                                     |
|-----------------------|---------------------------------------------------------------------------------------------------------------------------|-----------------------------|-------------------------------------------|------------------|-------------------------------------|
| Security scan         | Thực hiện Security scan để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.         | stress load > 10k TPS       | Cluster failover tự động trong 5s         | Manual test plan | So sánh benchmark với release trước |
| Data consistency test | Thực hiện Data consistency test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại. | API call batch 1000 request | Dữ liệu được khôi phục toàn vẹn sau sự cố | JMeter script    | Phải log toàn bộ kết quả            |
| Security scan         | Thực hiện Security scan để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.         | DB corruption               | Cluster failover tự động trong 5s         | Manual test plan | Gửi báo cáo PDF hàng ngày           |
| Failover test         | Thực hiện Failover test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.         | valid data                  | User login thành công trong <1s           | Kịch bản Ansible | Gửi báo cáo PDF hàng ngày           |
| Database recovery     | Thực hiện Database recovery test để                                                                                       | network                     | Cluster failover                          | Manual test      | So sánh benchmark với               |

<!-- image -->

## VIETTEL AI RACE

## KỊCH BẢN KIỂM THỬ QA

TD447

Lần ban hành: 1

| test            | kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.                            | disconnect                  | tự động trong 5s                             | plan                | release trước                       |
|-----------------|-------------------------------------------------------------------------------------------------------------------|-----------------------------|----------------------------------------------|---------------------|-------------------------------------|
| Security scan   | Thực hiện Security scan để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại. | API call batch 1000 request | Cluster failover tự động trong 5s            | JMeter script       | Theo chuẩn ISTQB                    |
| Failover test   | Thực hiện Failover test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại. | network disconnect          | Không phát hiện lỗ hổng bảo mật OWASP Top 10 | Automation Selenium | Phải log toàn bộ kết quả            |
| Load test       | Thực hiện Load test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.     | valid data                  | Không phát hiện lỗ hổng bảo mật OWASP Top 10 | Kịch bản Ansible    | Gửi báo cáo PDF hàng ngày           |
| API stress test | Thực hiện API stress test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất    | API call batch 1000 request | Dữ liệu được khôi phục toàn vẹn sau sự cố    | Automation Selenium | So sánh benchmark với release trước |

<!-- image -->

## VIETTEL AI RACE

## KỊCH BẢN KIỂM THỬ QA

TD447

Lần ban hành: 1

|                        | bại.                                                                                                                       |                             |                                           |                     |                           |
|------------------------|----------------------------------------------------------------------------------------------------------------------------|-----------------------------|-------------------------------------------|---------------------|---------------------------|
| API stress test        | Thực hiện API stress test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.        | API call batch 1000 request | User login thành công trong <1s           | JMeter script       | Phải log toàn bộ kết quả  |
| Failover test          | Thực hiện Failover test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.          | invalid data                | Dữ liệu được khôi phục toàn vẹn sau sự cố | Automation Selenium | Phải log toàn bộ kết quả  |
| Load test              | Thực hiện Load test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.              | stress load > 10k TPS       | User login thành công trong <1s           | JMeter script       | Test môi trường Pre- Prod |
| Database recovery test | Thực hiện Database recovery test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại. | API call batch 1000 request | Hệ thống chịu tải 20k TPS không gián đoạn | Kịch bản Ansible    | Theo chuẩn ISTQB          |
| Load test              | Thực hiện Load test để kiểm thử chức năng và hiệu năng                                                                     | invalid data                | Dữ liệu được khôi phục toàn               | JMeter script       | Test môi trường Pre-      |

<!-- image -->

## VIETTEL AI RACE

## KỊCH BẢN KIỂM THỬ QA

TD447

Lần ban hành: 1

|                  | của hệ thống, bao gồm kịch bản thành công và thất bại.                                                              |                             | vẹn sau sự cố                             |                     | Prod                                |
|------------------|---------------------------------------------------------------------------------------------------------------------|-----------------------------|-------------------------------------------|---------------------|-------------------------------------|
| Load test        | Thực hiện Load test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.       | stress load > 10k TPS       | Cluster failover tự động trong 5s         | Manual test plan    | Gửi báo cáo PDF hàng ngày           |
| Login test       | Thực hiện Login test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.      | invalid data                | Dữ liệu được khôi phục toàn vẹn sau sự cố | Kịch bản Ansible    | Theo chuẩn ISTQB                    |
| API stress test  | Thực hiện API stress test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại. | API call batch 1000 request | Dữ liệu được khôi phục toàn vẹn sau sự cố | Automation Selenium | Gửi báo cáo PDF hàng ngày           |
| API stress test  | Thực hiện API stress test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại. | stress load > 10k TPS       | Hệ thống chịu tải 20k TPS không gián đoạn | JMeter script       | So sánh benchmark với release trước |
| Data consistency | Thực hiện Data consistency test để                                                                                  | API call batch              | Không phát hiện                           | Kịch bản            | Theo chuẩn                          |

<!-- image -->

## VIETTEL AI RACE

## KỊCH BẢN KIỂM THỬ QA

TD447

Lần ban hành: 1

| test                   | kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.                                     | 1000 request          | lỗ hổng bảo mật OWASP Top 10                 | Ansible             | ISTQB                               |
|------------------------|----------------------------------------------------------------------------------------------------------------------------|-----------------------|----------------------------------------------|---------------------|-------------------------------------|
| Login test             | Thực hiện Login test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.             | valid data            | Dữ liệu được khôi phục toàn vẹn sau sự cố    | JMeter script       | Theo chuẩn ISTQB                    |
| Database recovery test | Thực hiện Database recovery test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại. | stress load > 10k TPS | User login thành công trong <1s              | Manual test plan    | So sánh benchmark với release trước |
| Load test              | Thực hiện Load test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.              | stress load > 10k TPS | User login thành công trong <1s              | Automation Selenium | Theo chuẩn ISTQB                    |
| Security scan          | Thực hiện Security scan để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.          | stress load > 10k TPS | Không phát hiện lỗ hổng bảo mật OWASP Top 10 | Manual test plan    | Theo chuẩn ISTQB                    |

<!-- image -->

## VIETTEL AI RACE

## KỊCH BẢN KIỂM THỬ QA

TD447

Lần ban hành: 1

| Data consistency test   | Thực hiện Data consistency test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.   | stress load > 10k TPS   | Hệ thống chịu tải 20k TPS không gián đoạn    | Kịch bản Ansible   | Phải log toàn bộ kết quả   |
|-------------------------|-----------------------------------------------------------------------------------------------------------------------------|-------------------------|----------------------------------------------|--------------------|----------------------------|
| Login test              | Thực hiện Login test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.              | stress load > 10k TPS   | Dữ liệu được khôi phục toàn vẹn sau sự cố    | Manual test plan   | Phải log toàn bộ kết quả   |
| Data consistency test   | Thực hiện Data consistency test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.   | invalid data            | Không phát hiện lỗ hổng bảo mật OWASP Top 10 | Manual test plan   | Test môi trường Pre- Prod  |
| API stress test         | Thực hiện API stress test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.         | network disconnect      | Dữ liệu được khôi phục toàn vẹn sau sự cố    | Manual test plan   | Gửi báo cáo PDF hàng ngày  |
| Database recovery test  | Thực hiện Database recovery test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch                              | invalid data            | Dữ liệu được khôi phục toàn vẹn sau          | JMeter script      | Theo chuẩn ISTQB           |

<!-- image -->

## VIETTEL AI RACE

## KỊCH BẢN KIỂM THỬ QA

TD447

Lần ban hành: 1

|                        | bản thành công và thất bại.                                                                                                |                             | sự cố                                     |                  |                           |
|------------------------|----------------------------------------------------------------------------------------------------------------------------|-----------------------------|-------------------------------------------|------------------|---------------------------|
| Database recovery test | Thực hiện Database recovery test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại. | API call batch 1000 request | User login thành công trong <1s           | Manual test plan | Test môi trường Pre- Prod |
| Login test             | Thực hiện Login test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.             | API call batch 1000 request | Hệ thống chịu tải 20k TPS không gián đoạn | JMeter script    | Gửi báo cáo PDF hàng ngày |
| Database recovery test | Thực hiện Database recovery test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại. | invalid data                | Dữ liệu được khôi phục toàn vẹn sau sự cố | Manual test plan | Phải log toàn bộ kết quả  |
| Security scan          | Thực hiện Security scan để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.          | network disconnect          | User login thành công trong <1s           | JMeter script    | Phải log toàn bộ kết quả  |
| Failover               | Thực hiện Failover test để kiểm thử                                                                                        | DB                          | Không phát hiện                           | Automation       | Theo chuẩn                |

<!-- image -->

## VIETTEL AI RACE

## KỊCH BẢN KIỂM THỬ QA

TD447

Lần ban hành: 1

| test            | chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.                                     | corruption                  | lỗ hổng bảo mật OWASP Top 10                 | Selenium            | ISTQB                               |
|-----------------|-------------------------------------------------------------------------------------------------------------------|-----------------------------|----------------------------------------------|---------------------|-------------------------------------|
| Load test       | Thực hiện Load test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.     | stress load > 10k TPS       | Không phát hiện lỗ hổng bảo mật OWASP Top 10 | Automation Selenium | Theo chuẩn ISTQB                    |
| Failover test   | Thực hiện Failover test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại. | valid data                  | Không phát hiện lỗ hổng bảo mật OWASP Top 10 | JMeter script       | So sánh benchmark với release trước |
| Security scan   | Thực hiện Security scan để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại. | API call batch 1000 request | Cluster failover tự động trong 5s            | Manual test plan    | Test môi trường Pre- Prod           |
| API stress test | Thực hiện API stress test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất    | network disconnect          | Không phát hiện lỗ hổng bảo mật OWASP Top 10 | Manual test plan    | So sánh benchmark với release trước |

<!-- image -->

## VIETTEL AI RACE

## KỊCH BẢN KIỂM THỬ QA

TD447

Lần ban hành: 1

|                   | bại.                                                                                                                |                             |                                              |                  |                           |
|-------------------|---------------------------------------------------------------------------------------------------------------------|-----------------------------|----------------------------------------------|------------------|---------------------------|
| API stress test   | Thực hiện API stress test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại. | API call batch 1000 request | User login thành công trong <1s              | JMeter script    | Gửi báo cáo PDF hàng ngày |
| Failover test     | Thực hiện Failover test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.   | API call batch 1000 request | Dữ liệu được khôi phục toàn vẹn sau sự cố    | JMeter script    | Phải log toàn bộ kết quả  |
| Failover test     | Thực hiện Failover test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.   | API call batch 1000 request | Dữ liệu được khôi phục toàn vẹn sau sự cố    | Kịch bản Ansible | Theo chuẩn ISTQB          |
| Login test        | Thực hiện Login test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.      | valid data                  | Không phát hiện lỗ hổng bảo mật OWASP Top 10 | Manual test plan | Test môi trường Pre- Prod |
| Database recovery | Thực hiện Database recovery test để kiểm thử chức năng                                                              | network disconnect          | Dữ liệu được khôi phục toàn                  | Kịch bản Ansible | Test môi trường Pre-      |

<!-- image -->

## VIETTEL AI RACE

## KỊCH BẢN KIỂM THỬ QA

TD447

Lần ban hành: 1

| test                   | và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.                                                        |                    | vẹn sau sự cố                             |                  | Prod                                |
|------------------------|----------------------------------------------------------------------------------------------------------------------------|--------------------|-------------------------------------------|------------------|-------------------------------------|
| Database recovery test | Thực hiện Database recovery test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại. | network disconnect | Hệ thống chịu tải 20k TPS không gián đoạn | Kịch bản Ansible | Gửi báo cáo PDF hàng ngày           |
| Security scan          | Thực hiện Security scan để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.          | invalid data       | Hệ thống chịu tải 20k TPS không gián đoạn | JMeter script    | So sánh benchmark với release trước |
| Load test              | Thực hiện Load test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.              | network disconnect | Cluster failover tự động trong 5s         | Kịch bản Ansible | Phải log toàn bộ kết quả            |
| Security scan          | Thực hiện Security scan để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.          | valid data         | Dữ liệu được khôi phục toàn vẹn sau sự cố | JMeter script    | Test môi trường Pre- Prod           |

<!-- image -->

## VIETTEL AI RACE

## KỊCH BẢN KIỂM THỬ QA

TD447

Lần ban hành: 1

| Load test              | Thực hiện Load test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.              | valid data            | Hệ thống chịu tải 20k TPS không gián đoạn    | Automation Selenium   | Gửi báo cáo PDF hàng ngày           |
|------------------------|----------------------------------------------------------------------------------------------------------------------------|-----------------------|----------------------------------------------|-----------------------|-------------------------------------|
| Database recovery test | Thực hiện Database recovery test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại. | stress load > 10k TPS | User login thành công trong <1s              | Automation Selenium   | So sánh benchmark với release trước |
| API stress test        | Thực hiện API stress test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.        | valid data            | Dữ liệu được khôi phục toàn vẹn sau sự cố    | JMeter script         | So sánh benchmark với release trước |
| Failover test          | Thực hiện Failover test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.          | stress load > 10k TPS | Không phát hiện lỗ hổng bảo mật OWASP Top 10 | Manual test plan      | Test môi trường Pre- Prod           |
| Load test              | Thực hiện Load test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành                                | stress load > 10k TPS | Không phát hiện lỗ hổng bảo mật OWASP        | Kịch bản Ansible      | Phải log toàn bộ kết quả            |

<!-- image -->

## VIETTEL AI RACE

## KỊCH BẢN KIỂM THỬ QA

TD447

Lần ban hành: 1

|                        | công và thất bại.                                                                                                          |                             | Top 10                                    |                  |                                     |
|------------------------|----------------------------------------------------------------------------------------------------------------------------|-----------------------------|-------------------------------------------|------------------|-------------------------------------|
| Data consistency test  | Thực hiện Data consistency test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.  | invalid data                | User login thành công trong <1s           | JMeter script    | Phải log toàn bộ kết quả            |
| Load test              | Thực hiện Load test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.              | network disconnect          | Dữ liệu được khôi phục toàn vẹn sau sự cố | JMeter script    | Theo chuẩn ISTQB                    |
| Database recovery test | Thực hiện Database recovery test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại. | network disconnect          | Dữ liệu được khôi phục toàn vẹn sau sự cố | JMeter script    | So sánh benchmark với release trước |
| Security scan          | Thực hiện Security scan để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.          | API call batch 1000 request | Dữ liệu được khôi phục toàn vẹn sau sự cố | Manual test plan | Phải log toàn bộ kết quả            |
| Failover test          | Thực hiện Failover test để kiểm thử chức năng và hiệu                                                                      | network disconnect          | Cluster failover tự động                  | Manual test plan | So sánh benchmark với               |

<!-- image -->

## VIETTEL AI RACE

## KỊCH BẢN KIỂM THỬ QA

TD447

Lần ban hành: 1

|                        | năng của hệ thống, bao gồm kịch bản thành công và thất bại.                                                               |                             | trong 5s                                     |                     | release trước                       |
|------------------------|---------------------------------------------------------------------------------------------------------------------------|-----------------------------|----------------------------------------------|---------------------|-------------------------------------|
| Data consistency test  | Thực hiện Data consistency test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại. | network disconnect          | Hệ thống chịu tải 20k TPS không gián đoạn    | Automation Selenium | So sánh benchmark với release trước |
| Failover test          | Thực hiện Failover test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.         | network disconnect          | Dữ liệu được khôi phục toàn vẹn sau sự cố    | Kịch bản Ansible    | Gửi báo cáo PDF hàng ngày           |
| Data consistency test  | Thực hiện Data consistency test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại. | invalid data                | Không phát hiện lỗ hổng bảo mật OWASP Top 10 | Kịch bản Ansible    | So sánh benchmark với release trước |
| Database recovery test | Thực hiện Database recovery test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và          | API call batch 1000 request | User login thành công trong <1s              | Automation Selenium | Test môi trường Pre- Prod           |

<!-- image -->

## VIETTEL AI RACE

## KỊCH BẢN KIỂM THỬ QA

TD447

Lần ban hành: 1

|                        | thất bại.                                                                                                                  |                             |                                              |                     |                                     |
|------------------------|----------------------------------------------------------------------------------------------------------------------------|-----------------------------|----------------------------------------------|---------------------|-------------------------------------|
| Security scan          | Thực hiện Security scan để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.          | valid data                  | Dữ liệu được khôi phục toàn vẹn sau sự cố    | Automation Selenium | Theo chuẩn ISTQB                    |
| Database recovery test | Thực hiện Database recovery test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại. | API call batch 1000 request | Hệ thống chịu tải 20k TPS không gián đoạn    | JMeter script       | Gửi báo cáo PDF hàng ngày           |
| Failover test          | Thực hiện Failover test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.          | network disconnect          | Không phát hiện lỗ hổng bảo mật OWASP Top 10 | Automation Selenium | Test môi trường Pre- Prod           |
| Data consistency test  | Thực hiện Data consistency test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.  | network disconnect          | Dữ liệu được khôi phục toàn vẹn sau sự cố    | Manual test plan    | So sánh benchmark với release trước |
| Security               | Thực hiện Security scan để kiểm thử                                                                                        | invalid                     | Hệ thống chịu tải                            | Kịch bản            | Test môi trường Pre-                |

<!-- image -->

## VIETTEL AI RACE

## KỊCH BẢN KIỂM THỬ QA

TD447

Lần ban hành: 1

| scan                   | chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.                                       | data                  | 20k TPS không gián đoạn                      | Ansible          | Prod                                |
|------------------------|---------------------------------------------------------------------------------------------------------------------|-----------------------|----------------------------------------------|------------------|-------------------------------------|
| Security scan          | Thực hiện Security scan để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.   | DB corruption         | User login thành công trong <1s              | Kịch bản Ansible | Test môi trường Pre- Prod           |
| Login test             | Thực hiện Login test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.      | stress load > 10k TPS | Hệ thống chịu tải 20k TPS không gián đoạn    | JMeter script    | Test môi trường Pre- Prod           |
| API stress test        | Thực hiện API stress test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại. | stress load > 10k TPS | Không phát hiện lỗ hổng bảo mật OWASP Top 10 | JMeter script    | So sánh benchmark với release trước |
| Database recovery test | Thực hiện Database recovery test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và    | network disconnect    | Cluster failover tự động trong 5s            | Kịch bản Ansible | Phải log toàn bộ kết quả            |

<!-- image -->

## VIETTEL AI RACE

## KỊCH BẢN KIỂM THỬ QA

TD447

Lần ban hành: 1

|                        | thất bại.                                                                                                         |                             |                                              |                     |                                     |
|------------------------|-------------------------------------------------------------------------------------------------------------------|-----------------------------|----------------------------------------------|---------------------|-------------------------------------|
| Failover test          | Thực hiện Failover test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại. | API call batch 1000 request | Không phát hiện lỗ hổng bảo mật OWASP Top 10 | JMeter script       | So sánh benchmark với release trước |
| Login test             | Thực hiện Login test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.    | DB corruption               | Cluster failover tự động trong 5s            | Manual test plan    | Test môi trường Pre- Prod           |
| Security scan          | Thực hiện Security scan để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại. | stress load > 10k TPS       | Hệ thống chịu tải 20k TPS không gián đoạn    | Kịch bản Ansible    | Test môi trường Pre- Prod           |
| Login test             | Thực hiện Login test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.    | stress load > 10k TPS       | Dữ liệu được khôi phục toàn vẹn sau sự cố    | Automation Selenium | So sánh benchmark với release trước |
| Database recovery test | Thực hiện Database recovery test để kiểm thử chức năng và hiệu năng của hệ                                        | valid data                  | User login thành công                        | Manual test plan    | Phải log toàn bộ kết quả            |

<!-- image -->

## VIETTEL AI RACE

## KỊCH BẢN KIỂM THỬ QA

TD447

Lần ban hành: 1

|                 | thống, bao gồm kịch bản thành công và thất bại.                                                                     |                             | trong <1s                                 |                     |                                     |
|-----------------|---------------------------------------------------------------------------------------------------------------------|-----------------------------|-------------------------------------------|---------------------|-------------------------------------|
| API stress test | Thực hiện API stress test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại. | invalid data                | Hệ thống chịu tải 20k TPS không gián đoạn | JMeter script       | So sánh benchmark với release trước |
| Security scan   | Thực hiện Security scan để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.   | network disconnect          | Dữ liệu được khôi phục toàn vẹn sau sự cố | Automation Selenium | Gửi báo cáo PDF hàng ngày           |
| Failover test   | Thực hiện Failover test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.   | invalid data                | Hệ thống chịu tải 20k TPS không gián đoạn | Kịch bản Ansible    | Theo chuẩn ISTQB                    |
| Login test      | Thực hiện Login test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.      | API call batch 1000 request | Dữ liệu được khôi phục toàn vẹn sau sự cố | Manual test plan    | Theo chuẩn ISTQB                    |

<!-- image -->

## VIETTEL AI RACE

## KỊCH BẢN KIỂM THỬ QA

TD447

Lần ban hành: 1

| Login test             | Thực hiện Login test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.             | DB corruption         | Dữ liệu được khôi phục toàn vẹn sau sự cố    | Manual test plan    | So sánh benchmark với release trước   |
|------------------------|----------------------------------------------------------------------------------------------------------------------------|-----------------------|----------------------------------------------|---------------------|---------------------------------------|
| Login test             | Thực hiện Login test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.             | DB corruption         | Dữ liệu được khôi phục toàn vẹn sau sự cố    | JMeter script       | Phải log toàn bộ kết quả              |
| Security scan          | Thực hiện Security scan để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.          | network disconnect    | Không phát hiện lỗ hổng bảo mật OWASP Top 10 | Automation Selenium | Gửi báo cáo PDF hàng ngày             |
| Database recovery test | Thực hiện Database recovery test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại. | stress load > 10k TPS | Cluster failover tự động trong 5s            | Automation Selenium | Gửi báo cáo PDF hàng ngày             |
| Login test             | Thực hiện Login test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành                               | invalid data          | User login thành công trong <1s              | Automation Selenium | Phải log toàn bộ kết quả              |

<!-- image -->

## VIETTEL AI RACE

## KỊCH BẢN KIỂM THỬ QA

TD447

Lần ban hành: 1

|                       | công và thất bại.                                                                                                         |                       |                                              |                  |                                     |
|-----------------------|---------------------------------------------------------------------------------------------------------------------------|-----------------------|----------------------------------------------|------------------|-------------------------------------|
| Data consistency test | Thực hiện Data consistency test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại. | network disconnect    | User login thành công trong <1s              | Manual test plan | Phải log toàn bộ kết quả            |
| Data consistency test | Thực hiện Data consistency test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại. | valid data            | Hệ thống chịu tải 20k TPS không gián đoạn    | Kịch bản Ansible | Test môi trường Pre- Prod           |
| Load test             | Thực hiện Load test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.             | stress load > 10k TPS | Dữ liệu được khôi phục toàn vẹn sau sự cố    | JMeter script    | So sánh benchmark với release trước |
| Failover test         | Thực hiện Failover test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.         | DB corruption         | Không phát hiện lỗ hổng bảo mật OWASP Top 10 | Kịch bản Ansible | Test môi trường Pre- Prod           |
| Load test             | Thực hiện Load test để kiểm thử chức năng và hiệu năng                                                                    | stress load > 10k     | User login thành                             | JMeter script    | So sánh benchmark với               |

<!-- image -->

## VIETTEL AI RACE

## KỊCH BẢN KIỂM THỬ QA

TD447

Lần ban hành: 1

|                 | của hệ thống, bao gồm kịch bản thành công và thất bại.                                                              | TPS                | công trong <1s                               |                  | release trước             |
|-----------------|---------------------------------------------------------------------------------------------------------------------|--------------------|----------------------------------------------|------------------|---------------------------|
| Security scan   | Thực hiện Security scan để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.   | network disconnect | Cluster failover tự động trong 5s            | Manual test plan | Phải log toàn bộ kết quả  |
| Login test      | Thực hiện Login test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.      | DB corruption      | Không phát hiện lỗ hổng bảo mật OWASP Top 10 | JMeter script    | Gửi báo cáo PDF hàng ngày |
| Failover test   | Thực hiện Failover test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.   | invalid data       | Không phát hiện lỗ hổng bảo mật OWASP Top 10 | Kịch bản Ansible | Theo chuẩn ISTQB          |
| API stress test | Thực hiện API stress test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại. | network disconnect | User login thành công trong <1s              | Kịch bản Ansible | Test môi trường Pre- Prod |

<!-- image -->

## VIETTEL AI RACE

## KỊCH BẢN KIỂM THỬ QA

TD447

Lần ban hành: 1

| Load test              | Thực hiện Load test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.              | stress load > 10k TPS       | Hệ thống chịu tải 20k TPS không gián đoạn    | JMeter script       | Theo chuẩn ISTQB          |
|------------------------|----------------------------------------------------------------------------------------------------------------------------|-----------------------------|----------------------------------------------|---------------------|---------------------------|
| Load test              | Thực hiện Load test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.              | API call batch 1000 request | Không phát hiện lỗ hổng bảo mật OWASP Top 10 | Manual test plan    | Gửi báo cáo PDF hàng ngày |
| Database recovery test | Thực hiện Database recovery test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại. | stress load > 10k TPS       | Dữ liệu được khôi phục toàn vẹn sau sự cố    | Kịch bản Ansible    | Gửi báo cáo PDF hàng ngày |
| Data consistency test  | Thực hiện Data consistency test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.  | valid data                  | Cluster failover tự động trong 5s            | Kịch bản Ansible    | Phải log toàn bộ kết quả  |
| Database recovery test | Thực hiện Database recovery test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và           | invalid data                | Dữ liệu được khôi phục toàn vẹn sau sự cố    | Automation Selenium | Test môi trường Pre- Prod |

<!-- image -->

## VIETTEL AI RACE

## KỊCH BẢN KIỂM THỬ QA

TD447

Lần ban hành: 1

|                        | thất bại.                                                                                                                  |                             |                                              |                  |                           |
|------------------------|----------------------------------------------------------------------------------------------------------------------------|-----------------------------|----------------------------------------------|------------------|---------------------------|
| API stress test        | Thực hiện API stress test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.        | valid data                  | Không phát hiện lỗ hổng bảo mật OWASP Top 10 | Manual test plan | Test môi trường Pre- Prod |
| Database recovery test | Thực hiện Database recovery test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại. | valid data                  | Hệ thống chịu tải 20k TPS không gián đoạn    | Kịch bản Ansible | Gửi báo cáo PDF hàng ngày |
| Data consistency test  | Thực hiện Data consistency test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.  | API call batch 1000 request | Hệ thống chịu tải 20k TPS không gián đoạn    | Kịch bản Ansible | Gửi báo cáo PDF hàng ngày |
| Login test             | Thực hiện Login test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.             | valid data                  | Dữ liệu được khôi phục toàn vẹn sau sự cố    | Manual test plan | Phải log toàn bộ kết quả  |
| Security scan          | Thực hiện Security scan để kiểm thử chức năng và hiệu                                                                      | API call batch 1000         | User login thành                             | Kịch bản Ansible | Phải log toàn bộ kết quả  |

<!-- image -->

## VIETTEL AI RACE

## KỊCH BẢN KIỂM THỬ QA

TD447

Lần ban hành: 1

|                       | năng của hệ thống, bao gồm kịch bản thành công và thất bại.                                                               | request                     | công trong <1s                            |                     |                                     |
|-----------------------|---------------------------------------------------------------------------------------------------------------------------|-----------------------------|-------------------------------------------|---------------------|-------------------------------------|
| Failover test         | Thực hiện Failover test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.         | DB corruption               | Dữ liệu được khôi phục toàn vẹn sau sự cố | Automation Selenium | Phải log toàn bộ kết quả            |
| API stress test       | Thực hiện API stress test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.       | valid data                  | Dữ liệu được khôi phục toàn vẹn sau sự cố | Automation Selenium | Test môi trường Pre- Prod           |
| Load test             | Thực hiện Load test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.             | API call batch 1000 request | Dữ liệu được khôi phục toàn vẹn sau sự cố | Automation Selenium | Test môi trường Pre- Prod           |
| Data consistency test | Thực hiện Data consistency test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại. | API call batch 1000 request | Cluster failover tự động trong 5s         | Automation Selenium | So sánh benchmark với release trước |

<!-- image -->

## VIETTEL AI RACE

## KỊCH BẢN KIỂM THỬ QA

TD447

Lần ban hành: 1

| Load test              | Thực hiện Load test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.              | network disconnect    | Cluster failover tự động trong 5s            | Manual test plan    | Gửi báo cáo PDF hàng ngày           |
|------------------------|----------------------------------------------------------------------------------------------------------------------------|-----------------------|----------------------------------------------|---------------------|-------------------------------------|
| API stress test        | Thực hiện API stress test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.        | stress load > 10k TPS | Hệ thống chịu tải 20k TPS không gián đoạn    | Kịch bản Ansible    | Gửi báo cáo PDF hàng ngày           |
| Login test             | Thực hiện Login test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.             | stress load > 10k TPS | Không phát hiện lỗ hổng bảo mật OWASP Top 10 | Automation Selenium | So sánh benchmark với release trước |
| Database recovery test | Thực hiện Database recovery test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại. | valid data            | User login thành công trong <1s              | Automation Selenium | Test môi trường Pre- Prod           |
| API stress test        | Thực hiện API stress test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất             | invalid data          | Hệ thống chịu tải 20k TPS không gián đoạn    | Kịch bản Ansible    | Phải log toàn bộ kết quả            |

<!-- image -->

## VIETTEL AI RACE

## KỊCH BẢN KIỂM THỬ QA

TD447

Lần ban hành: 1

|                        | bại.                                                                                                                       |                       |                                           |                     |                                     |
|------------------------|----------------------------------------------------------------------------------------------------------------------------|-----------------------|-------------------------------------------|---------------------|-------------------------------------|
| Data consistency test  | Thực hiện Data consistency test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.  | valid data            | Dữ liệu được khôi phục toàn vẹn sau sự cố | Kịch bản Ansible    | Test môi trường Pre- Prod           |
| API stress test        | Thực hiện API stress test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.        | DB corruption         | Cluster failover tự động trong 5s         | Manual test plan    | So sánh benchmark với release trước |
| Data consistency test  | Thực hiện Data consistency test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.  | DB corruption         | Dữ liệu được khôi phục toàn vẹn sau sự cố | Manual test plan    | Theo chuẩn ISTQB                    |
| Database recovery test | Thực hiện Database recovery test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại. | stress load > 10k TPS | Hệ thống chịu tải 20k TPS không gián đoạn | Automation Selenium | Phải log toàn bộ kết quả            |
| Load test              | Thực hiện Load test để kiểm thử chức                                                                                       | stress load > 10k     | Hệ thống chịu tải                         | Automation          | Phải log toàn                       |

<!-- image -->

## VIETTEL AI RACE

## KỊCH BẢN KIỂM THỬ QA

TD447

Lần ban hành: 1

|                        | năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.                                                   | TPS                | 20k TPS không gián đoạn                      | Selenium         | bộ kết quả                |
|------------------------|----------------------------------------------------------------------------------------------------------------------------|--------------------|----------------------------------------------|------------------|---------------------------|
| Database recovery test | Thực hiện Database recovery test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại. | network disconnect | Dữ liệu được khôi phục toàn vẹn sau sự cố    | Kịch bản Ansible | Gửi báo cáo PDF hàng ngày |
| Load test              | Thực hiện Load test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.              | DB corruption      | Cluster failover tự động trong 5s            | JMeter script    | Phải log toàn bộ kết quả  |
| Failover test          | Thực hiện Failover test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.          | DB corruption      | Cluster failover tự động trong 5s            | Kịch bản Ansible | Gửi báo cáo PDF hàng ngày |
| Login test             | Thực hiện Login test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.             | valid data         | Không phát hiện lỗ hổng bảo mật OWASP Top 10 | JMeter script    | Phải log toàn bộ kết quả  |

<!-- image -->

## VIETTEL AI RACE

## KỊCH BẢN KIỂM THỬ QA

TD447

Lần ban hành: 1

| Login test             | Thực hiện Login test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.             | stress load > 10k TPS   | Hệ thống chịu tải 20k TPS không gián đoạn   | JMeter script       | Phải log toàn bộ kết quả   |
|------------------------|----------------------------------------------------------------------------------------------------------------------------|-------------------------|---------------------------------------------|---------------------|----------------------------|
| Database recovery test | Thực hiện Database recovery test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại. | stress load > 10k TPS   | Dữ liệu được khôi phục toàn vẹn sau sự cố   | Kịch bản Ansible    | Test môi trường Pre- Prod  |
| Login test             | Thực hiện Login test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.             | valid data              | Hệ thống chịu tải 20k TPS không gián đoạn   | Automation Selenium | Phải log toàn bộ kết quả   |
| Load test              | Thực hiện Load test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.              | valid data              | User login thành công trong <1s             | Manual test plan    | Theo chuẩn ISTQB           |
| Data consistency test  | Thực hiện Data consistency test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và            | invalid data            | Cluster failover tự động trong 5s           | JMeter script       | Theo chuẩn ISTQB           |

<!-- image -->

## VIETTEL AI RACE

## KỊCH BẢN KIỂM THỬ QA

TD447

Lần ban hành: 1

|                        | thất bại.                                                                                                                  |                             |                                              |                  |                          |
|------------------------|----------------------------------------------------------------------------------------------------------------------------|-----------------------------|----------------------------------------------|------------------|--------------------------|
| Database recovery test | Thực hiện Database recovery test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại. | stress load > 10k TPS       | Dữ liệu được khôi phục toàn vẹn sau sự cố    | JMeter script    | Theo chuẩn ISTQB         |
| Database recovery test | Thực hiện Database recovery test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại. | API call batch 1000 request | Không phát hiện lỗ hổng bảo mật OWASP Top 10 | Kịch bản Ansible | Phải log toàn bộ kết quả |
| API stress test        | Thực hiện API stress test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.        | invalid data                | Dữ liệu được khôi phục toàn vẹn sau sự cố    | Kịch bản Ansible | Phải log toàn bộ kết quả |
| Database recovery test | Thực hiện Database recovery test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại. | valid data                  | Hệ thống chịu tải 20k TPS không gián đoạn    | Manual test plan | Phải log toàn bộ kết quả |
| Load test              | Thực hiện Load test để kiểm thử chức                                                                                       | invalid                     | Hệ thống chịu tải                            | Kịch bản         | Phải log toàn            |

<!-- image -->

## VIETTEL AI RACE

## KỊCH BẢN KIỂM THỬ QA

TD447

Lần ban hành: 1

|                        | năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.                                                   | data                        | 20k TPS không gián đoạn                   | Ansible          | bộ kết quả                          |
|------------------------|----------------------------------------------------------------------------------------------------------------------------|-----------------------------|-------------------------------------------|------------------|-------------------------------------|
| API stress test        | Thực hiện API stress test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.        | DB corruption               | Hệ thống chịu tải 20k TPS không gián đoạn | Kịch bản Ansible | Phải log toàn bộ kết quả            |
| Database recovery test | Thực hiện Database recovery test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại. | DB corruption               | Dữ liệu được khôi phục toàn vẹn sau sự cố | Manual test plan | Gửi báo cáo PDF hàng ngày           |
| Login test             | Thực hiện Login test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.             | network disconnect          | Hệ thống chịu tải 20k TPS không gián đoạn | JMeter script    | Theo chuẩn ISTQB                    |
| Load test              | Thực hiện Load test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.              | API call batch 1000 request | Dữ liệu được khôi phục toàn vẹn sau sự cố | Kịch bản Ansible | So sánh benchmark với release trước |

<!-- image -->

## VIETTEL AI RACE

## KỊCH BẢN KIỂM THỬ QA

TD447

Lần ban hành: 1

| Login test      | Thực hiện Login test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.      | network disconnect    | User login thành công trong <1s           | JMeter script       | Gửi báo cáo PDF hàng ngày           |
|-----------------|---------------------------------------------------------------------------------------------------------------------|-----------------------|-------------------------------------------|---------------------|-------------------------------------|
| API stress test | Thực hiện API stress test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại. | valid data            | Cluster failover tự động trong 5s         | Automation Selenium | Phải log toàn bộ kết quả            |
| Failover test   | Thực hiện Failover test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.   | DB corruption         | Hệ thống chịu tải 20k TPS không gián đoạn | Manual test plan    | Test môi trường Pre- Prod           |
| Failover test   | Thực hiện Failover test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.   | stress load > 10k TPS | User login thành công trong <1s           | Automation Selenium | Phải log toàn bộ kết quả            |
| Security scan   | Thực hiện Security scan để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản                           | invalid data          | Không phát hiện lỗ hổng bảo mật OWASP     | Kịch bản Ansible    | So sánh benchmark với release trước |

<!-- image -->

## VIETTEL AI RACE

## KỊCH BẢN KIỂM THỬ QA

TD447

Lần ban hành: 1

|                       | thành công và thất bại.                                                                                                   |                             | Top 10                                    |                  |                                     |
|-----------------------|---------------------------------------------------------------------------------------------------------------------------|-----------------------------|-------------------------------------------|------------------|-------------------------------------|
| Data consistency test | Thực hiện Data consistency test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại. | API call batch 1000 request | Hệ thống chịu tải 20k TPS không gián đoạn | JMeter script    | So sánh benchmark với release trước |
| Data consistency test | Thực hiện Data consistency test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại. | network disconnect          | User login thành công trong <1s           | Kịch bản Ansible | So sánh benchmark với release trước |
| Failover test         | Thực hiện Failover test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.         | invalid data                | Dữ liệu được khôi phục toàn vẹn sau sự cố | JMeter script    | Gửi báo cáo PDF hàng ngày           |
| Load test             | Thực hiện Load test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.             | valid data                  | Hệ thống chịu tải 20k TPS không gián đoạn | Manual test plan | So sánh benchmark với release trước |
| Login test            | Thực hiện Login test để kiểm thử chức                                                                                     | API call batch              | Cluster failover                          | Kịch bản         | So sánh benchmark với               |

<!-- image -->

## VIETTEL AI RACE

## KỊCH BẢN KIỂM THỬ QA

TD447

Lần ban hành: 1

|                        | năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.                                                   | 1000 request                | tự động trong 5s                          | Ansible          | release trước                       |
|------------------------|----------------------------------------------------------------------------------------------------------------------------|-----------------------------|-------------------------------------------|------------------|-------------------------------------|
| Database recovery test | Thực hiện Database recovery test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại. | network disconnect          | Hệ thống chịu tải 20k TPS không gián đoạn | Kịch bản Ansible | So sánh benchmark với release trước |
| Failover test          | Thực hiện Failover test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.          | valid data                  | Dữ liệu được khôi phục toàn vẹn sau sự cố | Manual test plan | Gửi báo cáo PDF hàng ngày           |
| Security scan          | Thực hiện Security scan để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.          | API call batch 1000 request | Hệ thống chịu tải 20k TPS không gián đoạn | JMeter script    | Phải log toàn bộ kết quả            |
| Data consistency test  | Thực hiện Data consistency test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và            | network disconnect          | Hệ thống chịu tải 20k TPS không gián đoạn | Kịch bản Ansible | Test môi trường Pre- Prod           |

<!-- image -->

## VIETTEL AI RACE

## KỊCH BẢN KIỂM THỬ QA

TD447

Lần ban hành: 1

|                        | thất bại.                                                                                                                  |                             |                                              |                     |                                     |
|------------------------|----------------------------------------------------------------------------------------------------------------------------|-----------------------------|----------------------------------------------|---------------------|-------------------------------------|
| Database recovery test | Thực hiện Database recovery test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại. | stress load > 10k TPS       | Dữ liệu được khôi phục toàn vẹn sau sự cố    | Manual test plan    | Gửi báo cáo PDF hàng ngày           |
| Data consistency test  | Thực hiện Data consistency test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.  | valid data                  | User login thành công trong <1s              | Automation Selenium | So sánh benchmark với release trước |
| Login test             | Thực hiện Login test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.             | invalid data                | User login thành công trong <1s              | Kịch bản Ansible    | So sánh benchmark với release trước |
| Security scan          | Thực hiện Security scan để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.          | API call batch 1000 request | Không phát hiện lỗ hổng bảo mật OWASP Top 10 | Kịch bản Ansible    | Theo chuẩn ISTQB                    |
| Failover test          | Thực hiện Failover test để kiểm thử chức năng và hiệu                                                                      | valid data                  | Không phát hiện lỗ hổng                      | Manual test plan    | So sánh benchmark với               |

<!-- image -->

## VIETTEL AI RACE

## KỊCH BẢN KIỂM THỬ QA

TD447

Lần ban hành: 1

|                        | năng của hệ thống, bao gồm kịch bản thành công và thất bại.                                                                |                       | bảo mật OWASP Top 10                      |                     | release trước                       |
|------------------------|----------------------------------------------------------------------------------------------------------------------------|-----------------------|-------------------------------------------|---------------------|-------------------------------------|
| Database recovery test | Thực hiện Database recovery test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại. | invalid data          | Dữ liệu được khôi phục toàn vẹn sau sự cố | Manual test plan    | So sánh benchmark với release trước |
| Failover test          | Thực hiện Failover test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.          | stress load > 10k TPS | User login thành công trong <1s           | Automation Selenium | So sánh benchmark với release trước |
| API stress test        | Thực hiện API stress test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.        | stress load > 10k TPS | User login thành công trong <1s           | JMeter script       | Test môi trường Pre- Prod           |
| Data consistency test  | Thực hiện Data consistency test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và            | network disconnect    | Hệ thống chịu tải 20k TPS không gián đoạn | JMeter script       | So sánh benchmark với release trước |

<!-- image -->

## VIETTEL AI RACE

## KỊCH BẢN KIỂM THỬ QA

TD447

Lần ban hành: 1

|                 | thất bại.                                                                                                           |                             |                                           |                  |                                     |
|-----------------|---------------------------------------------------------------------------------------------------------------------|-----------------------------|-------------------------------------------|------------------|-------------------------------------|
| Security scan   | Thực hiện Security scan để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.   | API call batch 1000 request | Dữ liệu được khôi phục toàn vẹn sau sự cố | JMeter script    | Gửi báo cáo PDF hàng ngày           |
| Failover test   | Thực hiện Failover test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.   | invalid data                | User login thành công trong <1s           | Kịch bản Ansible | So sánh benchmark với release trước |
| API stress test | Thực hiện API stress test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại. | valid data                  | Cluster failover tự động trong 5s         | Manual test plan | Test môi trường Pre- Prod           |
| Failover test   | Thực hiện Failover test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.   | invalid data                | Hệ thống chịu tải 20k TPS không gián đoạn | Kịch bản Ansible | Phải log toàn bộ kết quả            |
| Security        | Thực hiện Security scan để kiểm thử                                                                                 | API call batch              | Hệ thống chịu tải                         | Manual test      | So sánh benchmark với               |

<!-- image -->

## VIETTEL AI RACE

## KỊCH BẢN KIỂM THỬ QA

TD447

Lần ban hành: 1

| scan            | chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.                                       | 1000 request   | 20k TPS không gián đoạn                   | plan                | release trước                       |
|-----------------|---------------------------------------------------------------------------------------------------------------------|----------------|-------------------------------------------|---------------------|-------------------------------------|
| Load test       | Thực hiện Load test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.       | valid data     | Hệ thống chịu tải 20k TPS không gián đoạn | Manual test plan    | Theo chuẩn ISTQB                    |
| Load test       | Thực hiện Load test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.       | valid data     | Dữ liệu được khôi phục toàn vẹn sau sự cố | Automation Selenium | So sánh benchmark với release trước |
| API stress test | Thực hiện API stress test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại. | DB corruption  | Dữ liệu được khôi phục toàn vẹn sau sự cố | JMeter script       | So sánh benchmark với release trước |
| Load test       | Thực hiện Load test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.       | valid data     | User login thành công trong <1s           | Kịch bản Ansible    | Phải log toàn bộ kết quả            |
| API stress      | Thực hiện API stress                                                                                                | invalid        | Không                                     | Kịch bản            | Gửi báo cáo                         |

<!-- image -->

## VIETTEL AI RACE

## KỊCH BẢN KIỂM THỬ QA

TD447

Lần ban hành: 1

| test                   | test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.                             | data                        | phát hiện lỗ hổng bảo mật OWASP Top 10       | Ansible             | PDF hàng ngày                       |
|------------------------|----------------------------------------------------------------------------------------------------------------------------|-----------------------------|----------------------------------------------|---------------------|-------------------------------------|
| Database recovery test | Thực hiện Database recovery test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại. | API call batch 1000 request | Cluster failover tự động trong 5s            | Manual test plan    | Test môi trường Pre- Prod           |
| Load test              | Thực hiện Load test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.              | network disconnect          | Không phát hiện lỗ hổng bảo mật OWASP Top 10 | Automation Selenium | So sánh benchmark với release trước |
| Security scan          | Thực hiện Security scan để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.          | network disconnect          | User login thành công trong <1s              | Kịch bản Ansible    | Test môi trường Pre- Prod           |
| Data consistency test  | Thực hiện Data consistency test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và            | valid data                  | Dữ liệu được khôi phục toàn vẹn sau sự cố    | Manual test plan    | Test môi trường Pre- Prod           |

<!-- image -->

## VIETTEL AI RACE

## KỊCH BẢN KIỂM THỬ QA

TD447

Lần ban hành: 1

|               | thất bại.                                                                                                      |               |                                              |                     |                                     |
|---------------|----------------------------------------------------------------------------------------------------------------|---------------|----------------------------------------------|---------------------|-------------------------------------|
| Login test    | Thực hiện Login test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại. | invalid data  | Không phát hiện lỗ hổng bảo mật OWASP Top 10 | JMeter script       | So sánh benchmark với release trước |
| Load test     | Thực hiện Load test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.  | DB corruption | Không phát hiện lỗ hổng bảo mật OWASP Top 10 | Kịch bản Ansible    | Phải log toàn bộ kết quả            |
| Login test    | Thực hiện Login test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại. | DB corruption | Cluster failover tự động trong 5s            | JMeter script       | Test môi trường Pre- Prod           |
| Load test     | Thực hiện Load test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.  | valid data    | Cluster failover tự động trong 5s            | Automation Selenium | Gửi báo cáo PDF hàng ngày           |
| Security scan | Thực hiện Security scan để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất   | invalid data  | Không phát hiện lỗ hổng bảo mật OWASP        | JMeter script       | Phải log toàn bộ kết quả            |

<!-- image -->

## VIETTEL AI RACE

## KỊCH BẢN KIỂM THỬ QA

TD447

Lần ban hành: 1

|                        | bại.                                                                                                                       |                       | Top 10                                    |                     |                                     |
|------------------------|----------------------------------------------------------------------------------------------------------------------------|-----------------------|-------------------------------------------|---------------------|-------------------------------------|
| Security scan          | Thực hiện Security scan để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.          | valid data            | Hệ thống chịu tải 20k TPS không gián đoạn | Kịch bản Ansible    | So sánh benchmark với release trước |
| Database recovery test | Thực hiện Database recovery test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại. | valid data            | Hệ thống chịu tải 20k TPS không gián đoạn | Manual test plan    | Test môi trường Pre- Prod           |
| Load test              | Thực hiện Load test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.              | DB corruption         | User login thành công trong <1s           | Manual test plan    | Test môi trường Pre- Prod           |
| API stress test        | Thực hiện API stress test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.        | stress load > 10k TPS | Cluster failover tự động trong 5s         | Automation Selenium | Gửi báo cáo PDF hàng ngày           |
| Database recovery      | Thực hiện Database recovery test để kiểm thử chức năng                                                                     | valid data            | Cluster failover tự động                  | Kịch bản Ansible    | Gửi báo cáo PDF hàng ngày           |

<!-- image -->

## VIETTEL AI RACE

## KỊCH BẢN KIỂM THỬ QA

TD447

Lần ban hành: 1

| test                   | và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.                                                        |                             | trong 5s                                     |                  |                           |
|------------------------|----------------------------------------------------------------------------------------------------------------------------|-----------------------------|----------------------------------------------|------------------|---------------------------|
| Database recovery test | Thực hiện Database recovery test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại. | API call batch 1000 request | Dữ liệu được khôi phục toàn vẹn sau sự cố    | Kịch bản Ansible | Test môi trường Pre- Prod |
| Database recovery test | Thực hiện Database recovery test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại. | stress load > 10k TPS       | User login thành công trong <1s              | Kịch bản Ansible | Phải log toàn bộ kết quả  |
| Load test              | Thực hiện Load test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.              | valid data                  | Không phát hiện lỗ hổng bảo mật OWASP Top 10 | Manual test plan | Theo chuẩn ISTQB          |
| API stress test        | Thực hiện API stress test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.        | stress load > 10k TPS       | Không phát hiện lỗ hổng bảo mật OWASP Top 10 | Manual test plan | Gửi báo cáo PDF hàng ngày |

<!-- image -->

## VIETTEL AI RACE

## KỊCH BẢN KIỂM THỬ QA

TD447

Lần ban hành: 1

| Load test     | Thực hiện Load test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.     | invalid data       | User login thành công trong <1s              | Kịch bản Ansible    | Theo chuẩn ISTQB         |
|---------------|-------------------------------------------------------------------------------------------------------------------|--------------------|----------------------------------------------|---------------------|--------------------------|
| Login test    | Thực hiện Login test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.    | valid data         | Hệ thống chịu tải 20k TPS không gián đoạn    | Kịch bản Ansible    | Theo chuẩn ISTQB         |
| Login test    | Thực hiện Login test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.    | valid data         | Không phát hiện lỗ hổng bảo mật OWASP Top 10 | Kịch bản Ansible    | Theo chuẩn ISTQB         |
| Failover test | Thực hiện Failover test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại. | network disconnect | Dữ liệu được khôi phục toàn vẹn sau sự cố    | JMeter script       | Phải log toàn bộ kết quả |
| Login test    | Thực hiện Login test để kiểm thử chức năng và hiệu năng của hệ thống, bao gồm kịch bản thành công và thất bại.    | network disconnect | User login thành công trong <1s              | Automation Selenium | Theo chuẩn ISTQB         |

<!-- image -->

| VIETTEL AI RACE   | TD447   |
|-------------------|---------|