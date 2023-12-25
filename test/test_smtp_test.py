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

from listmonk_client.models.smtp_test import SMTPTest

class TestSMTPTest(unittest.TestCase):
    """SMTPTest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SMTPTest:
        """Test SMTPTest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SMTPTest`
        """
        model = SMTPTest()
        if include_optional:
            return SMTPTest(
                uuid = '',
                enabled = True,
                host = '',
                hello_hostname = '',
                port = 56,
                auth_protocol = '',
                username = '',
                email_headers = [
                    None
                    ],
                max_conns = 56,
                max_msg_retries = 56,
                idle_timeout = '',
                wait_timeout = '',
                tls_type = '',
                tls_skip_verify = True,
                str_email_headers = '',
                password = '',
                email = ''
            )
        else:
            return SMTPTest(
        )
        """

    def testSMTPTest(self):
        """Test SMTPTest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()