import pytest

from fb_post_clean_arch.models import Reactions
from fb_post_clean_arch.storages.storage_implementation import StorageImplementation


@pytest.mark.django_db
def test_undo_comment_reaction_given_dup_reaction_type(create_post,
                                                       create_comments,
                                                       create_comment_reactions):
    user_id = 1
    comment_id = 1
    comment_not_exist = False
    sql_storage = StorageImplementation()

    sql_storage.undo_comment_reaction(user_id=user_id,
                                      comment_id=comment_id)
    actual_result = Reactions.objects.filter(user_id=user_id,
                                             comment_id=comment_id).exists()

    assert actual_result == comment_not_exist
