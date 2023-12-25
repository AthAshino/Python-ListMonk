# DashboardCountData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subscribers** | [**DashboardCountDataSubscribers**](DashboardCountDataSubscribers.md) |  | [optional] 
**lists** | [**DashboardCountDataLists**](DashboardCountDataLists.md) |  | [optional] 
**campaigns** | [**DashboardCountDataCampaigns**](DashboardCountDataCampaigns.md) |  | [optional] 
**messages** | **int** |  | [optional] 

## Example

```python
from listmonk_client.models.dashboard_count_data import DashboardCountData

# TODO update the JSON string below
json = "{}"
# create an instance of DashboardCountData from a JSON string
dashboard_count_data_instance = DashboardCountData.from_json(json)
# print the JSON string representation of the object
print
DashboardCountData.to_json()

# convert the object into a dict
dashboard_count_data_dict = dashboard_count_data_instance.to_dict()
# create an instance of DashboardCountData from a dict
dashboard_count_data_form_dict = dashboard_count_data.from_dict(dashboard_count_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


