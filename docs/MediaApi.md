# openapi_client.MediaApi

All URIs are relative to *http://localhost:9000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_media_by_id**](MediaApi.md#delete_media_by_id) | **DELETE** /media/{id} | 
[**get_media**](MediaApi.md#get_media) | **GET** /media | 
[**get_media_by_id**](MediaApi.md#get_media_by_id) | **GET** /media/{id} | 
[**upload_media**](MediaApi.md#upload_media) | **POST** /media | 


# **delete_media_by_id**
> GetHealthCheck200Response delete_media_by_id(id)



handles deletion of uploaded media.

### Example

* Basic Authentication (basicAuth):

```python
import time
import os
import listmonk
from listmonk.models.get_health_check200_response import GetHealthCheck200Response
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
    api_instance = listmonk.MediaApi(api_client)
    id = 56  # int | The id value of the list you want to delete.
    
    try:
        api_response = api_instance.delete_media_by_id(id)
        print("The response of MediaApi->delete_media_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MediaApi->delete_media_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id value of the list you want to delete. | 

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
**200** | response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_media**
> GetMedia200Response get_media()



handles retrieval of uploaded media.

### Example

* Basic Authentication (basicAuth):

```python
import time
import os
import listmonk
from listmonk.models.get_media200_response import GetMedia200Response
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
    api_instance = listmonk.MediaApi(api_client)
    
    try:
        api_response = api_instance.get_media()
        print("The response of MediaApi->get_media:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MediaApi->get_media: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**GetMedia200Response**](GetMedia200Response.md)

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

# **get_media_by_id**
> UploadMedia200Response get_media_by_id(id)



handles retrieval of uploaded media.

### Example

* Basic Authentication (basicAuth):

```python
import time
import os
import listmonk
from listmonk.models.upload_media200_response import UploadMedia200Response
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
    api_instance = listmonk.MediaApi(api_client)
    id = 56  # int | media file id
    
    try:
        api_response = api_instance.get_media_by_id(id)
        print("The response of MediaApi->get_media_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MediaApi->get_media_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| media file id | 

### Return type

[**UploadMedia200Response**](UploadMedia200Response.md)

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

# **upload_media**
> UploadMedia200Response upload_media()



handles media file uploads.

### Example

* Basic Authentication (basicAuth):

```python
import time
import os
import listmonk
from listmonk.models.upload_media200_response import UploadMedia200Response
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
    api_instance = listmonk.MediaApi(api_client)
    
    try:
        api_response = api_instance.upload_media()
        print("The response of MediaApi->upload_media:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MediaApi->upload_media: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**UploadMedia200Response**](UploadMedia200Response.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

