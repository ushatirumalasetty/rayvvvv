# pylint: disable=wrong-import-position

APP_NAME = "fb_post_clean_arch"
OPERATION_NAME = "get_comment_replies"
REQUEST_METHOD = "get"
URL_SUFFIX = "comment/{comment_id}/replies/v1/"

from .test_case_01 import TestCase01GetCommentRepliesAPITestCase

__all__ = [
    "TestCase01GetCommentRepliesAPITestCase"
]
