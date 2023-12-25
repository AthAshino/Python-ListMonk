# Subscriber


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**created_at** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**uuid** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**attribs** | [**SubscriberProfileAttribs**](SubscriberProfileAttribs.md) |  | [optional] 
**status** | **str** |  | [optional] 
**lists** | [**List[SubscriberListsInner]**](SubscriberListsInner.md) |  | [optional] 

## Example

```python
from listmonk.models.subscriber import Subscriber

# TODO update the JSON string below
json = "{}"
# create an instance of Subscriber from a JSON string
subscriber_instance = Subscriber.from_json(json)
# print the JSON string representation of the object
print
Subscriber.to_json()

# convert the object into a dict
subscriber_dict = subscriber_instance.to_dict()
# create an instance of Subscriber from a dict
subscriber_form_dict = subscriber.from_dict(subscriber_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


