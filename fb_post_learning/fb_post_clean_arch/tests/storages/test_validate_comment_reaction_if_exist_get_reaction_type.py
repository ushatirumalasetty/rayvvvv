import pytest

from fb_post_clean_arch.exceptions.custom_exceptions import ReactionDoesNotExist
from fb_post_clean_arch.constants.enums import ReactionType
from fb_post_clean_arch.storages.storage_implementation import StorageImplementation


@pytest.mark.django_db
def test_validate_comment_reaction_if_exist_get_reaction_type(
        create_post,
        create_comments,
        create_comment_reactions
):
    comment_id = 1
    user_id = 1
    sql_storage = StorageImplementation()
    expected_reaction_type = ReactionType.HAHA.value

    reaction_type = sql_storage.validate_comment_reaction_if_exists_get_reaction_type(
        comment_id=comment_id,
        user_id=user_id
    )

    assert expected_reaction_type == reaction_type


@pytest.mark.django_db
def test_validate_comment_reaction_given_invalid_details_raises_exception():
    comment_id = 1
    user_id = 1
    sql_storage = StorageImplementation()

    with pytest.raises(ReactionDoesNotExist):
        sql_storage.validate_comment_reaction_if_exists_get_reaction_type(
            comment_id=comment_id,
            user_id=user_id
        )
