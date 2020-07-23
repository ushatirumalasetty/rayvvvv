import pytest
from freezegun import freeze_time
from fb_post_clean_arch_v2.interactors.post_interactor import PostInteractor


class TestPostInteractor:
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
            presenter_interface import GetPostPresenterInterface
        from mock import create_autospec
        presenter = create_autospec(GetPostPresenterInterface)
        return presenter

    def test_given_invalid_post_id_raises_exception(self, storage_mock,
                                                    presenter_mock):
        post_id = 1
        from fb_post_clean_arch_v2.exceptions.custom_exceptions import \
            InvalidPostId

        storage_mock.validate_post_id.side_effect = InvalidPostId
        from django_swagger_utils.drf_server.exceptions import NotFound
        presenter_mock.raise_exception_for_invalid_post.side_effect = NotFound

        interactor = PostInteractor(storage=storage_mock)

        with pytest.raises(NotFound):
            interactor.get_post_wrapper(post_id=post_id,
                                        presenter=presenter_mock)

        storage_mock.validate_post_id.assert_called_once_with(post_id=post_id)
        presenter_mock.raise_exception_for_invalid_post.assert_called_once()

    @freeze_time("2020-01-1 05:21:34")
    def test_given_valid_post_id_returns_post_details(self, mocker,
                                                      storage_mock,
                                                      presenter_mock):
        from fb_post_clean_arch_v2.tests.factories.storage_dtos import \
            PostDtoFactory, CommentDtoFactory, ReactionDtoFactory
        from fb_post_clean_arch_v2.interactors.storage_interfaces.dtos import \
            PostDetailsDto
        from fb_post_clean_arch_v2.interactors.presenter_interfaces. \
            dtos import PostCompleteDetailsDto
        from fb_post_clean_arch_v2.tests.common_fixtures.adapters. \
            auth_service import prepare_get_user_dtos_mock
        import datetime
        time = datetime.datetime.now()
        user_ids = [1, 2]
        post_id = 1

        get_user_dtos_mock = prepare_get_user_dtos_mock(mocker, user_ids)

        post_dto = PostDtoFactory(pub_date_time=time)
        comment_dtos = CommentDtoFactory.create_batch(2, post_id=1,
                                                      pub_date_time=time)
        reaction_dtos = ReactionDtoFactory.create_batch(2, post_id=1)

        storage_mock.get_post_details_dto.return_value = PostDetailsDto(
            post_dto=post_dto,
            user_ids=user_ids,
            comments_dto=comment_dtos,
            reactions_dto=reaction_dtos)
        from unittest.mock import Mock
        presenter_mock.get_response_for_get_post_details.return_value = Mock()
        interactor = PostInteractor(storage=storage_mock)
        interactor.get_post_wrapper(
            post_id=post_id,
            presenter=presenter_mock)

        user_dtos = get_user_dtos_mock(user_ids)
        post_complete_details_dto = PostCompleteDetailsDto(
            post_dto=post_dto,
            user_dtos=user_dtos,
            reactions_dto=reaction_dtos,
            comments_dto=comment_dtos
        )

        storage_mock.validate_post_id.assert_called_once_with(post_id=post_id)
        presenter_mock.get_response_for_get_post_details. \
            assert_called_once_with(post_details_dto=post_complete_details_dto)
        storage_mock.get_post_details_dto.assert_called_once_with(
            post_id=post_id)
