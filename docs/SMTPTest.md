# SMTPTest


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
**str_email_headers** | **str** |  | [optional] 
**password** | **str** |  | [optional] 
**email** | **str** |  | [optional] 

## Example

```python
from listmonk.models.smtp_test import SMTPTest

# TODO update the JSON string below
json = "{}"
# create an instance of SMTPTest from a JSON string
smtp_test_instance = SMTPTest.from_json(json)
# print the JSON string representation of the object
print
SMTPTest.to_json()

# convert the object into a dict
smtp_test_dict = smtp_test_instance.to_dict()
# create an instance of SMTPTest from a dict
smtp_test_form_dict = smtp_test.from_dict(smtp_test_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


