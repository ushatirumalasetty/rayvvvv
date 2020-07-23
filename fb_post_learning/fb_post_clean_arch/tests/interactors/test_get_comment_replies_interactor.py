import pytest
from django_swagger_utils.drf_server.exceptions import NotFound
from fb_post_clean_arch.interactors.get_comment_replies_interactor import \
    GetCommentRepliesInteractor
from mock import create_autospec

from fb_post_clean_arch.exceptions.custom_exceptions import InvalidCommentId
from fb_post_clean_arch.interactors.presenters.presenter_interface import \
    PresenterInterface
from fb_post_clean_arch.interactors.storages.storage_interface import \
    StorageInterface, CommentRepliesDto


class TestGetCommentRepliesInteractor:

    def test_given_invalid_comment_id_raises_exception(self):
        comment_id = 1
        storage = create_autospec(StorageInterface)
        interactor = GetCommentRepliesInteractor(storage=storage)
        presenter = create_autospec(PresenterInterface)
        storage.validate_comment_id.side_effect = InvalidCommentId
        presenter.raise_exception_for_invalid_comment_id.side_effect = NotFound

        with pytest.raises(NotFound):
            interactor.get_comment_replies_response(comment_id=comment_id,
                                                    presenter=presenter)

        storage.validate_comment_id.assert_called_once_with(
            comment_id=comment_id)
        presenter.raise_exception_for_invalid_comment_id.assert_called_once()

    def test_given_valid_comment_id_return_comment_replies_dict(self,
                                                                user_dtos,
                                                                replies_dtos):
        comment_id = 2
        expected_output = [{
            "comment_id": 2,
            "commenter": {
                "user_id": 1,
                "name": "James",
                "profile_pic_url": ""
            },
            "commented_at": "13-12-2019,00:00:1568140200.00",
            "comment_content": "nice",
        }]
        user_dtos = user_dtos
        comment_dtos = replies_dtos
        comment_replies_dto = CommentRepliesDto(
            users_dto=user_dtos,
            comments_dto=comment_dtos)
        storage = create_autospec(StorageInterface)
        presenter = create_autospec(PresenterInterface)
        interactor = GetCommentRepliesInteractor(storage=storage)
        storage.get_comment_replies_dto.return_value = comment_replies_dto
        presenter.get_response_for_get_comment_replies.return_value = \
            expected_output

        comment_replies_dict = interactor.get_comment_replies_response(
            comment_id=comment_id,
            presenter=presenter)

        assert comment_replies_dict == expected_output
        storage.validate_comment_id.assert_called_once_with(
            comment_id=comment_id)
        storage.get_comment_replies_dto.assert_called_once_with(
            comment_id=comment_id)
        presenter.get_response_for_get_comment_replies.assert_called_once_with(
            comment_replies_dto=comment_replies_dto)
