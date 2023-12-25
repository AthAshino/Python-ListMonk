# NewSubscriber


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
from listmonk_client.models.new_subscriber import NewSubscriber

# TODO update the JSON string below
json = "{}"
# create an instance of NewSubscriber from a JSON string
new_subscriber_instance = NewSubscriber.from_json(json)
# print the JSON string representation of the object
print
NewSubscriber.to_json()

# convert the object into a dict
new_subscriber_dict = new_subscriber_instance.to_dict()
# create an instance of NewSubscriber from a dict
new_subscriber_form_dict = new_subscriber.from_dict(new_subscriber_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


