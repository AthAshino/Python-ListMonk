# GetServerConfig200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ServerConfig**](ServerConfig.md) |  | [optional] 

## Example

```python
from listmonk.models.get_server_config200_response import GetServerConfig200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetServerConfig200Response from a JSON string
get_server_config200_response_instance = GetServerConfig200Response.from_json(json)
# print the JSON string representation of the object
print
GetServerConfig200Response.to_json()

# convert the object into a dict
get_server_config200_response_dict = get_server_config200_response_instance.to_dict()
# create an instance of GetServerConfig200Response from a dict
get_server_config200_response_form_dict = get_server_config200_response.from_dict(get_server_config200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


