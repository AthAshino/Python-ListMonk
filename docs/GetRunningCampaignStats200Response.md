# GetRunningCampaignStats200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[CampaignStats]**](CampaignStats.md) |  | [optional] 

## Example

```python
from listmonk.models.get_running_campaign_stats200_response import GetRunningCampaignStats200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetRunningCampaignStats200Response from a JSON string
get_running_campaign_stats200_response_instance = GetRunningCampaignStats200Response.from_json(json)
# print the JSON string representation of the object
print
GetRunningCampaignStats200Response.to_json()

# convert the object into a dict
get_running_campaign_stats200_response_dict = get_running_campaign_stats200_response_instance.to_dict()
# create an instance of GetRunningCampaignStats200Response from a dict
get_running_campaign_stats200_response_form_dict = get_running_campaign_stats200_response.from_dict(
    get_running_campaign_stats200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


