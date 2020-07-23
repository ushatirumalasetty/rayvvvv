import pytest
from mock import patch

from fb_post_clean_arch.storages.storage_implementation import StorageImplementation


@pytest.mark.django_db
def test_get_comment_replies_dto(create_post,
                                 create_comments,
                                 user_dtos,
                                 replies_dtos):
    comment_id = 2
    user_ids = [1, 2]
    sql_storage = StorageImplementation()
    user_dtos = user_dtos
    replies_dtos = replies_dtos

    comment_replies_dtos = sql_storage.get_comment_replies_dto(
        comment_id=comment_id)

    assert user_dtos == comment_replies_dtos.users_dto
    assert replies_dtos == comment_replies_dtos.replies_dtos

