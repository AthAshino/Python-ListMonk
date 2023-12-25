# SubscriberProfile


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**uuid** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**attribs** | [**SubscriberProfileAttribs**](SubscriberProfileAttribs.md) |  | [optional] 
**status** | **str** |  | [optional] 
**created_at** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 

## Example

```python
from listmonk.models.subscriber_profile import SubscriberProfile

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriberProfile from a JSON string
subscriber_profile_instance = SubscriberProfile.from_json(json)
# print the JSON string representation of the object
print
SubscriberProfile.to_json()

# convert the object into a dict
subscriber_profile_dict = subscriber_profile_instance.to_dict()
# create an instance of SubscriberProfile from a dict
subscriber_profile_form_dict = subscriber_profile.from_dict(subscriber_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


