from fb_post_clean_arch_v2.interactors.presenter_interfaces.presenter_interface import \
    CreateReplyPresenterInterface
from fb_post_clean_arch_v2.interactors.storage_interfaces.\
    comment_storage_interface import CommentStorageInterface


class CommentInteractor:

    def __init__(self, storage: CommentStorageInterface):
        self.storage = storage

    def create_comment(self):
        pass

    def create_reply_for_comment_wrapper(self, user_id: int,
                                         comment_id: int, reply_text: str,
                                         presenter:
                                         CreateReplyPresenterInterface):

        from fb_post_clean_arch_v2.exceptions.custom_exceptions import \
            InvalidCommentId
        try:
            reply_id = self.create_reply_for_comment(comment_id=comment_id,
                                                     user_id=user_id,
                                                     reply_text=reply_text)

        except InvalidCommentId:
            return presenter.raise_exception_for_invalid_comment_id()

        return presenter.get_response(reply_id=reply_id)

    def create_reply_for_comment(self, comment_id: int, user_id: int,
                                 reply_text: str) -> int:

        self.storage.validate_comment_id(comment_id=comment_id)
        parent_comment_id = self.storage.get_parent_comment_id(
            comment_id=comment_id)
        if parent_comment_id is not None:
            comment_id = parent_comment_id

        reply_id = self.storage.create_comment_reply(
            comment_id=comment_id,
            user_id=user_id,
            reply_text=reply_text)

        return reply_id

    def react_to_comment(self):
        pass

    def get_comment_replies(self):
        pass
