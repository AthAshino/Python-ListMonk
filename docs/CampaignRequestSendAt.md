# CampaignRequestSendAt


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**headers** | **List[object]** |  | [optional] 
**template_id** | **float** |  | [optional] 

## Example

```python
from listmonk_client.models.campaign_request_send_at import CampaignRequestSendAt

# TODO update the JSON string below
json = "{}"
# create an instance of CampaignRequestSendAt from a JSON string
campaign_request_send_at_instance = CampaignRequestSendAt.from_json(json)
# print the JSON string representation of the object
print
CampaignRequestSendAt.to_json()

# convert the object into a dict
campaign_request_send_at_dict = campaign_request_send_at_instance.to_dict()
# create an instance of CampaignRequestSendAt from a dict
campaign_request_send_at_form_dict = campaign_request_send_at.from_dict(campaign_request_send_at_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


