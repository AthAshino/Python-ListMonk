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

from listmonk.models.new_subscriber import NewSubscriber

class TestNewSubscriber(unittest.TestCase):
    """NewSubscriber unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> NewSubscriber:
        """Test NewSubscriber
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `NewSubscriber`
        """
        model = NewSubscriber()
        if include_optional:
            return NewSubscriber(
                email = '',
                name = '',
                status = '',
                lists = [
                    56
                    ],
                list_uuids = [
                    ''
                    ],
                preconfirm_subscriptions = True,
                attribs = listmonk.models.new_subscriber_attribs.NewSubscriber_attribs(
                    city = '', 
                    projects = 56, 
                    stack = listmonk.models.new_subscriber_attribs_stack.NewSubscriber_attribs_stack(
                        languages = [
                            ''
                            ], ), )
            )
        else:
            return NewSubscriber(
        )
        """

    def testNewSubscriber(self):
        """Test NewSubscriber"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
