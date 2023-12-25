# CampaignStats


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**status** | **str** |  | [optional] 
**to_send** | **int** |  | [optional] 
**sent** | **int** |  | [optional] 
**started_at** | **date** |  | [optional] 
**updated_at** | **date** |  | [optional] 
**rate** | **int** |  | [optional] 
**net_rate** | **int** |  | [optional] 

## Example

```python
from listmonk.models.campaign_stats import CampaignStats

# TODO update the JSON string below
json = "{}"
# create an instance of CampaignStats from a JSON string
campaign_stats_instance = CampaignStats.from_json(json)
# print the JSON string representation of the object
print
CampaignStats.to_json()

# convert the object into a dict
campaign_stats_dict = campaign_stats_instance.to_dict()
# create an instance of CampaignStats from a dict
campaign_stats_form_dict = campaign_stats.from_dict(campaign_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


