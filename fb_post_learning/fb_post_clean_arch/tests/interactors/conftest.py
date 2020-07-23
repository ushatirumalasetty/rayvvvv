import datetime

import pytest

from fb_post_clean_arch.constants.enums import ReactionType
from fb_post_clean_arch.interactors.storages.storage_interface import UserDto, \
    ReactionDto, CommentDto, PostDto


@pytest.fixture()
def user_dtos():
    user_dtos = [UserDto(
        user_id=1,
        name="John",
        profile_pic_url="url1"
    )]
    return user_dtos


@pytest.fixture()
def reaction_dtos():
    reaction_dtos = [
        ReactionDto(reaction_id=1,
                    comment_id=None,
                    post_id=1,
                    user_id=1,
                    reaction_type=ReactionType.HAHA),
        ReactionDto(reaction_id=2,
                    comment_id=1,
                    post_id=None,
                    user_id=1,
                    reaction_type=ReactionType.HAHA)
    ]
    return reaction_dtos


@pytest.fixture()
def comment_dtos():
    comment_dtos = [CommentDto(comment_id=1,
                               user_id=2,
                               post_id=1,
                               comment_content="nice post",
                               pub_date_time=datetime.datetime(2019, 4, 22, 0, 0),
                               parent_comment=None),
                    CommentDto(comment_id=2,
                               user_id=2,
                               post_id=None,
                               comment_content="nice post",
                               pub_date_time=datetime.datetime(2019, 4, 22, 0, 0),
                               parent_comment=1)
                    ]
    return comment_dtos


@pytest.fixture()
def post_dto():
    post_dtos = PostDto(user_id=1,
                        post_content="My Post Content",
                        pub_date_time=datetime.datetime(2019, 4, 22, 0, 0),
                        post_id=1)
    return post_dtos


@pytest.fixture()
def post_dtos():
    post_dtos = [
        PostDto(user_id=1,
                post_content="My Post Content",
                pub_date_time=datetime.datetime(2019, 4, 22, 0, 0),
                post_id=1)]
    return post_dtos


@pytest.fixture()
def replies_dtos():
    replies_dtos = [
        CommentDto(
            comment_id=3,
            user_id=1,
            post_id=None,
            parent_comment=2,
            comment_content='nice',
            pub_date_time=datetime.datetime(2019, 4, 22, 0, 0)
        )
    ]
    return replies_dtos


@pytest.fixture()
def reaction_dtos():
    reaction_dtos = [
        ReactionDto(
            reaction_id=1,
            post_id=1,
            user_id=1,
            reaction_type=ReactionType.LIKE.value,
            comment_id=None
        ),
        ReactionDto(
            reaction_id=2,
            post_id=None,
            user_id=1,
            reaction_type=ReactionType.SAD.value,
            comment_id=1
        )
    ]

    return reaction_dtos


@pytest.fixture()
def get_post_response():
    get_post_response = {
        'post_content': 'NEW POST',
        'post_id': 1,
        'posted_at': '13-12-2019,00:00:1568140200.00',
        'posted_by': {
            'name': 'James',
            'profile_pic': '',
            'user_id': 1
        },
        'reactions': {
            'count': 1,
            'type': [
                'HAHA'
            ]
        },
        'comments': [
            {
                'comment_content': 'nice post',
                'comment_id': 1,
                'commented_at': '13-12-2019,00:00:1568140200.00',
                'commenter': {
                    'name': 'James',
                    'profile_pic': '',
                    'user_id': 2
                },
                'reactions': {
                    'count': 1,
                    'type': [
                        'SAD'
                    ]
                },
                'replies': [
                    {
                        'comment_content': 'nice post',
                        'comment_id': 2,
                        'commented_at': '13-12-2019,00:00:1568140200.00',
                        'commenter': {
                            'name': 'James',
                            'profile_pic': '',
                            'user_id': 2
                        }
                    },
                    {
                        'count': 1,
                        'type': [
                            'WOW'
                        ]
                    }
                ],
                'replies_count': 1
            }

        ],
        "comments_count": 1
    }
    return get_post_response


@pytest.fixture()
def get_user_posts_response():
    get_user_posts_response = {
        'post_content': 'NEW POST',
        'post_id': 1,
        'posted_at': '13-12-2019,00:00:1568140200.00',
        'posted_by': {
            'name': 'James',
            'profile_pic': '',
            'user_id': 1
        },
        'reactions': {
            'count': 1,
            'type': [
                'HAHA'
            ]
        },
        'comments': [
            {
                'comment_content': 'nice post',
                'comment_id': 1,
                'commented_at': '13-12-2019,00:00:1568140200.00',
                'commenter': {
                    'name': 'James',
                    'profile_pic': '',
                    'user_id': 2
                },
                'reactions': {
                    'count': 1,
                    'type': [
                        'SAD'
                    ]
                },
                'replies': [
                    {
                        'comment_content': 'nice post',
                        'comment_id': 2,
                        'commented_at': '13-12-2019,00:00:1568140200.00',
                        'commenter': {
                            'name': 'James',
                            'profile_pic': '',
                            'user_id': 2
                        }
                    },
                    {
                        'count': 1,
                        'type': [
                            'WOW'
                        ]
                    }
                ],
                'replies_count': 1
            }

        ],
        "comments_count": 1
    }
    return get_user_posts_response
