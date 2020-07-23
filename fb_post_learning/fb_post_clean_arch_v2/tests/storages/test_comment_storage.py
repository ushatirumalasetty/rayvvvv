import pytest
from freezegun import freeze_time

from fb_post_clean_arch_v2.storages.comment_storage_implementation import \
    CommentStorageImplementation


class TestStorage:
    
    @pytest.mark.django_db
    def test_validate_comment_id_given_invalid_comment_id_raises_exception(
            self):
        comment_id = 10

        storage = CommentStorageImplementation()

        from fb_post_clean_arch_v2.exceptions.custom_exceptions import \
            InvalidCommentId
        with pytest.raises(InvalidCommentId):
            storage.validate_comment_id(
                comment_id=comment_id)

    @pytest.mark.django_db
    @freeze_time("2020-01-1 05:21:34")
    def test_get_parent_comment_id_given_comment_id(self):
        from fb_post_clean_arch_v2.tests.factories.models import ReplyFactory
        from fb_post_clean_arch_v2.tests.factories.models import CommentFactory
        comment = CommentFactory(parent_comment=None)
        reply = ReplyFactory(parent_comment=comment)
        reply_id = reply.id
        expected_parent_comment_id = comment.id

        storage = CommentStorageImplementation()

        actual_parent_comment_id = storage.get_parent_comment_id(
            comment_id=reply_id)

        assert actual_parent_comment_id == expected_parent_comment_id

    @pytest.mark.django_db
    @freeze_time("2020-01-1 05:21:34")
    def test_create_comment_reply_given_valid_details(self):
        user_id = 1
        reply_text = "Nice Post"
        from fb_post_clean_arch_v2.tests.factories.models import CommentFactory
        comment = CommentFactory(parent_comment=None)
        comment_id = comment.id

        storage = CommentStorageImplementation()
        storage.create_comment_reply(comment_id=comment_id,
                                     user_id=user_id,
                                     reply_text=reply_text)

        from fb_post_clean_arch_v2.models import Comment
        reply = Comment.objects.get(parent_comment_id=comment_id,
                                    user_id=user_id)
        assert reply.parent_comment.id == comment_id
        assert reply.user_id == user_id
        assert reply.comment_text == reply_text
