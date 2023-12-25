# GetSubscribers200ResponseData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[Subscriber]**](Subscriber.md) |  | [optional] 
**query** | **str** |  | [optional] 
**total** | **int** |  | [optional] 
**per_page** | **int** |  | [optional] 
**page** | **int** |  | [optional] 

## Example

```python
from listmonk.models.get_subscribers200_response_data import GetSubscribers200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of GetSubscribers200ResponseData from a JSON string
get_subscribers200_response_data_instance = GetSubscribers200ResponseData.from_json(json)
# print the JSON string representation of the object
print
GetSubscribers200ResponseData.to_json()

# convert the object into a dict
get_subscribers200_response_data_dict = get_subscribers200_response_data_instance.to_dict()
# create an instance of GetSubscribers200ResponseData from a dict
get_subscribers200_response_data_form_dict = get_subscribers200_response_data.from_dict(get_subscribers200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


