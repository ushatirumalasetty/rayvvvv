"""
Reply To A Comment Given Valid CommentId And Returns ReplyId
"""
import json

from fb_post_clean_arch.models import Comment
from fb_post_clean_arch.utils.custom_test_utils import CustomTestUtils
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX

REQUEST_BODY = """
{
    "comment_text": "string"
}
"""

TEST_CASE = {
    "request": {
        "path_params": {"comment_id": "1"},
        "query_params": {},
        "header_params": {},
        "securities": {"oauth": {"tokenUrl": "http://auth.ibtspl.com/oauth2/", "flow": "password", "scopes": ["superuser"], "type": "oauth2"}},
        "body": REQUEST_BODY,
    },
}


class TestCase01ReplyToACommentAPITestCase(CustomTestUtils):
    app_name = APP_NAME
    operation_name = OPERATION_NAME
    request_method = REQUEST_METHOD
    url_suffix = URL_SUFFIX
    test_case_dict = TEST_CASE

    def setupUser(self, username, password):
        super(TestCase01ReplyToACommentAPITestCase, self).setupUser(
            username=username, password=password
        )

        self.create_user()
        self.create_posts()
        self.create_comments()

    def test_case(self):
        response = self.default_test_case()
        response_content = json.loads(response.content)
        comment_id = response_content['comment_id']
        comment = Comment.objects.get(id=comment_id)

        user_id = self.foo_user.id
        comment_id = comment.parent_comment.id
        comment_text = comment.comment_text

        self.assert_match_snapshot(
            name='user_id',
            value=user_id
        )
        self.assert_match_snapshot(
            name='comment_id',
            value=comment_id
        )
        self.assert_match_snapshot(
            name='comment_text',
            value=comment_text
        )
