import pytest

from fb_post_clean_arch.exceptions.custom_exceptions import InvalidCommentId
from fb_post_clean_arch.storages.storage_implementation import StorageImplementation


@pytest.mark.django_db
def test_validate_post_id_given_invalid_comment_id_raises_exception():
    comment_id = 10
    sql_storage = StorageImplementation()

    with pytest.raises(InvalidCommentId):
        sql_storage.validate_comment_id(comment_id=comment_id)
