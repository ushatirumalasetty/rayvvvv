import pytest

from fb_post_clean_arch.storages.storage_implementation import StorageImplementation


@pytest.mark.django_db
def test_get_total_reactions_count(create_post,
                                   create_comments,
                                   create_post_reactions,
                                   create_comment_reactions):
    sql_storage = StorageImplementation()
    expected_reactions_count = 2

    reaction_count = sql_storage.get_total_reactions_count()

    assert reaction_count == expected_reactions_count

