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

from listmonk.models.import_status import ImportStatus

class TestImportStatus(unittest.TestCase):
    """ImportStatus unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ImportStatus:
        """Test ImportStatus
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ImportStatus`
        """
        model = ImportStatus()
        if include_optional:
            return ImportStatus(
                data = listmonk.models.import_status_data.ImportStatus_data(
                    name = '', 
                    total = 56, 
                    imported = 56, 
                    status = '', )
            )
        else:
            return ImportStatus(
        )
        """

    def testImportStatus(self):
        """Test ImportStatus"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
