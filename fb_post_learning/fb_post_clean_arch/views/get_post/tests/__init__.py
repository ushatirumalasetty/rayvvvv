# pylint: disable=wrong-import-position

APP_NAME = "fb_post_clean_arch"
OPERATION_NAME = "get_post"
REQUEST_METHOD = "post"
URL_SUFFIX = "post/{post_id}/v1/"

from .test_case_01 import TestCase01GetPostAPITestCase

__all__ = [
    "TestCase01GetPostAPITestCase"
]
