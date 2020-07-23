import pytest
from fb_post_clean_arch.storages.storage_implementation import \
    StorageImplementation


@pytest.mark.django_db
def test_get_post_reaction_dtos_given_post_id_returns_reactions_dto(
        create_post,
        create_post_reactions,
        post_reaction_dtos):
    post_id = 1
    user_ids = [1]
    reactions_dtos = post_reaction_dtos

    sql_storage = StorageImplementation()

    post_reaction_dtos = sql_storage.get_post_reaction_dtos(post_id=post_id)

    assert user_ids == post_reaction_dtos.user_ids
    assert reactions_dtos == post_reaction_dtos.reaction_dtos
