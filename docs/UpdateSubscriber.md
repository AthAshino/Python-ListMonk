# UpdateSubscriber


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**lists** | **List[int]** |  | [optional] 
**list_uuids** | **List[str]** |  | [optional] 
**preconfirm_subscriptions** | **bool** |  | [optional] 
**attribs** | [**NewSubscriberAttribs**](NewSubscriberAttribs.md) |  | [optional] 

## Example

```python
from listmonk.models.update_subscriber import UpdateSubscriber

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateSubscriber from a JSON string
update_subscriber_instance = UpdateSubscriber.from_json(json)
# print the JSON string representation of the object
print
UpdateSubscriber.to_json()

# convert the object into a dict
update_subscriber_dict = update_subscriber_instance.to_dict()
# create an instance of UpdateSubscriber from a dict
update_subscriber_form_dict = update_subscriber.from_dict(update_subscriber_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


