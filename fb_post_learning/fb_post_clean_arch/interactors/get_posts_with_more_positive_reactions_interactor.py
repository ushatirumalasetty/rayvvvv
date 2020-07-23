from fb_post_clean_arch.interactors.presenters.presenter_interface import \
    PresenterInterface
from fb_post_clean_arch.interactors.storages.storage_interface import \
    StorageInterface


class GetPostsWithMorePositiveReactionsInteractor:

    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def get_posts_with_more_positive_reactions_wrapper(
            self,
            presenter: PresenterInterface):

        post_ids = self.storage.get_posts_with_more_positive_reactions()
        return presenter.get_response_for_get_posts_with_more_positive_reaction(
            post_ids=post_ids)
