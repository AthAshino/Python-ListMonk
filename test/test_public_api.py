# coding: utf-8

"""
    Listmonk

    The API collection for listmonk

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from listmonk_client.api.public_api import PublicApi


class TestPublicApi(unittest.TestCase):
    """PublicApi unit test stubs"""

    def setUp(self) -> None:
        self.api = PublicApi()

    def tearDown(self) -> None:
        pass

    def test_get_public_lists(self) -> None:
        """Test case for get_public_lists

        """
        pass

    def test_handle_public_subscription(self) -> None:
        """Test case for handle_public_subscription

        """
        pass


if __name__ == '__main__':
    unittest.main()