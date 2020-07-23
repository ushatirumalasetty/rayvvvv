# pylint: disable=wrong-import-position

APP_NAME = "fb_post_clean_arch"
OPERATION_NAME = "get_user_reacted_posts"
REQUEST_METHOD = "get"
URL_SUFFIX = "user/reacted/posts/v1/"

from .test_case_01 import TestCase01GetUserReactedPostsAPITestCase

__all__ = [
    "TestCase01GetUserReactedPostsAPITestCase"
]
