import pytest

from fb_post_clean_arch.models import Comment
from fb_post_clean_arch.storages.storage_implementation import StorageImplementation


@pytest.mark.django_db
def test_create_comment_given_valid_details_creates_comment_triangulation(
        create_post):
    user_id = 1
    post_id = 1
    comment_text = "Nice Post"
    storage = StorageImplementation()

    comment_id = storage.create_comment(
        user_id=user_id,
        post_id=post_id,
        comment_text=comment_text)

    comment = Comment.objects.get(id=comment_id)
    assert comment.id == comment_id
    assert comment.user_id == user_id
    assert comment.post.id == post_id
    assert comment.comment_text == comment_text
