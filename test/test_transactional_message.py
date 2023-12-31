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

from listmonk.models.transactional_message import TransactionalMessage

class TestTransactionalMessage(unittest.TestCase):
    """TransactionalMessage unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TransactionalMessage:
        """Test TransactionalMessage
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TransactionalMessage`
        """
        model = TransactionalMessage()
        if include_optional:
            return TransactionalMessage(
                subscriber_email = '',
                subscriber_id = 56,
                template_id = 56,
                from_email = '',
                data = None,
                headers = [
                    None
                    ],
                messenger = '',
                content_type = ''
            )
        else:
            return TransactionalMessage(
        )
        """

    def testTransactionalMessage(self):
        """Test TransactionalMessage"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
