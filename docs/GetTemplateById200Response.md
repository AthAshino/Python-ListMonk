# GetTemplateById200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**Template**](Template.md) |  | [optional] 

## Example

```python
from listmonk.models.get_template_by_id200_response import GetTemplateById200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetTemplateById200Response from a JSON string
get_template_by_id200_response_instance = GetTemplateById200Response.from_json(json)
# print the JSON string representation of the object
print
GetTemplateById200Response.to_json()

# convert the object into a dict
get_template_by_id200_response_dict = get_template_by_id200_response_instance.to_dict()
# create an instance of GetTemplateById200Response from a dict
get_template_by_id200_response_form_dict = get_template_by_id200_response.from_dict(get_template_by_id200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


