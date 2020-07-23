# pylint: disable=wrong-import-position

APP_NAME = "fb_post_clean_arch"
OPERATION_NAME = "get_post_reactions"
REQUEST_METHOD = "get"
URL_SUFFIX = "post/{post_id}/reactions/v1/"

from .test_case_01 import TestCase01GetPostReactionsAPITestCase
from .test_case_02 import TestCase02GetPostReactionsAPITestCase

__all__ = [
    "TestCase01GetPostReactionsAPITestCase",
    "TestCase02GetPostReactionsAPITestCase"
]
