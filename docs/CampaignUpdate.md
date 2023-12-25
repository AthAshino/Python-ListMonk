# CampaignUpdate


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**subject** | **str** |  | [optional] 
**lists** | **List[int]** |  | [optional] 
**from_email** | **str** |  | [optional] 
**messenger** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**tags** | **List[str]** |  | [optional] 
**send_later** | **bool** |  | [optional] 
**send_at** | **object** |  | [optional] 
**headers** | **List[object]** |  | [optional] 
**template_id** | **int** |  | [optional] 
**content_type** | **str** |  | [optional] 
**body** | **str** |  | [optional] 
**altbody** | **str** |  | [optional] 
**archive** | **bool** |  | [optional] 
**archive_template_id** | **int** |  | [optional] 
**archive_meta** | **object** |  | [optional] 

## Example

```python
from listmonk_client.models.campaign_update import CampaignUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of CampaignUpdate from a JSON string
campaign_update_instance = CampaignUpdate.from_json(json)
# print the JSON string representation of the object
print
CampaignUpdate.to_json()

# convert the object into a dict
campaign_update_dict = campaign_update_instance.to_dict()
# create an instance of CampaignUpdate from a dict
campaign_update_form_dict = campaign_update.from_dict(campaign_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


