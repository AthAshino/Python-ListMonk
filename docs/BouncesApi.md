# openapi_client.BouncesApi

All URIs are relative to *http://localhost:9000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_bounce_by_id**](BouncesApi.md#delete_bounce_by_id) | **DELETE** /bounces/{id} | 
[**delete_bounces**](BouncesApi.md#delete_bounces) | **DELETE** /bounces | 
[**get_bounce_by_id**](BouncesApi.md#get_bounce_by_id) | **GET** /bounces/{id} | 
[**get_bounces**](BouncesApi.md#get_bounces) | **GET** /bounces | 


# **delete_bounce_by_id**
> GetHealthCheck200Response delete_bounce_by_id(id)



handles bounce deletion, either a single one (ID in the URI), or a list.

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
    api_instance = listmonk_client.BouncesApi(api_client)
    id = 56  # int | The id value of the bounce you want to delete.
    
    try:
        api_response = api_instance.delete_bounce_by_id(id)
        print("The response of BouncesApi->delete_bounce_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BouncesApi->delete_bounce_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id value of the bounce you want to delete. | 

### Return type

[**GetHealthCheck200Response**](GetHealthCheck200Response.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_bounces**
> GetHealthCheck200Response delete_bounces(all=all, id=id)



handles retrieval of bounce records.

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
    api_instance = listmonk_client.BouncesApi(api_client)
    all = True  # bool | flag for multiple bounce record deletion (optional)
    id = 'id_example'  # str | list of bounce ids to delete (optional)
    
    try:
        api_response = api_instance.delete_bounces(all=all, id=id)
        print("The response of BouncesApi->delete_bounces:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BouncesApi->delete_bounces: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **all** | **bool**| flag for multiple bounce record deletion | [optional] 
 **id** | **str**| list of bounce ids to delete | [optional] 

### Return type

[**GetHealthCheck200Response**](GetHealthCheck200Response.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bounce_by_id**
> GetBounceById200Response get_bounce_by_id(id)



handles retrieval of bounce record by id

### Example

* Basic Authentication (basicAuth):

```python
import time
import os
import listmonk_client
from listmonk_client.models.get_bounce_by_id200_response import GetBounceById200Response
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
    api_instance = listmonk_client.BouncesApi(api_client)
    id = 56  # int | The id value of the bounce you want to retreive.
    
    try:
        api_response = api_instance.get_bounce_by_id(id)
        print("The response of BouncesApi->get_bounce_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BouncesApi->get_bounce_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id value of the bounce you want to retreive. | 

### Return type

[**GetBounceById200Response**](GetBounceById200Response.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | bounce object |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bounces**
> GetBounces200Response get_bounces(campaign_id=campaign_id, page=page, per_page=per_page, source=source, order_by=order_by, order=order)



handles retrieval of bounce records.

### Example

* Basic Authentication (basicAuth):

```python
import time
import os
import listmonk_client
from listmonk_client.models.get_bounces200_response import GetBounces200Response
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
    api_instance = listmonk_client.BouncesApi(api_client)
    campaign_id = 56  # int | bounce record retrieval of particular campaign (optional)
    page = 56  # int | total number of pages (optional)
    per_page = 56  # int | number of items per page (optional)
    source = 'source_example'  # str |  (optional)
    order_by = 'order_by_example'  # str |  (optional)
    order = 'order_example'  # str |  (optional)
    
    try:
        api_response = api_instance.get_bounces(campaign_id=campaign_id, page=page, per_page=per_page, source=source,
                                                order_by=order_by, order=order)
        print("The response of BouncesApi->get_bounces:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BouncesApi->get_bounces: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **int**| bounce record retrieval of particular campaign | [optional] 
 **page** | **int**| total number of pages | [optional] 
 **per_page** | **int**| number of items per page | [optional] 
 **source** | **str**|  | [optional] 
 **order_by** | **str**|  | [optional] 
 **order** | **str**|  | [optional] 

### Return type

[**GetBounces200Response**](GetBounces200Response.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | list of bounce records |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

