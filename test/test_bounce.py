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

from listmonk_client.models.bounce import Bounce

class TestBounce(unittest.TestCase):
    """Bounce unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Bounce:
        """Test Bounce
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Bounce`
        """
        model = Bounce()
        if include_optional:
            return Bounce(
                results = [
                    listmonk_client.models.bounce_results_inner.Bounce_results_inner(
                        id = 56, 
                        type = '', 
                        source = '', 
                        meta = listmonk_client.models.meta.meta(),
                        created_at = '', 
                        email = '', 
                        subscriber_uuid = '', 
                        subscriber_id = 56, 
                        campaign = listmonk_client.models.bounce_results_inner_campaign.Bounce_results_inner_campaign(
                            id = 56, 
                            name = '', ), 
                        campaign_uuid = '', 
                        total = 56, )
                    ]
            )
        else:
            return Bounce(
        )
        """

    def testBounce(self):
        """Test Bounce"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()