# openapi_client.CampaignsApi

All URIs are relative to *http://localhost:9000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_campaign**](CampaignsApi.md#create_campaign) | **POST** /campaigns | 
[**create_campaign_content_by_id**](CampaignsApi.md#create_campaign_content_by_id) | **POST** /campaigns/{id}/content | 
[**delete_campaign_by_id**](CampaignsApi.md#delete_campaign_by_id) | **DELETE** /campaigns/{id} | 
[**get_campaign_analytics**](CampaignsApi.md#get_campaign_analytics) | **GET** /campaigns/analytics/{type} | 
[**get_campaign_by_id**](CampaignsApi.md#get_campaign_by_id) | **GET** /campaigns/{id} | 
[**get_campaigns**](CampaignsApi.md#get_campaigns) | **GET** /campaigns | 
[**get_running_campaign_stats**](CampaignsApi.md#get_running_campaign_stats) | **GET** /campaigns/running/stats | 
[**preview_campaign_by_id**](CampaignsApi.md#preview_campaign_by_id) | **GET** /campaigns/{id}/preview | 
[**preview_campaign_text_by_id**](CampaignsApi.md#preview_campaign_text_by_id) | **POST** /campaigns/{id}/text | 
[**test_campaign_by_id**](CampaignsApi.md#test_campaign_by_id) | **POST** /campaigns/{id}/test | 
[**update_campaign_archive_by_id**](CampaignsApi.md#update_campaign_archive_by_id) | **PUT** /campaigns/{id}/archive | 
[**update_campaign_by_id**](CampaignsApi.md#update_campaign_by_id) | **PUT** /campaigns/{id} | 
[**update_campaign_status_by_id**](CampaignsApi.md#update_campaign_status_by_id) | **PUT** /campaigns/{id}/status | 
[**update_preview_campaign_by_id**](CampaignsApi.md#update_preview_campaign_by_id) | **POST** /campaigns/{id}/preview | 


# **create_campaign**
> CreateCampaign200Response create_campaign(campaign_request=campaign_request)



handles campaign creation

### Example

* Basic Authentication (basicAuth):

```python
import time
import os
import listmonk_client
from listmonk_client.models.campaign_request import CampaignRequest
from listmonk_client.models.create_campaign200_response import CreateCampaign200Response
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
    api_instance = listmonk_client.CampaignsApi(api_client)
    campaign_request = listmonk_client.CampaignRequest()  # CampaignRequest | new campaign info (optional)
    
    try:
        api_response = api_instance.create_campaign(campaign_request=campaign_request)
        print("The response of CampaignsApi->create_campaign:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CampaignsApi->create_campaign: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_request** | [**CampaignRequest**](CampaignRequest.md)| new campaign info | [optional] 

### Return type

[**CreateCampaign200Response**](CreateCampaign200Response.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | new campaign object |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_campaign_content_by_id**
> GetImportSubscriberStats200Response create_campaign_content_by_id(id, campaign_content_request=campaign_content_request)



handles campaign content (body) format conversions.

### Example

* Basic Authentication (basicAuth):

```python
import time
import os
import listmonk_client
from listmonk_client.models.campaign_content_request import CampaignContentRequest
from listmonk_client.models.get_import_subscriber_stats200_response import GetImportSubscriberStats200Response
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
    api_instance = listmonk_client.CampaignsApi(api_client)
    id = 56  # int | ID of campaign that you choose to create content
    campaign_content_request = listmonk_client.CampaignContentRequest()  # CampaignContentRequest | updated campaign content (optional)
    
    try:
        api_response = api_instance.create_campaign_content_by_id(id, campaign_content_request=campaign_content_request)
        print("The response of CampaignsApi->create_campaign_content_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CampaignsApi->create_campaign_content_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of campaign that you choose to create content | 
 **campaign_content_request** | [**CampaignContentRequest**](CampaignContentRequest.md)| updated campaign content | [optional] 

### Return type

[**GetImportSubscriberStats200Response**](GetImportSubscriberStats200Response.md)

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

# **delete_campaign_by_id**
> GetHealthCheck200Response delete_campaign_by_id(id)



deletes specified campaign

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
    api_instance = listmonk_client.CampaignsApi(api_client)
    id = 56  # int | The id value of the campaign you want to get.
    
    try:
        api_response = api_instance.delete_campaign_by_id(id)
        print("The response of CampaignsApi->delete_campaign_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CampaignsApi->delete_campaign_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id value of the campaign you want to get. | 

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

# **get_campaign_analytics**
> GetCampaignAnalytics200Response get_campaign_analytics(type, var_from, to, id=id)



retrieves view counts for a campaign.

### Example

* Basic Authentication (basicAuth):

```python
import time
import os
import listmonk_client
from listmonk_client.models.get_campaign_analytics200_response import GetCampaignAnalytics200Response
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
    api_instance = listmonk_client.CampaignsApi(api_client)
    type = 'type_example'  # str | type of stats, either links, view, click or bounce
    var_from = 'var_from_example'  # str | start value of date range
    to = 'to_example'  # str | end value of date range
    id = 'id_example'  # str | campaign id/s to retrive view counts (optional)
    
    try:
        api_response = api_instance.get_campaign_analytics(type, var_from, to, id=id)
        print("The response of CampaignsApi->get_campaign_analytics:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CampaignsApi->get_campaign_analytics: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| type of stats, either links, view, click or bounce | 
 **var_from** | **str**| start value of date range | 
 **to** | **str**| end value of date range | 
 **id** | **str**| campaign id/s to retrive view counts | [optional] 

### Return type

[**GetCampaignAnalytics200Response**](GetCampaignAnalytics200Response.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | list of stats for given set of campaign ids |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_campaign_by_id**
> GetCampaignById200Response get_campaign_by_id(id, no_body=no_body)



handles retrieval of campaigns.

### Example

* Basic Authentication (basicAuth):

```python
import time
import os
import listmonk_client
from listmonk_client.models.get_campaign_by_id200_response import GetCampaignById200Response
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
    api_instance = listmonk_client.CampaignsApi(api_client)
    id = 56  # int | The id value of the campaign you want to get.
    no_body = True  # bool | boolean flag for response with/without body (optional)
    
    try:
        api_response = api_instance.get_campaign_by_id(id, no_body=no_body)
        print("The response of CampaignsApi->get_campaign_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CampaignsApi->get_campaign_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id value of the campaign you want to get. | 
 **no_body** | **bool**| boolean flag for response with/without body | [optional] 

### Return type

[**GetCampaignById200Response**](GetCampaignById200Response.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | campaign object |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_campaigns**
> GetCampaigns200Response get_campaigns(status=status, no_body=no_body, page=page, per_page=per_page, query=query, order_by=order_by, order=order)



handles retrieval of campaigns

### Example

* Basic Authentication (basicAuth):

```python
import time
import os
import listmonk_client
from listmonk_client.models.get_campaigns200_response import GetCampaigns200Response
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
    api_instance = listmonk_client.CampaignsApi(api_client)
    status = ['status_example']  # List[str] | status flag of campaign (optional)
    no_body = True  # bool | boolean flag for response with/without body (optional)
    page = 56  # int | total number of pages (optional)
    per_page = 56  # int | number of items per page (optional)
    query = 'query_example'  # str | Optional string to search a list by name. (optional)
    order_by = 'order_by_example'  # str | Field to sort results by. name|status|created_at|updated_at (optional)
    order = 'order_example'  # str | ASC|DESC Sort by ascending or descending order. (optional)
    
    try:
        api_response = api_instance.get_campaigns(status=status, no_body=no_body, page=page, per_page=per_page, query=query,
                                                  order_by=order_by, order=order)
        print("The response of CampaignsApi->get_campaigns:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CampaignsApi->get_campaigns: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status** | [**List[str]**](str.md)| status flag of campaign | [optional] 
 **no_body** | **bool**| boolean flag for response with/without body | [optional] 
 **page** | **int**| total number of pages | [optional] 
 **per_page** | **int**| number of items per page | [optional] 
 **query** | **str**| Optional string to search a list by name. | [optional] 
 **order_by** | **str**| Field to sort results by. name|status|created_at|updated_at | [optional] 
 **order** | **str**| ASC|DESC Sort by ascending or descending order. | [optional] 

### Return type

[**GetCampaigns200Response**](GetCampaigns200Response.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | list of campaigns |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_running_campaign_stats**
> GetRunningCampaignStats200Response get_running_campaign_stats()



returns stats of a given set of campaign IDs.

### Example

* Basic Authentication (basicAuth):

```python
import time
import os
import listmonk_client
from listmonk_client.models.get_running_campaign_stats200_response import GetRunningCampaignStats200Response
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
    api_instance = listmonk_client.CampaignsApi(api_client)
    
    try:
        api_response = api_instance.get_running_campaign_stats()
        print("The response of CampaignsApi->get_running_campaign_stats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CampaignsApi->get_running_campaign_stats: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**GetRunningCampaignStats200Response**](GetRunningCampaignStats200Response.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | list of stats for given set of campaign ids |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **preview_campaign_by_id**
> str preview_campaign_by_id(id, template_id=template_id)



renders the HTML preview of a campaign body

### Example

* Basic Authentication (basicAuth):

```python
import time
import os
import listmonk_client
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
    api_instance = listmonk_client.CampaignsApi(api_client)
    id = 56  # int | The id value of the campaign you want to get the preview of
    template_id = 56  # int | template id (optional)
    
    try:
        api_response = api_instance.preview_campaign_by_id(id, template_id=template_id)
        print("The response of CampaignsApi->preview_campaign_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CampaignsApi->preview_campaign_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id value of the campaign you want to get the preview of | 
 **template_id** | **int**| template id | [optional] 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | HTML Preview of requested campaign |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **preview_campaign_text_by_id**
> str preview_campaign_text_by_id(id, template_id=template_id, content_type=content_type, body=body)



renders the HTML preview of a campaign body

### Example

* Basic Authentication (basicAuth):

```python
import time
import os
import listmonk_client
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
    api_instance = listmonk_client.CampaignsApi(api_client)
    id = 56  # int | The id value of the campaign you want to get the preview of
    template_id = 56  # int | template id (optional)
    content_type = 'content_type_example'  # str | content type (optional)
    body = 'body_example'  # str | campaign body (optional)
    
    try:
        api_response = api_instance.preview_campaign_text_by_id(id, template_id=template_id, content_type=content_type, body=body)
        print("The response of CampaignsApi->preview_campaign_text_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CampaignsApi->preview_campaign_text_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id value of the campaign you want to get the preview of | 
 **template_id** | **int**| template id | [optional] 
 **content_type** | **str**| content type | [optional] 
 **body** | **str**| campaign body | [optional] 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **test_campaign_by_id**
> GetHealthCheck200Response test_campaign_by_id(id, template_id=template_id)



handles sending of campaign message to arbitrary subscribers for testing

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
    api_instance = listmonk_client.CampaignsApi(api_client)
    id = 56  # int | ID of campaign that you want to test
    template_id = 56  # int | template id (optional)
    
    try:
        api_response = api_instance.test_campaign_by_id(id, template_id=template_id)
        print("The response of CampaignsApi->test_campaign_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CampaignsApi->test_campaign_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of campaign that you want to test | 
 **template_id** | **int**| template id | [optional] 

### Return type

[**GetHealthCheck200Response**](GetHealthCheck200Response.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_campaign_archive_by_id**
> GetHealthCheck200Response update_campaign_archive_by_id(id, update_campaign_archive_by_id_request=update_campaign_archive_by_id_request)



handles campaign status modification

### Example

* Basic Authentication (basicAuth):

```python
import time
import os
import listmonk_client
from listmonk_client.models.get_health_check200_response import GetHealthCheck200Response
from listmonk_client.models.update_campaign_archive_by_id_request import UpdateCampaignArchiveByIdRequest
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
    api_instance = listmonk_client.CampaignsApi(api_client)
    id = 56  # int | The id value of the campaign you want to get the preview of
    update_campaign_archive_by_id_request = listmonk_client.UpdateCampaignArchiveByIdRequest()  # UpdateCampaignArchiveByIdRequest | archive campaign related parameters (optional)
    
    try:
        api_response = api_instance.update_campaign_archive_by_id(id,
                                                                  update_campaign_archive_by_id_request=update_campaign_archive_by_id_request)
        print("The response of CampaignsApi->update_campaign_archive_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CampaignsApi->update_campaign_archive_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id value of the campaign you want to get the preview of | 
 **update_campaign_archive_by_id_request** | [**UpdateCampaignArchiveByIdRequest**](UpdateCampaignArchiveByIdRequest.md)| archive campaign related parameters | [optional] 

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
**200** | response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_campaign_by_id**
> CreateCampaign200Response update_campaign_by_id(id, campaign_request=campaign_request)



handle updation of campaign

### Example

* Basic Authentication (basicAuth):

```python
import time
import os
import listmonk_client
from listmonk_client.models.campaign_request import CampaignRequest
from listmonk_client.models.create_campaign200_response import CreateCampaign200Response
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
    api_instance = listmonk_client.CampaignsApi(api_client)
    id = 56  # int | the id value of campaign you want to update
    campaign_request = listmonk_client.CampaignRequest()  # CampaignRequest | updated campaign fields (optional)
    
    try:
        api_response = api_instance.update_campaign_by_id(id, campaign_request=campaign_request)
        print("The response of CampaignsApi->update_campaign_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CampaignsApi->update_campaign_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| the id value of campaign you want to update | 
 **campaign_request** | [**CampaignRequest**](CampaignRequest.md)| updated campaign fields | [optional] 

### Return type

[**CreateCampaign200Response**](CreateCampaign200Response.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | updated campaign object |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_campaign_status_by_id**
> GetCampaignById200Response update_campaign_status_by_id(id, update_campaign_status_by_id_request=update_campaign_status_by_id_request)



handles campaign status modification

### Example

* Basic Authentication (basicAuth):

```python
import time
import os
import listmonk_client
from listmonk_client.models.get_campaign_by_id200_response import GetCampaignById200Response
from listmonk_client.models.update_campaign_status_by_id_request import UpdateCampaignStatusByIdRequest
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
    api_instance = listmonk_client.CampaignsApi(api_client)
    id = 56  # int | The id value of the campaign you want to get the preview of
    update_campaign_status_by_id_request = listmonk_client.UpdateCampaignStatusByIdRequest()  # UpdateCampaignStatusByIdRequest | campaign status update (optional)
    
    try:
        api_response = api_instance.update_campaign_status_by_id(id,
                                                                 update_campaign_status_by_id_request=update_campaign_status_by_id_request)
        print("The response of CampaignsApi->update_campaign_status_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CampaignsApi->update_campaign_status_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id value of the campaign you want to get the preview of | 
 **update_campaign_status_by_id_request** | [**UpdateCampaignStatusByIdRequest**](UpdateCampaignStatusByIdRequest.md)| campaign status update | [optional] 

### Return type

[**GetCampaignById200Response**](GetCampaignById200Response.md)

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

# **update_preview_campaign_by_id**
> str update_preview_campaign_by_id(id, template_id=template_id, content_type=content_type, body=body)



renders the HTML preview of a campaign body

### Example

* Basic Authentication (basicAuth):

```python
import time
import os
import listmonk_client
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
    api_instance = listmonk_client.CampaignsApi(api_client)
    id = 56  # int | The id value of the campaign you want to get the preview of
    template_id = 56  # int | template id (optional)
    content_type = 'content_type_example'  # str | content type (optional)
    body = 'body_example'  # str | template body (optional)
    
    try:
        api_response = api_instance.update_preview_campaign_by_id(id, template_id=template_id, content_type=content_type,
                                                                  body=body)
        print("The response of CampaignsApi->update_preview_campaign_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CampaignsApi->update_preview_campaign_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id value of the campaign you want to get the preview of | 
 **template_id** | **int**| template id | [optional] 
 **content_type** | **str**| content type | [optional] 
 **body** | **str**| template body | [optional] 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | HTML Preview of requested campaign |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

