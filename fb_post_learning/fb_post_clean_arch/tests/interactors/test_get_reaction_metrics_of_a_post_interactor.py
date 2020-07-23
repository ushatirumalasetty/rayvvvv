import pytest
from django_swagger_utils.drf_server.exceptions import NotFound
from fb_post_clean_arch.interactors.get_reaction_metrics_of_a_post_interactor import \
    GetReactionMetricsOfAPostInteractor
from mock import create_autospec

from fb_post_clean_arch.exceptions.custom_exceptions import InvalidPostId
from fb_post_clean_arch.constants.enums import ReactionType
from fb_post_clean_arch.interactors.presenters.presenter_interface import \
    PresenterInterface
from fb_post_clean_arch.interactors.storages.storage_interface import \
    StorageInterface, ReactionMetricDto


class TestGetReactionMetricsOfAPostInteractor:

    def test_given_invalid_post_raise_exception(self):
        post_id = 1
        storage = create_autospec(StorageInterface)
        presenter = create_autospec(PresenterInterface)
        storage.validate_post_id.side_effect = InvalidPostId
        interactor = GetReactionMetricsOfAPostInteractor(storage=storage)
        presenter.raise_exception_for_invalid_post.side_effect = NotFound

        with pytest.raises(NotFound):
            interactor.get_reaction_metrics_of_a_post_response(
                post_id=post_id,
                presenter=presenter
            )

        storage.validate_post_id.assert_called_once_with(post_id=post_id)
        presenter.raise_exception_for_invalid_post.assert_called_once()

    def test_given_valid_post_id_returns_reaction_metrics(self):
        post_id = 1
        storage = create_autospec(StorageInterface)
        presenter = create_autospec(PresenterInterface)
        interactor = GetReactionMetricsOfAPostInteractor(storage=storage)
        expected_output = [
            {
                "reaction_type": "WOW",
                "reaction_count": 5
            },
            {
                "reaction_type": "HAHA",
                "reaction_count": 4
            }
        ]
        reaction_metrics_details_dto = [
            ReactionMetricDto(
                reaction_type=ReactionType.WOW.value,
                reaction_count=5),
            ReactionMetricDto(
                reaction_type=ReactionType.HAHA.value,
                reaction_count=4)
        ]
        storage.get_reaction_metrics_of_a_post_dto.return_value = \
            reaction_metrics_details_dto
        presenter.get_response_for_get_reaction_metrics_of_a_post.return_value \
            = expected_output

        actual_result = interactor.get_reaction_metrics_of_a_post_response(
            post_id=post_id,
            presenter=presenter
        )

        assert actual_result == expected_output
        storage.validate_post_id.assert_called_once_with(post_id=post_id)
        storage.get_reaction_metrics_of_a_post_dto.assert_called_once_with(
            post_id=post_id)
        presenter.get_response_for_get_reaction_metrics_of_a_post. \
            assert_called_once_with(reaction_metrics_details_dto=
                                    reaction_metrics_details_dto)
