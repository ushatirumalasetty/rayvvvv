"""
Created on 27/06/20

@author: revanth
"""
from enum import Enum

from ib_common.constants import BaseEnumClass


class ReactionType(BaseEnumClass, Enum):
    LIKE = "LIKE"
    WOW = "WOW"
    HAHA = "HAHA"
    DISLIKE = "DISLIKE"
    SAD = "SAD"
    ANGRY = "ANGRY"
