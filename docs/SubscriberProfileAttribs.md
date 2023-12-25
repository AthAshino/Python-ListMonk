# SubscriberProfileAttribs


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**city** | **str** |  | [optional] 
**good** | **bool** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from listmonk.models.subscriber_profile_attribs import SubscriberProfileAttribs

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriberProfileAttribs from a JSON string
subscriber_profile_attribs_instance = SubscriberProfileAttribs.from_json(json)
# print the JSON string representation of the object
print
SubscriberProfileAttribs.to_json()

# convert the object into a dict
subscriber_profile_attribs_dict = subscriber_profile_attribs_instance.to_dict()
# create an instance of SubscriberProfileAttribs from a dict
subscriber_profile_attribs_form_dict = subscriber_profile_attribs.from_dict(subscriber_profile_attribs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


