## ARM template cost estimation



1. Download binary from release page: https://github.com/TheCloudTheory/arm-estimator/tags

2. Extract the zip folder, you will find binary named `azure-cost-estimator` to use

3. Run below command to get cost estimation

```
 ./azure-cost-estimator ../arm-template.json <azure subscription-id> <resource group name> 
```


Output:
You can find output log  [here](./output.log)