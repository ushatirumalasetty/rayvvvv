import pytest
from django_swagger_utils.drf_server.exceptions import NotFound
from fb_post_clean_arch.interactors.react_to_comment_interactor import \
    ReactToCommentInteractor
from mock import create_autospec

from fb_post_clean_arch.exceptions.custom_exceptions import InvalidCommentId, \
    ReactionDoesNotExist
from fb_post_clean_arch.constants.enums import ReactionType
from fb_post_clean_arch.interactors.presenters.presenter_interface import \
    PresenterInterface
from fb_post_clean_arch.interactors.storages.storage_interface import \
    StorageInterface


class TestReactToCommentInteractor:
    def test_given_invalid_comment_id_raises_exception(self):
        comment_id = 1
        user_id = 1
        reaction_type = ReactionType.HAHA.value
        storage = create_autospec(StorageInterface)
        presenter = create_autospec(PresenterInterface)
        storage.validate_comment_id.side_effect = InvalidCommentId
        presenter.raise_exception_for_invalid_comment_id.side_effect = NotFound
        interactor = ReactToCommentInteractor()

        with pytest.raises(NotFound):
            interactor.create_comment_reaction_response(
                comment_id=comment_id,
                user_id=user_id,
                reaction_type=reaction_type,
                storage=storage,
                presenter=presenter
            )
        storage.validate_comment_id.assert_called_once_with(
            comment_id=comment_id)
        presenter.raise_exception_for_invalid_comment_id.assert_called_once()

    def test_given_valid_comment_create_reaction(self):
        comment_id = 1
        user_id = 1
        reaction_type = ReactionType.HAHA.value
        storage = create_autospec(StorageInterface)
        presenter = create_autospec(PresenterInterface)
        interactor = ReactToCommentInteractor()
        storage.validate_comment_reaction_if_exists_get_reaction_type. \
            side_effect = ReactionDoesNotExist

        interactor.create_comment_reaction_response(
            comment_id=comment_id,
            user_id=user_id,
            reaction_type=reaction_type,
            storage=storage,
            presenter=presenter
        )

        storage.validate_comment_id.assert_called_once_with(
            comment_id=comment_id)
        storage.validate_comment_reaction_if_exists_get_reaction_type. \
            assert_called_once_with(comment_id=comment_id,
                                    user_id=user_id
                                    )
        storage.create_comment_reaction.assert_called_once_with(
            comment_id=comment_id,
            user_id=user_id,
            reaction_type=reaction_type
        )

    def test_given_duplicate_reaction_results_undo_reaction(self):
        comment_id = 1
        user_id = 1
        reaction_type = ReactionType.HAHA.value
        storage = create_autospec(StorageInterface)
        presenter = create_autospec(PresenterInterface)
        interactor = ReactToCommentInteractor()
        storage.validate_comment_reaction_if_exists_get_reaction_type. \
            return_value = ReactionType.HAHA.value

        interactor.create_comment_reaction_response(
            comment_id=comment_id,
            user_id=user_id,
            reaction_type=reaction_type,
            storage=storage,
            presenter=presenter
        )

        storage.validate_comment_id.assert_called_once_with(
            comment_id=comment_id)
        storage.validate_comment_reaction_if_exists_get_reaction_type. \
            assert_called_once_with(comment_id=comment_id,
                                    user_id=user_id
                                    )
        storage.undo_comment_reaction.assert_called_once_with(
            user_id=user_id,
            comment_id=comment_id
        )

    def test_given_duplicate_reaction_results_update_reaction(self):
        comment_id = 1
        user_id = 1
        reaction_type = ReactionType.HAHA.value
        storage = create_autospec(StorageInterface)
        presenter = create_autospec(PresenterInterface)
        interactor = ReactToCommentInteractor()
        storage.validate_comment_reaction_if_exists_get_reaction_type. \
            return_value = ReactionType.WOW.value

        interactor.create_comment_reaction_response(
            comment_id=comment_id,
            user_id=user_id,
            reaction_type=reaction_type,
            storage=storage,
            presenter=presenter
        )

        storage.validate_comment_id.assert_called_once_with(
            comment_id=comment_id)
        storage.validate_comment_reaction_if_exists_get_reaction_type. \
            assert_called_once_with(comment_id=comment_id,
                                    user_id=user_id
                                    )
        storage.update_comment_reaction.assert_called_once_with(
            user_id=user_id,
            comment_id=comment_id,
            reaction_type=reaction_type
        )
