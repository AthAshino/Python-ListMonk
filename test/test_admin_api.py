# coding: utf-8

"""
    Listmonk

    The API collection for listmonk

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from listmonk_client.api.admin_api import AdminApi


class TestAdminApi(unittest.TestCase):
    """AdminApi unit test stubs"""

    def setUp(self) -> None:
        self.api = AdminApi()

    def tearDown(self) -> None:
        pass

    def test_reload_app(self) -> None:
        """Test case for reload_app

        """
        pass


if __name__ == '__main__':
    unittest.main()