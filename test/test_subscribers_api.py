# coding: utf-8

"""
    Listmonk

    The API collection for listmonk

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from listmonk_client.api.subscribers_api import SubscribersApi


class TestSubscribersApi(unittest.TestCase):
    """SubscribersApi unit test stubs"""

    def setUp(self) -> None:
        self.api = SubscribersApi()

    def tearDown(self) -> None:
        pass

    def test_blocklist_subscribers_query(self) -> None:
        """Test case for blocklist_subscribers_query

        """
        pass

    def test_create_subscriber(self) -> None:
        """Test case for create_subscriber

        """
        pass

    def test_delete_subscriber_bounces_by_id(self) -> None:
        """Test case for delete_subscriber_bounces_by_id

        """
        pass

    def test_delete_subscriber_by_id(self) -> None:
        """Test case for delete_subscriber_by_id

        """
        pass

    def test_delete_subscriber_by_list(self) -> None:
        """Test case for delete_subscriber_by_list

        """
        pass

    def test_delete_subscriber_by_query(self) -> None:
        """Test case for delete_subscriber_by_query

        """
        pass

    def test_export_subscriber_data_by_id(self) -> None:
        """Test case for export_subscriber_data_by_id

        """
        pass

    def test_get_subscriber_bounces_by_id(self) -> None:
        """Test case for get_subscriber_bounces_by_id

        """
        pass

    def test_get_subscriber_by_id(self) -> None:
        """Test case for get_subscriber_by_id

        """
        pass

    def test_get_subscribers(self) -> None:
        """Test case for get_subscribers

        """
        pass

    def test_manage_blocklist_by_subscriber_list(self) -> None:
        """Test case for manage_blocklist_by_subscriber_list

        """
        pass

    def test_manage_blocklist_subscribers_by_id(self) -> None:
        """Test case for manage_blocklist_subscribers_by_id

        """
        pass

    def test_manage_subscriber_list_by_id(self) -> None:
        """Test case for manage_subscriber_list_by_id

        """
        pass

    def test_manage_subscriber_lists(self) -> None:
        """Test case for manage_subscriber_lists

        """
        pass

    def test_manage_subscriber_lists_by_query(self) -> None:
        """Test case for manage_subscriber_lists_by_query

        """
        pass

    def test_subscriber_send_optin_by_id(self) -> None:
        """Test case for subscriber_send_optin_by_id

        """
        pass

    def test_update_subscriber_by_id(self) -> None:
        """Test case for update_subscriber_by_id

        """
        pass


if __name__ == '__main__':
    unittest.main()
