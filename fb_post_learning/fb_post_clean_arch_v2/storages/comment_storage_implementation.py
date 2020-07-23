from fb_post_clean_arch_v2.interactors.storage_interfaces. \
    comment_storage_interface import CommentStorageInterface
from fb_post_clean_arch_v2.models import Comment


class CommentStorageImplementation(CommentStorageInterface):
    from typing import Optional

    def get_parent_comment_id(self, comment_id: int) -> Optional[int]:
        comment = Comment.objects.get(id=comment_id)
        parent_comment_id = comment.parent_comment_id
        return parent_comment_id

    def create_comment_reply(self, comment_id: int,
                             user_id: int,
                             reply_text: str) -> int:
        comment = Comment.objects.create(user_id=user_id,
                                         comment_text=reply_text,
                                         parent_comment_id=comment_id)
        return comment.id

    def validate_comment_id(self, comment_id: int):
        try:
            Comment.objects.get(id=comment_id)
        except Comment.DoesNotExist:
            from fb_post_clean_arch_v2.exceptions.custom_exceptions import \
                InvalidCommentId
            raise InvalidCommentId
