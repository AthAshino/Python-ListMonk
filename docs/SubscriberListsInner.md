# SubscriberListsInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subscription_status** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**uuid** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**tags** | **List[str]** |  | [optional] 
**created_at** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 

## Example

```python
from listmonk.models.subscriber_lists_inner import SubscriberListsInner

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriberListsInner from a JSON string
subscriber_lists_inner_instance = SubscriberListsInner.from_json(json)
# print the JSON string representation of the object
print
SubscriberListsInner.to_json()

# convert the object into a dict
subscriber_lists_inner_dict = subscriber_lists_inner_instance.to_dict()
# create an instance of SubscriberListsInner from a dict
subscriber_lists_inner_form_dict = subscriber_lists_inner.from_dict(subscriber_lists_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


