# pylint: disable=wrong-import-position

APP_NAME = "fb_post_clean_arch"
OPERATION_NAME = "react_to_comment"
REQUEST_METHOD = "post"
URL_SUFFIX = "comment/{comment_id}/reaction/v1/"

from .test_case_01 import TestCase01ReactToCommentAPITestCase

__all__ = [
    "TestCase01ReactToCommentAPITestCase"
]
