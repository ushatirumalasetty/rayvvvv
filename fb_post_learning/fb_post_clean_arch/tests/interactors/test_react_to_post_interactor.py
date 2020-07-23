import pytest
from django_swagger_utils.drf_server.exceptions import NotFound
from mock import create_autospec

from fb_post_clean_arch.exceptions.custom_exceptions import InvalidPostId, \
    ReactionDoesNotExist
from fb_post_clean_arch.constants.enums import ReactionType
from fb_post_clean_arch.interactors.presenters.presenter_interface import \
    PresenterInterface
from fb_post_clean_arch.interactors.react_to_post_interactor import \
    ReactToPostInteractor
from fb_post_clean_arch.interactors.storages.storage_interface import \
    StorageInterface


class TestReactToPostInteractor:
    def test_given_invalid_post_id_raises_exception(self):
        user_id = 1
        post_id = 1
        reaction_type = ReactionType.HAHA.value
        storage = create_autospec(StorageInterface)
        interactor = ReactToPostInteractor(storage)
        presenter = create_autospec(PresenterInterface)
        storage.validate_post_id.side_effect = InvalidPostId
        presenter.raise_exception_for_invalid_post.side_effect = NotFound
        with pytest.raises(NotFound):
            interactor.react_to_post_wrapper(
                user_id=user_id,
                post_id=post_id,
                reaction_type=reaction_type,
                presenter=presenter
            )
        storage.validate_post_id.assert_called_once_with(post_id=post_id)
        presenter.raise_exception_for_invalid_post.assert_called_once()

    def test_given_valid_post_creates_reaction(self):
        user_id = 1
        post_id = 1
        reaction_type = ReactionType.HAHA.value
        storage = create_autospec(StorageInterface)
        interactor = ReactToPostInteractor(storage)
        presenter = create_autospec(PresenterInterface)
        storage.validate_post_reaction_if_exists_get_reaction_type.side_effect \
            = ReactionDoesNotExist
        interactor.react_to_post_wrapper(
            user_id=user_id,
            post_id=post_id,
            reaction_type=reaction_type,
            presenter=presenter)

        storage.validate_post_reaction_if_exists_get_reaction_type.assert_called_once_with(
            user_id=user_id, post_id=post_id
        )
        storage.validate_post_id.assert_called_once_with(post_id=post_id)
        storage.create_post_reaction.assert_called_once_with(
            post_id=post_id,
            user_id=user_id,
            reaction_type=reaction_type)

    def test_given_same_reaction_results_undo_reaction(self):
        user_id = 1
        post_id = 1
        reaction_type = ReactionType.HAHA.value
        storage = create_autospec(StorageInterface)
        interactor = ReactToPostInteractor(storage)
        presenter = create_autospec(PresenterInterface)
        storage.validate_post_reaction_if_exists_get_reaction_type. \
            return_value = "HAHA"

        interactor.react_to_post_wrapper(
            user_id=user_id,
            post_id=post_id,
            reaction_type=reaction_type,
            presenter=presenter)

        storage.validate_post_id.assert_called_once_with(post_id=post_id)
        storage.validate_post_reaction_if_exists_get_reaction_type.\
            assert_called_once_with(user_id=user_id, 
                                    post_id=post_id)
        storage.undo_post_reaction.assert_called_once_with(
            user_id=user_id,
            post_id=post_id)

    def test_given_different_reaction_results_update_reaction(self):
        user_id = 1
        post_id = 1
        reaction_type = ReactionType.HAHA.value
        storage = create_autospec(StorageInterface)
        interactor = ReactToPostInteractor(storage)
        presenter = create_autospec(PresenterInterface)
        storage.validate_post_reaction_if_exists_get_reaction_type.\
            return_value = "WOW"

        interactor.react_to_post_wrapper(
            user_id=user_id,
            post_id=post_id,
            reaction_type=reaction_type,
            presenter=presenter)

        storage.validate_post_id.assert_called_once_with(post_id=post_id)
        storage.validate_post_reaction_if_exists_get_reaction_type.\
            assert_called_once_with(user_id=user_id, 
                                    post_id=post_id)
        storage.update_post_reaction.assert_called_once_with(
            user_id=user_id,
            post_id=post_id,
            reaction_type=reaction_type)
