import pytest

from fb_post_clean_arch.storages.storage_implementation import StorageImplementation


@pytest.mark.django_db
def test_get_posts_with_more_positive_reaction(create_post,
                                               create_post_reactions):

    expected_post_ids = [1]
    storage = StorageImplementation()

    post_ids = storage.get_posts_with_more_positive_reactions()

    assert expected_post_ids == post_ids
