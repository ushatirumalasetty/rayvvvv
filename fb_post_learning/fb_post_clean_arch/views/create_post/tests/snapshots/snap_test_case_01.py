# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot

snapshots = Snapshot()

snapshots['TestCase01CreatePostAPITestCase::test_case status'] = 201

snapshots['TestCase01CreatePostAPITestCase::test_case body'] = {
    'post_id': 1
}

snapshots['TestCase01CreatePostAPITestCase::test_case header_params'] = {
    'content-language': [
        'Content-Language',
        'en'
    ],
    'content-length': [
        '14',
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

snapshots['TestCase01CreatePostAPITestCase::test_case user_id'] = 1

snapshots['TestCase01CreatePostAPITestCase::test_case post_content'] = 'string'
