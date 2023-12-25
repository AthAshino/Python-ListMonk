# MediaFileObject


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**uuid** | **str** |  | [optional] 
**filename** | **str** |  | [optional] 
**created_at** | **str** |  | [optional] 
**thumb_url** | **str** |  | [optional] 
**uri** | **str** |  | [optional] 

## Example

```python
from listmonk_client.models.media_file_object import MediaFileObject

# TODO update the JSON string below
json = "{}"
# create an instance of MediaFileObject from a JSON string
media_file_object_instance = MediaFileObject.from_json(json)
# print the JSON string representation of the object
print
MediaFileObject.to_json()

# convert the object into a dict
media_file_object_dict = media_file_object_instance.to_dict()
# create an instance of MediaFileObject from a dict
media_file_object_form_dict = media_file_object.from_dict(media_file_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


