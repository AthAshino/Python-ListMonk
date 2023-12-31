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

from listmonk.models.campaign import Campaign

class TestCampaign(unittest.TestCase):
    """Campaign unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Campaign:
        """Test Campaign
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Campaign`
        """
        model = Campaign()
        if include_optional:
            return Campaign(
                id = 56,
                created_at = '',
                updated_at = '',
                campaign_id = 56,
                views = 56,
                clicks = 56,
                lists = [
                    listmonk.models.bounce_results_inner_campaign.Bounce_results_inner_campaign(
                        id = 56, 
                        name = '', )
                    ],
                started_at = '',
                to_send = 56,
                sent = 56,
                uuid = '',
                type = 'regular',
                name = '',
                subject = '',
                from_email = '',
                body = '',
                send_at = '',
                status = '',
                content_type = 'richtext',
                tags = [
                    ''
                    ],
                template_id = 56,
                messenger = ''
            )
        else:
            return Campaign(
        )
        """

    def testCampaign(self):
        """Test Campaign"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
