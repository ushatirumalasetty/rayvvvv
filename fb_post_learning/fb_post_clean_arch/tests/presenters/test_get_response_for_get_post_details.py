from fb_post_clean_arch.interactors.storages.storage_interface import \
    PostDetailsDto, PostCompleteDetailsDto
from fb_post_clean_arch.presenters.presenter_implementation import PresenterImplementation


def test_get_response_for_get_post_details_given_get_post_dto_returns_post_details(
        user_dtos,
        reaction_dtos,
        comment_dtos,
        post_dto,
        get_post_response
):
    post_details_dto = PostCompleteDetailsDto(post_dto=post_dto,
                                      user_dtos=user_dtos,
                                      reactions_dto=reaction_dtos,
                                      comments_dto=comment_dtos)

    expected_output = get_post_response

    presenter = PresenterImplementation()
    result = presenter.get_response_for_get_post_details(post_details_dto)
    print("result",result)

    assert result["post_id"] == expected_output["post_id"]
    assert result["posted_by"] == expected_output["posted_by"]
    assert result["reactions"] == expected_output["reactions"]
    assert result["comments"] == expected_output["comments"]
    assert result["comments_count"] == expected_output["comments_count"]
