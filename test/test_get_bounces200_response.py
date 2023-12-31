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

from listmonk.models.get_bounces200_response import GetBounces200Response

class TestGetBounces200Response(unittest.TestCase):
    """GetBounces200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetBounces200Response:
        """Test GetBounces200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetBounces200Response`
        """
        model = GetBounces200Response()
        if include_optional:
            return GetBounces200Response(
                data = listmonk.models.get_bounces_200_response_data.getBounces_200_response_data(
                    results = [
                        listmonk.models.bounce.Bounce()
                        ], 
                    query = '', 
                    total = 56, 
                    per_page = 56, 
                    page = 56, )
            )
        else:
            return GetBounces200Response(
        )
        """

    def testGetBounces200Response(self):
        """Test GetBounces200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
