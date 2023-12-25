# Subscriptions


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subscription_status** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**created_at** | **str** |  | [optional] 

## Example

```python
from listmonk.models.subscriptions import Subscriptions

# TODO update the JSON string below
json = "{}"
# create an instance of Subscriptions from a JSON string
subscriptions_instance = Subscriptions.from_json(json)
# print the JSON string representation of the object
print
Subscriptions.to_json()

# convert the object into a dict
subscriptions_dict = subscriptions_instance.to_dict()
# create an instance of Subscriptions from a dict
subscriptions_form_dict = subscriptions.from_dict(subscriptions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


