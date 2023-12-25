# openapi_client.LogsApi

All URIs are relative to *http://localhost:9000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_logs**](LogsApi.md#get_logs) | **GET** /logs | 


# **get_logs**
> GetLogs200Response get_logs()



returns the log entries stored in the log buffer

### Example

* Basic Authentication (basicAuth):

```python
import time
import os
import listmonk_client
from listmonk_client.models.get_logs200_response import GetLogs200Response
from listmonk_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:9000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = listmonk_client.Configuration(
    host="http://localhost:9000/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = listmonk_client.Configuration(
    username=os.environ["USERNAME"],
    password=os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with listmonk_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = listmonk_client.LogsApi(api_client)
    
    try:
        api_response = api_instance.get_logs()
        print("The response of LogsApi->get_logs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LogsApi->get_logs: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**GetLogs200Response**](GetLogs200Response.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | stored log entries |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

