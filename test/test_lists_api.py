# coding: utf-8

"""
    Listmonk

    The API collection for listmonk

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from listmonk_client.api.lists_api import ListsApi


class TestListsApi(unittest.TestCase):
    """ListsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ListsApi()

    def tearDown(self) -> None:
        pass

    def test_create_list(self) -> None:
        """Test case for create_list

        """
        pass

    def test_delete_list_by_id(self) -> None:
        """Test case for delete_list_by_id

        """
        pass

    def test_get_list_by_id(self) -> None:
        """Test case for get_list_by_id

        """
        pass

    def test_get_lists(self) -> None:
        """Test case for get_lists

        """
        pass

    def test_update_list_by_id(self) -> None:
        """Test case for update_list_by_id

        """
        pass


if __name__ == '__main__':
    unittest.main()