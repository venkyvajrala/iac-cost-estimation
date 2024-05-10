## Cloud cost estimation tools comparison

<br>
This table provides a comparison of various cloud tools and their features across different cloud providers:
</br>

| Name                                   | Usable | Pipeline integration | Open source | All services supported | Multi cloud | Cloud native solution | Additional features | Cloud             |
| -------------------------------------- | ------ | -------------------- | ----------- | ---------------------- | ----------- | --------------------- | ------------------- | ----------------- |
| Aws cloudformation cli                 | ✅     | ✅                   | ✅          | 🟢                     | 🔴          | ✅                    | 🔴                  | AWS               |
| arm-estimator                          | ✅     | ✅                   | ✅          | 🟠                     | 🔴          | 🔴                    | 🔴                  | Azure             |
| Scalr [Enterprise available]           | ✅     | ✅                   | 🔴          | 🟢                     | ✅          | 🔴                    | ✅                  | GCP , AWS , Azure |
| Terraform cloud [Enterprise available] | ✅     | ✅                   | 🔴          | 🟢                     | ✅          | 🔴                    | ✅                  | GCP , AWS , Azure |
| terraform-aws-pricing                  | ✅     | ✅                   | ✅          | 🟠                     | 🔴          | 🔴                    | 🔴                  | AWS               |
| terracost                              | ✅     | ✅                   | ✅          | 🔴                     | 🟠          | 🔴                    | 🔴                  | GCP , AWS , Azure |
| CSPARMPricingCalculator                | 🔴     | 🔴                   | 🔴          | 🔴                     | 🔴          | 🔴                    | 🔴                  | Azure             |
| Infracost [Enterprise available]       | ✅     | ✅                   | ✅          | 🟢                     | ✅          | 🔴                    | ✅                  | GCP , AWS , Azure |

                                                ✅ = YES      🟢 = Most

                                                🔴 = NO       🟠 = Few

> [!NOTE]
> All the additional features supported tools have dashboards ,policies to control cost,reports generation,notification triggers

<hr>
<br>

<b>Date: May 9th 2024</b>

### Our Recommendation:

### Infracost

<b>Compatibility:</b> Infracost is compatible with both Terraform and OpenTofu, making it a versatile tool for cloud infrastructure management.<br><br>
<b>Integrations:</b> Infracost can seamlessly integrate with Scalr and Terraform Cloud, expanding its functionality and ease of use.<br><br>
<b>CI/CD Support:</b> Infracost supports continuous integration and continuous deployment (CI/CD) processes, streamlining your development and deployment workflows.<br><br>
<b>Tagging Policies and Guardrails:</b> You can leverage Infracost to apply tagging policies and implement guardrails for better governance and cost management.<br><br>
<br><br>


> [!NOTE]
> You can estimate your costs with the pricing calculators provided by major cloud providers: <br>
> - AWS Pricing Calculator: [Click here](https://calculator.aws/)
> - Microsoft Azure Pricing Calculator [Click here](https://azure.microsoft.com/en-in/pricing/calculator/)
> - Google Cloud Pricing Calculator [Click here](https://cloud.google.com/products/calculator)
