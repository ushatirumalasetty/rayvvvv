from typing import List

from fb_post_auth.dtos.fb_post import UserDTO
from fb_post_auth.interactors.storages.storage_interface import \
    StorageInterface
from fb_post_auth.models import User


class StorageImplementation(StorageInterface):

    def get_user_details_dtos(self, user_ids: List[int]) -> List[UserDTO]:
        users = User.objects.filter(id__in=user_ids)
        user_dtos = []
        for user in users:
            user_dto = self._convert_user_object_to_dto(user=user)
            user_dtos.append(user_dto)
        return user_dtos

    @staticmethod
    def _convert_user_object_to_dto(user):
        return UserDTO(user_id=user.id,
                       name=user.name,
                       profile_pic_url=user.profile_pic_url)
