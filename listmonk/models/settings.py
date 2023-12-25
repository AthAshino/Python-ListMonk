# coding: utf-8

"""
    Listmonk

    The API collection for listmonk

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, ClassVar, Dict, List, Optional, Union
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from pydantic import Field
from listmonk_client.models.mail_box_bounces import MailBoxBounces
from listmonk_client.models.smtp_settings import SMTPSettings
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class Settings(BaseModel):
    """
    Settings
    """ # noqa: E501
    app_site_name: Optional[StrictStr] = Field(default=None, alias="app.site_name")
    app_root_url: Optional[StrictStr] = Field(default=None, alias="app.root_url")
    app_logo_url: Optional[StrictStr] = Field(default=None, alias="app.logo_url")
    app_favicon_url: Optional[StrictStr] = Field(default=None, alias="app.favicon_url")
    app_from_email: Optional[StrictStr] = Field(default=None, alias="app.from_email")
    app_notify_emails: Optional[List[StrictStr]] = Field(default=None, alias="app.notify_emails")
    app_enable_public_subscription_page: Optional[StrictBool] = Field(default=None, alias="app.enable_public_subscription_page")
    app_enable_public_archive: Optional[StrictBool] = Field(default=None, alias="app.enable_public_archive")
    app_send_optin_confirmation: Optional[StrictBool] = Field(default=None, alias="app.send_optin_confirmation")
    app_check_updates: Optional[StrictBool] = Field(default=None, alias="app.check_updates")
    app_lang: Optional[StrictStr] = Field(default=None, alias="app.lang")
    app_batch_size: Optional[StrictInt] = Field(default=None, alias="app.batch_size")
    app_concurrency: Optional[StrictInt] = Field(default=None, alias="app.concurrency")
    app_max_send_errors: Optional[StrictInt] = Field(default=None, alias="app.max_send_errors")
    app_message_rate: Optional[StrictInt] = Field(default=None, alias="app.message_rate")
    app_message_sliding_window: Optional[StrictBool] = Field(default=None, alias="app.message_sliding_window")
    app_message_sliding_window_duration: Optional[StrictStr] = Field(default=None, alias="app.message_sliding_window_duration")
    app_message_sliding_window_rate: Optional[StrictInt] = Field(default=None, alias="app.message_sliding_window_rate")
    privacy_individual_tracking: Optional[StrictBool] = Field(default=None, alias="privacy.individual_tracking")
    privacy_unsubscribe_header: Optional[StrictBool] = Field(default=None, alias="privacy.unsubscribe_header")
    privacy_allow_blocklist: Optional[StrictBool] = Field(default=None, alias="privacy.allow_blocklist")
    privacy_allow_preferences: Optional[StrictBool] = Field(default=None, alias="privacy.allow_preferences")
    privacy_allow_export: Optional[StrictBool] = Field(default=None, alias="privacy.allow_export")
    privacy_allow_wipe: Optional[StrictBool] = Field(default=None, alias="privacy.allow_wipe")
    privacy_exportable: Optional[List[StrictStr]] = Field(default=None, alias="privacy.exportable")
    privacy_domain_blocklist: Optional[List[Union[str, Any]]] = Field(default=None, alias="privacy.domain_blocklist")
    upload_provider: Optional[StrictStr] = Field(default=None, alias="upload.provider")
    upload_filesystem_upload_path: Optional[StrictStr] = Field(default=None, alias="upload.filesystem.upload_path")
    upload_filesystem_upload_uri: Optional[StrictStr] = Field(default=None, alias="upload.filesystem.upload_uri")
    upload_s3_url: Optional[StrictStr] = Field(default=None, alias="upload.s3.url")
    upload_s3_public_url: Optional[StrictStr] = Field(default=None, alias="upload.s3.public_url")
    upload_s3_aws_access_key_id: Optional[StrictStr] = Field(default=None, alias="upload.s3.aws_access_key_id")
    upload_s3_aws_default_region: Optional[StrictStr] = Field(default=None, alias="upload.s3.aws_default_region")
    upload_s3_bucket: Optional[StrictStr] = Field(default=None, alias="upload.s3.bucket")
    upload_s3_bucket_domain: Optional[StrictStr] = Field(default=None, alias="upload.s3.bucket_domain")
    upload_s3_bucket_path: Optional[StrictStr] = Field(default=None, alias="upload.s3.bucket_path")
    upload_s3_bucket_type: Optional[StrictStr] = Field(default=None, alias="upload.s3.bucket_type")
    upload_s3_expiry: Optional[StrictStr] = Field(default=None, alias="upload.s3.expiry")
    smtp: Optional[List[SMTPSettings]] = None
    messengers: Optional[List[Union[str, Any]]] = None
    bounce_enabled: Optional[StrictBool] = Field(default=None, alias="bounce.enabled")
    bounce_webhooks_enabled: Optional[StrictBool] = Field(default=None, alias="bounce.webhooks_enabled")
    bounce_count: Optional[StrictInt] = Field(default=None, alias="bounce.count")
    bounce_action: Optional[StrictStr] = Field(default=None, alias="bounce.action")
    bounce_ses_enabled: Optional[StrictBool] = Field(default=None, alias="bounce.ses_enabled")
    bounce_sendgrid_enabled: Optional[StrictBool] = Field(default=None, alias="bounce.sendgrid_enabled")
    bounce_sendgrid_key: Optional[StrictStr] = Field(default=None, alias="bounce.sendgrid_key")
    bounce_postmark_enabled: Optional[StrictBool] = Field(default=None, alias="bounce.postmark_enabled")
    bounce_postmark_username: Optional[StrictStr] = Field(default=None, alias="bounce.postmark_username")
    bounce_postmark_password: Optional[StrictStr] = Field(default=None, alias="bounce.postmark_password")
    bounce_mailboxes: Optional[List[MailBoxBounces]] = Field(default=None, alias="bounce.mailboxes")
    appearance_admin_custom_css: Optional[StrictStr] = Field(default=None, alias="appearance.admin.custom_css")
    appearance_admin_custom_js: Optional[StrictStr] = Field(default=None, alias="appearance.admin.custom_js")
    appearance_public_custom_css: Optional[StrictStr] = Field(default=None, alias="appearance.public.custom_css")
    appearance_public_custom_js: Optional[StrictStr] = Field(default=None, alias="appearance.public.custom_js")
    __properties: ClassVar[List[str]] = ["app.site_name", "app.root_url", "app.logo_url", "app.favicon_url", "app.from_email", "app.notify_emails", "app.enable_public_subscription_page", "app.enable_public_archive", "app.send_optin_confirmation", "app.check_updates", "app.lang", "app.batch_size", "app.concurrency", "app.max_send_errors", "app.message_rate", "app.message_sliding_window", "app.message_sliding_window_duration", "app.message_sliding_window_rate", "privacy.individual_tracking", "privacy.unsubscribe_header", "privacy.allow_blocklist", "privacy.allow_preferences", "privacy.allow_export", "privacy.allow_wipe", "privacy.exportable", "privacy.domain_blocklist", "upload.provider", "upload.filesystem.upload_path", "upload.filesystem.upload_uri", "upload.s3.url", "upload.s3.public_url", "upload.s3.aws_access_key_id", "upload.s3.aws_default_region", "upload.s3.bucket", "upload.s3.bucket_domain", "upload.s3.bucket_path", "upload.s3.bucket_type", "upload.s3.expiry", "smtp", "messengers", "bounce.enabled", "bounce.webhooks_enabled", "bounce.count", "bounce.action", "bounce.ses_enabled", "bounce.sendgrid_enabled", "bounce.sendgrid_key", "bounce.postmark_enabled", "bounce.postmark_username", "bounce.postmark_password", "bounce.mailboxes", "appearance.admin.custom_css", "appearance.admin.custom_js", "appearance.public.custom_css", "appearance.public.custom_js"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of Settings from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in smtp (list)
        _items = []
        if self.smtp:
            for _item in self.smtp:
                if _item:
                    _items.append(_item.to_dict())
            _dict['smtp'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in bounce_mailboxes (list)
        _items = []
        if self.bounce_mailboxes:
            for _item in self.bounce_mailboxes:
                if _item:
                    _items.append(_item.to_dict())
            _dict['bounce.mailboxes'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of Settings from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "app.site_name": obj.get("app.site_name"),
            "app.root_url": obj.get("app.root_url"),
            "app.logo_url": obj.get("app.logo_url"),
            "app.favicon_url": obj.get("app.favicon_url"),
            "app.from_email": obj.get("app.from_email"),
            "app.notify_emails": obj.get("app.notify_emails"),
            "app.enable_public_subscription_page": obj.get("app.enable_public_subscription_page"),
            "app.enable_public_archive": obj.get("app.enable_public_archive"),
            "app.send_optin_confirmation": obj.get("app.send_optin_confirmation"),
            "app.check_updates": obj.get("app.check_updates"),
            "app.lang": obj.get("app.lang"),
            "app.batch_size": obj.get("app.batch_size"),
            "app.concurrency": obj.get("app.concurrency"),
            "app.max_send_errors": obj.get("app.max_send_errors"),
            "app.message_rate": obj.get("app.message_rate"),
            "app.message_sliding_window": obj.get("app.message_sliding_window"),
            "app.message_sliding_window_duration": obj.get("app.message_sliding_window_duration"),
            "app.message_sliding_window_rate": obj.get("app.message_sliding_window_rate"),
            "privacy.individual_tracking": obj.get("privacy.individual_tracking"),
            "privacy.unsubscribe_header": obj.get("privacy.unsubscribe_header"),
            "privacy.allow_blocklist": obj.get("privacy.allow_blocklist"),
            "privacy.allow_preferences": obj.get("privacy.allow_preferences"),
            "privacy.allow_export": obj.get("privacy.allow_export"),
            "privacy.allow_wipe": obj.get("privacy.allow_wipe"),
            "privacy.exportable": obj.get("privacy.exportable"),
            "privacy.domain_blocklist": obj.get("privacy.domain_blocklist"),
            "upload.provider": obj.get("upload.provider"),
            "upload.filesystem.upload_path": obj.get("upload.filesystem.upload_path"),
            "upload.filesystem.upload_uri": obj.get("upload.filesystem.upload_uri"),
            "upload.s3.url": obj.get("upload.s3.url"),
            "upload.s3.public_url": obj.get("upload.s3.public_url"),
            "upload.s3.aws_access_key_id": obj.get("upload.s3.aws_access_key_id"),
            "upload.s3.aws_default_region": obj.get("upload.s3.aws_default_region"),
            "upload.s3.bucket": obj.get("upload.s3.bucket"),
            "upload.s3.bucket_domain": obj.get("upload.s3.bucket_domain"),
            "upload.s3.bucket_path": obj.get("upload.s3.bucket_path"),
            "upload.s3.bucket_type": obj.get("upload.s3.bucket_type"),
            "upload.s3.expiry": obj.get("upload.s3.expiry"),
            "smtp": [SMTPSettings.from_dict(_item) for _item in obj.get("smtp")] if obj.get("smtp") is not None else None,
            "messengers": obj.get("messengers"),
            "bounce.enabled": obj.get("bounce.enabled"),
            "bounce.webhooks_enabled": obj.get("bounce.webhooks_enabled"),
            "bounce.count": obj.get("bounce.count"),
            "bounce.action": obj.get("bounce.action"),
            "bounce.ses_enabled": obj.get("bounce.ses_enabled"),
            "bounce.sendgrid_enabled": obj.get("bounce.sendgrid_enabled"),
            "bounce.sendgrid_key": obj.get("bounce.sendgrid_key"),
            "bounce.postmark_enabled": obj.get("bounce.postmark_enabled"),
            "bounce.postmark_username": obj.get("bounce.postmark_username"),
            "bounce.postmark_password": obj.get("bounce.postmark_password"),
            "bounce.mailboxes": [MailBoxBounces.from_dict(_item) for _item in obj.get("bounce.mailboxes")] if obj.get("bounce.mailboxes") is not None else None,
            "appearance.admin.custom_css": obj.get("appearance.admin.custom_css"),
            "appearance.admin.custom_js": obj.get("appearance.admin.custom_js"),
            "appearance.public.custom_css": obj.get("appearance.public.custom_css"),
            "appearance.public.custom_js": obj.get("appearance.public.custom_js")
        })
        return _obj

