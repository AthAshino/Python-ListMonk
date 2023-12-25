# UpdateCampaignStatusByIdRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 

## Example

```python
from listmonk_client.models.update_campaign_status_by_id_request import UpdateCampaignStatusByIdRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateCampaignStatusByIdRequest from a JSON string
update_campaign_status_by_id_request_instance = UpdateCampaignStatusByIdRequest.from_json(json)
# print the JSON string representation of the object
print
UpdateCampaignStatusByIdRequest.to_json()

# convert the object into a dict
update_campaign_status_by_id_request_dict = update_campaign_status_by_id_request_instance.to_dict()
# create an instance of UpdateCampaignStatusByIdRequest from a dict
update_campaign_status_by_id_request_form_dict = update_campaign_status_by_id_request.from_dict(
    update_campaign_status_by_id_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


