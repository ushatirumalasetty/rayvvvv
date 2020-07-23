# pylint: disable=wrong-import-position

APP_NAME = "fb_post_clean_arch"
OPERATION_NAME = "get_posts_with_more_positive_reactions"
REQUEST_METHOD = "get"
URL_SUFFIX = "posts_with_more_positive_reactions/v1/"

from .test_case_01 import TestCase01GetPostsWithMorePositiveReactionsAPITestCase

__all__ = [
    "TestCase01GetPostsWithMorePositiveReactionsAPITestCase"
]
