# pylint: disable=wrong-import-position

APP_NAME = "fb_post_clean_arch"
OPERATION_NAME = "get_user_posts"
REQUEST_METHOD = "post"
URL_SUFFIX = "user/post/v1/"

from .test_case_01 import TestCase01GetUserPostsAPITestCase

__all__ = [
    "TestCase01GetUserPostsAPITestCase"
]
