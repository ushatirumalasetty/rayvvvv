# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01GetPostAPITestCase::test_case status'] = 200

snapshots['TestCase01GetPostAPITestCase::test_case body'] = {
    'comments': [
        {
            'comment_content': 'nice post',
            'comment_id': 1,
            'commented_at': '12-18-2019,00:00:1576607400.000000',
            'commenter': {
                'name': 'John',
                'profile_pic': 'profile_pic_url1',
                'user_id': 1
            },
            'reactions': {
                'count': 1,
                'type': [
                    'SAD'
                ]
            },
            'replies': [
                {
                }
            ],
            'replies_count': 1
        },
        {
            'comment_content': 'great',
            'comment_id': 2,
            'commented_at': '12-18-2019,00:00:1576607400.000000',
            'commenter': {
                'name': 'John',
                'profile_pic': 'profile_pic_url1',
                'user_id': 1
            },
            'reactions': {
                'count': 1,
                'type': [
                    'WOW'
                ]
            },
            'replies': [
                {
                    'comment_content': 'nice post',
                    'comment_id': 4,
                    'commented_at': '12-18-2019,00:00:1576607400.000000',
                    'commenter': {
                        'name': 'John',
                        'profile_pic': 'profile_pic_url1',
                        'user_id': 1
                    },
                    'reactions': {
                        'count': 0,
                        'type': [
                        ]
                    }
                }
            ],
            'replies_count': 1
        },
        {
            'comment_content': 'nice',
            'comment_id': 3,
            'commented_at': '12-18-2019,00:00:1576607400.000000',
            'commenter': {
                'name': 'John',
                'profile_pic': 'profile_pic_url1',
                'user_id': 1
            },
            'reactions': {
                'count': 0,
                'type': [
                ]
            },
            'replies': [
                {
                }
            ],
            'replies_count': 1
        }
    ],
    'comments_count': 3,
    'post_content': 'NEW POST',
    'post_id': 1,
    'posted_at': '09-11-2019,00:00:1568140200.000000',
    'posted_by': {
        'name': 'John',
        'profile_pic': 'profile_pic_url1',
        'user_id': 1
    },
    'reactions': {
        'count': 1,
        'type': [
            'LIKE'
        ]
    }
}

snapshots['TestCase01GetPostAPITestCase::test_case header_params'] = {
    'content-language': [
        'Content-Language',
        'en'
    ],
    'content-length': [
        '1257',
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
