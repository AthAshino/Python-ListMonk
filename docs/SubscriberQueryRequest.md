# SubscriberQueryRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query** | **str** |  | [optional] 
**ids** | **List[int]** | The ids of the subscribers to be modified. | [optional] 
**action** | **str** | Whether to add, remove, or unsubscribe the users. | [optional] 
**target_list_ids** | **List[int]** | The ids of the lists to be modified. | [optional] 
**status** | **str** | confirmed, unconfirmed, or unsubscribed status. | [optional] 

## Example

```python
from listmonk_client.models.subscriber_query_request import SubscriberQueryRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriberQueryRequest from a JSON string
subscriber_query_request_instance = SubscriberQueryRequest.from_json(json)
# print the JSON string representation of the object
print
SubscriberQueryRequest.to_json()

# convert the object into a dict
subscriber_query_request_dict = subscriber_query_request_instance.to_dict()
# create an instance of SubscriberQueryRequest from a dict
subscriber_query_request_form_dict = subscriber_query_request.from_dict(subscriber_query_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


