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

from listmonk.models.handle_public_subscription_request import HandlePublicSubscriptionRequest

class TestHandlePublicSubscriptionRequest(unittest.TestCase):
    """HandlePublicSubscriptionRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> HandlePublicSubscriptionRequest:
        """Test HandlePublicSubscriptionRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `HandlePublicSubscriptionRequest`
        """
        model = HandlePublicSubscriptionRequest()
        if include_optional:
            return HandlePublicSubscriptionRequest(
                name = '',
                email = '',
                list_uuids = [
                    ''
                    ]
            )
        else:
            return HandlePublicSubscriptionRequest(
        )
        """

    def testHandlePublicSubscriptionRequest(self):
        """Test HandlePublicSubscriptionRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
