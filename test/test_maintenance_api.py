# coding: utf-8

"""
    Listmonk

    The API collection for listmonk

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from listmonk.api.maintenance_api import MaintenanceApi


class TestMaintenanceApi(unittest.TestCase):
    """MaintenanceApi unit test stubs"""

    def setUp(self) -> None:
        self.api = MaintenanceApi()

    def tearDown(self) -> None:
        pass

    def test_delete_campaign_analytics_by_type(self) -> None:
        """Test case for delete_campaign_analytics_by_type

        """
        pass

    def test_delete_gc_subscribers(self) -> None:
        """Test case for delete_gc_subscribers

        """
        pass

    def test_delete_unconfirmed_subscriptions(self) -> None:
        """Test case for delete_unconfirmed_subscriptions

        """
        pass


if __name__ == '__main__':
    unittest.main()
