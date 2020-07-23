import pytest

from fb_post_clean_arch.constants.enums import ReactionType
from fb_post_clean_arch.models import Reactions
from fb_post_clean_arch.storages.storage_implementation import StorageImplementation


@pytest.mark.django_db
def test_update_post_reaction_given_diff_reaction_updates_reaction(
        create_post,
        create_post_reactions,
):
    user_id = 1
    post_id = 1
    reaction_type = ReactionType.HAHA.value
    sql_storage = StorageImplementation()

    sql_storage.update_post_reaction(user_id=user_id,
                                     post_id=post_id,
                                     reaction_type=reaction_type)
    reaction = Reactions.objects.get(user_id=user_id,
                                     post_id=post_id)

    assert reaction.user_id == user_id
    assert reaction.post_id == post_id
    assert reaction.reaction_type == reaction_type
