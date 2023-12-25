# LanguagePack


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**LanguagePackData**](LanguagePackData.md) |  | [optional] 

## Example

```python
from listmonk_client.models.language_pack import LanguagePack

# TODO update the JSON string below
json = "{}"
# create an instance of LanguagePack from a JSON string
language_pack_instance = LanguagePack.from_json(json)
# print the JSON string representation of the object
print
LanguagePack.to_json()

# convert the object into a dict
language_pack_dict = language_pack_instance.to_dict()
# create an instance of LanguagePack from a dict
language_pack_form_dict = language_pack.from_dict(language_pack_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


