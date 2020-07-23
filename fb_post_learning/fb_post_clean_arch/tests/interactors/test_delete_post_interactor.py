import pytest
from django_swagger_utils.drf_server.exceptions import NotFound
from fb_post_clean_arch.interactors.delete_post_interactor import \
    DeletePostInteractor
from mock import create_autospec

from fb_post_clean_arch.exceptions.custom_exceptions import InvalidPostId, \
    InvalidAccess
from fb_post_clean_arch.interactors.presenters.presenter_interface import \
    PresenterInterface
from fb_post_clean_arch.interactors.storages.storage_interface import \
    StorageInterface


class TestDeletePostInteractor:

    def test_given_invalid_post_raise_exception(self):
        post_id = 1
        user_id = 1
        storage = create_autospec(StorageInterface)
        presenter = create_autospec(PresenterInterface)
        interactor = DeletePostInteractor(storage, presenter)
        storage.validate_post_id.side_effect = InvalidPostId
        presenter.raise_exception_for_invalid_post.side_effect = NotFound

        with pytest.raises(NotFound):
            interactor.delete_post_response(
                post_id=post_id,
                user_id=user_id,
            )

        storage.validate_post_id.assert_called_once_with(post_id=post_id)
        presenter.raise_exception_for_invalid_post.assert_called_once()

    def test_given_valid_post_id_delete_post(self):
        post_id = 1
        user_id = 1
        storage = create_autospec(StorageInterface)
        presenter = create_autospec(PresenterInterface)
        interactor = DeletePostInteractor(storage, presenter)
        storage.get_user_id_of_a_post.return_value = 1

        interactor.delete_post_response(
            post_id=post_id,
            user_id=user_id,
        )

        storage.validate_post_id.assert_called_once_with(post_id=post_id)
        storage.get_user_id_of_a_post.assert_called_once_with(
            post_id=post_id)
        storage.delete_post(post_id=post_id)

    def test_given_invalid_post_owner_id_raise_exception(self):
        post_id = 1
        user_id = 1
        storage = create_autospec(StorageInterface)
        presenter = create_autospec(PresenterInterface)
        interactor = DeletePostInteractor(storage, presenter)
        storage.get_user_id_of_a_post.return_value = 3
        presenter.raise_exception_for_invalid_access.side_effect = \
            InvalidAccess

        with pytest.raises(InvalidAccess):
            interactor.delete_post_response(
                post_id=post_id,
                user_id=user_id,
            )

        storage.validate_post_id.assert_called_once_with(post_id=post_id)
        storage.get_user_id_of_a_post.assert_called_once_with(
            post_id=post_id)
        storage.delete_post(post_id=post_id)
        presenter.raise_exception_for_invalid_access.assert_called_once()
