# GetImportSubscribers200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ImportStatus**](ImportStatus.md) |  | [optional] 

## Example

```python
from listmonk_client.models.get_import_subscribers200_response import GetImportSubscribers200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetImportSubscribers200Response from a JSON string
get_import_subscribers200_response_instance = GetImportSubscribers200Response.from_json(json)
# print the JSON string representation of the object
print
GetImportSubscribers200Response.to_json()

# convert the object into a dict
get_import_subscribers200_response_dict = get_import_subscribers200_response_instance.to_dict()
# create an instance of GetImportSubscribers200Response from a dict
get_import_subscribers200_response_form_dict = get_import_subscribers200_response.from_dict(
    get_import_subscribers200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


