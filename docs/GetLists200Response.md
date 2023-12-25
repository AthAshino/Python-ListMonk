# GetLists200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**GetLists200ResponseData**](GetLists200ResponseData.md) |  | [optional] 

## Example

```python
from listmonk.models.get_lists200_response import GetLists200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetLists200Response from a JSON string
get_lists200_response_instance = GetLists200Response.from_json(json)
# print the JSON string representation of the object
print
GetLists200Response.to_json()

# convert the object into a dict
get_lists200_response_dict = get_lists200_response_instance.to_dict()
# create an instance of GetLists200Response from a dict
get_lists200_response_form_dict = get_lists200_response.from_dict(get_lists200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


