from unittest.mock import create_autospec

from fb_post_clean_arch.interactors. \
    get_posts_with_more_positive_reactions_interactor import \
    GetPostsWithMorePositiveReactionsInteractor
from fb_post_clean_arch.interactors.presenters.presenter_interface import \
    PresenterInterface
from fb_post_clean_arch.interactors.storages.storage_interface import \
    StorageInterface


class TestGetPostsWithMorePositiveReactionsInteractor:
    def test_returns_post_ids(self):
        expected_post_ids = [1, 2, 3]
        storage = create_autospec(StorageInterface)
        presenter = create_autospec(PresenterInterface)
        interactor = GetPostsWithMorePositiveReactionsInteractor(storage)
        storage.get_posts_with_more_positive_reactions. \
            return_value = expected_post_ids
        presenter.get_response_for_get_posts_with_more_positive_reaction. \
            return_value = expected_post_ids
    
        actual_posts_ids = interactor. \
            get_posts_with_more_positive_reactions_wrapper(presenter)
    
        assert expected_post_ids == actual_posts_ids
        presenter.get_response_for_get_posts_with_more_positive_reaction. \
            assert_called_once_with(post_ids=actual_posts_ids)
        storage.get_posts_with_more_positive_reactions. \
            assert_called_once()
