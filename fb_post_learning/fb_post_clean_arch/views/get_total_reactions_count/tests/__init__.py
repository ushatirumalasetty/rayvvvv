# pylint: disable=wrong-import-position

APP_NAME = "fb_post_clean_arch"
OPERATION_NAME = "get_total_reactions_count"
REQUEST_METHOD = "get"
URL_SUFFIX = "reactions/count/v1/"

from .test_case_01 import TestCase01GetTotalReactionsCountAPITestCase

__all__ = [
    "TestCase01GetTotalReactionsCountAPITestCase"
]
