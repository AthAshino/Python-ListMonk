# UploadMedia200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**MediaFileObject**](MediaFileObject.md) |  | [optional] 

## Example

```python
from listmonk.models.upload_media200_response import UploadMedia200Response

# TODO update the JSON string below
json = "{}"
# create an instance of UploadMedia200Response from a JSON string
upload_media200_response_instance = UploadMedia200Response.from_json(json)
# print the JSON string representation of the object
print
UploadMedia200Response.to_json()

# convert the object into a dict
upload_media200_response_dict = upload_media200_response_instance.to_dict()
# create an instance of UploadMedia200Response from a dict
upload_media200_response_form_dict = upload_media200_response.from_dict(upload_media200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


