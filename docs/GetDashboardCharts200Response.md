# GetDashboardCharts200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**DashboardChart**](DashboardChart.md) |  | [optional] 

## Example

```python
from listmonk.models.get_dashboard_charts200_response import GetDashboardCharts200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetDashboardCharts200Response from a JSON string
get_dashboard_charts200_response_instance = GetDashboardCharts200Response.from_json(json)
# print the JSON string representation of the object
print
GetDashboardCharts200Response.to_json()

# convert the object into a dict
get_dashboard_charts200_response_dict = get_dashboard_charts200_response_instance.to_dict()
# create an instance of GetDashboardCharts200Response from a dict
get_dashboard_charts200_response_form_dict = get_dashboard_charts200_response.from_dict(get_dashboard_charts200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


