"""
Created on 03/07/20

@author: revanth
"""
import abc

from fb_post_clean_arch_v2.interactors.storage_interfaces.dtos import \
    PostDetailsDto


class PostStorageInterface(abc.ABC):

    @abc.abstractmethod
    def get_post_details_dto(self, post_id: int) -> PostDetailsDto:
        pass

    @abc.abstractmethod
    def validate_post_id(self, post_id: int):
        pass
