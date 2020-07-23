from fb_post_clean_arch.presenters.presenter_implementation import PresenterImplementation


def test_get_total_reactions_count_method_given_reactions_count_returns_reactions_count_dict():
    json_presenter = PresenterImplementation()
    reactions_count = 6
    expected_reactions_count = {
        "reactions_count": reactions_count
    }

    reactions_count_dict = json_presenter.get_response_for_get_total_reactions_count(
        reactions_count=reactions_count)

    assert reactions_count_dict == expected_reactions_count


