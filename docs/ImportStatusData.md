# ImportStatusData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**total** | **int** |  | [optional] 
**imported** | **int** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from listmonk_client.models.import_status_data import ImportStatusData

# TODO update the JSON string below
json = "{}"
# create an instance of ImportStatusData from a JSON string
import_status_data_instance = ImportStatusData.from_json(json)
# print the JSON string representation of the object
print
ImportStatusData.to_json()

# convert the object into a dict
import_status_data_dict = import_status_data_instance.to_dict()
# create an instance of ImportStatusData from a dict
import_status_data_form_dict = import_status_data.from_dict(import_status_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


