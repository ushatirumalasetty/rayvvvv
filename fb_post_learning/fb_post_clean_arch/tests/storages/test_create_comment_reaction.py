import pytest

from fb_post_clean_arch.constants.enums import ReactionType
from fb_post_clean_arch.models import Reactions
from fb_post_clean_arch.storages.storage_implementation import StorageImplementation


@pytest.mark.django_db
def test_create_comment_reaction_given_valid_details_creates_comment(
        create_post,
        create_comments
):
    user_id = 1
    comment_id = 1
    reaction_type = ReactionType.HAHA.value
    sql_storage = StorageImplementation()

    sql_storage.create_comment_reaction(user_id=user_id,
                                        comment_id=comment_id,
                                        reaction_type=reaction_type)
    reaction = Reactions.objects.get(user_id=user_id,
                                     comment_id=comment_id)

    assert reaction.user_id == user_id
    assert reaction.comment_id == comment_id
    assert reaction.reaction_type == reaction_type
