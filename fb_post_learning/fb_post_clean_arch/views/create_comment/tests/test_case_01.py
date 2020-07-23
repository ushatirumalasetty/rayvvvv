"""
Create Comment Given Valid PostId And Return CommentId.
"""

from fb_post_clean_arch.models import Comment
from fb_post_clean_arch.utils.custom_test_utils import CustomTestUtils
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX

REQUEST_BODY = """
{
    "post_id": 1,
    "comment_text": "string"
}
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


class TestCase01CreateCommentAPITestCase(CustomTestUtils):
    app_name = APP_NAME
    operation_name = OPERATION_NAME
    request_method = REQUEST_METHOD
    url_suffix = URL_SUFFIX
    test_case_dict = TEST_CASE

    def setupUser(self, username, password):
        super(TestCase01CreateCommentAPITestCase, self).setupUser(
            username=username, password=password
        )

        self.create_posts()

    def test_case(self):
        response = self.default_test_case()
        import json

        response_content = json.loads(response.content)

        comment_id = response_content['comment_id']

        comment = Comment.objects.get(id=comment_id)

        self.assert_match_snapshot(
            name='user_id',
            value=comment.user_id
        )

        self.assert_match_snapshot(
            name='post_id',
            value=comment.post.id
        )
        self.assert_match_snapshot(
            name='comment_text',
            value=comment.comment_text
        )
