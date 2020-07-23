import pytest
from freezegun import freeze_time

from fb_post_clean_arch_v2.storages.post_storage_implementation import \
    PostStorageImplementation


class TestStorage:
    @pytest.mark.django_db
    def test_validate_post_id_given_invalid_post_id_raises_exception(self):
        from fb_post_clean_arch_v2.exceptions.custom_exceptions import \
            InvalidPostId
        post_id = 2
        storage = PostStorageImplementation()

        with pytest.raises(InvalidPostId):
            storage.validate_post_id(post_id=post_id)

    @freeze_time("2020-01-1 05:21:34")
    @pytest.mark.django_db
    def test_get_post_details_dto_given_post_id(self):
        from fb_post_clean_arch_v2.tests.factories.models import PostFactory, \
            CommentFactory, ReactionFactory
        from fb_post_clean_arch_v2.tests.factories.storage_dtos import \
            PostDtoFactory, CommentDtoFactory, ReactionDtoFactory

        PostFactory.create_batch(2)
        comment = CommentFactory(parent_comment=None, post_id=1)
        CommentFactory(post_id=None, user_id=1, parent_comment=comment)
        ReactionFactory(comment=None, post_id=1)
        post_id = 1
        post_dtos = PostDtoFactory()
        user_ids = [1]
        comment_dtos = [
            CommentDtoFactory(post_id=1, parent_comment=None,
                              user_id=1),
            CommentDtoFactory(post_id=None,
                              parent_comment=comment.id, user_id=1)]

        reaction_dtos = [ReactionDtoFactory(comment_id=None)]

        storage = PostStorageImplementation()
        post_details_dtos = storage.get_post_details_dto(post_id=post_id)
        assert post_dtos == post_details_dtos.post_dto
        assert user_ids == post_details_dtos.user_ids
        assert comment_dtos == post_details_dtos.comments_dto
        assert reaction_dtos == post_details_dtos.reactions_dto
