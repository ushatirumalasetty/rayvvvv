import pytest
from django_swagger_utils.drf_server.exceptions import NotFound
from mock import create_autospec, patch

from fb_post_clean_arch.exceptions.custom_exceptions import InvalidPostId
from fb_post_clean_arch.interactors.get_post_reactions_interactor import \
    GetPostReactionsInteractor
from fb_post_clean_arch.interactors.presenters.presenter_interface import \
    PresenterInterface
from fb_post_clean_arch.interactors.storages.storage_interface import \
    StorageInterface, PostReactionDto, UserDto, PostReactionCompleteDetailsDto


class TestGetPostReactionsInteractor:

    def test_given_invalid_post_id_raises_exception(self):
        post_id = 1
        storage = create_autospec(StorageInterface)
        presenter = create_autospec(PresenterInterface)
        interactor = GetPostReactionsInteractor(storage=storage)
        storage.validate_post_id.side_effect = InvalidPostId
        presenter.raise_exception_for_invalid_post.side_effect = NotFound

        with pytest.raises(NotFound):
            interactor.get_post_reactions_wrapper(
                post_id=post_id,
                presenter=presenter
            )

        storage.validate_post_id.assert_called_once_with(post_id=post_id)
        presenter.raise_exception_for_invalid_post.assert_called_once()

    @patch(
        'fb_post_clean_arch.adapters.service_adapter.ServiceAdapter.get_user_dtos')
    def test_given_valid_post_id_return_post_reactions_dict(
            self, get_user_dtos, reaction_dtos):
        reaction_dto = reaction_dtos
        user_dtos = [UserDto(
            user_id=1,
            name="John",
            profile_pic_url="profile_pic_url1"
        ),
            UserDto(
                user_id=2,
                name="John",
                profile_pic_url="profile_pic_url1"
            )
        ]
        get_user_dtos.return_value = user_dtos
        user_ids = [1]
        post_reactions_dto = PostReactionDto(user_ids=user_ids,
                                             reaction_dtos=reaction_dto)
        post_id = 1
        storage = create_autospec(StorageInterface)
        presenter = create_autospec(PresenterInterface)
        expected_output = [
            {
                "user_id": 1,
                "name": "John",
                "profile_pic_url": "",
                "reaction": "LIKE"
            }
        ]
        interactor = GetPostReactionsInteractor(storage=storage)
        storage.get_post_reaction_dtos.return_value = post_reactions_dto
        presenter.get_response_for_get_post_reactions.return_value = \
            expected_output
        post_reaction_complete_details_dtos = PostReactionCompleteDetailsDto(
            reaction_dtos=reaction_dtos,
            user_dtos=user_dtos)
        post_reactions = interactor.get_post_reactions_wrapper(
            post_id=post_id,
            presenter=presenter)

        index = 0
        for user in post_reactions:
            assert user["user_id"] == expected_output[index]["user_id"]
            index += 1

        storage.validate_post_id.assert_called_once_with(post_id=post_id)
        storage.get_post_reaction_dtos.assert_called_once_with(post_id=post_id)
        presenter.get_response_for_get_post_reactions.assert_called_once_with(
            post_reaction_dtos=post_reaction_complete_details_dtos)
        get_user_dtos.assert_called_once_with(user_ids=user_ids)

