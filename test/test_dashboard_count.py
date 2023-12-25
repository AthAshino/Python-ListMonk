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

from listmonk_client.models.dashboard_count import DashboardCount

class TestDashboardCount(unittest.TestCase):
    """DashboardCount unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DashboardCount:
        """Test DashboardCount
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DashboardCount`
        """
        model = DashboardCount()
        if include_optional:
            return DashboardCount(
                data = listmonk_client.models.dashboard_count_data.DashboardCount_data(
                    subscribers = listmonk_client.models.dashboard_count_data_subscribers.DashboardCount_data_subscribers(
                        total = 56, 
                        blocklisted = listmonk_client.models.blocklisted.blocklisted(),
                        orphans = 56, ), 
                    lists = listmonk_client.models.dashboard_count_data_lists.DashboardCount_data_lists(
                        total = 56, 
                        private = 56, 
                        public = 56, 
                        optin_single = 56, 
                        optin_double = 56, ), 
                    campaigns = listmonk_client.models.dashboard_count_data_campaigns.DashboardCount_data_campaigns(
                        total = 56, 
                        by_status = listmonk_client.models.dashboard_count_data_campaigns_by_status.DashboardCount_data_campaigns_by_status(
                            draft = 56, ), ), 
                    messages = 56, )
            )
        else:
            return DashboardCount(
        )
        """

    def testDashboardCount(self):
        """Test DashboardCount"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
