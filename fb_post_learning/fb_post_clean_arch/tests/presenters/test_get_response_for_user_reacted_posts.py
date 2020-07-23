from fb_post_clean_arch.presenters.presenter_implementation import PresenterImplementation


def test_get_response_for_user_reacted_posts_given_post_ids_returns_post_ids_dict():
    post_ids = [1, 2, 3]
    expected_post_ids_dict = {
        "post_ids": post_ids
    }
    json_presenter = PresenterImplementation()

    post_ids_dict = json_presenter.get_response_for_user_reacted_posts(
        post_ids=post_ids)

    assert expected_post_ids_dict == post_ids_dict

