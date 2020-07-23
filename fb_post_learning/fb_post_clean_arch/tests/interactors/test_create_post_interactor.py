from unittest.mock import create_autospec

from fb_post_clean_arch.interactors.create_post_interactor import \
    CreatePostInteractor

from fb_post_clean_arch.interactors.presenters.presenter_interface import \
    PresenterInterface
from fb_post_clean_arch.interactors.storages.storage_interface import \
    StorageInterface


class TestCreatePostInteractor:

    def test_given_valid_details_creates_post_and_returns_post_id_dict(self):
        user_id = 1
        post_content = "Nice Post"
        post_id = 3
        expected_post_id_dict = {
            "post_id": post_id
        }
        presenter = create_autospec(PresenterInterface)
        storage = create_autospec(StorageInterface)
        interactor = CreatePostInteractor(storage=storage)
        storage.create_post.return_value = post_id
        presenter.get_create_post_response.return_value = \
            expected_post_id_dict

        actual_post_id_dict = interactor.create_post_wrapper(
            user_id=user_id,
            post_content=post_content,
            presenter=presenter)

        assert expected_post_id_dict["post_id"] == actual_post_id_dict[
            "post_id"]
        storage.create_post.assert_called_once_with(
            user_id=user_id,
            post_content=post_content)
        presenter.get_create_post_response.assert_called_once_with(
            post_id=post_id)
