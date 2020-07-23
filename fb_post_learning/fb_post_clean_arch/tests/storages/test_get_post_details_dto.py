import pytest
from fb_post_clean_arch.storages.storage_implementation import StorageImplementation


@pytest.mark.django_db
def test_get_post_details_dto_given_post_id(create_post,
                                            create_comments,
                                            create_replies,
                                            create_post_reactions,
                                            create_comment_reactions,
                                            post_dtos,
                                            comment_dtos,
                                            reaction_dtos):

    post_id = 1
    post_dtos = post_dtos
    user_ids = [1, 2]
    comment_dtos = comment_dtos
    reaction_dtos = reaction_dtos
    sql_storage = StorageImplementation()

    post_details_dtos = sql_storage.get_post_details_dto(post_id=post_id)

    assert post_dtos == post_details_dtos.post_dto
    assert user_ids == post_details_dtos.user_ids
    assert comment_dtos == post_details_dtos.comments_dto
    assert reaction_dtos == post_details_dtos.reactions_dto



