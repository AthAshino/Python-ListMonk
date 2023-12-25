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

from listmonk_client.models.get_templates200_response import GetTemplates200Response

class TestGetTemplates200Response(unittest.TestCase):
    """GetTemplates200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetTemplates200Response:
        """Test GetTemplates200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetTemplates200Response`
        """
        model = GetTemplates200Response()
        if include_optional:
            return GetTemplates200Response(
                data = [
                    listmonk_client.models.template.Template(
                        id = 56, 
                        created_at = '', 
                        updated_at = '', 
                        name = '', 
                        body = '', 
                        type = '', 
                        is_default = True, )
                    ]
            )
        else:
            return GetTemplates200Response(
        )
        """

    def testGetTemplates200Response(self):
        """Test GetTemplates200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()