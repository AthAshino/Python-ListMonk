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

from listmonk_client.models.get_campaign_by_id200_response import GetCampaignById200Response

class TestGetCampaignById200Response(unittest.TestCase):
    """GetCampaignById200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetCampaignById200Response:
        """Test GetCampaignById200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetCampaignById200Response`
        """
        model = GetCampaignById200Response()
        if include_optional:
            return GetCampaignById200Response(
                data = listmonk_client.models.campaign.Campaign(
                    id = 56, 
                    created_at = '', 
                    updated_at = '', 
                    campaign_id = 56, 
                    views = 56, 
                    clicks = 56, 
                    lists = [
                        listmonk_client.models.bounce_results_inner_campaign.Bounce_results_inner_campaign(
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
                    messenger = '', )
            )
        else:
            return GetCampaignById200Response(
        )
        """

    def testGetCampaignById200Response(self):
        """Test GetCampaignById200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()