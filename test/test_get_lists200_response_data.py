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

from listmonk.models.get_lists200_response_data import GetLists200ResponseData

class TestGetLists200ResponseData(unittest.TestCase):
    """GetLists200ResponseData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetLists200ResponseData:
        """Test GetLists200ResponseData
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetLists200ResponseData`
        """
        model = GetLists200ResponseData()
        if include_optional:
            return GetLists200ResponseData(
                results = [
                    listmonk.models.list.List(
                        id = 56, 
                        created_at = '', 
                        updated_at = '', 
                        uuid = '', 
                        name = '', 
                        type = '', 
                        optin = '', 
                        tags = [
                            ''
                            ], 
                        subscriber_count = 56, )
                    ],
                total = 56,
                per_page = 56,
                page = 56
            )
        else:
            return GetLists200ResponseData(
        )
        """

    def testGetLists200ResponseData(self):
        """Test GetLists200ResponseData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
