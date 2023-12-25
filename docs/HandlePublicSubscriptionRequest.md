# HandlePublicSubscriptionRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**list_uuids** | **List[str]** |  | [optional] 

## Example

```python
from listmonk_client.models.handle_public_subscription_request import HandlePublicSubscriptionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of HandlePublicSubscriptionRequest from a JSON string
handle_public_subscription_request_instance = HandlePublicSubscriptionRequest.from_json(json)
# print the JSON string representation of the object
print
HandlePublicSubscriptionRequest.to_json()

# convert the object into a dict
handle_public_subscription_request_dict = handle_public_subscription_request_instance.to_dict()
# create an instance of HandlePublicSubscriptionRequest from a dict
handle_public_subscription_request_form_dict = handle_public_subscription_request.from_dict(
    handle_public_subscription_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


