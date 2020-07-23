from fb_post_clean_arch.presenters.presenter_implementation import PresenterImplementation


def test_get_response_for_get_posts_with_more_positive_reaction_given_list_of_post_ids_returns_post_ids_dict():
    json_presenter = PresenterImplementation()
    post_ids = [1, 2, 3]
    expected_post_ids_dict = {
        "post_ids": post_ids
    }

    actual_post_ids_dict = json_presenter.get_response_for_get_posts_with_more_positive_reaction(
        post_ids=post_ids
    )

    assert expected_post_ids_dict == actual_post_ids_dict
