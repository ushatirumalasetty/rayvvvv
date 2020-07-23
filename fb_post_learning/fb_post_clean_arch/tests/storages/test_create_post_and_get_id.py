import pytest

from fb_post_clean_arch.models import Post
from fb_post_clean_arch.storages.storage_implementation import StorageImplementation


@pytest.mark.django_db
def test_create_post_and_get_id_method_given_valid_details_returns_post_id():
    user_id = 1
    post_content = "Post Content"
    storage = StorageImplementation()

    post_id = storage.create_post(user_id=user_id,
                                  post_content=post_content)

    post = Post.objects.get(id=post_id)

    assert post_id == post.id
