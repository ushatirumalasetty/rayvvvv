import pytest

from fb_post_clean_arch.exceptions.custom_exceptions import \
    ReactionDoesNotExist
from fb_post_clean_arch.storages.storage_implementation import StorageImplementation


@pytest.mark.django_db
def test_validate_post_reaction_if_exists_get_reaction_type(
        create_post,
        create_post_reactions
):
    user_id = 1
    post_id = 1
    sql_storage = StorageImplementation()

    reaction_type = sql_storage. \
        validate_post_reaction_if_exists_get_reaction_type(user_id=user_id,
                                                           post_id=post_id)

    assert reaction_type == "LIKE"


@pytest.mark.django_db
def test_validate_post_reaction_if_not_exists_raise_exception():
    user_id = 1
    post_id = 1
    sql_storage = StorageImplementation()

    with pytest.raises(ReactionDoesNotExist):
        sql_storage.validate_post_reaction_if_exists_get_reaction_type(
            user_id=user_id,
            post_id=post_id)
