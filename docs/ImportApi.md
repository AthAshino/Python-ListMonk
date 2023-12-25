# openapi_client.ImportApi

All URIs are relative to *http://localhost:9000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_import_subscriber_stats**](ImportApi.md#get_import_subscriber_stats) | **GET** /import/subscribers/logs | 
[**get_import_subscribers**](ImportApi.md#get_import_subscribers) | **GET** /import/subscribers | 
[**import_subscribers**](ImportApi.md#import_subscribers) | **POST** /import/subscribers | 
[**stop_import_subscribers**](ImportApi.md#stop_import_subscribers) | **DELETE** /import/subscribers | 


# **get_import_subscriber_stats**
> GetImportSubscriberStats200Response get_import_subscriber_stats()



returns import statistics

### Example

* Basic Authentication (basicAuth):

```python
import time
import os
import listmonk
from listmonk.models.get_import_subscriber_stats200_response import GetImportSubscriberStats200Response
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
    api_instance = listmonk.ImportApi(api_client)
    
    try:
        api_response = api_instance.get_import_subscriber_stats()
        print("The response of ImportApi->get_import_subscriber_stats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImportApi->get_import_subscriber_stats: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**GetImportSubscriberStats200Response**](GetImportSubscriberStats200Response.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | import statistics |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_import_subscribers**
> GetImportSubscribers200Response get_import_subscribers()



returns import status.

### Example

* Basic Authentication (basicAuth):

```python
import time
import os
import listmonk
from listmonk.models.get_import_subscribers200_response import GetImportSubscribers200Response
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
    api_instance = listmonk.ImportApi(api_client)
    
    try:
        api_response = api_instance.get_import_subscribers()
        print("The response of ImportApi->get_import_subscribers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImportApi->get_import_subscribers: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**GetImportSubscribers200Response**](GetImportSubscribers200Response.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | import status |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_subscribers**
> GetImportSubscribers200Response import_subscribers(import_subscribers_request=import_subscribers_request)



handles the uploading and bulk importing of a ZIP file of one or more CSV files.

### Example

* Basic Authentication (basicAuth):

```python
import time
import os
import listmonk
from listmonk.models.get_import_subscribers200_response import GetImportSubscribers200Response
from listmonk.models.import_subscribers_request import ImportSubscribersRequest
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
    api_instance = listmonk.ImportApi(api_client)
    import_subscribers_request = listmonk.ImportSubscribersRequest()  # ImportSubscribersRequest | uploads and bulk imports of compressed CSV files (optional)
    
    try:
        api_response = api_instance.import_subscribers(import_subscribers_request=import_subscribers_request)
        print("The response of ImportApi->import_subscribers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImportApi->import_subscribers: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **import_subscribers_request** | [**ImportSubscribersRequest**](ImportSubscribersRequest.md)| uploads and bulk imports of compressed CSV files | [optional] 

### Return type

[**GetImportSubscribers200Response**](GetImportSubscribers200Response.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | updated import status |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stop_import_subscribers**
> GetImportSubscribers200Response stop_import_subscribers()



sends a stop signal to the importer.

### Example

* Basic Authentication (basicAuth):

```python
import time
import os
import listmonk
from listmonk.models.get_import_subscribers200_response import GetImportSubscribers200Response
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
    api_instance = listmonk.ImportApi(api_client)
    
    try:
        api_response = api_instance.stop_import_subscribers()
        print("The response of ImportApi->stop_import_subscribers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImportApi->stop_import_subscribers: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**GetImportSubscribers200Response**](GetImportSubscribers200Response.md)

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

