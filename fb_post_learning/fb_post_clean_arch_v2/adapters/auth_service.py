import dataclasses
from typing import List

from fb_post_clean_arch_v2.adapters.dtos import UserDTO


class AuthService:
    @property
    def interface(self):
        from fb_post_auth.interfaces.service_interface import ServiceInterface
        return ServiceInterface()

    def get_user_dtos(self, user_ids: List[int]) -> List[UserDTO]:
        user_dtos = self.interface.get_user_dtos(user_ids=user_ids)

        return [
            UserDTO(**dataclasses.asdict(user_dto)) for user_dto in user_dtos
        ]
