# DashboardCountDataSubscribers


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** |  | [optional] 
**blocklisted** | **object** |  | [optional] 
**orphans** | **int** |  | [optional] 

## Example

```python
from listmonk_client.models.dashboard_count_data_subscribers import DashboardCountDataSubscribers

# TODO update the JSON string below
json = "{}"
# create an instance of DashboardCountDataSubscribers from a JSON string
dashboard_count_data_subscribers_instance = DashboardCountDataSubscribers.from_json(json)
# print the JSON string representation of the object
print
DashboardCountDataSubscribers.to_json()

# convert the object into a dict
dashboard_count_data_subscribers_dict = dashboard_count_data_subscribers_instance.to_dict()
# create an instance of DashboardCountDataSubscribers from a dict
dashboard_count_data_subscribers_form_dict = dashboard_count_data_subscribers.from_dict(dashboard_count_data_subscribers_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


