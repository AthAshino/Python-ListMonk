# Settings


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_site_name** | **str** |  | [optional] 
**app_root_url** | **str** |  | [optional] 
**app_logo_url** | **str** |  | [optional] 
**app_favicon_url** | **str** |  | [optional] 
**app_from_email** | **str** |  | [optional] 
**app_notify_emails** | **List[str]** |  | [optional] 
**app_enable_public_subscription_page** | **bool** |  | [optional] 
**app_enable_public_archive** | **bool** |  | [optional] 
**app_send_optin_confirmation** | **bool** |  | [optional] 
**app_check_updates** | **bool** |  | [optional] 
**app_lang** | **str** |  | [optional] 
**app_batch_size** | **int** |  | [optional] 
**app_concurrency** | **int** |  | [optional] 
**app_max_send_errors** | **int** |  | [optional] 
**app_message_rate** | **int** |  | [optional] 
**app_message_sliding_window** | **bool** |  | [optional] 
**app_message_sliding_window_duration** | **str** |  | [optional] 
**app_message_sliding_window_rate** | **int** |  | [optional] 
**privacy_individual_tracking** | **bool** |  | [optional] 
**privacy_unsubscribe_header** | **bool** |  | [optional] 
**privacy_allow_blocklist** | **bool** |  | [optional] 
**privacy_allow_preferences** | **bool** |  | [optional] 
**privacy_allow_export** | **bool** |  | [optional] 
**privacy_allow_wipe** | **bool** |  | [optional] 
**privacy_exportable** | **List[str]** |  | [optional] 
**privacy_domain_blocklist** | **List[object]** |  | [optional] 
**upload_provider** | **str** |  | [optional] 
**upload_filesystem_upload_path** | **str** |  | [optional] 
**upload_filesystem_upload_uri** | **str** |  | [optional] 
**upload_s3_url** | **str** |  | [optional] 
**upload_s3_public_url** | **str** |  | [optional] 
**upload_s3_aws_access_key_id** | **str** |  | [optional] 
**upload_s3_aws_default_region** | **str** |  | [optional] 
**upload_s3_bucket** | **str** |  | [optional] 
**upload_s3_bucket_domain** | **str** |  | [optional] 
**upload_s3_bucket_path** | **str** |  | [optional] 
**upload_s3_bucket_type** | **str** |  | [optional] 
**upload_s3_expiry** | **str** |  | [optional] 
**smtp** | [**List[SMTPSettings]**](SMTPSettings.md) |  | [optional] 
**messengers** | **List[object]** |  | [optional] 
**bounce_enabled** | **bool** |  | [optional] 
**bounce_webhooks_enabled** | **bool** |  | [optional] 
**bounce_count** | **int** |  | [optional] 
**bounce_action** | **str** |  | [optional] 
**bounce_ses_enabled** | **bool** |  | [optional] 
**bounce_sendgrid_enabled** | **bool** |  | [optional] 
**bounce_sendgrid_key** | **str** |  | [optional] 
**bounce_postmark_enabled** | **bool** |  | [optional] 
**bounce_postmark_username** | **str** |  | [optional] 
**bounce_postmark_password** | **str** |  | [optional] 
**bounce_mailboxes** | [**List[MailBoxBounces]**](MailBoxBounces.md) |  | [optional] 
**appearance_admin_custom_css** | **str** |  | [optional] 
**appearance_admin_custom_js** | **str** |  | [optional] 
**appearance_public_custom_css** | **str** |  | [optional] 
**appearance_public_custom_js** | **str** |  | [optional] 

## Example

```python
from listmonk.models.settings import Settings

# TODO update the JSON string below
json = "{}"
# create an instance of Settings from a JSON string
settings_instance = Settings.from_json(json)
# print the JSON string representation of the object
print
Settings.to_json()

# convert the object into a dict
settings_dict = settings_instance.to_dict()
# create an instance of Settings from a dict
settings_form_dict = settings.from_dict(settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


