# pylint: disable=wrong-import-position

APP_NAME = "fb_post_clean_arch"
OPERATION_NAME = "react_to_post"
REQUEST_METHOD = "post"
URL_SUFFIX = "post/{post_id}/reaction/v1/"

from .test_case_01 import TestCase01ReactToPostAPITestCase

__all__ = [
    "TestCase01ReactToPostAPITestCase"
]
