import pytest

from fb_post_clean_arch.storages.storage_implementation import StorageImplementation


@pytest.mark.django_db
def test_get_user_reacted_posts_given_user_id_returns_list_of_post_ids(
        create_post
):
    user_id = 1
    expected_post_ids = [1]
    storage = StorageImplementation()

    actual_post_ids = storage.get_user_reacted_posts(user_id=user_id)

    assert actual_post_ids == expected_post_ids
