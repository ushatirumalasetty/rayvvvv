"""
Created on 03/07/20

@author: revanth
"""
import datetime

from fb_post_clean_arch_v2.constants.enums import ReactionType
from typing import Optional, List
from dataclasses import dataclass


@dataclass
class PostDto:
    user_id: int
    post_content: str
    post_id: int
    pub_date_time: datetime


@dataclass
class CommentDto:
    from datetime import datetime
    comment_id: int
    user_id: int
    post_id: Optional[int]
    comment_content: str
    pub_date_time: datetime
    parent_comment: Optional


@dataclass
class ReactionDto:
    reaction_id: int
    comment_id: Optional[int]
    post_id: Optional[int]
    user_id: int
    reaction_type: ReactionType


@dataclass
class PostDetailsDto:
    post_dto: PostDto
    user_ids: List[int]
    comments_dto: List[CommentDto]
    reactions_dto: List[ReactionDto]
