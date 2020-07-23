from fb_post_clean_arch.interactors.storages.storage_interface import \
    GetUserPostsDto
from fb_post_clean_arch.presenters.presenter_implementation import PresenterImplementation


def test_get_response_for_get_user_posts_given_user_posts_dtos_returns_user_posts(
        user_dtos,
        reaction_dtos,
        comment_dtos,
        post_dtos,
        get_user_posts_response
):
    user_posts_dto = GetUserPostsDto(post_dto=post_dtos,
                                     users_dto=user_dtos,
                                     reactions_dto=reaction_dtos,
                                     comments_dto=comment_dtos)

    expected_output = get_user_posts_response

    presenter = PresenterImplementation()
    result = presenter.get_response_for_get_user_posts(
        user_posts_dto=user_posts_dto)
    for user_post in range(0, len(result), 1):
        assert result[user_post]["post_id"] == expected_output[user_post][
            "post_id"]
        assert result[user_post]["posted_by"] == expected_output[user_post][
            "posted_by"]
        assert result[user_post]["reactions"] == expected_output[user_post][
            "reactions"]
        assert result[user_post]["comments"] == expected_output[user_post][
            "comments"]
