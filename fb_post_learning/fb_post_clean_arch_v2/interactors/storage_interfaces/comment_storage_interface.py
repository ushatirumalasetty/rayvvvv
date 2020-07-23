"""
Created on 03/07/20

@author: revanth
"""
import abc


class CommentStorageInterface(abc.ABC):
    from typing import Optional

    @abc.abstractmethod
    def validate_comment_id(self, comment_id: int) -> bool:
        pass

    @abc.abstractmethod
    def get_parent_comment_id(self, comment_id: int) -> Optional[int]:
        pass

    @abc.abstractmethod
    def create_comment_reply(self, comment_id: int,
                             user_id: int,
                             reply_text: str) -> int:
        pass
