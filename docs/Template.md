# Template


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**created_at** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**body** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**is_default** | **bool** |  | [optional] 

## Example

```python
from listmonk.models.template import Template

# TODO update the JSON string below
json = "{}"
# create an instance of Template from a JSON string
template_instance = Template.from_json(json)
# print the JSON string representation of the object
print
Template.to_json()

# convert the object into a dict
template_dict = template_instance.to_dict()
# create an instance of Template from a dict
template_form_dict = template.from_dict(template_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


