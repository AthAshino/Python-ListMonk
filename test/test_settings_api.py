# coding: utf-8

"""
    Listmonk

    The API collection for listmonk

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from listmonk.api.settings_api import SettingsApi


class TestSettingsApi(unittest.TestCase):
    """SettingsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = SettingsApi()

    def tearDown(self) -> None:
        pass

    def test_get_settings(self) -> None:
        """Test case for get_settings

        """
        pass

    def test_test_smtp_settings(self) -> None:
        """Test case for test_smtp_settings

        """
        pass

    def test_update_settings(self) -> None:
        """Test case for update_settings

        """
        pass


if __name__ == '__main__':
    unittest.main()
