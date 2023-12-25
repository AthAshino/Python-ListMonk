# NewList


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**optin** | **str** |  | [optional] 
**tags** | **List[str]** |  | [optional] 

## Example

```python
from listmonk.models.new_list import NewList

# TODO update the JSON string below
json = "{}"
# create an instance of NewList from a JSON string
new_list_instance = NewList.from_json(json)
# print the JSON string representation of the object
print
NewList.to_json()

# convert the object into a dict
new_list_dict = new_list_instance.to_dict()
# create an instance of NewList from a dict
new_list_form_dict = new_list.from_dict(new_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


