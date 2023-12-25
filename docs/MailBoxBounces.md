# MailBoxBounces


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** |  | [optional] 
**enabled** | **bool** |  | [optional] 
**type** | **str** |  | [optional] 
**host** | **str** |  | [optional] 
**port** | **int** |  | [optional] 
**auth_protocol** | **str** |  | [optional] 
**return_path** | **str** |  | [optional] 
**username** | **str** |  | [optional] 
**tls_enabled** | **bool** |  | [optional] 
**tls_skip_verify** | **bool** |  | [optional] 
**scan_interval** | **str** |  | [optional] 

## Example

```python
from listmonk.models.mail_box_bounces import MailBoxBounces

# TODO update the JSON string below
json = "{}"
# create an instance of MailBoxBounces from a JSON string
mail_box_bounces_instance = MailBoxBounces.from_json(json)
# print the JSON string representation of the object
print
MailBoxBounces.to_json()

# convert the object into a dict
mail_box_bounces_dict = mail_box_bounces_instance.to_dict()
# create an instance of MailBoxBounces from a dict
mail_box_bounces_form_dict = mail_box_bounces.from_dict(mail_box_bounces_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


