import pytest

from fb_post_clean_arch.exceptions.custom_exceptions import InvalidPostId
from fb_post_clean_arch.storages.storage_implementation import StorageImplementation


@pytest.mark.django_db
def test_validate_post_id_given_invalid_post_id_raises_exception():
    post_id = 2
    sql_storage = StorageImplementation()

    with pytest.raises(InvalidPostId):
        sql_storage.validate_post_id(post_id=post_id)
