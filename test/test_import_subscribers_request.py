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

from listmonk.models.import_subscribers_request import ImportSubscribersRequest

class TestImportSubscribersRequest(unittest.TestCase):
    """ImportSubscribersRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ImportSubscribersRequest:
        """Test ImportSubscribersRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ImportSubscribersRequest`
        """
        model = ImportSubscribersRequest()
        if include_optional:
            return ImportSubscribersRequest(
                params = '',
                file = ''
            )
        else:
            return ImportSubscribersRequest(
        )
        """

    def testImportSubscribersRequest(self):
        """Test ImportSubscribersRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
