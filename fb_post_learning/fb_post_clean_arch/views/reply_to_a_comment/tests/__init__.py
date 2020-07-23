# pylint: disable=wrong-import-position

APP_NAME = "fb_post_clean_arch"
OPERATION_NAME = "reply_to_a_comment"
REQUEST_METHOD = "post"
URL_SUFFIX = "comment/{comment_id}/reply/v1/"

from .test_case_01 import TestCase01ReplyToACommentAPITestCase

__all__ = [
    "TestCase01ReplyToACommentAPITestCase"
]
