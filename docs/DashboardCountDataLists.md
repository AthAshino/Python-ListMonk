# DashboardCountDataLists


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** |  | [optional] 
**private** | **int** |  | [optional] 
**public** | **int** |  | [optional] 
**optin_single** | **int** |  | [optional] 
**optin_double** | **int** |  | [optional] 

## Example

```python
from listmonk_client.models.dashboard_count_data_lists import DashboardCountDataLists

# TODO update the JSON string below
json = "{}"
# create an instance of DashboardCountDataLists from a JSON string
dashboard_count_data_lists_instance = DashboardCountDataLists.from_json(json)
# print the JSON string representation of the object
print
DashboardCountDataLists.to_json()

# convert the object into a dict
dashboard_count_data_lists_dict = dashboard_count_data_lists_instance.to_dict()
# create an instance of DashboardCountDataLists from a dict
dashboard_count_data_lists_form_dict = dashboard_count_data_lists.from_dict(dashboard_count_data_lists_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


