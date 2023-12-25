# CampaignContentRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**created_at** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**campaign_id** | **int** |  | [optional] 
**views** | **int** |  | [optional] 
**clicks** | **int** |  | [optional] 
**lists** | [**List[BounceResultsInnerCampaign]**](BounceResultsInnerCampaign.md) |  | [optional] 
**started_at** | **str** |  | [optional] 
**to_send** | **int** |  | [optional] 
**sent** | **int** |  | [optional] 
**uuid** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**subject** | **str** |  | [optional] 
**from_email** | **str** |  | [optional] 
**body** | **str** |  | [optional] 
**send_at** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**content_type** | **str** |  | [optional] 
**tags** | **List[str]** |  | [optional] 
**template_id** | **int** |  | [optional] 
**messenger** | **str** |  | [optional] 
**var_from** | **str** |  | [optional] 
**to** | **str** |  | [optional] 

## Example

```python
from listmonk.models.campaign_content_request import CampaignContentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CampaignContentRequest from a JSON string
campaign_content_request_instance = CampaignContentRequest.from_json(json)
# print the JSON string representation of the object
print
CampaignContentRequest.to_json()

# convert the object into a dict
campaign_content_request_dict = campaign_content_request_instance.to_dict()
# create an instance of CampaignContentRequest from a dict
campaign_content_request_form_dict = campaign_content_request.from_dict(campaign_content_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


