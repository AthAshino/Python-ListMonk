# SMTPSettings


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** |  | [optional] 
**enabled** | **bool** |  | [optional] 
**host** | **str** |  | [optional] 
**hello_hostname** | **str** |  | [optional] 
**port** | **int** |  | [optional] 
**auth_protocol** | **str** |  | [optional] 
**username** | **str** |  | [optional] 
**email_headers** | **List[object]** |  | [optional] 
**max_conns** | **int** |  | [optional] 
**max_msg_retries** | **int** |  | [optional] 
**idle_timeout** | **str** |  | [optional] 
**wait_timeout** | **str** |  | [optional] 
**tls_type** | **str** |  | [optional] 
**tls_skip_verify** | **bool** |  | [optional] 

## Example

```python
from listmonk.models.smtp_settings import SMTPSettings

# TODO update the JSON string below
json = "{}"
# create an instance of SMTPSettings from a JSON string
smtp_settings_instance = SMTPSettings.from_json(json)
# print the JSON string representation of the object
print
SMTPSettings.to_json()

# convert the object into a dict
smtp_settings_dict = smtp_settings_instance.to_dict()
# create an instance of SMTPSettings from a dict
smtp_settings_form_dict = smtp_settings.from_dict(smtp_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


