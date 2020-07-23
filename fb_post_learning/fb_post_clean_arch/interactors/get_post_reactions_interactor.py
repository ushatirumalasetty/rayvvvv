from fb_post_clean_arch.adapters.service_adapter import get_service_adapter
from fb_post_clean_arch.exceptions.custom_exceptions import InvalidPostId
from fb_post_clean_arch.interactors.presenters.presenter_interface import \
    PresenterInterface
from fb_post_clean_arch.interactors.storages.storage_interface import \
    StorageInterface, PostReactionCompleteDetailsDto


class GetPostReactionsInteractor:

    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def get_post_reactions_wrapper(self,
                                   post_id: int,
                                   presenter: PresenterInterface):
        try:
            post_reaction_complete_details_dtos = self.get_post_reactions(
                post_id=post_id)
        except InvalidPostId:
            return presenter.raise_exception_for_invalid_post()

        return presenter.get_response_for_get_post_reactions(
            post_reaction_dtos=post_reaction_complete_details_dtos)

    def get_post_reactions(self, post_id: int):
        self.storage.validate_post_id(post_id=post_id)
        post_reaction_dtos = self.storage.get_post_reaction_dtos(
            post_id=post_id)
        user_ids = post_reaction_dtos.user_ids
        service_adapter = get_service_adapter()
        user_dtos = service_adapter.auth_service.get_user_dtos(
            user_ids=user_ids
        )

        post_reaction_complete_details_dtos = PostReactionCompleteDetailsDto(
            reaction_dtos=post_reaction_dtos.reaction_dtos,
            user_dtos=user_dtos)
        return post_reaction_complete_details_dtos
