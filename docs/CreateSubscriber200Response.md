# CreateSubscriber200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**Subscriber**](Subscriber.md) |  | [optional] 

## Example

```python
from listmonk.models.create_subscriber200_response import CreateSubscriber200Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSubscriber200Response from a JSON string
create_subscriber200_response_instance = CreateSubscriber200Response.from_json(json)
# print the JSON string representation of the object
print
CreateSubscriber200Response.to_json()

# convert the object into a dict
create_subscriber200_response_dict = create_subscriber200_response_instance.to_dict()
# create an instance of CreateSubscriber200Response from a dict
create_subscriber200_response_form_dict = create_subscriber200_response.from_dict(create_subscriber200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


