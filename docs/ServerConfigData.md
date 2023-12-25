# ServerConfigData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**messengers** | **List[str]** |  | [optional] 
**langs** | [**List[ServerConfigDataLangsInner]**](ServerConfigDataLangsInner.md) |  | [optional] 
**lang** | **str** |  | [optional] 
**update** | **str** |  | [optional] 
**needs_restart** | **bool** |  | [optional] 
**version** | **str** |  | [optional] 

## Example

```python
from listmonk.models.server_config_data import ServerConfigData

# TODO update the JSON string below
json = "{}"
# create an instance of ServerConfigData from a JSON string
server_config_data_instance = ServerConfigData.from_json(json)
# print the JSON string representation of the object
print
ServerConfigData.to_json()

# convert the object into a dict
server_config_data_dict = server_config_data_instance.to_dict()
# create an instance of ServerConfigData from a dict
server_config_data_form_dict = server_config_data.from_dict(server_config_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


