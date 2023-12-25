# openapi_client.SettingsApi

All URIs are relative to *http://localhost:9000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_settings**](SettingsApi.md#get_settings) | **GET** /settings | 
[**test_smtp_settings**](SettingsApi.md#test_smtp_settings) | **POST** /settings/smtp/test | 
[**update_settings**](SettingsApi.md#update_settings) | **PUT** /settings | 


# **get_settings**
> GetSettings200Response get_settings()



returns settings from DB

### Example

* Basic Authentication (basicAuth):

```python
import time
import os
import listmonk
from listmonk.models.get_settings200_response import GetSettings200Response
from listmonk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:9000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = listmonk.Configuration(
    host="http://localhost:9000/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = listmonk.Configuration(
    username=os.environ["USERNAME"],
    password=os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with listmonk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = listmonk.SettingsApi(api_client)
    
    try:
        api_response = api_instance.get_settings()
        print("The response of SettingsApi->get_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsApi->get_settings: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**GetSettings200Response**](GetSettings200Response.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | settings object |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **test_smtp_settings**
> GetHealthCheck200Response test_smtp_settings(smtp_test=smtp_test)



test smtp settings

### Example

* Basic Authentication (basicAuth):

```python
import time
import os
import listmonk
from listmonk.models.get_health_check200_response import GetHealthCheck200Response
from listmonk.models.smtp_test import SMTPTest
from listmonk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:9000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = listmonk.Configuration(
    host="http://localhost:9000/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = listmonk.Configuration(
    username=os.environ["USERNAME"],
    password=os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with listmonk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = listmonk.SettingsApi(api_client)
    smtp_test = listmonk.SMTPTest()  # SMTPTest | updated SMTP settings field values (optional)
    
    try:
        api_response = api_instance.test_smtp_settings(smtp_test=smtp_test)
        print("The response of SettingsApi->test_smtp_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsApi->test_smtp_settings: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **smtp_test** | [**SMTPTest**](SMTPTest.md)| updated SMTP settings field values | [optional] 

### Return type

[**GetHealthCheck200Response**](GetHealthCheck200Response.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | updated SMTP test settings |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_settings**
> GetHealthCheck200Response update_settings(settings=settings)



returns updated settings from the DB.

### Example

* Basic Authentication (basicAuth):

```python
import time
import os
import listmonk
from listmonk.models.get_health_check200_response import GetHealthCheck200Response
from listmonk.models.settings import Settings
from listmonk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:9000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = listmonk.Configuration(
    host="http://localhost:9000/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = listmonk.Configuration(
    username=os.environ["USERNAME"],
    password=os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with listmonk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = listmonk.SettingsApi(api_client)
    settings = listmonk.Settings()  # Settings | updated settings field values (optional)
    
    try:
        api_response = api_instance.update_settings(settings=settings)
        print("The response of SettingsApi->update_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsApi->update_settings: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settings** | [**Settings**](Settings.md)| updated settings field values | [optional] 

### Return type

[**GetHealthCheck200Response**](GetHealthCheck200Response.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | updated settings object |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

