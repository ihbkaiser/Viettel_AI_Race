<!-- image -->

## VIETTEL AI RACE

## DANH MỤC CHỨC NĂNG BCCS2

TD444

Lần ban hành: 1

| Tên ứng dụng        | Chức năng              | API/Action              | Mô tả                                               | Kết quả mong muốn   | Ghi chú                      |
|---------------------|------------------------|-------------------------|-----------------------------------------------------|---------------------|------------------------------|
| BCCS2-Core          | Validate IVRPrompt     | /ivrprompt/validate     | Validate dữ liệu IVRPrompt trong BCCS2-Core.        | Thông báo qua SMS   | Có cơ chế rollback           |
| Infra-Server        | Config QoS             | /qos/config             | Config dữ liệu QoS trong Infra-Server.              | Hiển thị báo cáo    | Có cơ chế rollback           |
| RPA-Engine          | Delete CustomerProfile | /customerprofile/delete | Delete dữ liệu CustomerProfile trong RPA-Engine.    | Cảnh báo            | Kết nối với hệ thống Billing |
| QA- Automation      | Generate AgentStatus   | /agentstatus/generate   | Generate dữ liệu AgentStatus trong QA-Automation.   | Lỗi nghiêm trọng    | Dữ liệu backup mỗi ngày      |
| Security- Firewall  | Config ClusterNode     | /clusternode/config     | Config dữ liệu ClusterNode trong Security-Firewall. | Không lỗi           | Tích hợp với CRM             |
| Security- Firewall  | Update Queue           | /queue/update           | Update dữ liệu Queue trong Security-Firewall.       | Ghi log đầy đủ      | Theo quy định Viettel        |
| IPCC- ContactCenter | Insert AccountLock     | /accountlock/insert     | Insert dữ liệu AccountLock trong                    | Không lỗi           | Chỉ dùng                     |

<!-- image -->

TD444

Lần ban hành: 1

## VIETTEL AI RACE

## DANH MỤC CHỨC NĂNG BCCS2

|                     |                        |                         | IPCC- ContactCenter.                                |                     | cho admin                    |
|---------------------|------------------------|-------------------------|-----------------------------------------------------|---------------------|------------------------------|
| IVR-System          | Monitor ClusterNode    | /clusternode/monitor    | Monitor dữ liệu ClusterNode trong IVR-System.       | Thông báo qua email | Chạy theo lịch cron          |
| Infra-Server        | Import Contact         | /contact/import         | Import dữ liệu Contact trong Infra- Server.         | Hiển thị báo cáo    | Có cơ chế rollback           |
| IPCC- ContactCenter | Insert Blacklist       | /blacklist/insert       | Insert dữ liệu Blacklist trong IPCC- ContactCenter. | Thông báo qua SMS   | Kết nối với hệ thống Billing |
| Security- Firewall  | Import Blacklist       | /blacklist/import       | Import dữ liệu Blacklist trong Security-Firewall.   | Tự động retry       | Dữ liệu backup mỗi ngày      |
| QA- Automation      | Schedule PackagePlan   | /packageplan/schedule   | Schedule dữ liệu PackagePlan trong QA-Automation.   | Thông báo qua SMS   | Chạy theo lịch cron          |
| RPA-Engine          | Analyze Blacklist      | /blacklist/analyze      | Analyze dữ liệu Blacklist trong RPA- Engine.        | Ghi log đầy đủ      | Tích hợp với CRM             |
| Infra-Server        | Analyze VPN            | /vpn/analyze            | Analyze dữ liệu VPN trong Infra- Server.            | Không lỗi           | Có cơ chế rollback           |
| Infra-Network       | Analyze FirewallPolicy | /firewallpolicy/analyze | Analyze dữ liệu FirewallPolicy trong Infra-Network. | Thông báo           | Chạy theo                    |

<!-- image -->

## VIETTEL AI RACE

## DANH MỤC CHỨC NĂNG BCCS2

TD444

Lần ban hành: 1

|                     |                     |                      |                                                        | qua SMS          | lịch cron                    |
|---------------------|---------------------|----------------------|--------------------------------------------------------|------------------|------------------------------|
| BCCS2-Core          | Import Opportunity  | /opportunity/import  | Import dữ liệu Opportunity trong BCCS2-Core.           | Tự động retry    | Kết nối với hệ thống Billing |
| IPCC- ContactCenter | Analyze AgentStatus | /agentstatus/analyze | Analyze dữ liệu AgentStatus trong IPCC- ContactCenter. | Cảnh báo         | Theo chuẩn ISO 27001         |
| CRM- Platform       | Insert IVRPrompt    | /ivrprompt/insert    | Insert dữ liệu IVRPrompt trong CRM-Platform.           | Hiển thị báo cáo | Yêu cầu xác thực người dùng  |
| BCCS2-Core          | Import CDRReport    | /cdrreport/import    | Import dữ liệu CDRReport trong BCCS2-Core.             | Cảnh báo         | Chỉ dùng cho admin           |
| CRM- Platform       | Analyze QoS         | /qos/analyze         | Analyze dữ liệu QoS trong CRM- Platform.               | Cảnh báo         | Tích hợp với CRM             |
| BCCS2-Core          | Update Campaign     | /campaign/update     | Update dữ liệu Campaign trong BCCS2-Core.              | Lỗi nghiêm trọng | Chạy theo lịch cron          |
| Infra-Network       | Export AccountLock  | /accountlock/export  | Export dữ liệu AccountLock trong Infra-Network.        | Hiển thị báo cáo | Chạy theo lịch cron          |

<!-- image -->

## VIETTEL AI RACE

## DANH MỤC CHỨC NĂNG BCCS2

TD444

Lần ban hành: 1

| CRM- Platform      | Analyze TransactionLog   | /transactionlog/analyze   | Analyze dữ liệu TransactionLog trong CRM- Platform.   | Không lỗi           | Tích hợp với CRM             |
|--------------------|--------------------------|---------------------------|-------------------------------------------------------|---------------------|------------------------------|
| CRM- Platform      | Config KPIReport         | /kpireport/config         | Config dữ liệu KPIReport trong CRM-Platform.          | Đồng bộ dữ liệu     | Theo chuẩn ISO 27001         |
| RPA-Engine         | Optimize Campaign        | /campaign/optimize        | Optimize dữ liệu Campaign trong RPA-Engine.           | Thông báo qua email | Chỉ dùng cho admin           |
| IVR-System         | Delete Queue             | /queue/delete             | Delete dữ liệu Queue trong IVR-System.                | Tự động retry       | Kết nối với hệ thống Billing |
| RPA-Engine         | Delete AgentStatus       | /agentstatus/delete       | Delete dữ liệu AgentStatus trong RPA-Engine.          | Thông báo qua SMS   | Tích hợp với CRM             |
| BCCS2- Billing     | Schedule AgentStatus     | /agentstatus/schedule     | Schedule dữ liệu AgentStatus trong BCCS2-Billing.     | Đồng bộ dữ liệu     | Dữ liệu backup mỗi ngày      |
| CRM- Platform      | Validate CustomerProfile | /customerprofile/validate | Validate dữ liệu CustomerProfile trong CRM- Platform. | Lỗi nghiêm trọng    | Tích hợp với CRM             |
| Security- Firewall | Update VPN               | /vpn/update               | Update dữ liệu VPN trong Security- Firewall.          | Ghi log đầy đủ      | Tích hợp với CRM             |

<!-- image -->

## VIETTEL AI RACE

## DANH MỤC CHỨC NĂNG BCCS2

TD444

Lần ban hành: 1

| IVR-System          | Schedule Invoice        | /invoice/schedule        | Schedule dữ liệu Invoice trong IVR- System.           | Không lỗi           | Tích hợp với CRM        |
|---------------------|-------------------------|--------------------------|-------------------------------------------------------|---------------------|-------------------------|
| BCCS2-Core          | Search Whitelist        | /whitelist/search        | Search dữ liệu Whitelist trong BCCS2-Core.            | Ghi log đầy đủ      | Theo chuẩn ISO 27001    |
| BCCS2-Core          | Optimize PackagePlan    | /packageplan/optimize    | Optimize dữ liệu PackagePlan trong BCCS2-Core.        | Hiển thị báo cáo    | Theo chuẩn ISO 27001    |
| Infra-Server        | Optimize VPN            | /vpn/optimize            | Optimize dữ liệu VPN trong Infra- Server.             | Thông báo qua email | Dữ liệu backup mỗi ngày |
| IVR-System          | Schedule QoS            | /qos/schedule            | Schedule dữ liệu QoS trong IVR- System.               | Hiển thị báo cáo    | Tích hợp với CRM        |
| CRM- Platform       | Optimize IVRPrompt      | /ivrprompt/optimize      | Optimize dữ liệu IVRPrompt trong CRM-Platform.        | Thông báo qua email | Bảo mật 2 lớp           |
| IPCC- ContactCenter | Optimize KPIReport      | /kpireport/optimize      | Optimize dữ liệu KPIReport trong IPCC- ContactCenter. | Lỗi nghiêm trọng    | Bảo mật 2 lớp           |
| Infra-Server        | Schedule FirewallPolicy | /firewallpolicy/schedule | Schedule dữ liệu FirewallPolicy trong Infra-Server.   | Tự động retry       | Có cơ chế rollback      |

<!-- image -->

## VIETTEL AI RACE

## DANH MỤC CHỨC NĂNG BCCS2

TD444

Lần ban hành: 1

| Security- Firewall   | Schedule QoS          | /qos/schedule          | Schedule dữ liệu QoS trong Security- Firewall.        | Thông báo qua SMS   | Chạy theo lịch cron          |
|----------------------|-----------------------|------------------------|-------------------------------------------------------|---------------------|------------------------------|
| RPA-Engine           | Optimize KPIReport    | /kpireport/optimize    | Optimize dữ liệu KPIReport trong RPA-Engine.          | Lỗi nghiêm trọng    | Chạy theo lịch cron          |
| IPCC- ContactCenter  | Update KPIReport      | /kpireport/update      | Update dữ liệu KPIReport trong IPCC- ContactCenter.   | Tự động retry       | Kết nối với hệ thống Billing |
| RPA-Engine           | Config FirewallPolicy | /firewallpolicy/config | Config dữ liệu FirewallPolicy trong RPA-Engine.       | Thành công          | Theo quy định Viettel        |
| Security- Firewall   | Optimize ClusterNode  | /clusternode/optimize  | Optimize dữ liệu ClusterNode trong Security-Firewall. | Ghi log đầy đủ      | Chỉ dùng cho admin           |
| Infra-Network        | Schedule SwitchConfig | /switchconfig/schedule | Schedule dữ liệu SwitchConfig trong Infra-Network.    | Thông báo qua email | Chạy theo lịch cron          |
| RPA-Engine           | Analyze KPIReport     | /kpireport/analyze     | Analyze dữ liệu KPIReport trong RPA-Engine.           | Không lỗi           | Dữ liệu backup mỗi ngày      |
| QA- Automation       | Config IVRPrompt      | /ivrprompt/config      | Config dữ liệu IVRPrompt trong QA-Automation.         | Không lỗi           | Kết nối với hệ               |

<!-- image -->

## VIETTEL AI RACE

## DANH MỤC CHỨC NĂNG BCCS2

TD444

Lần ban hành: 1

|                |                        |                         |                                                  |                  | thống Billing           |
|----------------|------------------------|-------------------------|--------------------------------------------------|------------------|-------------------------|
| QA- Automation | Monitor Invoice        | /invoice/monitor        | Monitor dữ liệu Invoice trong QA- Automation.    | Cảnh báo         | Theo chuẩn ISO 27001    |
| IVR-System     | Insert CustomerProfile | /customerprofile/insert | Insert dữ liệu CustomerProfile trong IVR-System. | Hiển thị báo cáo | Bảo mật 2 lớp           |
| IVR-System     | Optimize QoS           | /qos/optimize           | Optimize dữ liệu QoS trong IVR- System.          | Hiển thị báo cáo | Chỉ dùng cho admin      |
| BCCS2- Billing | Schedule Invoice       | /invoice/schedule       | Schedule dữ liệu Invoice trong BCCS2-Billing.    | Đồng bộ dữ liệu  | Dữ liệu backup mỗi ngày |
| BCCS2- Billing | Search DebtControl     | /debtcontrol/search     | Search dữ liệu DebtControl trong BCCS2-Billing.  | Cảnh báo         | Tích hợp với CRM        |
| IVR-System     | Optimize Lead          | /lead/optimize          | Optimize dữ liệu Lead trong IVR- System.         | Không lỗi        | Chỉ dùng cho admin      |
| RPA-Engine     | Config Lead            | /lead/config            | Config dữ liệu Lead trong RPA-Engine.            | Cảnh báo         | Chỉ dùng cho admin      |

<!-- image -->

## VIETTEL AI RACE

## DANH MỤC CHỨC NĂNG BCCS2

TD444

Lần ban hành: 1

| Security- Firewall   | Monitor ClusterNode   | /clusternode/monitor   | Monitor dữ liệu ClusterNode trong Security-Firewall.   | Thông báo qua SMS   | Chạy theo lịch cron          |
|----------------------|-----------------------|------------------------|--------------------------------------------------------|---------------------|------------------------------|
| Security- Firewall   | Update QoS            | /qos/update            | Update dữ liệu QoS trong Security- Firewall.           | Ghi log đầy đủ      | Theo chuẩn ISO 27001         |
| RPA-Engine           | Import Blacklist      | /blacklist/import      | Import dữ liệu Blacklist trong RPA- Engine.            | Ghi log đầy đủ      | Tích hợp với CRM             |
| RPA-Engine           | Delete StorageVolume  | /storagevolume/delete  | Delete dữ liệu StorageVolume trong RPA-Engine.         | Tự động retry       | Bảo mật 2 lớp                |
| RPA-Engine           | Generate Invoice      | /invoice/generate      | Generate dữ liệu Invoice trong RPA- Engine.            | Không lỗi           | Chỉ dùng cho admin           |
| Infra-Network        | Search CDRReport      | /cdrreport/search      | Search dữ liệu CDRReport trong Infra-Network.          | Đồng bộ dữ liệu     | Chạy theo lịch cron          |
| BCCS2-Core           | Optimize DebtControl  | /debtcontrol/optimize  | Optimize dữ liệu DebtControl trong BCCS2-Core.         | Thông báo qua email | Yêu cầu xác thực người dùng  |
| Infra-Network        | Delete Campaign       | /campaign/delete       | Delete dữ liệu Campaign trong Infra-Network.           | Thành công          | Kết nối với hệ thống Billing |

<!-- image -->

## VIETTEL AI RACE

## DANH MỤC CHỨC NĂNG BCCS2

TD444

Lần ban hành: 1

| Infra-Network      | Delete CustomerProfile   | /customerprofile/delete   | Delete dữ liệu CustomerProfile trong Infra-Network.   | Không lỗi        | Chạy theo lịch cron         |
|--------------------|--------------------------|---------------------------|-------------------------------------------------------|------------------|-----------------------------|
| BCCS2-Core         | Monitor TransactionLog   | /transactionlog/monitor   | Monitor dữ liệu TransactionLog trong BCCS2-Core.      | Hiển thị báo cáo | Yêu cầu xác thực người dùng |
| QA- Automation     | Export Contact           | /contact/export           | Export dữ liệu Contact trong QA- Automation.          | Hiển thị báo cáo | Yêu cầu xác thực người dùng |
| Security- Firewall | Delete Contact           | /contact/delete           | Delete dữ liệu Contact trong Security-Firewall.       | Ghi log đầy đủ   | Theo chuẩn ISO 27001        |
| Security- Firewall | Search Whitelist         | /whitelist/search         | Search dữ liệu Whitelist trong Security-Firewall.     | Lỗi nghiêm trọng | Chỉ dùng cho admin          |
| BCCS2- Billing     | Import Contact           | /contact/import           | Import dữ liệu Contact trong BCCS2-Billing.           | Cảnh báo         | Theo quy định Viettel       |
| Infra-Server       | Insert APIGateway        | /apigateway/insert        | Insert dữ liệu APIGateway trong Infra-Server.         | Không lỗi        | Theo quy định Viettel       |

<!-- image -->

## VIETTEL AI RACE

## DANH MỤC CHỨC NĂNG BCCS2

TD444

Lần ban hành: 1

| QA- Automation     | Optimize TransactionLog   | /transactionlog/optimize   | Optimize dữ liệu TransactionLog trong QA- Automation.   | Thành công          | Tích hợp với CRM             |
|--------------------|---------------------------|----------------------------|---------------------------------------------------------|---------------------|------------------------------|
| Infra-Network      | Optimize Opportunity      | /opportunity/optimize      | Optimize dữ liệu Opportunity trong Infra-Network.       | Không lỗi           | Kết nối với hệ thống Billing |
| RPA-Engine         | Update PackagePlan        | /packageplan/update        | Update dữ liệu PackagePlan trong RPA-Engine.            | Lỗi nghiêm trọng    | Theo chuẩn ISO 27001         |
| BCCS2-Core         | Generate Invoice          | /invoice/generate          | Generate dữ liệu Invoice trong BCCS2-Core.              | Thông báo qua email | Kết nối với hệ thống Billing |
| BCCS2-Core         | Import SwitchConfig       | /switchconfig/import       | Import dữ liệu SwitchConfig trong BCCS2-Core.           | Không lỗi           | Theo chuẩn ISO 27001         |
| Security- Firewall | Schedule Campaign         | /campaign/schedule         | Schedule dữ liệu Campaign trong Security-Firewall.      | Tự động retry       | Yêu cầu xác thực người dùng  |
| BCCS2- Billing     | Update Whitelist          | /whitelist/update          | Update dữ liệu Whitelist trong BCCS2-Billing.           | Tự động retry       | Theo chuẩn ISO 27001         |

<!-- image -->

## VIETTEL AI RACE

## DANH MỤC CHỨC NĂNG BCCS2

TD444

Lần ban hành: 1

| QA- Automation     | Insert DataLake       | /datalake/insert       | Insert dữ liệu DataLake trong QA- Automation.         | Ghi log đầy đủ    | Yêu cầu xác thực người dùng   |
|--------------------|-----------------------|------------------------|-------------------------------------------------------|-------------------|-------------------------------|
| CRM- Platform      | Import CDRReport      | /cdrreport/import      | Import dữ liệu CDRReport trong CRM-Platform.          | Tự động retry     | Chạy theo lịch cron           |
| QA- Automation     | Config AgentStatus    | /agentstatus/config    | Config dữ liệu AgentStatus trong QA-Automation.       | Hiển thị báo cáo  | Kết nối với hệ thống Billing  |
| IVR-System         | Search CDRReport      | /cdrreport/search      | Search dữ liệu CDRReport trong IVR-System.            | Lỗi nghiêm trọng  | Dữ liệu backup mỗi ngày       |
| Infra-Network      | Validate SwitchConfig | /switchconfig/validate | Validate dữ liệu SwitchConfig trong Infra-Network.    | Thông báo qua SMS | Yêu cầu xác thực người dùng   |
| BCCS2- Billing     | Monitor ClusterNode   | /clusternode/monitor   | Monitor dữ liệu ClusterNode trong BCCS2-Billing.      | Thông báo qua SMS | Tích hợp với CRM              |
| Security- Firewall | Validate Opportunity  | /opportunity/validate  | Validate dữ liệu Opportunity trong Security-Firewall. | Thông báo qua SMS | Chỉ dùng cho admin            |

<!-- image -->

## VIETTEL AI RACE

## DANH MỤC CHỨC NĂNG BCCS2

TD444

Lần ban hành: 1

| Security- Firewall   | Schedule Whitelist   | /whitelist/schedule   | Schedule dữ liệu Whitelist trong Security-Firewall.   | Đồng bộ dữ liệu     | Tích hợp với CRM             |
|----------------------|----------------------|-----------------------|-------------------------------------------------------|---------------------|------------------------------|
| BCCS2- Billing       | Delete APIGateway    | /apigateway/delete    | Delete dữ liệu APIGateway trong BCCS2-Billing.        | Thành công          | Theo quy định Viettel        |
| Infra-Network        | Search ClusterNode   | /clusternode/search   | Search dữ liệu ClusterNode trong Infra-Network.       | Đồng bộ dữ liệu     | Theo quy định Viettel        |
| BCCS2-Core           | Config Contact       | /contact/config       | Config dữ liệu Contact trong BCCS2-Core.              | Thông báo qua email | Yêu cầu xác thực người dùng  |
| IPCC- ContactCenter  | Config Contact       | /contact/config       | Config dữ liệu Contact trong IPCC- ContactCenter.     | Thành công          | Chỉ dùng cho admin           |
| QA- Automation       | Config CDRReport     | /cdrreport/config     | Config dữ liệu CDRReport trong QA-Automation.         | Không lỗi           | Kết nối với hệ thống Billing |
| BCCS2-Core           | Schedule KPIReport   | /kpireport/schedule   | Schedule dữ liệu KPIReport trong BCCS2-Core.          | Thông báo qua SMS   | Chạy theo lịch cron          |
| Infra-Network        | Delete IVRPrompt     | /ivrprompt/delete     | Delete dữ liệu IVRPrompt trong Infra-Network.         | Tự động retry       | Dữ liệu backup               |

<!-- image -->

TD444

Lần ban hành: 1

## VIETTEL AI RACE

## DANH MỤC CHỨC NĂNG BCCS2

|                    |                        |                         |                                                       |                     | mỗi ngày                    |
|--------------------|------------------------|-------------------------|-------------------------------------------------------|---------------------|-----------------------------|
| Security- Firewall | Validate DebtControl   | /debtcontrol/validate   | Validate dữ liệu DebtControl trong Security-Firewall. | Thành công          | Có cơ chế rollback          |
| BCCS2-Core         | Optimize Lead          | /lead/optimize          | Optimize dữ liệu Lead trong BCCS2- Core.              | Thông báo qua SMS   | Theo quy định Viettel       |
| RPA-Engine         | Validate Opportunity   | /opportunity/validate   | Validate dữ liệu Opportunity trong RPA-Engine.        | Cảnh báo            | Có cơ chế rollback          |
| IVR-System         | Update DataLake        | /datalake/update        | Update dữ liệu DataLake trong IVR-System.             | Không lỗi           | Theo chuẩn ISO 27001        |
| Infra-Server       | Config CustomerProfile | /customerprofile/config | Config dữ liệu CustomerProfile trong Infra-Server.    | Thông báo qua SMS   | Yêu cầu xác thực người dùng |
| BCCS2- Billing     | Validate StorageVolume | /storagevolume/validate | Validate dữ liệu StorageVolume trong BCCS2- Billing.  | Thông báo qua email | Theo quy định Viettel       |
| CRM- Platform      | Analyze APIGateway     | /apigateway/analyze     | Analyze dữ liệu APIGateway trong CRM-Platform.        | Tự động retry       | Theo quy định Viettel       |

<!-- image -->

## VIETTEL AI RACE

## DANH MỤC CHỨC NĂNG BCCS2

TD444

Lần ban hành: 1

| Infra-Network      | Search Contact        | /contact/search        | Search dữ liệu Contact trong Infra- Network.      | Hiển thị báo cáo   | Theo quy định Viettel       |
|--------------------|-----------------------|------------------------|---------------------------------------------------|--------------------|-----------------------------|
| Infra-Network      | Monitor QoS           | /qos/monitor           | Monitor dữ liệu QoS trong Infra-Network.          | Lỗi nghiêm trọng   | Chạy theo lịch cron         |
| Security- Firewall | Update KPIReport      | /kpireport/update      | Update dữ liệu KPIReport trong Security-Firewall. | Thông báo qua SMS  | Yêu cầu xác thực người dùng |
| RPA-Engine         | Export StorageVolume  | /storagevolume/export  | Export dữ liệu StorageVolume trong RPA-Engine.    | Tự động retry      | Dữ liệu backup mỗi ngày     |
| IVR-System         | Config PackagePlan    | /packageplan/config    | Config dữ liệu PackagePlan trong IVR-System.      | Cảnh báo           | Theo quy định Viettel       |
| CRM- Platform      | Update FirewallPolicy | /firewallpolicy/update | Update dữ liệu FirewallPolicy trong CRM-Platform. | Thành công         | Tích hợp với CRM            |
| QA- Automation     | Analyze Blacklist     | /blacklist/analyze     | Analyze dữ liệu Blacklist trong QA- Automation.   | Không lỗi          | Dữ liệu backup mỗi ngày     |
| CRM- Platform      | Insert AgentStatus    | /agentstatus/insert    | Insert dữ liệu AgentStatus trong CRM-Platform.    | Tự động retry      | Bảo mật 2 lớp               |

<!-- image -->

## VIETTEL AI RACE

## DANH MỤC CHỨC NĂNG BCCS2

TD444

Lần ban hành: 1

| BCCS2-Core          | Config DataLake    | /datalake/config    | Config dữ liệu DataLake trong BCCS2-Core.           | Ghi log đầy đủ   | Kết nối với hệ thống Billing   |
|---------------------|--------------------|---------------------|-----------------------------------------------------|------------------|--------------------------------|
| IPCC- ContactCenter | Generate Invoice   | /invoice/generate   | Generate dữ liệu Invoice trong IPCC- ContactCenter. | Thành công       | Yêu cầu xác thực người dùng    |
| BCCS2-Core          | Update DebtControl | /debtcontrol/update | Update dữ liệu DebtControl trong BCCS2-Core.        | Tự động retry    | Tích hợp với CRM               |
| BCCS2- Billing      | Optimize IVRPrompt | /ivrprompt/optimize | Optimize dữ liệu IVRPrompt trong BCCS2-Billing.     | Lỗi nghiêm trọng | Dữ liệu backup mỗi ngày        |
| BCCS2-Core          | Update IVRPrompt   | /ivrprompt/update   | Update dữ liệu IVRPrompt trong BCCS2-Core.          | Thành công       | Bảo mật 2 lớp                  |
| IVR-System          | Validate CDRReport | /cdrreport/validate | Validate dữ liệu CDRReport trong IVR-System.        | Lỗi nghiêm trọng | Có cơ chế rollback             |
| IPCC- ContactCenter | Insert Blacklist   | /blacklist/insert   | Insert dữ liệu Blacklist trong IPCC- ContactCenter. | Ghi log đầy đủ   | Có cơ chế rollback             |
| BCCS2-Core          | Import PackagePlan | /packageplan/import | Import dữ liệu PackagePlan trong BCCS2-Core.        | Lỗi nghiêm trọng | Theo quy định Viettel          |

<!-- image -->

## VIETTEL AI RACE

## DANH MỤC CHỨC NĂNG BCCS2

TD444

Lần ban hành: 1

| QA- Automation      | Delete IVRPrompt       | /ivrprompt/delete       | Delete dữ liệu IVRPrompt trong QA-Automation.         | Cảnh báo            | Theo chuẩn ISO 27001         |
|---------------------|------------------------|-------------------------|-------------------------------------------------------|---------------------|------------------------------|
| QA- Automation      | Import Opportunity     | /opportunity/import     | Import dữ liệu Opportunity trong QA-Automation.       | Ghi log đầy đủ      | Dữ liệu backup mỗi ngày      |
| RPA-Engine          | Delete Promotion       | /promotion/delete       | Delete dữ liệu Promotion trong RPA-Engine.            | Cảnh báo            | Yêu cầu xác thực người dùng  |
| IVR-System          | Update Campaign        | /campaign/update        | Update dữ liệu Campaign trong IVR-System.             | Không lỗi           | Tích hợp với CRM             |
| IPCC- ContactCenter | Optimize CDRReport     | /cdrreport/optimize     | Optimize dữ liệu CDRReport trong IPCC- ContactCenter. | Thông báo qua email | Kết nối với hệ thống Billing |
| Infra-Network       | Monitor VPN            | /vpn/monitor            | Monitor dữ liệu VPN trong Infra- Network.             | Thành công          | Tích hợp với CRM             |
| RPA-Engine          | Import IVRPrompt       | /ivrprompt/import       | Import dữ liệu IVRPrompt trong RPA-Engine.            | Không lỗi           | Theo chuẩn ISO 27001         |
| BCCS2- Billing      | Validate StorageVolume | /storagevolume/validate | Validate dữ liệu StorageVolume trong BCCS2- Billing.  | Đồng bộ dữ liệu     | Chỉ dùng cho admin           |

<!-- image -->

## VIETTEL AI RACE

## DANH MỤC CHỨC NĂNG BCCS2

TD444

Lần ban hành: 1

| QA- Automation     | Delete Invoice       | /invoice/delete       | Delete dữ liệu Invoice trong QA- Automation.        | Ghi log đầy đủ      | Yêu cầu xác thực người dùng   |
|--------------------|----------------------|-----------------------|-----------------------------------------------------|---------------------|-------------------------------|
| BCCS2-Core         | Update PackagePlan   | /packageplan/update   | Update dữ liệu PackagePlan trong BCCS2-Core.        | Tự động retry       | Chỉ dùng cho admin            |
| CRM- Platform      | Search Campaign      | /campaign/search      | Search dữ liệu Campaign trong CRM-Platform.         | Đồng bộ dữ liệu     | Tích hợp với CRM              |
| BCCS2- Billing     | Insert VPN           | /vpn/insert           | Insert dữ liệu VPN trong BCCS2- Billing.            | Lỗi nghiêm trọng    | Dữ liệu backup mỗi ngày       |
| IVR-System         | Schedule ClusterNode | /clusternode/schedule | Schedule dữ liệu ClusterNode trong IVR-System.      | Thông báo qua email | Kết nối với hệ thống Billing  |
| Security- Firewall | Optimize KPIReport   | /kpireport/optimize   | Optimize dữ liệu KPIReport trong Security-Firewall. | Cảnh báo            | Tích hợp với CRM              |
| Infra-Server       | Analyze Promotion    | /promotion/analyze    | Analyze dữ liệu Promotion trong Infra-Server.       | Tự động retry       | Theo chuẩn ISO 27001          |
| BCCS2- Billing     | Export IVRPrompt     | /ivrprompt/export     | Export dữ liệu IVRPrompt trong BCCS2-Billing.       | Thành công          | Chạy theo lịch cron           |

<!-- image -->

## VIETTEL AI RACE

## DANH MỤC CHỨC NĂNG BCCS2

TD444

Lần ban hành: 1

| Security- Firewall   | Insert DebtControl    | /debtcontrol/insert    | Insert dữ liệu DebtControl trong Security-Firewall.   | Không lỗi           | Theo quy định Viettel        |
|----------------------|-----------------------|------------------------|-------------------------------------------------------|---------------------|------------------------------|
| QA- Automation       | Schedule KPIReport    | /kpireport/schedule    | Schedule dữ liệu KPIReport trong QA-Automation.       | Tự động retry       | Theo chuẩn ISO 27001         |
| Infra-Server         | Monitor Whitelist     | /whitelist/monitor     | Monitor dữ liệu Whitelist trong Infra-Server.         | Thông báo qua email | Chạy theo lịch cron          |
| Infra-Server         | Config FirewallPolicy | /firewallpolicy/config | Config dữ liệu FirewallPolicy trong Infra-Server.     | Thông báo qua SMS   | Kết nối với hệ thống Billing |
| Infra-Network        | Monitor Lead          | /lead/monitor          | Monitor dữ liệu Lead trong Infra- Network.            | Không lỗi           | Dữ liệu backup mỗi ngày      |
| IPCC- ContactCenter  | Delete PackagePlan    | /packageplan/delete    | Delete dữ liệu PackagePlan trong IPCC- ContactCenter. | Đồng bộ dữ liệu     | Yêu cầu xác thực người dùng  |
| BCCS2-Core           | Generate AccountLock  | /accountlock/generate  | Generate dữ liệu AccountLock trong BCCS2-Core.        | Thông báo qua email | Yêu cầu xác thực người dùng  |

<!-- image -->

## VIETTEL AI RACE

## DANH MỤC CHỨC NĂNG BCCS2

TD444

Lần ban hành: 1

| IVR-System          | Config IVRPrompt       | /ivrprompt/config       | Config dữ liệu IVRPrompt trong IVR-System.               | Ghi log đầy đủ    | Bảo mật 2 lớp         |
|---------------------|------------------------|-------------------------|----------------------------------------------------------|-------------------|-----------------------|
| Infra-Network       | Optimize Opportunity   | /opportunity/optimize   | Optimize dữ liệu Opportunity trong Infra-Network.        | Đồng bộ dữ liệu   | Chỉ dùng cho admin    |
| Infra-Network       | Monitor Contact        | /contact/monitor        | Monitor dữ liệu Contact trong Infra- Network.            | Không lỗi         | Chạy theo lịch cron   |
| Security- Firewall  | Import Campaign        | /campaign/import        | Import dữ liệu Campaign trong Security-Firewall.         | Thành công        | Chỉ dùng cho admin    |
| Infra-Network       | Schedule AgentStatus   | /agentstatus/schedule   | Schedule dữ liệu AgentStatus trong Infra-Network.        | Hiển thị báo cáo  | Theo chuẩn ISO 27001  |
| Security- Firewall  | Import CustomerProfile | /customerprofile/import | Import dữ liệu CustomerProfile trong Security- Firewall. | Thông báo qua SMS | Theo quy định Viettel |
| IPCC- ContactCenter | Delete QoS             | /qos/delete             | Delete dữ liệu QoS trong IPCC- ContactCenter.            | Ghi log đầy đủ    | Theo quy định Viettel |
| Infra-Server        | Validate Lead          | /lead/validate          | Validate dữ liệu Lead trong Infra- Server.               | Đồng bộ dữ liệu   | Có cơ chế rollback    |

<!-- image -->

## VIETTEL AI RACE

## DANH MỤC CHỨC NĂNG BCCS2

TD444

Lần ban hành: 1

| BCCS2- Billing      | Delete CustomerProfile   | /customerprofile/delete   | Delete dữ liệu CustomerProfile trong BCCS2- Billing.   | Hiển thị báo cáo   | Có cơ chế rollback           |
|---------------------|--------------------------|---------------------------|--------------------------------------------------------|--------------------|------------------------------|
| BCCS2- Billing      | Generate AccountLock     | /accountlock/generate     | Generate dữ liệu AccountLock trong BCCS2-Billing.      | Thành công         | Kết nối với hệ thống Billing |
| CRM- Platform       | Delete PackagePlan       | /packageplan/delete       | Delete dữ liệu PackagePlan trong CRM-Platform.         | Ghi log đầy đủ     | Chạy theo lịch cron          |
| CRM- Platform       | Validate Opportunity     | /opportunity/validate     | Validate dữ liệu Opportunity trong CRM-Platform.       | Ghi log đầy đủ     | Có cơ chế rollback           |
| Infra-Network       | Optimize Promotion       | /promotion/optimize       | Optimize dữ liệu Promotion trong Infra-Network.        | Không lỗi          | Bảo mật 2 lớp                |
| IPCC- ContactCenter | Search DebtControl       | /debtcontrol/search       | Search dữ liệu DebtControl trong IPCC- ContactCenter.  | Ghi log đầy đủ     | Tích hợp với CRM             |
| RPA-Engine          | Generate AgentStatus     | /agentstatus/generate     | Generate dữ liệu AgentStatus trong RPA-Engine.         | Không lỗi          | Tích hợp với CRM             |
| Infra-Server        | Config VPN               | /vpn/config               | Config dữ liệu VPN trong Infra-Server.                 | Đồng bộ dữ liệu    | Chỉ dùng cho admin           |

<!-- image -->

## VIETTEL AI RACE

## DANH MỤC CHỨC NĂNG BCCS2

TD444

Lần ban hành: 1

| Security- Firewall   | Update ClusterNode      | /clusternode/update      | Update dữ liệu ClusterNode trong Security-Firewall.       | Không lỗi           | Theo quy định Viettel        |
|----------------------|-------------------------|--------------------------|-----------------------------------------------------------|---------------------|------------------------------|
| RPA-Engine           | Config IVRPrompt        | /ivrprompt/config        | Config dữ liệu IVRPrompt trong RPA-Engine.                | Thông báo qua SMS   | Có cơ chế rollback           |
| CRM- Platform        | Search DataLake         | /datalake/search         | Search dữ liệu DataLake trong CRM-Platform.               | Ghi log đầy đủ      | Chỉ dùng cho admin           |
| Security- Firewall   | Optimize TransactionLog | /transactionlog/optimize | Optimize dữ liệu TransactionLog trong Security- Firewall. | Thông báo qua email | Dữ liệu backup mỗi ngày      |
| IPCC- ContactCenter  | Schedule Invoice        | /invoice/schedule        | Schedule dữ liệu Invoice trong IPCC- ContactCenter.       | Thành công          | Kết nối với hệ thống Billing |
| BCCS2-Core           | Update TransactionLog   | /transactionlog/update   | Update dữ liệu TransactionLog trong BCCS2-Core.           | Thông báo qua SMS   | Chỉ dùng cho admin           |
| BCCS2-Core           | Delete TransactionLog   | /transactionlog/delete   | Delete dữ liệu TransactionLog trong BCCS2-Core.           | Ghi log đầy đủ      | Bảo mật 2 lớp                |
| IVR-System           | Config VPN              | /vpn/config              | Config dữ liệu VPN trong IVR-System.                      | Không lỗi           | Chỉ dùng cho admin           |

<!-- image -->

## VIETTEL AI RACE

## DANH MỤC CHỨC NĂNG BCCS2

TD444

Lần ban hành: 1

| CRM- Platform   | Generate ClusterNode   | /clusternode/generate   | Generate dữ liệu ClusterNode trong CRM-Platform.   | Không lỗi           | Bảo mật 2 lớp                |
|-----------------|------------------------|-------------------------|----------------------------------------------------|---------------------|------------------------------|
| BCCS2-Core      | Optimize Lead          | /lead/optimize          | Optimize dữ liệu Lead trong BCCS2- Core.           | Lỗi nghiêm trọng    | Kết nối với hệ thống Billing |
| IVR-System      | Update CustomerProfile | /customerprofile/update | Update dữ liệu CustomerProfile trong IVR-System.   | Thông báo qua email | Theo chuẩn ISO 27001         |
| Infra-Network   | Schedule AccountLock   | /accountlock/schedule   | Schedule dữ liệu AccountLock trong Infra-Network.  | Lỗi nghiêm trọng    | Chỉ dùng cho admin           |
| BCCS2-Core      | Search ClusterNode     | /clusternode/search     | Search dữ liệu ClusterNode trong BCCS2-Core.       | Đồng bộ dữ liệu     | Tích hợp với CRM             |
| BCCS2- Billing  | Monitor Opportunity    | /opportunity/monitor    | Monitor dữ liệu Opportunity trong BCCS2-Billing.   | Thông báo qua SMS   | Yêu cầu xác thực người dùng  |
| RPA-Engine      | Import Campaign        | /campaign/import        | Import dữ liệu Campaign trong RPA-Engine.          | Lỗi nghiêm trọng    | Có cơ chế rollback           |
| QA- Automation  | Search SwitchConfig    | /switchconfig/search    | Search dữ liệu SwitchConfig trong QA-Automation.   | Tự động retry       | Có cơ chế rollback           |

<!-- image -->

## VIETTEL AI RACE

## DANH MỤC CHỨC NĂNG BCCS2

TD444

Lần ban hành: 1

| BCCS2- Billing     | Export QoS            | /qos/export            | Export dữ liệu QoS trong BCCS2- Billing.              | Đồng bộ dữ liệu   | Theo chuẩn ISO 27001    |
|--------------------|-----------------------|------------------------|-------------------------------------------------------|-------------------|-------------------------|
| Infra-Server       | Update Invoice        | /invoice/update        | Update dữ liệu Invoice trong Infra- Server.           | Ghi log đầy đủ    | Có cơ chế rollback      |
| BCCS2- Billing     | Monitor VPN           | /vpn/monitor           | Monitor dữ liệu VPN trong BCCS2- Billing.             | Thông báo qua SMS | Dữ liệu backup mỗi ngày |
| QA- Automation     | Search SwitchConfig   | /switchconfig/search   | Search dữ liệu SwitchConfig trong QA-Automation.      | Đồng bộ dữ liệu   | Chạy theo lịch cron     |
| Security- Firewall | Optimize PackagePlan  | /packageplan/optimize  | Optimize dữ liệu PackagePlan trong Security-Firewall. | Thành công        | Theo quy định Viettel   |
| QA- Automation     | Delete Contact        | /contact/delete        | Delete dữ liệu Contact trong QA- Automation.          | Tự động retry     | Theo chuẩn ISO 27001    |
| BCCS2-Core         | Schedule SwitchConfig | /switchconfig/schedule | Schedule dữ liệu SwitchConfig trong BCCS2-Core.       | Thông báo qua SMS | Có cơ chế rollback      |
| IVR-System         | Analyze Promotion     | /promotion/analyze     | Analyze dữ liệu Promotion trong IVR-System.           | Không lỗi         | Dữ liệu backup mỗi ngày |

<!-- image -->

## VIETTEL AI RACE

## DANH MỤC CHỨC NĂNG BCCS2

TD444

Lần ban hành: 1

| QA- Automation     | Import Invoice      | /invoice/import      | Import dữ liệu Invoice trong QA- Automation.      | Thành công          | Tích hợp với CRM            |
|--------------------|---------------------|----------------------|---------------------------------------------------|---------------------|-----------------------------|
| QA- Automation     | Import VPN          | /vpn/import          | Import dữ liệu VPN trong QA- Automation.          | Thông báo qua email | Theo quy định Viettel       |
| IVR-System         | Update SwitchConfig | /switchconfig/update | Update dữ liệu SwitchConfig trong IVR-System.     | Thành công          | Chỉ dùng cho admin          |
| BCCS2- Billing     | Insert CDRReport    | /cdrreport/insert    | Insert dữ liệu CDRReport trong BCCS2-Billing.     | Thành công          | Theo quy định Viettel       |
| Security- Firewall | Export Whitelist    | /whitelist/export    | Export dữ liệu Whitelist trong Security-Firewall. | Cảnh báo            | Chỉ dùng cho admin          |
| CRM- Platform      | Search DataLake     | /datalake/search     | Search dữ liệu DataLake trong CRM-Platform.       | Cảnh báo            | Bảo mật 2 lớp               |
| Infra-Server       | Schedule IVRPrompt  | /ivrprompt/schedule  | Schedule dữ liệu IVRPrompt trong Infra-Server.    | Thông báo qua email | Yêu cầu xác thực người dùng |
| Infra-Network      | Analyze Campaign    | /campaign/analyze    | Analyze dữ liệu Campaign trong Infra-Network.     | Thông báo qua SMS   | Bảo mật 2 lớp               |

<!-- image -->

## VIETTEL AI RACE

## DANH MỤC CHỨC NĂNG BCCS2

TD444

Lần ban hành: 1

| BCCS2- Billing     | Delete Opportunity      | /opportunity/delete      | Delete dữ liệu Opportunity trong BCCS2-Billing.   | Hiển thị báo cáo   | Yêu cầu xác thực người dùng   |
|--------------------|-------------------------|--------------------------|---------------------------------------------------|--------------------|-------------------------------|
| QA- Automation     | Monitor AccountLock     | /accountlock/monitor     | Monitor dữ liệu AccountLock trong QA-Automation.  | Ghi log đầy đủ     | Chạy theo lịch cron           |
| BCCS2-Core         | Monitor Campaign        | /campaign/monitor        | Monitor dữ liệu Campaign trong BCCS2-Core.        | Không lỗi          | Chỉ dùng cho admin            |
| IVR-System         | Export QoS              | /qos/export              | Export dữ liệu QoS trong IVR-System.              | Ghi log đầy đủ     | Yêu cầu xác thực người dùng   |
| Security- Firewall | Config KPIReport        | /kpireport/config        | Config dữ liệu KPIReport trong Security-Firewall. | Hiển thị báo cáo   | Theo chuẩn ISO 27001          |
| Infra-Server       | Monitor Blacklist       | /blacklist/monitor       | Monitor dữ liệu Blacklist trong Infra- Server.    | Thông báo qua SMS  | Theo quy định Viettel         |
| BCCS2-Core         | Optimize FirewallPolicy | /firewallpolicy/optimize | Optimize dữ liệu FirewallPolicy trong BCCS2-Core. | Lỗi nghiêm trọng   | Bảo mật 2 lớp                 |

<!-- image -->

## VIETTEL AI RACE

## DANH MỤC CHỨC NĂNG BCCS2

TD444

Lần ban hành: 1

| IPCC- ContactCenter   | Search PackagePlan   | /packageplan/search   | Search dữ liệu PackagePlan trong IPCC- ContactCenter.   | Tự động retry       | Chỉ dùng cho admin          |
|-----------------------|----------------------|-----------------------|---------------------------------------------------------|---------------------|-----------------------------|
| IPCC- ContactCenter   | Delete Promotion     | /promotion/delete     | Delete dữ liệu Promotion trong IPCC- ContactCenter.     | Thông báo qua SMS   | Yêu cầu xác thực người dùng |
| BCCS2-Core            | Monitor SwitchConfig | /switchconfig/monitor | Monitor dữ liệu SwitchConfig trong BCCS2-Core.          | Tự động retry       | Yêu cầu xác thực người dùng |
| IPCC- ContactCenter   | Schedule DataLake    | /datalake/schedule    | Schedule dữ liệu DataLake trong IPCC- ContactCenter.    | Ghi log đầy đủ      | Theo chuẩn ISO 27001        |
| IPCC- ContactCenter   | Insert Queue         | /queue/insert         | Insert dữ liệu Queue trong IPCC- ContactCenter.         | Thông báo qua email | Tích hợp với CRM            |
| RPA-Engine            | Validate APIGateway  | /apigateway/validate  | Validate dữ liệu APIGateway trong RPA-Engine.           | Thông báo qua SMS   | Theo chuẩn ISO 27001        |
| Infra-Server          | Schedule AgentStatus | /agentstatus/schedule | Schedule dữ liệu AgentStatus trong Infra-Server.        | Đồng bộ dữ liệu     | Theo chuẩn ISO 27001        |

<!-- image -->

## VIETTEL AI RACE

## DANH MỤC CHỨC NĂNG BCCS2

TD444

Lần ban hành: 1

| IVR-System          | Optimize Lead         | /lead/optimize         | Optimize dữ liệu Lead trong IVR- System.                | Không lỗi         | Chỉ dùng cho admin           |
|---------------------|-----------------------|------------------------|---------------------------------------------------------|-------------------|------------------------------|
| BCCS2-Core          | Optimize Promotion    | /promotion/optimize    | Optimize dữ liệu Promotion trong BCCS2-Core.            | Thông báo qua SMS | Kết nối với hệ thống Billing |
| BCCS2- Billing      | Generate Queue        | /queue/generate        | Generate dữ liệu Queue trong BCCS2-Billing.             | Đồng bộ dữ liệu   | Yêu cầu xác thực người dùng  |
| BCCS2-Core          | Monitor PackagePlan   | /packageplan/monitor   | Monitor dữ liệu PackagePlan trong BCCS2-Core.           | Hiển thị báo cáo  | Kết nối với hệ thống Billing |
| Security- Firewall  | Analyze StorageVolume | /storagevolume/analyze | Analyze dữ liệu StorageVolume trong Security- Firewall. | Thông báo qua SMS | Yêu cầu xác thực người dùng  |
| IPCC- ContactCenter | Export Contact        | /contact/export        | Export dữ liệu Contact trong IPCC- ContactCenter.       | Đồng bộ dữ liệu   | Chạy theo lịch cron          |
| Infra-Network       | Validate QoS          | /qos/validate          | Validate dữ liệu QoS trong Infra-Network.               | Thành công        | Theo quy định Viettel        |

<!-- image -->

## VIETTEL AI RACE

## DANH MỤC CHỨC NĂNG BCCS2

TD444

Lần ban hành: 1

| RPA-Engine          | Search Invoice        | /invoice/search        | Search dữ liệu Invoice trong RPA- Engine.                | Thông báo qua SMS   | Tích hợp với CRM      |
|---------------------|-----------------------|------------------------|----------------------------------------------------------|---------------------|-----------------------|
| IPCC- ContactCenter | Update FirewallPolicy | /firewallpolicy/update | Update dữ liệu FirewallPolicy trong IPCC- ContactCenter. | Tự động retry       | Theo chuẩn ISO 27001  |
| QA- Automation      | Config ClusterNode    | /clusternode/config    | Config dữ liệu ClusterNode trong QA-Automation.          | Lỗi nghiêm trọng    | Tích hợp với CRM      |
| BCCS2- Billing      | Delete FirewallPolicy | /firewallpolicy/delete | Delete dữ liệu FirewallPolicy trong BCCS2-Billing.       | Cảnh báo            | Bảo mật 2 lớp         |
| IVR-System          | Schedule APIGateway   | /apigateway/schedule   | Schedule dữ liệu APIGateway trong IVR-System.            | Hiển thị báo cáo    | Có cơ chế rollback    |
| BCCS2-Core          | Config DataLake       | /datalake/config       | Config dữ liệu DataLake trong BCCS2-Core.                | Đồng bộ dữ liệu     | Theo quy định Viettel |
| BCCS2- Billing      | Optimize Whitelist    | /whitelist/optimize    | Optimize dữ liệu Whitelist trong BCCS2-Billing.          | Không lỗi           | Chạy theo lịch cron   |
| Infra-Network       | Search ClusterNode    | /clusternode/search    | Search dữ liệu ClusterNode trong Infra-Network.          | Hiển thị báo cáo    | Có cơ chế rollback    |

<!-- image -->

## VIETTEL AI RACE

## DANH MỤC CHỨC NĂNG BCCS2

TD444

Lần ban hành: 1

| IPCC- ContactCenter   | Search Blacklist         | /blacklist/search         | Search dữ liệu Blacklist trong IPCC- ContactCenter.   | Hiển thị báo cáo    | Bảo mật 2 lớp                |
|-----------------------|--------------------------|---------------------------|-------------------------------------------------------|---------------------|------------------------------|
| IPCC- ContactCenter   | Optimize Queue           | /queue/optimize           | Optimize dữ liệu Queue trong IPCC- ContactCenter.     | Lỗi nghiêm trọng    | Có cơ chế rollback           |
| Infra-Network         | Schedule IVRPrompt       | /ivrprompt/schedule       | Schedule dữ liệu IVRPrompt trong Infra-Network.       | Tự động retry       | Theo quy định Viettel        |
| RPA-Engine            | Schedule CustomerProfile | /customerprofile/schedule | Schedule dữ liệu CustomerProfile trong RPA-Engine.    | Thông báo qua email | Tích hợp với CRM             |
| Infra-Network         | Analyze Queue            | /queue/analyze            | Analyze dữ liệu Queue trong Infra- Network.           | Không lỗi           | Theo chuẩn ISO 27001         |
| CRM- Platform         | Update DataLake          | /datalake/update          | Update dữ liệu DataLake trong CRM-Platform.           | Thông báo qua SMS   | Chỉ dùng cho admin           |
| QA- Automation        | Export AgentStatus       | /agentstatus/export       | Export dữ liệu AgentStatus trong QA-Automation.       | Đồng bộ dữ liệu     | Kết nối với hệ thống Billing |
| BCCS2- Billing        | Schedule SwitchConfig    | /switchconfig/schedule    | Schedule dữ liệu SwitchConfig trong BCCS2-Billing.    | Lỗi nghiêm trọng    | Tích hợp với CRM             |

<!-- image -->

## VIETTEL AI RACE

## DANH MỤC CHỨC NĂNG BCCS2

TD444

Lần ban hành: 1

| IVR-System          | Update Contact        | /contact/update        | Update dữ liệu Contact trong IVR- System.           | Hiển thị báo cáo   | Kết nối với hệ thống Billing   |
|---------------------|-----------------------|------------------------|-----------------------------------------------------|--------------------|--------------------------------|
| IVR-System          | Insert ClusterNode    | /clusternode/insert    | Insert dữ liệu ClusterNode trong IVR-System.        | Thông báo qua SMS  | Chạy theo lịch cron            |
| Security- Firewall  | Validate Campaign     | /campaign/validate     | Validate dữ liệu Campaign trong Security-Firewall.  | Hiển thị báo cáo   | Theo chuẩn ISO 27001           |
| IPCC- ContactCenter | Search Queue          | /queue/search          | Search dữ liệu Queue trong IPCC- ContactCenter.     | Tự động retry      | Chạy theo lịch cron            |
| IPCC- ContactCenter | Search Whitelist      | /whitelist/search      | Search dữ liệu Whitelist trong IPCC- ContactCenter. | Ghi log đầy đủ     | Theo quy định Viettel          |
| IVR-System          | Config FirewallPolicy | /firewallpolicy/config | Config dữ liệu FirewallPolicy trong IVR-System.     | Hiển thị báo cáo   | Bảo mật 2 lớp                  |
| QA- Automation      | Validate AccountLock  | /accountlock/validate  | Validate dữ liệu AccountLock trong QA-Automation.   | Tự động retry      | Tích hợp với CRM               |
| RPA-Engine          | Insert AccountLock    | /accountlock/insert    | Insert dữ liệu AccountLock trong RPA-Engine.        | Thông báo qua SMS  | Yêu cầu xác thực người dùng    |

<!-- image -->

## VIETTEL AI RACE

## DANH MỤC CHỨC NĂNG BCCS2

TD444

Lần ban hành: 1

| Infra-Network   | Insert Invoice          | /invoice/insert          | Insert dữ liệu Invoice trong Infra- Network.         | Thông báo qua SMS   | Chỉ dùng cho admin           |
|-----------------|-------------------------|--------------------------|------------------------------------------------------|---------------------|------------------------------|
| RPA-Engine      | Generate Whitelist      | /whitelist/generate      | Generate dữ liệu Whitelist trong RPA-Engine.         | Tự động retry       | Theo quy định Viettel        |
| BCCS2-Core      | Analyze Invoice         | /invoice/analyze         | Analyze dữ liệu Invoice trong BCCS2-Core.            | Thông báo qua email | Kết nối với hệ thống Billing |
| QA- Automation  | Generate FirewallPolicy | /firewallpolicy/generate | Generate dữ liệu FirewallPolicy trong QA-Automation. | Tự động retry       | Theo quy định Viettel        |
| Infra-Server    | Analyze AgentStatus     | /agentstatus/analyze     | Analyze dữ liệu AgentStatus trong Infra-Server.      | Đồng bộ dữ liệu     | Yêu cầu xác thực người dùng  |
| Infra-Server    | Export DataLake         | /datalake/export         | Export dữ liệu DataLake trong Infra-Server.          | Thành công          | Kết nối với hệ thống Billing |
| BCCS2-Core      | Insert PackagePlan      | /packageplan/insert      | Insert dữ liệu PackagePlan trong BCCS2-Core.         | Ghi log đầy đủ      | Dữ liệu backup mỗi ngày      |

<!-- image -->

## VIETTEL AI RACE

## DANH MỤC CHỨC NĂNG BCCS2

TD444

Lần ban hành: 1

| BCCS2-Core          | Delete DataLake        | /datalake/delete        | Delete dữ liệu DataLake trong BCCS2-Core.            | Ghi log đầy đủ   | Dữ liệu backup mỗi ngày     |
|---------------------|------------------------|-------------------------|------------------------------------------------------|------------------|-----------------------------|
| Infra-Server        | Validate DataLake      | /datalake/validate      | Validate dữ liệu DataLake trong Infra-Server.        | Không lỗi        | Chạy theo lịch cron         |
| Infra-Server        | Schedule QoS           | /qos/schedule           | Schedule dữ liệu QoS trong Infra- Server.            | Tự động retry    | Yêu cầu xác thực người dùng |
| RPA-Engine          | Search CustomerProfile | /customerprofile/search | Search dữ liệu CustomerProfile trong RPA-Engine.     | Hiển thị báo cáo | Dữ liệu backup mỗi ngày     |
| Infra-Server        | Update Lead            | /lead/update            | Update dữ liệu Lead trong Infra-Server.              | Không lỗi        | Có cơ chế rollback          |
| Security- Firewall  | Generate CDRReport     | /cdrreport/generate     | Generate dữ liệu CDRReport trong Security-Firewall.  | Đồng bộ dữ liệu  | Chỉ dùng cho admin          |
| Security- Firewall  | Monitor PackagePlan    | /packageplan/monitor    | Monitor dữ liệu PackagePlan trong Security-Firewall. | Cảnh báo         | Yêu cầu xác thực người dùng |
| IPCC- ContactCenter | Export FirewallPolicy  | /firewallpolicy/export  | Export dữ liệu FirewallPolicy trong                  | Thông báo        | Theo chuẩn                  |

<!-- image -->

## VIETTEL AI RACE

## DANH MỤC CHỨC NĂNG BCCS2

TD444

Lần ban hành: 1

|                     |                      |                       | IPCC- ContactCenter.                                   | qua SMS           | ISO 27001                    |
|---------------------|----------------------|-----------------------|--------------------------------------------------------|-------------------|------------------------------|
| Security- Firewall  | Import Promotion     | /promotion/import     | Import dữ liệu Promotion trong Security-Firewall.      | Ghi log đầy đủ    | Dữ liệu backup mỗi ngày      |
| BCCS2- Billing      | Delete KPIReport     | /kpireport/delete     | Delete dữ liệu KPIReport trong BCCS2-Billing.          | Thông báo qua SMS | Yêu cầu xác thực người dùng  |
| IPCC- ContactCenter | Import VPN           | /vpn/import           | Import dữ liệu VPN trong IPCC- ContactCenter.          | Cảnh báo          | Tích hợp với CRM             |
| IPCC- ContactCenter | Monitor Whitelist    | /whitelist/monitor    | Monitor dữ liệu Whitelist trong IPCC- ContactCenter.   | Ghi log đầy đủ    | Kết nối với hệ thống Billing |
| QA- Automation      | Optimize DebtControl | /debtcontrol/optimize | Optimize dữ liệu DebtControl trong QA-Automation.      | Lỗi nghiêm trọng  | Kết nối với hệ thống Billing |
| IPCC- ContactCenter | Insert SwitchConfig  | /switchconfig/insert  | Insert dữ liệu SwitchConfig trong IPCC- ContactCenter. | Tự động retry     | Kết nối với hệ thống Billing |
| IPCC- ContactCenter | Config CDRReport     | /cdrreport/config     | Config dữ liệu CDRReport trong IPCC- ContactCenter.    | Lỗi nghiêm trọng  | Theo quy định Viettel        |

<!-- image -->

## VIETTEL AI RACE

## DANH MỤC CHỨC NĂNG BCCS2

TD444

Lần ban hành: 1

| IPCC- ContactCenter   | Config PackagePlan    | /packageplan/config    | Config dữ liệu PackagePlan trong IPCC- ContactCenter.   | Ghi log đầy đủ    | Yêu cầu xác thực người dùng   |
|-----------------------|-----------------------|------------------------|---------------------------------------------------------|-------------------|-------------------------------|
| IPCC- ContactCenter   | Config AgentStatus    | /agentstatus/config    | Config dữ liệu AgentStatus trong IPCC- ContactCenter.   | Cảnh báo          | Có cơ chế rollback            |
| Security- Firewall    | Monitor IVRPrompt     | /ivrprompt/monitor     | Monitor dữ liệu IVRPrompt trong Security-Firewall.      | Ghi log đầy đủ    | Dữ liệu backup mỗi ngày       |
| RPA-Engine            | Update FirewallPolicy | /firewallpolicy/update | Update dữ liệu FirewallPolicy trong RPA-Engine.         | Hiển thị báo cáo  | Chạy theo lịch cron           |
| Infra-Server          | Delete Contact        | /contact/delete        | Delete dữ liệu Contact trong Infra- Server.             | Thông báo qua SMS | Theo quy định Viettel         |
| Infra-Network         | Insert Invoice        | /invoice/insert        | Insert dữ liệu Invoice trong Infra- Network.            | Đồng bộ dữ liệu   | Tích hợp với CRM              |
| QA- Automation        | Schedule Campaign     | /campaign/schedule     | Schedule dữ liệu Campaign trong QA- Automation.         | Ghi log đầy đủ    | Yêu cầu xác thực người dùng   |

<!-- image -->

## VIETTEL AI RACE

## DANH MỤC CHỨC NĂNG BCCS2

TD444

Lần ban hành: 1

| BCCS2- Billing      | Analyze Whitelist     | /whitelist/analyze     | Analyze dữ liệu Whitelist trong BCCS2-Billing.       | Thông báo qua SMS   | Yêu cầu xác thực người dùng   |
|---------------------|-----------------------|------------------------|------------------------------------------------------|---------------------|-------------------------------|
| Security- Firewall  | Generate CDRReport    | /cdrreport/generate    | Generate dữ liệu CDRReport trong Security-Firewall.  | Thành công          | Có cơ chế rollback            |
| IPCC- ContactCenter | Analyze Whitelist     | /whitelist/analyze     | Analyze dữ liệu Whitelist trong IPCC- ContactCenter. | Không lỗi           | Dữ liệu backup mỗi ngày       |
| QA- Automation      | Export Invoice        | /invoice/export        | Export dữ liệu Invoice trong QA- Automation.         | Hiển thị báo cáo    | Theo chuẩn ISO 27001          |
| IPCC- ContactCenter | Export QoS            | /qos/export            | Export dữ liệu QoS trong IPCC- ContactCenter.        | Cảnh báo            | Dữ liệu backup mỗi ngày       |
| BCCS2-Core          | Insert CDRReport      | /cdrreport/insert      | Insert dữ liệu CDRReport trong BCCS2-Core.           | Lỗi nghiêm trọng    | Kết nối với hệ thống Billing  |
| BCCS2-Core          | Update APIGateway     | /apigateway/update     | Update dữ liệu APIGateway trong BCCS2-Core.          | Tự động retry       | Chỉ dùng cho admin            |
| Infra-Server        | Export TransactionLog | /transactionlog/export | Export dữ liệu TransactionLog trong Infra-Server.    | Cảnh báo            | Theo chuẩn                    |

<!-- image -->

TD444

Lần ban hành: 1

## VIETTEL AI RACE

## DANH MỤC CHỨC NĂNG BCCS2

|                    |                     |                      |                                                      |                  | ISO 27001             |
|--------------------|---------------------|----------------------|------------------------------------------------------|------------------|-----------------------|
| Infra-Server       | Update Contact      | /contact/update      | Update dữ liệu Contact trong Infra- Server.          | Cảnh báo         | Theo quy định Viettel |
| CRM- Platform      | Insert CDRReport    | /cdrreport/insert    | Insert dữ liệu CDRReport trong CRM-Platform.         | Thành công       | Bảo mật 2 lớp         |
| BCCS2-Core         | Export KPIReport    | /kpireport/export    | Export dữ liệu KPIReport trong BCCS2-Core.           | Hiển thị báo cáo | Tích hợp với CRM      |
| IVR-System         | Monitor APIGateway  | /apigateway/monitor  | Monitor dữ liệu APIGateway trong IVR-System.         | Ghi log đầy đủ   | Theo quy định Viettel |
| Security- Firewall | Import Queue        | /queue/import        | Import dữ liệu Queue trong Security-Firewall.        | Cảnh báo         | Bảo mật 2 lớp         |
| BCCS2-Core         | Import Queue        | /queue/import        | Import dữ liệu Queue trong BCCS2-Core.               | Đồng bộ dữ liệu  | Chạy theo lịch cron   |
| IVR-System         | Analyze Campaign    | /campaign/analyze    | Analyze dữ liệu Campaign trong IVR-System.           | Ghi log đầy đủ   | Chỉ dùng cho admin    |
| Security- Firewall | Generate APIGateway | /apigateway/generate | Generate dữ liệu APIGateway trong Security-Firewall. | Đồng bộ dữ liệu  | Kết nối với hệ        |

<!-- image -->

## VIETTEL AI RACE

## DANH MỤC CHỨC NĂNG BCCS2

TD444

Lần ban hành: 1

|                     |                    |                     |                                                       |                   | thống Billing                |
|---------------------|--------------------|---------------------|-------------------------------------------------------|-------------------|------------------------------|
| CRM- Platform       | Monitor Promotion  | /promotion/monitor  | Monitor dữ liệu Promotion trong CRM-Platform.         | Cảnh báo          | Tích hợp với CRM             |
| Security- Firewall  | Monitor Whitelist  | /whitelist/monitor  | Monitor dữ liệu Whitelist trong Security-Firewall.    | Thông báo qua SMS | Theo chuẩn ISO 27001         |
| IPCC- ContactCenter | Delete PackagePlan | /packageplan/delete | Delete dữ liệu PackagePlan trong IPCC- ContactCenter. | Thành công        | Yêu cầu xác thực người dùng  |
| IVR-System          | Insert DebtControl | /debtcontrol/insert | Insert dữ liệu DebtControl trong IVR-System.          | Lỗi nghiêm trọng  | Yêu cầu xác thực người dùng  |
| Infra-Server        | Optimize Whitelist | /whitelist/optimize | Optimize dữ liệu Whitelist trong Infra-Server.        | Tự động retry     | Dữ liệu backup mỗi ngày      |
| Infra-Network       | Monitor Promotion  | /promotion/monitor  | Monitor dữ liệu Promotion trong Infra-Network.        | Hiển thị báo cáo  | Kết nối với hệ thống Billing |
| BCCS2-Core          | Import IVRPrompt   | /ivrprompt/import   | Import dữ liệu IVRPrompt trong BCCS2-Core.            | Không lỗi         | Theo chuẩn ISO 27001         |

<!-- image -->

## VIETTEL AI RACE

## DANH MỤC CHỨC NĂNG BCCS2

TD444

Lần ban hành: 1

| IVR-System     | Validate TransactionLog   | /transactionlog/validate   | Validate dữ liệu TransactionLog trong IVR-System.   | Ghi log đầy đủ   | Chạy theo lịch cron     |
|----------------|---------------------------|----------------------------|-----------------------------------------------------|------------------|-------------------------|
| BCCS2-Core     | Import CustomerProfile    | /customerprofile/import    | Import dữ liệu CustomerProfile trong BCCS2-Core.    | Lỗi nghiêm trọng | Dữ liệu backup mỗi ngày |
| BCCS2- Billing | Optimize QoS              | /qos/optimize              | Optimize dữ liệu QoS trong BCCS2- Billing.          | Cảnh báo         | Theo quy định Viettel   |
| BCCS2-Core     | Schedule Queue            | /queue/schedule            | Schedule dữ liệu Queue trong BCCS2-Core.            | Cảnh báo         | Có cơ chế rollback      |
| CRM- Platform  | Optimize ClusterNode      | /clusternode/optimize      | Optimize dữ liệu ClusterNode trong CRM-Platform.    | Lỗi nghiêm trọng | Chạy theo lịch cron     |
| CRM- Platform  | Delete FirewallPolicy     | /firewallpolicy/delete     | Delete dữ liệu FirewallPolicy trong CRM-Platform.   | Tự động retry    | Chỉ dùng cho admin      |
| Infra-Server   | Export Whitelist          | /whitelist/export          | Export dữ liệu Whitelist trong Infra-Server.        | Thành công       | Chạy theo lịch cron     |
| Infra-Server   | Import CDRReport          | /cdrreport/import          | Import dữ liệu CDRReport trong Infra-Server.        | Đồng bộ dữ liệu  | Tích hợp với CRM        |

<!-- image -->

## VIETTEL AI RACE

## DANH MỤC CHỨC NĂNG BCCS2

TD444

Lần ban hành: 1

| Infra-Server        | Update KPIReport   | /kpireport/update   | Update dữ liệu KPIReport trong Infra-Server.       | Tự động retry     | Có cơ chế rollback          |
|---------------------|--------------------|---------------------|----------------------------------------------------|-------------------|-----------------------------|
| BCCS2- Billing      | Config Lead        | /lead/config        | Config dữ liệu Lead trong BCCS2- Billing.          | Đồng bộ dữ liệu   | Có cơ chế rollback          |
| CRM- Platform       | Analyze Blacklist  | /blacklist/analyze  | Analyze dữ liệu Blacklist trong CRM-Platform.      | Cảnh báo          | Chạy theo lịch cron         |
| QA- Automation      | Update Whitelist   | /whitelist/update   | Update dữ liệu Whitelist trong QA- Automation.     | Thông báo qua SMS | Tích hợp với CRM            |
| IPCC- ContactCenter | Monitor Invoice    | /invoice/monitor    | Monitor dữ liệu Invoice trong IPCC- ContactCenter. | Ghi log đầy đủ    | Bảo mật 2 lớp               |
| CRM- Platform       | Export Invoice     | /invoice/export     | Export dữ liệu Invoice trong CRM- Platform.        | Lỗi nghiêm trọng  | Yêu cầu xác thực người dùng |
| Infra-Server        | Import KPIReport   | /kpireport/import   | Import dữ liệu KPIReport trong Infra-Server.       | Tự động retry     | Chạy theo lịch cron         |
| QA- Automation      | Validate Lead      | /lead/validate      | Validate dữ liệu Lead trong QA- Automation.        | Thành công        | Chỉ dùng cho admin          |

<!-- image -->

## VIETTEL AI RACE

## DANH MỤC CHỨC NĂNG BCCS2

TD444

Lần ban hành: 1

| Infra-Server       | Update VPN         | /vpn/update         | Update dữ liệu VPN trong Infra-Server.             | Thông báo qua email   | Yêu cầu xác thực người dùng   |
|--------------------|--------------------|---------------------|----------------------------------------------------|-----------------------|-------------------------------|
| Infra-Network      | Search VPN         | /vpn/search         | Search dữ liệu VPN trong Infra-Network.            | Thông báo qua email   | Chạy theo lịch cron           |
| BCCS2- Billing     | Export APIGateway  | /apigateway/export  | Export dữ liệu APIGateway trong BCCS2-Billing.     | Đồng bộ dữ liệu       | Yêu cầu xác thực người dùng   |
| Infra-Network      | Import KPIReport   | /kpireport/import   | Import dữ liệu KPIReport trong Infra-Network.      | Thông báo qua email   | Kết nối với hệ thống Billing  |
| Security- Firewall | Export APIGateway  | /apigateway/export  | Export dữ liệu APIGateway trong Security-Firewall. | Tự động retry         | Theo chuẩn ISO 27001          |
| Infra-Server       | Schedule Blacklist | /blacklist/schedule | Schedule dữ liệu Blacklist trong Infra- Server.    | Hiển thị báo cáo      | Yêu cầu xác thực người dùng   |
| QA- Automation     | Schedule Blacklist | /blacklist/schedule | Schedule dữ liệu Blacklist trong QA- Automation.   | Tự động retry         | Tích hợp với CRM              |

<!-- image -->

## VIETTEL AI RACE

## DANH MỤC CHỨC NĂNG BCCS2

TD444

Lần ban hành: 1

| Infra-Server   | Monitor CustomerProfile   | /customerprofile/monitor   | Monitor dữ liệu CustomerProfile trong Infra-Server.   | Đồng bộ dữ liệu   | Chỉ dùng cho admin           |
|----------------|---------------------------|----------------------------|-------------------------------------------------------|-------------------|------------------------------|
| IVR-System     | Generate PackagePlan      | /packageplan/generate      | Generate dữ liệu PackagePlan trong IVR-System.        | Thông báo qua SMS | Có cơ chế rollback           |
| BCCS2-Core     | Optimize IVRPrompt        | /ivrprompt/optimize        | Optimize dữ liệu IVRPrompt trong BCCS2-Core.          | Đồng bộ dữ liệu   | Yêu cầu xác thực người dùng  |
| Infra-Network  | Delete Whitelist          | /whitelist/delete          | Delete dữ liệu Whitelist trong Infra-Network.         | Lỗi nghiêm trọng  | Theo chuẩn ISO 27001         |
| Infra-Server   | Delete PackagePlan        | /packageplan/delete        | Delete dữ liệu PackagePlan trong Infra-Server.        | Không lỗi         | Theo chuẩn ISO 27001         |
| RPA-Engine     | Update IVRPrompt          | /ivrprompt/update          | Update dữ liệu IVRPrompt trong RPA-Engine.            | Thông báo qua SMS | Theo quy định Viettel        |
| IVR-System     | Generate Blacklist        | /blacklist/generate        | Generate dữ liệu Blacklist trong IVR- System.         | Thành công        | Kết nối với hệ thống Billing |

<!-- image -->

## VIETTEL AI RACE

## DANH MỤC CHỨC NĂNG BCCS2

TD444

Lần ban hành: 1

| RPA-Engine          | Analyze CDRReport      | /cdrreport/analyze      | Analyze dữ liệu CDRReport trong RPA-Engine.         | Hiển thị báo cáo    | Tích hợp với CRM            |
|---------------------|------------------------|-------------------------|-----------------------------------------------------|---------------------|-----------------------------|
| IPCC- ContactCenter | Search Contact         | /contact/search         | Search dữ liệu Contact trong IPCC- ContactCenter.   | Thành công          | Chỉ dùng cho admin          |
| IVR-System          | Analyze FirewallPolicy | /firewallpolicy/analyze | Analyze dữ liệu FirewallPolicy trong IVR-System.    | Không lỗi           | Yêu cầu xác thực người dùng |
| Infra-Network       | Search IVRPrompt       | /ivrprompt/search       | Search dữ liệu IVRPrompt trong Infra-Network.       | Thông báo qua email | Yêu cầu xác thực người dùng |
| Infra-Network       | Schedule VPN           | /vpn/schedule           | Schedule dữ liệu VPN trong Infra- Network.          | Hiển thị báo cáo    | Chỉ dùng cho admin          |
| IVR-System          | Monitor TransactionLog | /transactionlog/monitor | Monitor dữ liệu TransactionLog trong IVR-System.    | Tự động retry       | Yêu cầu xác thực người dùng |
| QA- Automation      | Monitor StorageVolume  | /storagevolume/monitor  | Monitor dữ liệu StorageVolume trong QA- Automation. | Thông báo qua email | Tích hợp với CRM            |

<!-- image -->

## VIETTEL AI RACE

## DANH MỤC CHỨC NĂNG BCCS2

TD444

Lần ban hành: 1

| BCCS2- Billing   | Insert FirewallPolicy   | /firewallpolicy/insert   | Insert dữ liệu FirewallPolicy trong BCCS2-Billing.   | Thông báo qua email   | Dữ liệu backup mỗi ngày   |
|------------------|-------------------------|--------------------------|------------------------------------------------------|-----------------------|---------------------------|
| RPA-Engine       | Optimize Campaign       | /campaign/optimize       | Optimize dữ liệu Campaign trong RPA-Engine.          | Tự động retry         | Dữ liệu backup mỗi ngày   |