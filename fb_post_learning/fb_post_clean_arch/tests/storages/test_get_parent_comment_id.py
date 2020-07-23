import pytest

from fb_post_clean_arch.storages.storage_implementation import StorageImplementation


@pytest.mark.django_db
def test_get_parent_comment_id(create_replies):
    comment_id = 3
    expected_parent_comment_id = 2
    sql_storage = StorageImplementation()

    actual_parent_comment_id = sql_storage.get_parent_comment_id(
        comment_id=comment_id)

    assert actual_parent_comment_id == expected_parent_comment_id
