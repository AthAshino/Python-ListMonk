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

from listmonk_client.models.get_subscribers200_response import GetSubscribers200Response

class TestGetSubscribers200Response(unittest.TestCase):
    """GetSubscribers200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetSubscribers200Response:
        """Test GetSubscribers200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetSubscribers200Response`
        """
        model = GetSubscribers200Response()
        if include_optional:
            return GetSubscribers200Response(
                data = listmonk.models.get_subscribers_200_response_data.getSubscribers_200_response_data(
                    results = [
                        listmonk.models.subscriber.Subscriber(
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
                                ], )
                        ], 
                    query = '', 
                    total = 56, 
                    per_page = 56, 
                    page = 56, )
            )
        else:
            return GetSubscribers200Response(
        )
        """

    def testGetSubscribers200Response(self):
        """Test GetSubscribers200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
