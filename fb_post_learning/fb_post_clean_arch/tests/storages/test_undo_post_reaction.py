import pytest

from fb_post_clean_arch.models import Reactions
from fb_post_clean_arch.storages.storage_implementation import StorageImplementation


@pytest.mark.django_db
def test_undo_post_reaction_given_dup_reaction_results_undo_reaction(
        create_post,
        create_post_reactions
):
    user_id = 1
    post_id = 1
    reaction_not_exists = False
    sql_storage = StorageImplementation()

    sql_storage.undo_post_reaction(user_id=user_id,
                                   post_id=post_id)

    actual_result = Reactions.objects.filter(user_id=user_id,
                                             post_id=post_id).exists()

    assert actual_result == reaction_not_exists
