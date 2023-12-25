# openapi_client.MaintenanceApi

All URIs are relative to *http://localhost:9000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_campaign_analytics_by_type**](MaintenanceApi.md#delete_campaign_analytics_by_type) | **DELETE** /maintenance/analytics/{type} | 
[**delete_gc_subscribers**](MaintenanceApi.md#delete_gc_subscribers) | **DELETE** /maintenance/subscribers/{type} | 
[**delete_unconfirmed_subscriptions**](MaintenanceApi.md#delete_unconfirmed_subscriptions) | **DELETE** /maintenance/subscriptions/unconfirmed | 


# **delete_campaign_analytics_by_type**
> GetHealthCheck200Response delete_campaign_analytics_by_type(type, before_date=before_date)



garbage collects (deletes) campaign analytics.

### Example

* Basic Authentication (basicAuth):

```python
import time
import os
import listmonk_client
from listmonk_client.models.get_health_check200_response import GetHealthCheck200Response
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
    api_instance = listmonk_client.MaintenanceApi(api_client)
    type = 'type_example'  # str | type of GC collected subscribers
    before_date = '2013-10-20'  # date |  (optional)
    
    try:
        api_response = api_instance.delete_campaign_analytics_by_type(type, before_date=before_date)
        print("The response of MaintenanceApi->delete_campaign_analytics_by_type:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MaintenanceApi->delete_campaign_analytics_by_type: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| type of GC collected subscribers | 
 **before_date** | **date**|  | [optional] 

### Return type

[**GetHealthCheck200Response**](GetHealthCheck200Response.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_gc_subscribers**
> DeleteGCSubscribers200Response delete_gc_subscribers(type)



garbage collects (deletes) orphaned or blocklisted subscribers.

### Example

* Basic Authentication (basicAuth):

```python
import time
import os
import listmonk_client
from listmonk_client.models.delete_gc_subscribers200_response import DeleteGCSubscribers200Response
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
    api_instance = listmonk_client.MaintenanceApi(api_client)
    type = 'type_example'  # str | type of GC collected subscribers
    
    try:
        api_response = api_instance.delete_gc_subscribers(type)
        print("The response of MaintenanceApi->delete_gc_subscribers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MaintenanceApi->delete_gc_subscribers: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| type of GC collected subscribers | 

### Return type

[**DeleteGCSubscribers200Response**](DeleteGCSubscribers200Response.md)

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

# **delete_unconfirmed_subscriptions**
> DeleteGCSubscribers200Response delete_unconfirmed_subscriptions(before_date=before_date)



garbage collects (deletes) orphaned or blocklisted subscribers.

### Example

* Basic Authentication (basicAuth):

```python
import time
import os
import listmonk_client
from listmonk_client.models.delete_gc_subscribers200_response import DeleteGCSubscribers200Response
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
    api_instance = listmonk_client.MaintenanceApi(api_client)
    before_date = '2013-10-20'  # date |  (optional)
    
    try:
        api_response = api_instance.delete_unconfirmed_subscriptions(before_date=before_date)
        print("The response of MaintenanceApi->delete_unconfirmed_subscriptions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MaintenanceApi->delete_unconfirmed_subscriptions: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **before_date** | **date**|  | [optional] 

### Return type

[**DeleteGCSubscribers200Response**](DeleteGCSubscribers200Response.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

