import datetime

import pytest
from freezegun import freeze_time

from fb_post_clean_arch.constants.enums import ReactionType
from fb_post_clean_arch.interactors.storages.storage_interface import PostDto, \
    CommentDto, ReactionDto, UserDto
from fb_post_clean_arch.models import Post, Comment, Reactions


@pytest.fixture()
def create_post():
    posts = [
        {
            "user_id": 1,
            "post_content": "NEW POST1",
        },
        {
            "user_id": 2,
            "post_content": "NEW POST2",
        }
    ]

    for post in posts:
        with freeze_time("22-04-2019"):
            Post.objects.create(
                user_id=post['user_id'],
                post_content=post['post_content'])


@pytest.fixture()
def create_comments():
    comments = [
        {
            "user_id": 1,
            "post_id": 1,
            "comment_content": "nice post",
            "parent_comment_id": None
        },
        {
            "user_id": 2,
            "post_id": 1,
            "comment_content": "great",
            "parent_comment_id": None
        }
    ]

    for comment in comments:
        with freeze_time("22-04-2019"):
            Comment.objects.create(user_id=comment['user_id'],
                                   post_id=comment['post_id'],
                                   comment_text=comment['comment_content'])


@pytest.fixture()
def create_replies():
    replies = [
        {
            "user_id": 1,
            "post_id": None,
            "comment_content": "nice",
            "parent_comment_id": 2
        }
    ]

    for comment in replies:
        with freeze_time("22-04-2019"):
            Comment.objects.create(user_id=comment['user_id'],
                                   comment_text=comment['comment_content'],
                                   parent_comment_id=comment['parent_comment_id'])


@pytest.fixture()
def create_post_reactions():
    reactions = [
        {
            "post_id": 1,
            "user_id": 1,
            "reaction_type": "LIKE",
            "comment_id": None
        }
    ]

    for reaction in reactions:
        Reactions.objects.create(post_id=reaction['post_id'],
                                 user_id=reaction['user_id'],
                                 reaction_type=reaction['reaction_type'])


@pytest.fixture()
def create_comment_reactions():
    reactions = [
        {
            "post_id": None,
            "user_id": 1,
            "reaction_type": "SAD",
            "comment_id": 1
        }
    ]

    for reaction in reactions:
        Reactions.objects.create(user_id=reaction['user_id'],
                                 reaction_type=reaction['reaction_type'],
                                 comment_id=reaction['comment_id'])


@pytest.fixture()
def post_dtos():
    post_dtos = PostDto(
        post_id=1,
        user_id=1,
        post_content='NEW POST1',
        pub_date_time=datetime.datetime(2019, 4, 22, 0, 0)
)

    return post_dtos


@pytest.fixture()
def user_dtos():
    user_dtos = [
        UserDto(
            user_id=1,
            name='John',
            profile_pic_url='profile_pic_url1',
        )
    ]
    return user_dtos


@pytest.fixture()
def comment_dtos():
    comment_dtos = [
        CommentDto(
            comment_id=1,
            user_id=1,
            post_id=1,
            parent_comment=None,
            comment_content='nice post',
            pub_date_time=datetime.datetime(2019, 4, 22, 0, 0)
        ),
        CommentDto(
            comment_id=2,
            user_id=2,
            post_id=1,
            parent_comment=None,
            comment_content='great',
            pub_date_time=datetime.datetime(2019, 4, 22, 0, 0)
        ),
        CommentDto(
            comment_id=3,
            user_id=1,
            post_id=None,
            parent_comment=2,
            comment_content='nice',
            pub_date_time=datetime.datetime(2019, 4, 22, 0, 0)
        )
    ]
    return comment_dtos


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
def post_reaction_dtos():
    post_reaction_dtos = [
        ReactionDto(
            reaction_id=1,
            post_id=1,
            user_id=1,
            reaction_type=ReactionType.LIKE.value,
            comment_id=None
        )
    ]
    return post_reaction_dtos
