# openapi_client.PublicApi

All URIs are relative to *http://localhost:9000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_public_lists**](PublicApi.md#get_public_lists) | **GET** /public/lists | 
[**handle_public_subscription**](PublicApi.md#handle_public_subscription) | **POST** /public/subscription | 


# **get_public_lists**
> List[GetPublicLists200ResponseInner] get_public_lists()



returns the list of public lists with minimal fields

### Example

* Basic Authentication (basicAuth):

```python
import time
import os
import listmonk
from listmonk.models.get_public_lists200_response_inner import GetPublicLists200ResponseInner
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
    api_instance = listmonk.PublicApi(api_client)
    
    try:
        api_response = api_instance.get_public_lists()
        print("The response of PublicApi->get_public_lists:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApi->get_public_lists: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**List[GetPublicLists200ResponseInner]**](GetPublicLists200ResponseInner.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **handle_public_subscription**
> HandlePublicSubscription200Response handle_public_subscription(handle_public_subscription_request=handle_public_subscription_request)



handles subscription requests coming from public API calls.

### Example

* Basic Authentication (basicAuth):

```python
import time
import os
import listmonk
from listmonk.models.handle_public_subscription200_response import HandlePublicSubscription200Response
from listmonk.models.handle_public_subscription_request import HandlePublicSubscriptionRequest
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
    api_instance = listmonk.PublicApi(api_client)
    handle_public_subscription_request = listmonk.HandlePublicSubscriptionRequest()  # HandlePublicSubscriptionRequest | subscription request parameters (optional)
    
    try:
        api_response = api_instance.handle_public_subscription(
            handle_public_subscription_request=handle_public_subscription_request)
        print("The response of PublicApi->handle_public_subscription:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApi->handle_public_subscription: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **handle_public_subscription_request** | [**HandlePublicSubscriptionRequest**](HandlePublicSubscriptionRequest.md)| subscription request parameters | [optional] 

### Return type

[**HandlePublicSubscription200Response**](HandlePublicSubscription200Response.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

