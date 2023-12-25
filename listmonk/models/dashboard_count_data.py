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


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictInt
from listmonk_client.models.dashboard_count_data_campaigns import DashboardCountDataCampaigns
from listmonk_client.models.dashboard_count_data_lists import DashboardCountDataLists
from listmonk_client.models.dashboard_count_data_subscribers import DashboardCountDataSubscribers
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class DashboardCountData(BaseModel):
    """
    DashboardCountData
    """ # noqa: E501
    subscribers: Optional[DashboardCountDataSubscribers] = None
    lists: Optional[DashboardCountDataLists] = None
    campaigns: Optional[DashboardCountDataCampaigns] = None
    messages: Optional[StrictInt] = None
    __properties: ClassVar[List[str]] = ["subscribers", "lists", "campaigns", "messages"]

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
        """Create an instance of DashboardCountData from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of subscribers
        if self.subscribers:
            _dict['subscribers'] = self.subscribers.to_dict()
        # override the default output from pydantic by calling `to_dict()` of lists
        if self.lists:
            _dict['lists'] = self.lists.to_dict()
        # override the default output from pydantic by calling `to_dict()` of campaigns
        if self.campaigns:
            _dict['campaigns'] = self.campaigns.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of DashboardCountData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "subscribers": DashboardCountDataSubscribers.from_dict(obj.get("subscribers")) if obj.get("subscribers") is not None else None,
            "lists": DashboardCountDataLists.from_dict(obj.get("lists")) if obj.get("lists") is not None else None,
            "campaigns": DashboardCountDataCampaigns.from_dict(obj.get("campaigns")) if obj.get("campaigns") is not None else None,
            "messages": obj.get("messages")
        })
        return _obj

