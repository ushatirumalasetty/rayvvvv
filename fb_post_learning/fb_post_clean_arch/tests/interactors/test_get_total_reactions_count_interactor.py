from fb_post_clean_arch.interactors.get_total_reactions_count_interactor import \
    GetTotalReactionsCountInteractor
from mock import create_autospec

from fb_post_clean_arch.interactors.presenters.presenter_interface import \
    PresenterInterface
from fb_post_clean_arch.interactors.storages.storage_interface import \
    StorageInterface


def test_get_total_reactions_count_interactor_returns_reactions_count():
    presenter = create_autospec(PresenterInterface)
    storage = create_autospec(StorageInterface)
    interactor = GetTotalReactionsCountInteractor(storage=storage)
    reactions_count = 6
    expected_total_reactions_count = {
        "reactions_count": reactions_count
    }
    storage.get_total_reactions_count.return_value = reactions_count
    presenter.get_total_reactions_count_response.return_value = \
        expected_total_reactions_count
    actual_total_reactions_count = interactor. \
        get_response_for_total_reaction_count(presenter=presenter)

    assert expected_total_reactions_count == actual_total_reactions_count
    storage.get_total_reactions_count.assert_called_once()
    presenter.get_total_reactions_count_response.\
        assert_called_once_with(reactions_count=reactions_count)
