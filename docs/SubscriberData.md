# SubscriberData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | [optional] 
**profile** | [**List[SubscriberProfile]**](SubscriberProfile.md) |  | [optional] 
**subscriptions** | [**List[Subscriptions]**](Subscriptions.md) |  | [optional] 
**campaign_views** | **List[object]** |  | [optional] 
**link_clicks** | **List[object]** |  | [optional] 

## Example

```python
from listmonk.models.subscriber_data import SubscriberData

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriberData from a JSON string
subscriber_data_instance = SubscriberData.from_json(json)
# print the JSON string representation of the object
print
SubscriberData.to_json()

# convert the object into a dict
subscriber_data_dict = subscriber_data_instance.to_dict()
# create an instance of SubscriberData from a dict
subscriber_data_form_dict = subscriber_data.from_dict(subscriber_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


