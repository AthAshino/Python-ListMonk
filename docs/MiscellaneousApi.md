# openapi_client.MiscellaneousApi

All URIs are relative to *http://localhost:9000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_dashboard_charts**](MiscellaneousApi.md#get_dashboard_charts) | **GET** /dashboard/charts | 
[**get_dashboard_counts**](MiscellaneousApi.md#get_dashboard_counts) | **GET** /dashboard/counts | 
[**get_health_check**](MiscellaneousApi.md#get_health_check) | **GET** /health | 
[**get_i18n_lang**](MiscellaneousApi.md#get_i18n_lang) | **GET** /lang/{lang} | 
[**get_server_config**](MiscellaneousApi.md#get_server_config) | **GET** /config | 


# **get_dashboard_charts**
> GetDashboardCharts200Response get_dashboard_charts()



returns chart data points to render on the dashboard.

### Example

* Basic Authentication (basicAuth):

```python
import time
import os
import listmonk
from listmonk.models.get_dashboard_charts200_response import GetDashboardCharts200Response
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
    api_instance = listmonk.MiscellaneousApi(api_client)
    
    try:
        api_response = api_instance.get_dashboard_charts()
        print("The response of MiscellaneousApi->get_dashboard_charts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MiscellaneousApi->get_dashboard_charts: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**GetDashboardCharts200Response**](GetDashboardCharts200Response.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | chart data points |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dashboard_counts**
> GetDashboardCounts200Response get_dashboard_counts()



returns stats counts to show on the dashboard

### Example

* Basic Authentication (basicAuth):

```python
import time
import os
import listmonk
from listmonk.models.get_dashboard_counts200_response import GetDashboardCounts200Response
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
    api_instance = listmonk.MiscellaneousApi(api_client)
    
    try:
        api_response = api_instance.get_dashboard_counts()
        print("The response of MiscellaneousApi->get_dashboard_counts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MiscellaneousApi->get_dashboard_counts: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**GetDashboardCounts200Response**](GetDashboardCounts200Response.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | stat counts |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_health_check**
> GetHealthCheck200Response get_health_check()



healthcheck endpoint

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
    api_instance = listmonk.MiscellaneousApi(api_client)
    
    try:
        api_response = api_instance.get_health_check()
        print("The response of MiscellaneousApi->get_health_check:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MiscellaneousApi->get_health_check: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

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

# **get_i18n_lang**
> GetI18nLang200Response get_i18n_lang(lang)



returns the JSON language pack given the language code

### Example

* Basic Authentication (basicAuth):

```python
import time
import os
import listmonk
from listmonk.models.get_i18n_lang200_response import GetI18nLang200Response
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
    api_instance = listmonk.MiscellaneousApi(api_client)
    lang = 'lang_example'  # str | JSON language pack required
    
    try:
        api_response = api_instance.get_i18n_lang(lang)
        print("The response of MiscellaneousApi->get_i18n_lang:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MiscellaneousApi->get_i18n_lang: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lang** | **str**| JSON language pack required | 

### Return type

[**GetI18nLang200Response**](GetI18nLang200Response.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | requested language pack |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_server_config**
> GetServerConfig200Response get_server_config()



returns general server config.

### Example

* Basic Authentication (basicAuth):

```python
import time
import os
import listmonk
from listmonk.models.get_server_config200_response import GetServerConfig200Response
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
    api_instance = listmonk.MiscellaneousApi(api_client)
    
    try:
        api_response = api_instance.get_server_config()
        print("The response of MiscellaneousApi->get_server_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MiscellaneousApi->get_server_config: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**GetServerConfig200Response**](GetServerConfig200Response.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A server config object |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

