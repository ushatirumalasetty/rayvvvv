from fb_post_clean_arch.constants.enums import ReactionType
from fb_post_clean_arch.interactors.storages.storage_interface import \
    ReactionMetricsDto
from fb_post_clean_arch.presenters.presenter_implementation import PresenterImplementation


def test_get_response_for_get_reaction_metrics_of_a_post_method_given_reaction_metrics_dto_returns_reaction_metrics():
    reaction_metrics_dtos = [ReactionMetricsDto(
        reaction_type=ReactionType.WOW.value,
        reaction_count=3)]

    json_presenter = PresenterImplementation()
    expected_reaction_metrics = [
        {
            "reaction_type": "WOW",
            "reaction_count": 3
        }
    ]

    reaction_metrics = json_presenter.get_response_for_get_reaction_metrics_of_a_post(
        reaction_metrics_details_dto=reaction_metrics_dtos
    )

    assert reaction_metrics == expected_reaction_metrics
