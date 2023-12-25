# GetDashboardCounts200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**DashboardCount**](DashboardCount.md) |  | [optional] 

## Example

```python
from listmonk_client.models.get_dashboard_counts200_response import GetDashboardCounts200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetDashboardCounts200Response from a JSON string
get_dashboard_counts200_response_instance = GetDashboardCounts200Response.from_json(json)
# print the JSON string representation of the object
print
GetDashboardCounts200Response.to_json()

# convert the object into a dict
get_dashboard_counts200_response_dict = get_dashboard_counts200_response_instance.to_dict()
# create an instance of GetDashboardCounts200Response from a dict
get_dashboard_counts200_response_form_dict = get_dashboard_counts200_response.from_dict(get_dashboard_counts200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


