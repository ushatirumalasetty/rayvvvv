"""
Create Post Given Valid UserId, Post_content And Return PostId.
"""
import json

from django_swagger_utils.utils.test import CustomAPITestCase

from fb_post_clean_arch.models import Post
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX

REQUEST_BODY = """
{
    "post_content": "string"
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


class TestCase01CreatePostAPITestCase(CustomAPITestCase):
    app_name = APP_NAME
    operation_name = OPERATION_NAME
    request_method = REQUEST_METHOD
    url_suffix = URL_SUFFIX
    test_case_dict = TEST_CASE

    def setupUser(self, username, password):
        super(TestCase01CreatePostAPITestCase, self).setupUser(
            username=username, password=password
        )

    def test_case(self):
        response = self.default_test_case()
        response_content = json.loads(response.content)
        post_id = response_content['post_id']
        post = Post.objects.get(id=post_id)
        post_content = post.post_content

        self.assert_match_snapshot(
            name='user_id',
            value=post.user_id
        )
        self.assert_match_snapshot(
            name='post_content',
            value=post_content
        )
