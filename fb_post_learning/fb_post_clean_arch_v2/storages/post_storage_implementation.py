from django.db.models import Prefetch

from fb_post_clean_arch_v2.interactors.storage_interfaces.dtos import \
    PostDetailsDto
from fb_post_clean_arch_v2.interactors.storage_interfaces.\
    post_storage_interface import PostStorageInterface
from fb_post_clean_arch_v2.models import Post, Reaction, Comment


class PostStorageImplementation(PostStorageInterface):

    def validate_post_id(self, post_id: int):
        from fb_post_clean_arch_v2.exceptions.custom_exceptions import \
            InvalidPostId
        is_valid_post_id = Post.objects.filter(id=post_id).exists()
        is_invalid_post_id = not is_valid_post_id
        if is_invalid_post_id:
            raise InvalidPostId

    def get_post_details_dto(self, post_id: int) -> PostDetailsDto:
        prefetch_reactions = Prefetch('reactions',
                                      queryset=Reaction.objects.filter(
                                          post_id=post_id))
        prefetch_comments = Prefetch(
            'comments',
            queryset=Comment.objects.prefetch_related(
                Prefetch('reactions')
            ).prefetch_related('parent_comment__reactions')
        )

        post = Post.objects.prefetch_related(
            prefetch_reactions, prefetch_comments).get(id=post_id)

        post_details_dto_obj = self._get_post_details_dto_obj(post)

        return post_details_dto_obj

    def _get_post_details_dto_obj(self, post):
        user_ids = []
        post_dto = self._convert_post_obj_to_dto(post)
        post_reaction_dtos = self._get_post_reactions(post)
        user_ids.append(post.user_id)

        comments = post.comments.all()
        users_dto_dict, comment_dtos, comment_reaction_dtos = \
            self._get_comments_details(comments=comments, user_ids=user_ids)

        reply_dtos, reply_reaction_dtos, user_ids = self._get_replies_details(
            comments=comments, user_ids=user_ids)

        comment_reaction_dtos = comment_reaction_dtos + reply_reaction_dtos
        comment_dtos = comment_dtos + reply_dtos
        reaction_dtos = post_reaction_dtos + comment_reaction_dtos

        post_details_dto = PostDetailsDto(post_dto=post_dto,
                                          reactions_dto=reaction_dtos,
                                          comments_dto=comment_dtos,
                                          user_ids=user_ids)
        return post_details_dto

    @staticmethod
    def _convert_post_obj_to_dto(post):
        from fb_post_clean_arch_v2.interactors.storage_interfaces.dtos import \
            PostDto
        post_dto = PostDto(user_id=post.user_id,
                           post_content=post.post_content,
                           pub_date_time=post.pub_date_time.replace(
                               tzinfo=None),
                           post_id=post.id)
        return post_dto

    def _get_post_reactions(self, post):
        post_reaction_dtos = []
        post_reactions = post.reactions.all()
        for reaction in post_reactions:
            post_reaction_dto = self._convert_reaction_object_to_dto(
                reaction)
            post_reaction_dtos.append(post_reaction_dto)
        return post_reaction_dtos

    def _convert_reaction_objects_to_dtos(self, replies):
        reactions_dto = []
        for reply in replies:
            reaction_dto = self._convert_reaction_object_to_dto(reply)
            reactions_dto.append(reaction_dto)
        return reactions_dto

    def _get_comment_details(self, comment, user_ids):
        comments_dto = []
        comment_dto = self._convert_comment_obj_to_dto(comment)
        comments_dto.append(comment_dto)

        if comment.user_id not in user_ids:
            user_ids.append(comment.user_id)

        comment_reactions = comment.reactions.all()
        comment_reactions_dto = self._convert_reaction_objects_to_dtos(
            comment_reactions)

        return user_ids, comments_dto, comment_reactions_dto

    def _get_comments_details(self, comments, user_ids):
        comments_dto = []
        comments_reactions_dto = []

        for comment in comments:
            user_ids, comment_dto, comment_reaction_dto = \
                self._get_comment_details(comment, user_ids)
            comments_dto += comment_dto
            comments_reactions_dto += comment_reaction_dto

        return user_ids, comments_dto, comments_reactions_dto

    def _get_replies_details(self, comments, user_ids):
        reply_dtos = []
        reply_reaction_dtos = []

        for comment in comments:
            comment_dto, comment_reaction_dto, user_ids = self \
                ._get_reply_details(comment, user_ids=user_ids)
            reply_dtos += comment_dto
            reply_reaction_dtos += comment_reaction_dto

        return reply_dtos, reply_reaction_dtos, user_ids

    def _get_reply_dtos(self, replies):
        comments_dto = []
        for reply in replies:
            comment_dto = self._convert_comment_obj_to_dto(reply)
            comments_dto.append(comment_dto)
        return comments_dto

    def _get_reply_reaction_dtos(self, replies):
        reply_reaction_dtos = []
        for reply in replies:
            reply_reactions = reply.reactions.all()
            reactions_dto = self._convert_reaction_objects_to_dtos(
                reply_reactions)
            reply_reaction_dtos += reactions_dto
        return reply_reaction_dtos

    def _get_reply_details(self, comment, user_ids):
        reply_dtos = []
        reply_reaction_dtos = []
        replies = comment.replies.all()
        reply_dtos += self._get_reply_dtos(replies)

        for reply in replies:
            user_id = reply.user_id
            if user_id not in user_ids:
                user_ids.append(reply.user_id)

        reply_reaction_dtos += self._get_reply_reaction_dtos(replies)
        return reply_dtos, reply_reaction_dtos, user_ids

    @staticmethod
    def _convert_reaction_object_to_dto(reaction):
        from fb_post_clean_arch_v2.interactors.storage_interfaces.dtos import \
            ReactionDto
        reaction_dto = ReactionDto(
            reaction_id=reaction.id,
            user_id=reaction.user_id,
            comment_id=reaction.comment_id,
            post_id=reaction.post_id,
            reaction_type=reaction.reaction_type)
        return reaction_dto

    @staticmethod
    def _convert_comment_obj_to_dto(comment):
        from fb_post_clean_arch_v2.interactors.storage_interfaces.dtos import \
            CommentDto
        comment_dto = CommentDto(
            comment_id=comment.id,
            user_id=comment.user_id,
            post_id=comment.post_id,
            comment_content=comment.comment_text,
            pub_date_time=comment.pub_date_time.replace(tzinfo=None),
            parent_comment=comment.parent_comment_id)
        return comment_dto
