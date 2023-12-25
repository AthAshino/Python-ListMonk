# ImportSubscribersRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**params** | **str** |  | [optional] 
**file** | **str** |  | [optional] 

## Example

```python
from listmonk.models.import_subscribers_request import ImportSubscribersRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ImportSubscribersRequest from a JSON string
import_subscribers_request_instance = ImportSubscribersRequest.from_json(json)
# print the JSON string representation of the object
print
ImportSubscribersRequest.to_json()

# convert the object into a dict
import_subscribers_request_dict = import_subscribers_request_instance.to_dict()
# create an instance of ImportSubscribersRequest from a dict
import_subscribers_request_form_dict = import_subscribers_request.from_dict(import_subscribers_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


