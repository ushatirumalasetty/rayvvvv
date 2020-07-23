from typing import List

from fb_post_auth.dtos.fb_post import UserDTO
from fb_post_auth.interactors.storages.storage_interface import \
    StorageInterface


class GetUserDetailsInteractor:

    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def get_user_details_dtos(self, user_ids: List[int]) -> List[UserDTO]:
        user_dtos = self.storage.get_user_details_dtos(user_ids=user_ids)
        return user_dtos
