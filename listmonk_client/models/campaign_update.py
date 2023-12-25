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
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class CampaignUpdate(BaseModel):
    """
    CampaignUpdate
    """ # noqa: E501
    name: Optional[StrictStr] = None
    subject: Optional[StrictStr] = None
    lists: Optional[List[StrictInt]] = None
    from_email: Optional[StrictStr] = None
    messenger: Optional[StrictStr] = None
    type: Optional[StrictStr] = None
    tags: Optional[List[StrictStr]] = None
    send_later: Optional[StrictBool] = None
    send_at: Optional[Union[str, Any]] = None
    headers: Optional[List[Union[str, Any]]] = None
    template_id: Optional[StrictInt] = None
    content_type: Optional[StrictStr] = None
    body: Optional[StrictStr] = None
    altbody: Optional[StrictStr] = None
    archive: Optional[StrictBool] = None
    archive_template_id: Optional[StrictInt] = None
    archive_meta: Optional[Union[str, Any]] = None
    __properties: ClassVar[List[str]] = ["name", "subject", "lists", "from_email", "messenger", "type", "tags", "send_later", "send_at", "headers", "template_id", "content_type", "body", "altbody", "archive", "archive_template_id", "archive_meta"]

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
        """Create an instance of CampaignUpdate from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of CampaignUpdate from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "subject": obj.get("subject"),
            "lists": obj.get("lists"),
            "from_email": obj.get("from_email"),
            "messenger": obj.get("messenger"),
            "type": obj.get("type"),
            "tags": obj.get("tags"),
            "send_later": obj.get("send_later"),
            "send_at": obj.get("send_at"),
            "headers": obj.get("headers"),
            "template_id": obj.get("template_id"),
            "content_type": obj.get("content_type"),
            "body": obj.get("body"),
            "altbody": obj.get("altbody"),
            "archive": obj.get("archive"),
            "archive_template_id": obj.get("archive_template_id"),
            "archive_meta": obj.get("archive_meta")
        })
        return _obj

