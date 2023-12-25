# TransactionalMessage


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subscriber_email** | **str** |  | [optional] 
**subscriber_id** | **int** |  | [optional] 
**template_id** | **int** |  | [optional] 
**from_email** | **str** |  | [optional] 
**data** | **object** |  | [optional] 
**headers** | **List[object]** |  | [optional] 
**messenger** | **str** |  | [optional] 
**content_type** | **str** |  | [optional] 

## Example

```python
from listmonk.models.transactional_message import TransactionalMessage

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionalMessage from a JSON string
transactional_message_instance = TransactionalMessage.from_json(json)
# print the JSON string representation of the object
print
TransactionalMessage.to_json()

# convert the object into a dict
transactional_message_dict = transactional_message_instance.to_dict()
# create an instance of TransactionalMessage from a dict
transactional_message_form_dict = transactional_message.from_dict(transactional_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


