# pylint: disable=wrong-import-position

APP_NAME = "fb_post_clean_arch"
OPERATION_NAME = "get_reaction_metrics_of_a_post"
REQUEST_METHOD = "get"
URL_SUFFIX = "post/{post_id}/reactions/metrics/v1/"

from .test_case_01 import TestCase01GetReactionMetricsOfAPostAPITestCase

__all__ = [
    "TestCase01GetReactionMetricsOfAPostAPITestCase"
]
