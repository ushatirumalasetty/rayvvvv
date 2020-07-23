from fb_post_clean_arch.interactors.storages.storage_interface import \
    CommentRepliesDto
from fb_post_clean_arch.presenters.presenter_implementation import PresenterImplementation


def test_get_response_for_get_comment_replies_given_replied_dto_returns_replies_dict(
        user_dtos,
        replies_dtos
):
    comment_replies_dtos = CommentRepliesDto(users_dto=user_dtos,
                                             comments_dto=replies_dtos)

    expected_replies_dict = [{
        "comment_id": 3,
        "commenter": {
            "user_id": 1,
            "user_name": "John",
            "profile_pic_url": " "
        },
        "commented_at": '04-22-2019,00:00:1555871400.000000',
        "comment_content": "nice"
    }]
    json_presenter = PresenterImplementation()

    replies_dict = json_presenter.get_response_for_get_comment_replies(
        comment_replies_dto=comment_replies_dtos
    )

    assert replies_dict == expected_replies_dict
