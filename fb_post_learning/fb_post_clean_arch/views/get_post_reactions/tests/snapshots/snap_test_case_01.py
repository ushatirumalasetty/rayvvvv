# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01GetPostReactionsAPITestCase::test_case status'] = 200

snapshots['TestCase01GetPostReactionsAPITestCase::test_case body'] = [
    {
        'name': 'John',
        'profile_pic': 'profile_pic_url1',
        'reaction_type': 'LIKE',
        'user_id': 1
    }
]

snapshots['TestCase01GetPostReactionsAPITestCase::test_case header_params'] = {
    'content-language': [
        'Content-Language',
        'en'
    ],
    'content-length': [
        '92',
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
