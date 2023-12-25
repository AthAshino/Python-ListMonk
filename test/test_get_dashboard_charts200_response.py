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

from listmonk.models.get_dashboard_charts200_response import GetDashboardCharts200Response

class TestGetDashboardCharts200Response(unittest.TestCase):
    """GetDashboardCharts200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetDashboardCharts200Response:
        """Test GetDashboardCharts200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetDashboardCharts200Response`
        """
        model = GetDashboardCharts200Response()
        if include_optional:
            return GetDashboardCharts200Response(
                data = listmonk.models.dashboard_chart.DashboardChart(
                    link_clicks = [
                        listmonk.models.dashboard_chart_link_clicks_inner.DashboardChart_link_clicks_inner(
                            count = 56, 
                            date = '', )
                        ], 
                    campaign_views = [
                        listmonk.models.dashboard_chart_link_clicks_inner.DashboardChart_link_clicks_inner(
                            count = 56, 
                            date = '', )
                        ], )
            )
        else:
            return GetDashboardCharts200Response(
        )
        """

    def testGetDashboardCharts200Response(self):
        """Test GetDashboardCharts200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
