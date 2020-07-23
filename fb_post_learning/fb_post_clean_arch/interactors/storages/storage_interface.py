from datetime import datetime
from abc import abstractmethod
from dataclasses import dataclass
from typing import Optional, List

from fb_post_clean_arch.constants.enums import ReactionType


@dataclass()
class UserDto:
    user_id: int
    name: str
    profile_pic_url: str


@dataclass()
class ReactionDto:
    reaction_id: int
    comment_id: Optional[int]
    post_id: Optional[int]
    user_id: int
    reaction_type: ReactionType


@dataclass()
class PostReactionDto:
    user_ids: List[int]
    reaction_dtos: List[ReactionDto]


@dataclass()
class PostReactionCompleteDetailsDto:
    user_dtos: List[UserDto]
    reaction_dtos: List[ReactionDto]


@dataclass()
class CommentDto:
    comment_id: int
    user_id: int
    post_id: Optional[int]
    comment_content: str
    pub_date_time: datetime
    parent_comment: Optional


@dataclass()
class CommentRepliesDto:
    users_dto: List[UserDto]
    comments_dto: List[CommentDto]


@dataclass()
class PostDto:
    user_id: int
    post_content: str
    post_id: int
    pub_date_time: datetime


@dataclass()
class PostDetailsDto:
    post_dto: PostDto
    user_ids: List[int]
    comments_dto: List[CommentDto]
    reactions_dto: List[ReactionDto]


@dataclass
class PostCompleteDetailsDto:
    post_dto: PostDto
    user_dtos: List[UserDto]
    comments_dto: List[CommentDto]
    reactions_dto: List[ReactionDto]


class StorageInterface:

    @abstractmethod
    def create_post(self, user_id: int,
                    post_content: str) -> int:
        pass

    @abstractmethod
    def validate_post_id(self, post_id: int):
        pass

    @abstractmethod
    def get_posts_with_more_positive_reactions(self) -> List[int]:
        pass

    @abstractmethod
    def validate_post_reaction_if_exists_get_reaction_type(
            self,
            user_id: int,
            post_id: int) -> Optional[ReactionType]:
        pass

    @abstractmethod
    def undo_post_reaction(self,
                           user_id: int,
                           post_id: int):
        pass

    @abstractmethod
    def update_post_reaction(self,
                             user_id: int,
                             post_id: int,
                             reaction_type: ReactionType):
        pass

    @abstractmethod
    def get_post_details_dto(self, post_id: int) -> PostDetailsDto:
        pass

    @abstractmethod
    def create_post_reaction(self,
                             user_id: int,
                             post_id: int,
                             reaction_type: ReactionType):
        pass

    @abstractmethod
    def create_comment(self, post_id: int,
                       comment_text: str,
                       user_id: int) -> int:
        pass

    @abstractmethod
    def get_post_reaction_dtos(self, post_id: int) -> \
            PostReactionDto:
        pass
