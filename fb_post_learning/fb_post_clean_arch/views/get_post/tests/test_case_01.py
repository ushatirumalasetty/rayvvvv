"""
Get Post Details Given Valid PostId.
"""
from mock import patch

from fb_post_clean_arch.interactors.storages.storage_interface import UserDto
from fb_post_clean_arch.utils.custom_test_utils import CustomTestUtils
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX

REQUEST_BODY = """
{}
"""

TEST_CASE = {
    "request": {
        "path_params": {"post_id": "1"},
        "query_params": {},
        "header_params": {},
        "securities": {"oauth": {"tokenUrl": "http://auth.ibtspl.com/oauth2/",
                                 "flow": "password", "scopes": ["superuser"],
                                 "type": "oauth2"}},
        "body": REQUEST_BODY,
    },
}


class TestCase01GetPostAPITestCase(CustomTestUtils):
    app_name = APP_NAME
    operation_name = OPERATION_NAME
    request_method = REQUEST_METHOD
    url_suffix = URL_SUFFIX
    test_case_dict = TEST_CASE

    def setupUser(self, username, password):
        super(TestCase01GetPostAPITestCase, self).setupUser(
            username=username, password=password
        )
        self.create_user()
        self.create_posts()
        self.create_comments()
        self.create_post_reactions()
        self.create_comment_reactions()
        self.create_replies_for_comment()
        self.create_reply_reactions()

    @patch(
        'fb_post_clean_arch.adapters.service_adapter.ServiceAdapter.get_user_dtos')
    def test_case(self, get_user_dtos):
        get_user_dtos.return_value = [UserDto(
            user_id=1,
            name="John",
            profile_pic_url="profile_pic_url1"
        )]
        self.default_test_case()  # Returns response object.
        # Which can be used for further response object checks.
        # Add database state checks here.
