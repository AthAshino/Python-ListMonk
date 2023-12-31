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

from listmonk.models.get_template_by_id200_response import GetTemplateById200Response

class TestGetTemplateById200Response(unittest.TestCase):
    """GetTemplateById200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetTemplateById200Response:
        """Test GetTemplateById200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetTemplateById200Response`
        """
        model = GetTemplateById200Response()
        if include_optional:
            return GetTemplateById200Response(
                data = listmonk.models.template.Template(
                    id = 56, 
                    created_at = '', 
                    updated_at = '', 
                    name = '', 
                    body = '', 
                    type = '', 
                    is_default = True, )
            )
        else:
            return GetTemplateById200Response(
        )
        """

    def testGetTemplateById200Response(self):
        """Test GetTemplateById200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
