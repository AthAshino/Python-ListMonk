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

from listmonk.models.subscriber import Subscriber

class TestSubscriber(unittest.TestCase):
    """Subscriber unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Subscriber:
        """Test Subscriber
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Subscriber`
        """
        model = Subscriber()
        if include_optional:
            return Subscriber(
                id = 56,
                created_at = '',
                updated_at = '',
                uuid = '',
                email = '',
                name = '',
                attribs = listmonk.models.subscriber_profile_attribs.SubscriberProfile_attribs(
                    city = '', 
                    good = True, 
                    type = '', ),
                status = '',
                lists = [
                    listmonk.models.subscriber_lists_inner.Subscriber_lists_inner(
                        subscription_status = '', 
                        id = 56, 
                        uuid = '', 
                        name = '', 
                        type = '', 
                        tags = [
                            ''
                            ], 
                        created_at = '', 
                        updated_at = '', )
                    ]
            )
        else:
            return Subscriber(
        )
        """

    def testSubscriber(self):
        """Test Subscriber"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
