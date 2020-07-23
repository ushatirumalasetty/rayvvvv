from fb_post_clean_arch.adapters.service_adapter import get_service_adapter
from fb_post_clean_arch.exceptions.custom_exceptions import InvalidPostId
from fb_post_clean_arch.interactors.presenters.presenter_interface import \
    PresenterInterface
from fb_post_clean_arch.interactors.storages.storage_interface import \
    StorageInterface, PostCompleteDetailsDto


class GetPostInteractor:

    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def get_post_wrapper(self,
                         post_id: int,
                         presenter: PresenterInterface):
        try:
            post_complete_details_dto = self.get_post(post_id=post_id)
        except InvalidPostId:
            return presenter.raise_exception_for_invalid_post()

        post_details_dict = presenter.get_response_for_get_post_details(
            get_post_dto=post_complete_details_dto)
        return post_details_dict

    def get_post(self, post_id: int):
        self.storage.validate_post_id(post_id=post_id)
        post_details_dto = self.storage.get_post_details_dto(post_id=post_id)

        user_ids = post_details_dto.user_ids
        service_adapter = get_service_adapter()
        user_dtos = service_adapter.auth_service.get_user_dtos(
            user_ids=user_ids
        )

        post_complete_details_dto = PostCompleteDetailsDto(
            user_dtos=user_dtos,
            post_dto=post_details_dto.post_dto,
            reactions_dto=post_details_dto.reactions_dto,
            comments_dto=post_details_dto.comments_dto)

        return post_complete_details_dto
