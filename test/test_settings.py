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

from listmonk.models.settings import Settings

class TestSettings(unittest.TestCase):
    """Settings unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Settings:
        """Test Settings
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Settings`
        """
        model = Settings()
        if include_optional:
            return Settings(
                app_site_name = '',
                app_root_url = '',
                app_logo_url = '',
                app_favicon_url = '',
                app_from_email = '',
                app_notify_emails = [
                    ''
                    ],
                app_enable_public_subscription_page = True,
                app_enable_public_archive = True,
                app_send_optin_confirmation = True,
                app_check_updates = True,
                app_lang = '',
                app_batch_size = 56,
                app_concurrency = 56,
                app_max_send_errors = 56,
                app_message_rate = 56,
                app_message_sliding_window = True,
                app_message_sliding_window_duration = '',
                app_message_sliding_window_rate = 56,
                privacy_individual_tracking = True,
                privacy_unsubscribe_header = True,
                privacy_allow_blocklist = True,
                privacy_allow_preferences = True,
                privacy_allow_export = True,
                privacy_allow_wipe = True,
                privacy_exportable = [
                    ''
                    ],
                privacy_domain_blocklist = [
                    None
                    ],
                upload_provider = '',
                upload_filesystem_upload_path = '',
                upload_filesystem_upload_uri = '',
                upload_s3_url = '',
                upload_s3_public_url = '',
                upload_s3_aws_access_key_id = '',
                upload_s3_aws_default_region = '',
                upload_s3_bucket = '',
                upload_s3_bucket_domain = '',
                upload_s3_bucket_path = '',
                upload_s3_bucket_type = '',
                upload_s3_expiry = '',
                smtp = [
                    listmonk.models.smtp_settings.SMTPSettings(
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
                        tls_skip_verify = True, )
                    ],
                messengers = [
                    None
                    ],
                bounce_enabled = True,
                bounce_webhooks_enabled = True,
                bounce_count = 56,
                bounce_action = '',
                bounce_ses_enabled = True,
                bounce_sendgrid_enabled = True,
                bounce_sendgrid_key = '',
                bounce_postmark_enabled = True,
                bounce_postmark_username = '',
                bounce_postmark_password = '',
                bounce_mailboxes = [
                    listmonk.models.mail_box_bounces.MailBoxBounces(
                        uuid = '', 
                        enabled = True, 
                        type = '', 
                        host = '', 
                        port = 56, 
                        auth_protocol = '', 
                        return_path = '', 
                        username = '', 
                        tls_enabled = True, 
                        tls_skip_verify = True, 
                        scan_interval = '', )
                    ],
                appearance_admin_custom_css = '',
                appearance_admin_custom_js = '',
                appearance_public_custom_css = '',
                appearance_public_custom_js = ''
            )
        else:
            return Settings(
        )
        """

    def testSettings(self):
        """Test Settings"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
