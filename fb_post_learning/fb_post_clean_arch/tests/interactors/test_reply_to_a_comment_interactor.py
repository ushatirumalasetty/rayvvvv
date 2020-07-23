import pytest
from django_swagger_utils.drf_server.exceptions import NotFound
from fb_post_clean_arch.interactors.reply_to_a_comment_interactor import \
    ReplyToACommentInteractor
from mock import create_autospec

from fb_post_clean_arch.exceptions.custom_exceptions import InvalidCommentId
from fb_post_clean_arch.interactors.presenters.presenter_interface import \
    PresenterInterface
from fb_post_clean_arch.interactors.storages.storage_interface import \
    StorageInterface


class TestReplyToACommentInteractor:
    def test_given_invalid_comment_raise_exception(self):
        comment_id = 1
        reply_user_id = 1
        reply_text = "Nice Comment"
        storage = create_autospec(StorageInterface)
        interactor = ReplyToACommentInteractor(storage=storage)
        presenter = create_autospec(PresenterInterface)
        storage.validate_comment_id.side_effect = InvalidCommentId
        presenter.raise_exception_for_invalid_comment_id.side_effect = NotFound

        with pytest.raises(NotFound):
            interactor.get_response_for_reply_to_a_comment(
                comment_id=comment_id,
                reply_user_id=reply_user_id,
                reply_text=reply_text,
                presenter=presenter
            )

        storage.validate_comment_id.assert_called_once_with(
            comment_id=comment_id)
        presenter.raise_exception_for_invalid_comment_id.assert_called_once()

    def test_given_valid_comment_id_creates_reply_returns_comment_id(self):
        comment_id = 1
        reply_user_id = 1
        reply_text = "Nice Comment"
        expected_reply_id = 2
        storage = create_autospec(StorageInterface)
        interactor = ReplyToACommentInteractor(storage=storage)
        presenter = create_autospec(PresenterInterface)
        storage.get_parent_comment_id.return_value = None
        storage.create_comment_reply.return_value = expected_reply_id

        reply_id = interactor.get_response_for_reply_to_a_comment(
            comment_id=comment_id,
            reply_user_id=reply_user_id,
            reply_text=reply_text,
            presenter=presenter
        )

        assert reply_id == expected_reply_id
        storage.validate_comment_id.assert_called_once_with(
            comment_id=comment_id)
        storage.get_parent_comment_id.assert_called_once_with(
            comment_id=comment_id)
        storage.create_comment_reply.assert_called_once_with(
            comment_id=comment_id,
            reply_user_id=reply_user_id,
            reply_text=reply_text
        )

    def test_given_reply_id_creates_reply_returns_reply_id(self):
        comment_id = 2
        reply_user_id = 1
        reply_text = "Nice Comment"
        expected_reply_id = 3
        parent_comment_id = 1
        storage = create_autospec(StorageInterface)
        interactor = ReplyToACommentInteractor(storage=storage)
        presenter = create_autospec(PresenterInterface)
        storage.get_parent_comment_id.return_value = parent_comment_id
        storage.create_comment_reply.return_value = expected_reply_id

        reply_id = interactor.get_response_for_reply_to_a_comment(
            comment_id=comment_id,
            reply_user_id=reply_user_id,
            reply_text=reply_text,
            presenter=presenter
        )

        assert reply_id == expected_reply_id
        storage.validate_comment_id.assert_called_once_with(
            comment_id=comment_id)
        storage.get_parent_comment_id.assert_called_once_with(
            comment_id=comment_id)
        storage.create_comment_reply.assert_called_once_with(
            comment_id=parent_comment_id,
            reply_user_id=reply_user_id,
            reply_text=reply_text
        )
