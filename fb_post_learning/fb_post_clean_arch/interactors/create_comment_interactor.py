from fb_post_clean_arch.exceptions.custom_exceptions import InvalidPostId
from fb_post_clean_arch.interactors.presenters.presenter_interface import \
    PresenterInterface
from fb_post_clean_arch.interactors.storages.storage_interface import \
    StorageInterface


class CreateCommentInteractor:

    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def create_comment_wrapper(self, post_id: int,
                               comment_text: str,
                               user_id: int,
                               presenter: PresenterInterface):
        try:
            comment_id = self.create_comment(post_id=post_id,
                                             comment_text=comment_text,
                                             user_id=user_id)
        except InvalidPostId:
            presenter.raise_exception_for_invalid_post()
            return

        return presenter.get_create_comment_response(
            comment_id=comment_id)

    def create_comment(self, post_id: int,
                       comment_text: str,
                       user_id: int):
        self.storage.validate_post_id(post_id=post_id)
        comment_id = self.storage.create_comment(post_id=post_id,
                                                 comment_text=comment_text,
                                                 user_id=user_id)
        return comment_id
