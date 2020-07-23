from fb_post_clean_arch.constants.enums import ReactionType
from fb_post_clean_arch.interactors.storages.storage_interface import \
    PostReactionDto
from fb_post_clean_arch.presenters.presenter_implementation import PresenterImplementation


def test_get_response_for_get_post_reactions_given_reaction_dtos_returns_dict(
        user_dtos,
        post_reaction_dtos):
    user_dtos = user_dtos
    reactions_dtos = post_reaction_dtos
    post_reaction_dto = PostReactionDto(user_dtos=user_dtos,
                                        reaction_dtos=reactions_dtos)
    json_presenter = PresenterImplementation()
    expected_post_reactions = [
        {
            "user_id": 1,
            "user_name": "James",
            "profile_pic": " ",
            "reaction_type": ReactionType.LIKE.value
        }
    ]

    post_reactions = json_presenter.get_response_for_get_post_reactions(
        post_reactions_dto=post_reaction_dto
    )

    index = 0
    for user in post_reactions:
        assert user["user_id"] == expected_post_reactions[index]["user_id"]
        assert user["reaction_type"] == expected_post_reactions[index][
            "reaction_type"]
        index += 1
