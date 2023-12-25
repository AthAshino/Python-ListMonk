# NewSubscriberAttribs


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**city** | **str** |  | [optional] 
**projects** | **int** |  | [optional] 
**stack** | [**NewSubscriberAttribsStack**](NewSubscriberAttribsStack.md) |  | [optional] 

## Example

```python
from listmonk.models.new_subscriber_attribs import NewSubscriberAttribs

# TODO update the JSON string below
json = "{}"
# create an instance of NewSubscriberAttribs from a JSON string
new_subscriber_attribs_instance = NewSubscriberAttribs.from_json(json)
# print the JSON string representation of the object
print
NewSubscriberAttribs.to_json()

# convert the object into a dict
new_subscriber_attribs_dict = new_subscriber_attribs_instance.to_dict()
# create an instance of NewSubscriberAttribs from a dict
new_subscriber_attribs_form_dict = new_subscriber_attribs.from_dict(new_subscriber_attribs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


