from fb_post_clean_arch_v2.constants.enums import ReactionType
from fb_post_clean_arch_v2.interactors.mixins.validation_mixin import \
    ValidationMixin
from fb_post_clean_arch_v2.interactors.presenter_interfaces. \
    presenter_interface import GetPostPresenterInterface, \
    PostCompleteDetailsDto 
from fb_post_clean_arch_v2.interactors.storage_interfaces. \
    post_storage_interface import PostStorageInterface


class PostInteractor(ValidationMixin):
    def __init__(self, storage: PostStorageInterface):
        self.storage = storage

    def create_post(self, user_id: int, content: str):
        pass

    def delete_post(self, user_id: int, post_id: int):
        pass

    def get_post_wrapper(self, post_id: int,
                         presenter: GetPostPresenterInterface):
        from fb_post_clean_arch_v2.exceptions.custom_exceptions import \
            InvalidPostId
        try:
            post_complete_details_dto = self.get_post(post_id=post_id)
        except InvalidPostId:
            return presenter.raise_exception_for_invalid_post()

        post_details_dict = presenter.get_response_for_get_post_details(
            post_details_dto=post_complete_details_dto)
        return post_details_dict

    def get_post(self, post_id: int) -> PostCompleteDetailsDto:
        from fb_post_clean_arch_v2.adapters.service_adapter import \
            get_service_adapter
        self.validate_post_id(post_id=post_id)
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
            comments_dto=post_details_dto.comments_dto
        )
        return post_complete_details_dto

    def react_to_post(
            self, user_id: int, post_id: int, reaction_type: ReactionType):
        pass
