# openapi_client.SubscribersApi

All URIs are relative to *http://localhost:9000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**blocklist_subscribers_query**](SubscribersApi.md#blocklist_subscribers_query) | **PUT** /subscribers/query/blocklist | 
[**create_subscriber**](SubscribersApi.md#create_subscriber) | **POST** /subscribers | 
[**delete_subscriber_bounces_by_id**](SubscribersApi.md#delete_subscriber_bounces_by_id) | **DELETE** /subscribers/{id}/bounces | 
[**delete_subscriber_by_id**](SubscribersApi.md#delete_subscriber_by_id) | **DELETE** /subscribers/{id} | 
[**delete_subscriber_by_list**](SubscribersApi.md#delete_subscriber_by_list) | **DELETE** /subscribers | 
[**delete_subscriber_by_query**](SubscribersApi.md#delete_subscriber_by_query) | **POST** /subscribers/query/delete | 
[**export_subscriber_data_by_id**](SubscribersApi.md#export_subscriber_data_by_id) | **GET** /subscribers/{id}/export | 
[**get_subscriber_bounces_by_id**](SubscribersApi.md#get_subscriber_bounces_by_id) | **GET** /subscribers/{id}/bounces | 
[**get_subscriber_by_id**](SubscribersApi.md#get_subscriber_by_id) | **GET** /subscribers/{id} | 
[**get_subscribers**](SubscribersApi.md#get_subscribers) | **GET** /subscribers | 
[**manage_blocklist_by_subscriber_list**](SubscribersApi.md#manage_blocklist_by_subscriber_list) | **PUT** /subscribers/blocklist | 
[**manage_blocklist_subscribers_by_id**](SubscribersApi.md#manage_blocklist_subscribers_by_id) | **PUT** /subscribers/{id}/blocklist | 
[**manage_subscriber_list_by_id**](SubscribersApi.md#manage_subscriber_list_by_id) | **PUT** /subscribers/lists/{id} | 
[**manage_subscriber_lists**](SubscribersApi.md#manage_subscriber_lists) | **PUT** /subscribers/lists | 
[**manage_subscriber_lists_by_query**](SubscribersApi.md#manage_subscriber_lists_by_query) | **PUT** /subscribers/query/lists | 
[**subscriber_send_optin_by_id**](SubscribersApi.md#subscriber_send_optin_by_id) | **POST** /subscribers/{id}/optin | 
[**update_subscriber_by_id**](SubscribersApi.md#update_subscriber_by_id) | **PUT** /subscribers/{id} | 


# **blocklist_subscribers_query**
> GetHealthCheck200Response blocklist_subscribers_query(body=body)



bulk blocklists subscribers based on an arbitrary SQL expression.

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
    api_instance = listmonk_client.SubscribersApi(api_client)
    body = 'body_example'  # str | Arbitrary SQL expression. (optional)
    
    try:
        api_response = api_instance.blocklist_subscribers_query(body=body)
        print("The response of SubscribersApi->blocklist_subscribers_query:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscribersApi->blocklist_subscribers_query: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **str**| Arbitrary SQL expression. | [optional] 

### Return type

[**GetHealthCheck200Response**](GetHealthCheck200Response.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: text/plain, application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_subscriber**
> CreateSubscriber200Response create_subscriber(new_subscriber=new_subscriber)



handles creation of new subscriber

### Example

* Basic Authentication (basicAuth):

```python
import time
import os
import listmonk_client
from listmonk_client.models.create_subscriber200_response import CreateSubscriber200Response
from listmonk_client.models.new_subscriber import NewSubscriber
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
    api_instance = listmonk_client.SubscribersApi(api_client)
    new_subscriber = listmonk_client.NewSubscriber()  # NewSubscriber | new subscriber info (optional)
    
    try:
        api_response = api_instance.create_subscriber(new_subscriber=new_subscriber)
        print("The response of SubscribersApi->create_subscriber:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscribersApi->create_subscriber: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **new_subscriber** | [**NewSubscriber**](NewSubscriber.md)| new subscriber info | [optional] 

### Return type

[**CreateSubscriber200Response**](CreateSubscriber200Response.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | subscriber object |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_subscriber_bounces_by_id**
> GetHealthCheck200Response delete_subscriber_bounces_by_id(id)



deletes a subscriber's bounce records

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
    api_instance = listmonk_client.SubscribersApi(api_client)
    id = 56  # int | subscriber id
    
    try:
        api_response = api_instance.delete_subscriber_bounces_by_id(id)
        print("The response of SubscribersApi->delete_subscriber_bounces_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscribersApi->delete_subscriber_bounces_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| subscriber id | 

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

# **delete_subscriber_by_id**
> GetHealthCheck200Response delete_subscriber_by_id(id)



handles subscriber deletion based on id

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
    api_instance = listmonk_client.SubscribersApi(api_client)
    id = 56  # int | The id value of the subscriber you want to get.
    
    try:
        api_response = api_instance.delete_subscriber_by_id(id)
        print("The response of SubscribersApi->delete_subscriber_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscribersApi->delete_subscriber_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id value of the subscriber you want to get. | 

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

# **delete_subscriber_by_list**
> GetHealthCheck200Response delete_subscriber_by_list(id)



handles subscribers deletion

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
    api_instance = listmonk_client.SubscribersApi(api_client)
    id = 'id_example'  # str | subscriber id/s to be deleted
    
    try:
        api_response = api_instance.delete_subscriber_by_list(id)
        print("The response of SubscribersApi->delete_subscriber_by_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscribersApi->delete_subscriber_by_list: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| subscriber id/s to be deleted | 

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

# **delete_subscriber_by_query**
> GetHealthCheck200Response delete_subscriber_by_query(body=body)



bulk deletes based on an arbitrary SQL expression.

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
    api_instance = listmonk_client.SubscribersApi(api_client)
    body = 'body_example'  # str | Arbitrary SQL expression. (optional)
    
    try:
        api_response = api_instance.delete_subscriber_by_query(body=body)
        print("The response of SubscribersApi->delete_subscriber_by_query:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscribersApi->delete_subscriber_by_query: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **str**| Arbitrary SQL expression. | [optional] 

### Return type

[**GetHealthCheck200Response**](GetHealthCheck200Response.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: text/plain, application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_subscriber_data_by_id**
> SubscriberData export_subscriber_data_by_id(id)



retrieves a subscriber's profile

### Example

* Basic Authentication (basicAuth):

```python
import time
import os
import listmonk_client
from listmonk_client.models.subscriber_data import SubscriberData
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
    api_instance = listmonk_client.SubscribersApi(api_client)
    id = 56  # int | The id value of subscriber profile you want to export
    
    try:
        api_response = api_instance.export_subscriber_data_by_id(id)
        print("The response of SubscribersApi->export_subscriber_data_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscribersApi->export_subscriber_data_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id value of subscriber profile you want to export | 

### Return type

[**SubscriberData**](SubscriberData.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | subscriber data object |  * Cache-Control -  <br>  * Content-Disposition -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_subscriber_bounces_by_id**
> GetSubscriberBouncesById200Response get_subscriber_bounces_by_id(id)



retrieves a subscriber's bounce records

### Example

* Basic Authentication (basicAuth):

```python
import time
import os
import listmonk_client
from listmonk_client.models.get_subscriber_bounces_by_id200_response import GetSubscriberBouncesById200Response
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
    api_instance = listmonk_client.SubscribersApi(api_client)
    id = 56  # int | subscriber id
    
    try:
        api_response = api_instance.get_subscriber_bounces_by_id(id)
        print("The response of SubscribersApi->get_subscriber_bounces_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscribersApi->get_subscriber_bounces_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| subscriber id | 

### Return type

[**GetSubscriberBouncesById200Response**](GetSubscriberBouncesById200Response.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | list of bounce records of a subscriber |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_subscriber_by_id**
> CreateSubscriber200Response get_subscriber_by_id(id)



handles the retrieval of a single subscriber by ID.

### Example

* Basic Authentication (basicAuth):

```python
import time
import os
import listmonk_client
from listmonk_client.models.create_subscriber200_response import CreateSubscriber200Response
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
    api_instance = listmonk_client.SubscribersApi(api_client)
    id = 56  # int | The id value of the subscriber you want to get.
    
    try:
        api_response = api_instance.get_subscriber_by_id(id)
        print("The response of SubscribersApi->get_subscriber_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscribersApi->get_subscriber_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id value of the subscriber you want to get. | 

### Return type

[**CreateSubscriber200Response**](CreateSubscriber200Response.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | gets a single subscriber. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_subscribers**
> GetSubscribers200Response get_subscribers(page=page, per_page=per_page, query=query)



returns all subscribers.

### Example

* Basic Authentication (basicAuth):

```python
import time
import os
import listmonk_client
from listmonk_client.models.get_subscribers200_response import GetSubscribers200Response
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
    api_instance = listmonk_client.SubscribersApi(api_client)
    page = 56  # int | number of records to skip (optional)
    per_page = 56  # int | max number of records to return per page (optional)
    query = 'query_example'  # str | query subscribers with an SQL expression. (optional)
    
    try:
        api_response = api_instance.get_subscribers(page=page, per_page=per_page, query=query)
        print("The response of SubscribersApi->get_subscribers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscribersApi->get_subscribers: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| number of records to skip | [optional] 
 **per_page** | **int**| max number of records to return per page | [optional] 
 **query** | **str**| query subscribers with an SQL expression. | [optional] 

### Return type

[**GetSubscribers200Response**](GetSubscribers200Response.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | subscribers list |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **manage_blocklist_by_subscriber_list**
> GetHealthCheck200Response manage_blocklist_by_subscriber_list(subscriber_query_request=subscriber_query_request)



handles blocklisting of subscriber list

### Example

* Basic Authentication (basicAuth):

```python
import time
import os
import listmonk_client
from listmonk_client.models.get_health_check200_response import GetHealthCheck200Response
from listmonk_client.models.subscriber_query_request import SubscriberQueryRequest
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
    api_instance = listmonk_client.SubscribersApi(api_client)
    subscriber_query_request = listmonk_client.SubscriberQueryRequest()  # SubscriberQueryRequest | The list of subscribers to blocklist (optional)
    
    try:
        api_response = api_instance.manage_blocklist_by_subscriber_list(subscriber_query_request=subscriber_query_request)
        print("The response of SubscribersApi->manage_blocklist_by_subscriber_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscribersApi->manage_blocklist_by_subscriber_list: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscriber_query_request** | [**SubscriberQueryRequest**](SubscriberQueryRequest.md)| The list of subscribers to blocklist | [optional] 

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

# **manage_blocklist_subscribers_by_id**
> GetHealthCheck200Response manage_blocklist_subscribers_by_id(id, subscriber_query_request=subscriber_query_request)



handles the blocklisting of one or more subscribers.

### Example

* Basic Authentication (basicAuth):

```python
import time
import os
import listmonk_client
from listmonk_client.models.get_health_check200_response import GetHealthCheck200Response
from listmonk_client.models.subscriber_query_request import SubscriberQueryRequest
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
    api_instance = listmonk_client.SubscribersApi(api_client)
    id = 56  # int | The id value of the subscriber you want to blocklist.
    subscriber_query_request = listmonk_client.SubscriberQueryRequest()  # SubscriberQueryRequest | The id of subscriber to add or remove (optional)
    
    try:
        api_response = api_instance.manage_blocklist_subscribers_by_id(id, subscriber_query_request=subscriber_query_request)
        print("The response of SubscribersApi->manage_blocklist_subscribers_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscribersApi->manage_blocklist_subscribers_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id value of the subscriber you want to blocklist. | 
 **subscriber_query_request** | [**SubscriberQueryRequest**](SubscriberQueryRequest.md)| The id of subscriber to add or remove | [optional] 

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

# **manage_subscriber_list_by_id**
> GetHealthCheck200Response manage_subscriber_list_by_id(id, subscriber_query_request=subscriber_query_request)



handles bulk addition or removal of subscribers for a specified list id

### Example

* Basic Authentication (basicAuth):

```python
import time
import os
import listmonk_client
from listmonk_client.models.get_health_check200_response import GetHealthCheck200Response
from listmonk_client.models.subscriber_query_request import SubscriberQueryRequest
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
    api_instance = listmonk_client.SubscribersApi(api_client)
    id = 56  # int | The id of list you want to update
    subscriber_query_request = listmonk_client.SubscriberQueryRequest()  # SubscriberQueryRequest | The list of subscribers to add or remove (optional)
    
    try:
        api_response = api_instance.manage_subscriber_list_by_id(id, subscriber_query_request=subscriber_query_request)
        print("The response of SubscribersApi->manage_subscriber_list_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscribersApi->manage_subscriber_list_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of list you want to update | 
 **subscriber_query_request** | [**SubscriberQueryRequest**](SubscriberQueryRequest.md)| The list of subscribers to add or remove | [optional] 

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

# **manage_subscriber_lists**
> GetHealthCheck200Response manage_subscriber_lists(subscriber_query_request=subscriber_query_request)



handles bulk addition or removal of subscribers

### Example

* Basic Authentication (basicAuth):

```python
import time
import os
import listmonk_client
from listmonk_client.models.get_health_check200_response import GetHealthCheck200Response
from listmonk_client.models.subscriber_query_request import SubscriberQueryRequest
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
    api_instance = listmonk_client.SubscribersApi(api_client)
    subscriber_query_request = listmonk_client.SubscriberQueryRequest()  # SubscriberQueryRequest | The list of subscribers details to add or remove (optional)
    
    try:
        api_response = api_instance.manage_subscriber_lists(subscriber_query_request=subscriber_query_request)
        print("The response of SubscribersApi->manage_subscriber_lists:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscribersApi->manage_subscriber_lists: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscriber_query_request** | [**SubscriberQueryRequest**](SubscriberQueryRequest.md)| The list of subscribers details to add or remove | [optional] 

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

# **manage_subscriber_lists_by_query**
> GetHealthCheck200Response manage_subscriber_lists_by_query(body=body)



bulk adds/removes/unsubscribes subscribers from one or more lists based on an arbitrary SQL expression.

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
    api_instance = listmonk_client.SubscribersApi(api_client)
    body = 'body_example'  # str | Arbitrary SQL expression. (optional)
    
    try:
        api_response = api_instance.manage_subscriber_lists_by_query(body=body)
        print("The response of SubscribersApi->manage_subscriber_lists_by_query:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscribersApi->manage_subscriber_lists_by_query: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **str**| Arbitrary SQL expression. | [optional] 

### Return type

[**GetHealthCheck200Response**](GetHealthCheck200Response.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: text/plain, application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **subscriber_send_optin_by_id**
> GetHealthCheck200Response subscriber_send_optin_by_id(id)



sends an optin confirmation e-mail to a subscriber.

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
    api_instance = listmonk_client.SubscribersApi(api_client)
    id = 56  # int | sends an optin confirmation e-mail to a subscriber
    
    try:
        api_response = api_instance.subscriber_send_optin_by_id(id)
        print("The response of SubscribersApi->subscriber_send_optin_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscribersApi->subscriber_send_optin_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| sends an optin confirmation e-mail to a subscriber | 

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

# **update_subscriber_by_id**
> CreateSubscriber200Response update_subscriber_by_id(id, update_subscriber=update_subscriber)



modify subscriber data

### Example

* Basic Authentication (basicAuth):

```python
import time
import os
import listmonk_client
from listmonk_client.models.create_subscriber200_response import CreateSubscriber200Response
from listmonk_client.models.update_subscriber import UpdateSubscriber
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
    api_instance = listmonk_client.SubscribersApi(api_client)
    id = 56  # int | The id of subscriber to update
    update_subscriber = listmonk_client.UpdateSubscriber()  # UpdateSubscriber | new subscriber info (optional)
    
    try:
        api_response = api_instance.update_subscriber_by_id(id, update_subscriber=update_subscriber)
        print("The response of SubscribersApi->update_subscriber_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscribersApi->update_subscriber_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of subscriber to update | 
 **update_subscriber** | [**UpdateSubscriber**](UpdateSubscriber.md)| new subscriber info | [optional] 

### Return type

[**CreateSubscriber200Response**](CreateSubscriber200Response.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | returns updated subscriber. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

