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

from listmonk.models.dashboard_chart import DashboardChart

class TestDashboardChart(unittest.TestCase):
    """DashboardChart unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DashboardChart:
        """Test DashboardChart
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DashboardChart`
        """
        model = DashboardChart()
        if include_optional:
            return DashboardChart(
                link_clicks = [
                    listmonk.models.dashboard_chart_link_clicks_inner.DashboardChart_link_clicks_inner(
                        count = 56, 
                        date = '', )
                    ],
                campaign_views = [
                    listmonk.models.dashboard_chart_link_clicks_inner.DashboardChart_link_clicks_inner(
                        count = 56, 
                        date = '', )
                    ]
            )
        else:
            return DashboardChart(
        )
        """

    def testDashboardChart(self):
        """Test DashboardChart"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
