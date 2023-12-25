# openapi_client.TransactionalApi

All URIs are relative to *http://localhost:9000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**transact_with_subscriber**](TransactionalApi.md#transact_with_subscriber) | **POST** /tx | 


# **transact_with_subscriber**
> GetHealthCheck200Response transact_with_subscriber(transactional_message=transactional_message)



send message to a subscriber

### Example

* Basic Authentication (basicAuth):

```python
import time
import os
import listmonk_client
from listmonk_client.models.get_health_check200_response import GetHealthCheck200Response
from listmonk_client.models.transactional_message import TransactionalMessage
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
    api_instance = listmonk_client.TransactionalApi(api_client)
    transactional_message = listmonk_client.TransactionalMessage()  # TransactionalMessage | email message to a subscriber (optional)
    
    try:
        api_response = api_instance.transact_with_subscriber(transactional_message=transactional_message)
        print("The response of TransactionalApi->transact_with_subscriber:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionalApi->transact_with_subscriber: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transactional_message** | [**TransactionalMessage**](TransactionalMessage.md)| email message to a subscriber | [optional] 

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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

