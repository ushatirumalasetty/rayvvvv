"""
Created on 03/07/20

@author: revanth
"""
import abc
import dataclasses
from fb_post_clean_arch_v2.adapters.dtos import UserDTO
from fb_post_clean_arch_v2.interactors.storage_interfaces.dtos import *


@dataclasses.dataclass
class PostCompleteDetailsDto:
    post_dto: PostDto
    user_dtos: List[UserDTO]
    comments_dto: List[CommentDto]
    reactions_dto: List[ReactionDto]


class CreateReplyPresenterInterface(abc.ABC):

    @abc.abstractmethod
    def raise_exception_for_invalid_comment_id(self):
        pass



    @abc.abstractmethod
    def get_response(self, reply_id: int):
        pass


class GetPostPresenterInterface(abc.ABC):
    @abc.abstractmethod
    def raise_exception_for_invalid_post(self):
        pass

    @abc.abstractmethod
    def get_response_for_get_post_details(
            self, post_details_dto: PostCompleteDetailsDto):
        pass
