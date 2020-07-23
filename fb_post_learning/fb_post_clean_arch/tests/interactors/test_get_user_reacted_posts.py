from unittest.mock import create_autospec

from fb_post_clean_arch.interactors.get_user_reacted_posts_interactor import \
    GetUserReactedPostInteractor

from fb_post_clean_arch.interactors.presenters.presenter_interface import \
    PresenterInterface
from fb_post_clean_arch.interactors.storages.storage_interface import \
    StorageInterface


def test_get_user_reacted_posts_interactor_given_user_id_return_post_ids():
    user_id = 1
    post_ids = [1, 2, 3]
    expected_output = {
        "post_ids": post_ids
    }
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = GetUserReactedPostInteractor(storage=storage)

    presenter.get_response_for_user_reacted_posts.return_value = \
        expected_output

    post_ids_dict = interactor.get_response_for_user_reacted_posts(
        user_id=user_id,
        presenter=presenter
    )

    assert post_ids_dict == expected_output
    storage.get_user_reacted_posts.assert_called_once_with(user_id=user_id)
    presenter.get_response_for_user_reacted_posts.assert_called_once_with(
        user_reacted_posts_dto=post_ids)
