# coding: utf-8

"""
    Listmonk

    The API collection for listmonk

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from listmonk_client.models.update_campaign_status_by_id_request import UpdateCampaignStatusByIdRequest

class TestUpdateCampaignStatusByIdRequest(unittest.TestCase):
    """UpdateCampaignStatusByIdRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UpdateCampaignStatusByIdRequest:
        """Test UpdateCampaignStatusByIdRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UpdateCampaignStatusByIdRequest`
        """
        model = UpdateCampaignStatusByIdRequest()
        if include_optional:
            return UpdateCampaignStatusByIdRequest(
                status = 'scheduled'
            )
        else:
            return UpdateCampaignStatusByIdRequest(
        )
        """

    def testUpdateCampaignStatusByIdRequest(self):
        """Test UpdateCampaignStatusByIdRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
