# CampaignAnalyticsCount


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**campaign_id** | **int** |  | [optional] 
**count** | **int** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 

## Example

```python
from listmonk_client.models.campaign_analytics_count import CampaignAnalyticsCount

# TODO update the JSON string below
json = "{}"
# create an instance of CampaignAnalyticsCount from a JSON string
campaign_analytics_count_instance = CampaignAnalyticsCount.from_json(json)
# print the JSON string representation of the object
print
CampaignAnalyticsCount.to_json()

# convert the object into a dict
campaign_analytics_count_dict = campaign_analytics_count_instance.to_dict()
# create an instance of CampaignAnalyticsCount from a dict
campaign_analytics_count_form_dict = campaign_analytics_count.from_dict(campaign_analytics_count_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


