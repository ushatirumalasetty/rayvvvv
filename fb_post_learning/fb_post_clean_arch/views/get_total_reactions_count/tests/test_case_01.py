"""
Get Total Reactions Count.
"""


from fb_post_clean_arch.utils.custom_test_utils import CustomTestUtils
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX

REQUEST_BODY = """

"""

TEST_CASE = {
    "request": {
        "path_params": {},
        "query_params": {},
        "header_params": {},
        "securities": {"oauth": {"tokenUrl": "http://auth.ibtspl.com/oauth2/", "flow": "password", "scopes": ["superuser"], "type": "oauth2"}},
        "body": REQUEST_BODY,
    },
}


class TestCase01GetTotalReactionsCountAPITestCase(CustomTestUtils):
    app_name = APP_NAME
    operation_name = OPERATION_NAME
    request_method = REQUEST_METHOD
    url_suffix = URL_SUFFIX
    test_case_dict = TEST_CASE

    def setupUser(self, username, password):
        super(TestCase01GetTotalReactionsCountAPITestCase, self).setupUser(
            username=username, password=password
        )

        self.create_user()
        self.create_posts()
        self.create_comments()
        self.create_post_reactions()
        self.create_comment_reactions()

    def test_case(self):
        self.default_test_case() # Returns response object.
        # Which can be used for further response object checks.
        # Add database state checks here.
