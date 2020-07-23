from typing import List

from fb_post_auth.dtos.fb_post import UserDTO


class ServiceInterface:

    @staticmethod
    def get_user_dtos(user_ids: List[int]) -> List[UserDTO]:
        from fb_post_auth.storages.storage_implementation import \
            StorageImplementation
        storage = StorageImplementation()

        from fb_post_auth.interactors.get_user_details_interactor import \
            GetUserDetailsInteractor
        interactor = GetUserDetailsInteractor(storage=storage)

        user_dtos = interactor.get_user_details_dtos(user_ids=user_ids)
        return user_dtos
