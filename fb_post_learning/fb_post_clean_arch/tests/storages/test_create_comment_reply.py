import pytest

from fb_post_clean_arch.models import Comment
from fb_post_clean_arch.storages.storage_implementation import StorageImplementation


@pytest.mark.django_db
def test_create_comment_reply_given_valid_details_creates_comment(
        create_post,
        create_comments
):
    comment_id = 1
    reply_user_id = 2
    reply_text = "Nice Post"
    sql_storage = StorageImplementation()

    sql_storage.create_comment_reply(comment_id=comment_id,
                                     reply_user_id=reply_user_id,
                                     reply_text=reply_text)

    comment = Comment.objects.get(parent_comment_id=comment_id,
                                  user_id=reply_user_id)

    assert comment.parent_comment.id == comment_id
    assert comment.user_id == reply_user_id
    assert comment.comment_text == reply_text
