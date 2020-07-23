from abc import abstractmethod
from typing import List

from fb_post_clean_arch.interactors.storages.storage_interface import \
    PostReactionDto, PostDetailsDto, PostCompleteDetailsDto, \
    PostReactionCompleteDetailsDto


class PresenterInterface:

    @abstractmethod
    def raise_exception_for_invalid_post(self):
        pass

    @abstractmethod
    def get_response_for_get_post_reactions(
            self,
            post_reaction_dtos: PostReactionCompleteDetailsDto):
        pass

    @abstractmethod
    def get_response_for_get_posts_with_more_positive_reaction(
            self,
            post_ids: List[int]):
        pass

    @abstractmethod
    def get_response_for_get_total_reactions_count(self, reactions_count: int):
        pass

    @abstractmethod
    def get_response_for_get_post_details(
            self,
            get_post_dto: PostCompleteDetailsDto):
        pass

    @abstractmethod
    def get_create_comment_response(self, comment_id: int):
        pass

    @abstractmethod
    def get_create_post_response(self, post_id: int):
        pass
