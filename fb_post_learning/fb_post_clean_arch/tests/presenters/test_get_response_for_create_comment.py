from fb_post_clean_arch.presenters.presenter_implementation import PresenterImplementation


def test_get_response_for_create_comment_given_comment_id_returns_comment_dict():
    json_presenter = PresenterImplementation()
    comment_id = 1
    expected_comment_id_dict = {
        "comment_id": comment_id
    }

    comment_id_dict = json_presenter.get_create_comment_response(
        comment_id=comment_id)

    assert comment_id_dict == expected_comment_id_dict

