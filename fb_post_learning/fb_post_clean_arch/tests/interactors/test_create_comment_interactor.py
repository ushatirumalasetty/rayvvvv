import pytest
from django_swagger_utils.drf_server.exceptions import NotFound
from mock import create_autospec

from fb_post_clean_arch.exceptions.custom_exceptions import InvalidPostId
from fb_post_clean_arch.interactors.create_comment_interactor import \
    CreateCommentInteractor
from fb_post_clean_arch.interactors.presenters.presenter_interface import \
    PresenterInterface
from fb_post_clean_arch.interactors.storages.storage_interface import \
    StorageInterface


class TestCreateCommentInteractor:

    def test_given_invalid_post_id_raises_exception(self):
        post_id = 1
        comment_text = "nice post"
        user_id = 1
        storage = create_autospec(StorageInterface)
        interactor = CreateCommentInteractor(storage)
        presenter = create_autospec(PresenterInterface)
        storage.validate_post_id.side_effect = InvalidPostId
        presenter.raise_exception_for_invalid_post.side_effect = NotFound

        with pytest.raises(NotFound):
            interactor.create_comment_wrapper(post_id=post_id,
                                              comment_text=comment_text,
                                              user_id=user_id,
                                              presenter=presenter)

        storage.validate_post_id.assert_called_once_with(post_id=post_id)
        presenter.raise_exception_for_invalid_post.assert_called_once()

    def test_given_valid_post_id_creates_comment_and_returns_comment_id_dict(
            self):
        post_id = 1
        comment_text = "nice post"
        user_id = 1
        expected_comment_id = 1
        expected_comment_id_dict = {
            "comment_id": expected_comment_id
        }
        storage = create_autospec(StorageInterface)
        interactor = CreateCommentInteractor(storage)
        presenter = create_autospec(PresenterInterface)
        storage.create_comment.return_value = \
            expected_comment_id
        presenter.get_create_comment_response.return_value = \
            expected_comment_id_dict

        actual_comment_id_dict = interactor.create_comment_wrapper(
            post_id=post_id,
            comment_text=comment_text,
            user_id=user_id,
            presenter=presenter)

        assert expected_comment_id_dict == actual_comment_id_dict
        storage.validate_post_id.assert_called_once_with(post_id=post_id)
        storage.create_comment.assert_called_once_with(
            user_id=user_id,
            post_id=post_id,
            comment_text=comment_text)
        presenter.get_create_comment_response.assert_called_once_with(
            comment_id=expected_comment_id)
