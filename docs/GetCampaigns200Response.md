# GetCampaigns200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**GetCampaigns200ResponseData**](GetCampaigns200ResponseData.md) |  | [optional] 

## Example

```python
from listmonk_client.models.get_campaigns200_response import GetCampaigns200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetCampaigns200Response from a JSON string
get_campaigns200_response_instance = GetCampaigns200Response.from_json(json)
# print the JSON string representation of the object
print
GetCampaigns200Response.to_json()

# convert the object into a dict
get_campaigns200_response_dict = get_campaigns200_response_instance.to_dict()
# create an instance of GetCampaigns200Response from a dict
get_campaigns200_response_form_dict = get_campaigns200_response.from_dict(get_campaigns200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


