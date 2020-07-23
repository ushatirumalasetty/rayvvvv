
from fb_post_clean_arch_v2.interactors.comment_interactor import \
    CommentInteractor


class TestCreateComment:
    import pytest

    @pytest.fixture
    def storage_mock(self):
        from fb_post_clean_arch_v2.interactors.storage_interfaces. \
            comment_storage_interface import StorageInterface
        from mock import create_autospec
        storage = create_autospec(StorageInterface)
        return storage
 
    @pytest.fixture
    def presenter_mock(self):
        from fb_post_clean_arch_v2.interactors.presenter_interfaces. \
            presenter_interface import CreateReplyPresenterInterface
        from mock import create_autospec
        presenter = create_autospec(CreateReplyPresenterInterface)
        return presenter

    def test_given_invalid_comment_id_then_raise_exception(self, storage_mock,
                                                           presenter_mock):
        comment_id = 1
        reply_user_id = 1
        reply_text = "Nice Comment"
        interactor = CommentInteractor(storage=storage_mock)
        from fb_post_clean_arch_v2.exceptions.custom_exceptions import \
            InvalidCommentId
        storage_mock.validate_comment_id.side_effect = InvalidCommentId
        from django_swagger_utils.drf_server.exceptions import NotFound
        from fb_post_clean_arch_v2.constants.exception_messages import \
            INVALID_COMMENT_ID
        presenter_mock.raise_exception_for_invalid_comment_id.side_effect = \
            NotFound(*INVALID_COMMENT_ID)
        exception_message = INVALID_COMMENT_ID[0]
        response_status_code = INVALID_COMMENT_ID[1]

        import pytest
        with pytest.raises(NotFound) as exception:
            interactor.create_reply_for_comment_wrapper(
                comment_id=comment_id,
                user_id=reply_user_id,
                reply_text=reply_text,
                presenter=presenter_mock)

        assert exception_message == exception.value.message
        assert response_status_code == exception.value.res_status
        storage_mock.validate_comment_id.assert_called_once_with(
            comment_id=comment_id)
        presenter_mock.raise_exception_for_invalid_comment_id. \
            assert_called_once()

    def test_given_valid_comment_id_creates_reply_returns_reply_id(
            self, storage_mock, presenter_mock):
        comment_id = 1
        reply_user_id = 1
        reply_text = "Nice Comment"
        expected_reply_id = 2
        from unittest.mock import Mock
        expected_result = Mock()
        interactor = CommentInteractor(storage=storage_mock)
        storage_mock.get_parent_comment_id.return_value = None
        storage_mock.create_comment_reply.return_value = expected_reply_id
        presenter_mock.get_response.return_value = \
            expected_result

        reply_id_dict = interactor.create_reply_for_comment_wrapper(
            comment_id=comment_id,
            user_id=reply_user_id,
            reply_text=reply_text,
            presenter=presenter_mock)

        assert reply_id_dict == expected_result
        storage_mock.validate_comment_id.assert_called_once_with(
            comment_id=comment_id)
        storage_mock.get_parent_comment_id.assert_called_once_with(
            comment_id=comment_id)
        storage_mock.create_comment_reply.assert_called_once_with(
            comment_id=comment_id,
            user_id=reply_user_id,
            reply_text=reply_text)
        presenter_mock.get_response.assert_called_once_with(
            reply_id=expected_reply_id)

    def test_given_reply_id_to_create_reply_to_its_parent_comment_return_reply_id(
            self, storage_mock, presenter_mock):
        comment_id = 2
        reply_user_id = 1
        reply_text = "Nice Comment"
        expected_reply_id = 3
        parent_comment_id = 1
        from unittest.mock import Mock
        expected_result = Mock()
        interactor = CommentInteractor(storage=storage_mock)
        storage_mock.get_parent_comment_id.return_value = parent_comment_id
        storage_mock.create_comment_reply.return_value = expected_reply_id
        presenter_mock.get_response.return_value = \
            expected_result

        reply_id_dict = interactor.create_reply_for_comment_wrapper(
            comment_id=comment_id,
            user_id=reply_user_id,
            reply_text=reply_text,
            presenter=presenter_mock)

        assert reply_id_dict == expected_result
        storage_mock.validate_comment_id.assert_called_once_with(
            comment_id=comment_id)
        storage_mock.get_parent_comment_id.assert_called_once_with(
            comment_id=comment_id)
        storage_mock.create_comment_reply.assert_called_once_with(
            comment_id=parent_comment_id,
            user_id=reply_user_id,
            reply_text=reply_text
        )
        presenter_mock.get_response.assert_called_once_with(
            reply_id=expected_reply_id)
