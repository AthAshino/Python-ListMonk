# openapi_client.ListsApi

All URIs are relative to *http://localhost:9000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_list**](ListsApi.md#create_list) | **POST** /lists | 
[**delete_list_by_id**](ListsApi.md#delete_list_by_id) | **DELETE** /lists/{list_id} | 
[**get_list_by_id**](ListsApi.md#get_list_by_id) | **GET** /lists/{list_id} | 
[**get_lists**](ListsApi.md#get_lists) | **GET** /lists | 
[**update_list_by_id**](ListsApi.md#update_list_by_id) | **PUT** /lists/{list_id} | 


# **create_list**
> CreateList200Response create_list(new_list=new_list)



handles list creation

### Example

* Basic Authentication (basicAuth):

```python
import time
import os
import listmonk_client
from listmonk_client.models.create_list200_response import CreateList200Response
from listmonk_client.models.new_list import NewList
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
    api_instance = listmonk_client.ListsApi(api_client)
    new_list = listmonk_client.NewList()  # NewList | new list info (optional)
    
    try:
        api_response = api_instance.create_list(new_list=new_list)
        print("The response of ListsApi->create_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ListsApi->create_list: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **new_list** | [**NewList**](NewList.md)| new list info | [optional] 

### Return type

[**CreateList200Response**](CreateList200Response.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | updated list object |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_list_by_id**
> GetHealthCheck200Response delete_list_by_id(list_id)



handles list deletion, either a single one (ID in the URI), or a list.

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
    api_instance = listmonk_client.ListsApi(api_client)
    list_id = 56  # int | The id value of the lists you want to delete.
    
    try:
        api_response = api_instance.delete_list_by_id(list_id)
        print("The response of ListsApi->delete_list_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ListsApi->delete_list_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_id** | **int**| The id value of the lists you want to delete. | 

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

# **get_list_by_id**
> CreateList200Response get_list_by_id(list_id)



retrieves lists with additional metadata like subscriber counts. This may be slow.

### Example

* Basic Authentication (basicAuth):

```python
import time
import os
import listmonk_client
from listmonk_client.models.create_list200_response import CreateList200Response
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
    api_instance = listmonk_client.ListsApi(api_client)
    list_id = 56  # int | The id value of the list you want to retreive.
    
    try:
        api_response = api_instance.get_list_by_id(list_id)
        print("The response of ListsApi->get_list_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ListsApi->get_list_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_id** | **int**| The id value of the list you want to retreive. | 

### Return type

[**CreateList200Response**](CreateList200Response.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | list object |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_lists**
> GetLists200Response get_lists(page=page, per_page=per_page, query=query, order_by=order_by, order=order, minimal=minimal)



retrieves lists with additional metadata like subscriber counts. This may be slow.

### Example

* Basic Authentication (basicAuth):

```python
import time
import os
import listmonk_client
from listmonk_client.models.get_lists200_response import GetLists200Response
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
    api_instance = listmonk_client.ListsApi(api_client)
    page = 56  # int | total number of pages (optional)
    per_page = 56  # int | number of items per page (optional)
    query = 'query_example'  # str | Optional string to search a list by name. (optional)
    order_by = 'order_by_example'  # str | Field to sort results by. name|status|created_at|updated_at (optional)
    order = 'order_example'  # str | ASC|DESC Sort by ascending or descending order. (optional)
    minimal = True  # bool |  (optional)
    
    try:
        api_response = api_instance.get_lists(page=page, per_page=per_page, query=query, order_by=order_by, order=order,
                                              minimal=minimal)
        print("The response of ListsApi->get_lists:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ListsApi->get_lists: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| total number of pages | [optional] 
 **per_page** | **int**| number of items per page | [optional] 
 **query** | **str**| Optional string to search a list by name. | [optional] 
 **order_by** | **str**| Field to sort results by. name|status|created_at|updated_at | [optional] 
 **order** | **str**| ASC|DESC Sort by ascending or descending order. | [optional] 
 **minimal** | **bool**|  | [optional] 

### Return type

[**GetLists200Response**](GetLists200Response.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | list of metadata |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_list_by_id**
> CreateList200Response update_list_by_id(list_id, list=list)



handles list modification

### Example

* Basic Authentication (basicAuth):

```python
import time
import os
import listmonk_client
from listmonk_client.models.create_list200_response import CreateList200Response
from listmonk_client.models.list import List
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
    api_instance = listmonk_client.ListsApi(api_client)
    list_id = 56  # int | The id value of the list you want to update
    list = None  # List | updated list field values (optional)
    
    try:
        api_response = api_instance.update_list_by_id(list_id, list=list)
        print("The response of ListsApi->update_list_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ListsApi->update_list_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_id** | **int**| The id value of the list you want to update | 
 **list** | [**List**](List.md)| updated list field values | [optional] 

### Return type

[**CreateList200Response**](CreateList200Response.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | updated list object |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

