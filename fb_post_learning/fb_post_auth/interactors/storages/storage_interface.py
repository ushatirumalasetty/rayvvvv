from abc import abstractmethod
from typing import List

from fb_post_auth.dtos.fb_post import UserDTO


class StorageInterface:

    @abstractmethod
    def get_user_details_dtos(self, user_ids: List[int]) -> List[UserDTO]:
        pass
