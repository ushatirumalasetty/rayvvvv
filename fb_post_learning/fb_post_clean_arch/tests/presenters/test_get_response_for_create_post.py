from fb_post_clean_arch.presenters.presenter_implementation import PresenterImplementation


def test_get_response_for_create_post_given_post_id_returns_post_id_dict():
    post_id = 1
    expected_post_id_dict = {
        "post_id": post_id
    }
    json_presenter = PresenterImplementation()

    post_id_dict = json_presenter.get_create_post_response(post_id=post_id)

    assert post_id_dict == expected_post_id_dict

