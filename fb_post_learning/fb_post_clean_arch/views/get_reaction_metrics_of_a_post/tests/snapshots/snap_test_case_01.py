# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot

snapshots = Snapshot()

snapshots['TestCase01GetReactionMetricsOfAPostAPITestCase::test_case status'] = 200

snapshots['TestCase01GetReactionMetricsOfAPostAPITestCase::test_case body'] = [
    {
        'reaction_count': 1,
        'reaction_type': 'WOW'
    }
]

snapshots['TestCase01GetReactionMetricsOfAPostAPITestCase::test_case header_params'] = {
    'content-language': [
        'Content-Language',
        'en'
    ],
    'content-length': [
        '47',
        'Content-Length'
    ],
    'content-type': [
        'Content-Type',
        'text/html; charset=utf-8'
    ],
    'vary': [
        'Accept-Language, Origin, Cookie',
        'Vary'
    ],
    'x-frame-options': [
        'SAMEORIGIN',
        'X-Frame-Options'
    ]
}
