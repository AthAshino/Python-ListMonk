# DashboardCountDataCampaigns


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** |  | [optional] 
**by_status** | [**DashboardCountDataCampaignsByStatus**](DashboardCountDataCampaignsByStatus.md) |  | [optional] 

## Example

```python
from listmonk.models.dashboard_count_data_campaigns import DashboardCountDataCampaigns

# TODO update the JSON string below
json = "{}"
# create an instance of DashboardCountDataCampaigns from a JSON string
dashboard_count_data_campaigns_instance = DashboardCountDataCampaigns.from_json(json)
# print the JSON string representation of the object
print
DashboardCountDataCampaigns.to_json()

# convert the object into a dict
dashboard_count_data_campaigns_dict = dashboard_count_data_campaigns_instance.to_dict()
# create an instance of DashboardCountDataCampaigns from a dict
dashboard_count_data_campaigns_form_dict = dashboard_count_data_campaigns.from_dict(dashboard_count_data_campaigns_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


