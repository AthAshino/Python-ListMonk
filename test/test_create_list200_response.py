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

from listmonk_client.models.create_list200_response import CreateList200Response

class TestCreateList200Response(unittest.TestCase):
    """CreateList200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateList200Response:
        """Test CreateList200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateList200Response`
        """
        model = CreateList200Response()
        if include_optional:
            return CreateList200Response(
                data = listmonk.models.list.List(
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
            )
        else:
            return CreateList200Response(
        )
        """

    def testCreateList200Response(self):
        """Test CreateList200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
