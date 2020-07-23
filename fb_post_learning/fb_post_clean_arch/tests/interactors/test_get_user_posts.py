from unittest.mock import create_autospec

from fb_post_clean_arch.interactors.get_user_posts import \
    GetUserPostsInteractor

from fb_post_clean_arch.interactors.presenters.presenter_interface import \
    PresenterInterface
from fb_post_clean_arch.interactors.storages.storage_interface import \
    StorageInterface, UserPostsDetailsDto


def test_get_user_posts_given_user_id_returns_user_posts(
        post_dtos,
        user_dtos,
        comment_dtos,
        reaction_dtos,
        get_user_posts_response
):
    user_id = 1

    user_posts_dto = UserPostsDetailsDto(post_dto=post_dtos,
                                         users_dto=user_dtos,
                                         comments_dto=comment_dtos,
                                         reactions_dto=reaction_dtos)
    expected_post_details_dict = get_user_posts_response
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = GetUserPostsInteractor(storage=storage)
    storage.get_user_posts_dto.return_value = user_posts_dto
    presenter.get_response_for_get_user_posts.return_value \
        = expected_post_details_dict

    user_posts_dict = interactor.get_user_posts_response(
        user_id=user_id,
        presenter=presenter)

    assert user_posts_dict == expected_post_details_dict
    storage.get_user_posts_dto.assert_called_once_with(user_id=user_id)
    presenter.get_response_for_get_user_posts.assert_called_once_with(
        user_posts_dto=user_posts_dto)
