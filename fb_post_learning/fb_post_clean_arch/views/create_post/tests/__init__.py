# pylint: disable=wrong-import-position

APP_NAME = "fb_post_clean_arch"
OPERATION_NAME = "create_post"
REQUEST_METHOD = "post"
URL_SUFFIX = "post/create/v1/"

from .test_case_01 import TestCase01CreatePostAPITestCase

__all__ = [
    "TestCase01CreatePostAPITestCase"
]
