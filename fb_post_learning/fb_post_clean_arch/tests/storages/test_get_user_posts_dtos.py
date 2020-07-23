import pytest
from mock import patch

from fb_post_clean_arch.storages.storage_implementation import \
    StorageImplementation


@pytest.mark.django_db
def test_get_user_posts_dto_given_user_id_returns_user_posts_dtos(
        get_user_dtos,
        post_dtos,
        comment_dtos,
        reaction_dtos,
        user_dtos
):
    user_id = 1
    expected_user_post_dtos = GetUserPostDtos(post_dto=post_dtos,
                                              users_dto=user_dtos,
                                              comments_dto=comment_dtos,
                                              reactions_dto=reaction_dtos)
    sql_storage = StorageImplementation()

    user_post_dtos = sql_storage.get_user_posts_dto(user_id=user_id)

    assert user_post_dtos.post_dto == expected_user_post_dtos.post_dto
    assert user_post_dtos.users_dto == expected_user_post_dtos.users_dto
    assert user_post_dtos.comments_dto == expected_user_post_dtos.comments_dto
    assert user_post_dtos.reactions_dto == expected_user_post_dtos.reactions_dto
