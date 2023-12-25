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

from listmonk_client.models.get_bounces200_response_data import GetBounces200ResponseData

class TestGetBounces200ResponseData(unittest.TestCase):
    """GetBounces200ResponseData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetBounces200ResponseData:
        """Test GetBounces200ResponseData
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetBounces200ResponseData`
        """
        model = GetBounces200ResponseData()
        if include_optional:
            return GetBounces200ResponseData(
                results = [
                    listmonk.models.bounce.Bounce(
                        results = [
                            listmonk.models.bounce_results_inner.Bounce_results_inner(
                                id = 56, 
                                type = '', 
                                source = '', 
                                meta = listmonk.models.meta.meta(),
                                created_at = '', 
                                email = '', 
                                subscriber_uuid = '', 
                                subscriber_id = 56, 
                                campaign = listmonk.models.bounce_results_inner_campaign.Bounce_results_inner_campaign(
                                    id = 56, 
                                    name = '', ), 
                                campaign_uuid = '', 
                                total = 56, )
                            ], )
                    ],
                query = '',
                total = 56,
                per_page = 56,
                page = 56
            )
        else:
            return GetBounces200ResponseData(
        )
        """

    def testGetBounces200ResponseData(self):
        """Test GetBounces200ResponseData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
