# BounceResultsInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**type** | **str** |  | [optional] 
**source** | **str** |  | [optional] 
**meta** | **object** |  | [optional] 
**created_at** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**subscriber_uuid** | **str** |  | [optional] 
**subscriber_id** | **int** |  | [optional] 
**campaign** | [**BounceResultsInnerCampaign**](BounceResultsInnerCampaign.md) |  | [optional] 
**campaign_uuid** | **str** |  | [optional] 
**total** | **int** |  | [optional] 

## Example

```python
from listmonk_client.models.bounce_results_inner import BounceResultsInner

# TODO update the JSON string below
json = "{}"
# create an instance of BounceResultsInner from a JSON string
bounce_results_inner_instance = BounceResultsInner.from_json(json)
# print the JSON string representation of the object
print
BounceResultsInner.to_json()

# convert the object into a dict
bounce_results_inner_dict = bounce_results_inner_instance.to_dict()
# create an instance of BounceResultsInner from a dict
bounce_results_inner_form_dict = bounce_results_inner.from_dict(bounce_results_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


