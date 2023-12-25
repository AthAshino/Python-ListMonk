# openapi_client.TemplatesApi

All URIs are relative to *http://localhost:9000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_template_by_id**](TemplatesApi.md#delete_template_by_id) | **DELETE** /templates/{id} | 
[**get_template_by_id**](TemplatesApi.md#get_template_by_id) | **GET** /templates/{id} | 
[**get_templates**](TemplatesApi.md#get_templates) | **GET** /templates | 
[**preview_template**](TemplatesApi.md#preview_template) | **POST** /templates/preview | 
[**preview_template_by_id**](TemplatesApi.md#preview_template_by_id) | **GET** /templates/{id}/preview | 
[**update_template_by_id**](TemplatesApi.md#update_template_by_id) | **PUT** /templates/{id}/default | 


# **delete_template_by_id**
> GetHealthCheck200Response delete_template_by_id(id)



handles deletion of templates

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
    api_instance = listmonk_client.TemplatesApi(api_client)
    id = 56  # int | The id value of the template you want to delete.
    
    try:
        api_response = api_instance.delete_template_by_id(id)
        print("The response of TemplatesApi->delete_template_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemplatesApi->delete_template_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id value of the template you want to delete. | 

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

# **get_template_by_id**
> GetTemplateById200Response get_template_by_id(id, no_body=no_body)



handles retrieval of templates

### Example

* Basic Authentication (basicAuth):

```python
import time
import os
import listmonk_client
from listmonk_client.models.get_template_by_id200_response import GetTemplateById200Response
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
    api_instance = listmonk_client.TemplatesApi(api_client)
    id = 56  # int | The id value of the template you want to get.
    no_body = True  # bool | boolean flag for response with/without body (optional)
    
    try:
        api_response = api_instance.get_template_by_id(id, no_body=no_body)
        print("The response of TemplatesApi->get_template_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemplatesApi->get_template_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id value of the template you want to get. | 
 **no_body** | **bool**| boolean flag for response with/without body | [optional] 

### Return type

[**GetTemplateById200Response**](GetTemplateById200Response.md)

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

# **get_templates**
> GetTemplates200Response get_templates(no_body)



handles retrieval of templates

### Example

* Basic Authentication (basicAuth):

```python
import time
import os
import listmonk_client
from listmonk_client.models.get_templates200_response import GetTemplates200Response
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
    api_instance = listmonk_client.TemplatesApi(api_client)
    no_body = True  # bool | boolean flag for response with/without body
    
    try:
        api_response = api_instance.get_templates(no_body)
        print("The response of TemplatesApi->get_templates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemplatesApi->get_templates: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **no_body** | **bool**| boolean flag for response with/without body | 

### Return type

[**GetTemplates200Response**](GetTemplates200Response.md)

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

# **preview_template**
> str preview_template(template_type=template_type, body=body)



get the HTML preview of a template.

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
    api_instance = listmonk_client.TemplatesApi(api_client)
    template_type = 'template_type_example'  # str | type of template (optional)
    body = 'body_example'  # str | template body (optional)
    
    try:
        api_response = api_instance.preview_template(template_type=template_type, body=body)
        print("The response of TemplatesApi->preview_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemplatesApi->preview_template: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_type** | **str**| type of template | [optional] 
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
**200** | response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **preview_template_by_id**
> str preview_template_by_id(id, template_type=template_type, body=body)



renders the HTML preview of a template.

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
    api_instance = listmonk_client.TemplatesApi(api_client)
    id = 56  # int | The id value of the template you want to get.
    template_type = 'template_type_example'  # str | type of template (optional)
    body = 'body_example'  # str | template body (optional)
    
    try:
        api_response = api_instance.preview_template_by_id(id, template_type=template_type, body=body)
        print("The response of TemplatesApi->preview_template_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemplatesApi->preview_template_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id value of the template you want to get. | 
 **template_type** | **str**| type of template | [optional] 
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
**200** | response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_template_by_id**
> Template update_template_by_id(id)



handles template modification.

### Example

* Basic Authentication (basicAuth):

```python
import time
import os
import listmonk_client
from listmonk_client.models.template import Template
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
    api_instance = listmonk_client.TemplatesApi(api_client)
    id = 56  # int | The id value of the template you want to set to the default template.
    
    try:
        api_response = api_instance.update_template_by_id(id)
        print("The response of TemplatesApi->update_template_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemplatesApi->update_template_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id value of the template you want to set to the default template. | 

### Return type

[**Template**](Template.md)

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

