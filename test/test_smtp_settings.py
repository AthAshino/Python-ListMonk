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

from listmonk.models.smtp_settings import SMTPSettings

class TestSMTPSettings(unittest.TestCase):
    """SMTPSettings unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SMTPSettings:
        """Test SMTPSettings
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SMTPSettings`
        """
        model = SMTPSettings()
        if include_optional:
            return SMTPSettings(
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
                tls_skip_verify = True
            )
        else:
            return SMTPSettings(
        )
        """

    def testSMTPSettings(self):
        """Test SMTPSettings"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
