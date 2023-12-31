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

from listmonk.models.get_media200_response import GetMedia200Response

class TestGetMedia200Response(unittest.TestCase):
    """GetMedia200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetMedia200Response:
        """Test GetMedia200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetMedia200Response`
        """
        model = GetMedia200Response()
        if include_optional:
            return GetMedia200Response(
                data = [
                    listmonk.models.media_file_object.MediaFileObject(
                        id = 56, 
                        uuid = '', 
                        filename = '', 
                        created_at = '', 
                        thumb_url = '', 
                        uri = '', )
                    ]
            )
        else:
            return GetMedia200Response(
        )
        """

    def testGetMedia200Response(self):
        """Test GetMedia200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
