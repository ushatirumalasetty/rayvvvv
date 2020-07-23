import pytest

from fb_post_clean_arch.constants.enums import ReactionType
from fb_post_clean_arch.models import Reactions
from fb_post_clean_arch.storages.storage_implementation import StorageImplementation


@pytest.mark.django_db
def test_create_post_reaction_given_valid_details_creates_post_reaction(
create_post
):
    user_id = 1
    post_id = 1
    reaction_type = ReactionType.HAHA.value
    sql_storage = StorageImplementation()

    sql_storage.create_post_reaction(user_id=user_id,
                                     post_id=post_id,
                                     reaction_type=reaction_type)

    reaction = Reactions.objects.get(user_id=user_id,
                                     post_id=post_id)

    assert reaction.user_id == user_id
    assert reaction.post.id == post_id
    assert reaction.reaction_type == reaction_type
