# GetMedia200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[MediaFileObject]**](MediaFileObject.md) |  | [optional] 

## Example

```python
from listmonk.models.get_media200_response import GetMedia200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetMedia200Response from a JSON string
get_media200_response_instance = GetMedia200Response.from_json(json)
# print the JSON string representation of the object
print
GetMedia200Response.to_json()

# convert the object into a dict
get_media200_response_dict = get_media200_response_instance.to_dict()
# create an instance of GetMedia200Response from a dict
get_media200_response_form_dict = get_media200_response.from_dict(get_media200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


