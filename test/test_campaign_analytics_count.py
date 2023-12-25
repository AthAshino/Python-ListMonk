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

from listmonk_client.models.campaign_analytics_count import CampaignAnalyticsCount

class TestCampaignAnalyticsCount(unittest.TestCase):
    """CampaignAnalyticsCount unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CampaignAnalyticsCount:
        """Test CampaignAnalyticsCount
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CampaignAnalyticsCount`
        """
        model = CampaignAnalyticsCount()
        if include_optional:
            return CampaignAnalyticsCount(
                campaign_id = 56,
                count = 56,
                timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else:
            return CampaignAnalyticsCount(
        )
        """

    def testCampaignAnalyticsCount(self):
        """Test CampaignAnalyticsCount"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()