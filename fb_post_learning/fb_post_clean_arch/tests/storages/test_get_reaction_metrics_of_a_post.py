import pytest

from fb_post_clean_arch.constants.enums import ReactionType
from fb_post_clean_arch.storages.storage_implementation import StorageImplementation


@pytest.mark.django_db
def test_reaction_metrics_of_a_post_given_post_id_returns_reaction_metrics():
    post_id = 1
    expected_reaction_metrics_dto = [ReactionMetricsDetailsDto(
                reaction_type=ReactionType.WOW.value,
                reaction_count=3)]
    sql_storage = StorageImplementation()

    reaction_metrics_dto = sql_storage.get_reaction_metrics_of_a_post_dto(
        post_id=post_id)

    assert reaction_metrics_dto.reaction_metrics_details_dto == \
           expected_reaction_metrics_dto
