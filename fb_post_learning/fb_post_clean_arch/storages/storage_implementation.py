from typing import Optional, List

from django.db.models import Count, Q, F, Prefetch

from fb_post_clean_arch.exceptions.custom_exceptions import InvalidPostId, \
    ReactionDoesNotExist
from fb_post_clean_arch.constants.enums import ReactionType
from fb_post_clean_arch.interactors.storages.storage_interface import \
    StorageInterface, CommentDto, PostReactionDto, \
    ReactionDto, \
    PostDetailsDto, PostDto
from fb_post_clean_arch.models import Post, Comment, Reactions


class StorageImplementation(StorageInterface):

    def create_comment(self, post_id: int,
                       comment_text: str,
                       user_id: int) -> int:

        comment = Comment.objects.create(post_id=post_id,
                                         comment_text=comment_text,
                                         user_id=user_id)
        comment_id = comment.id
        return comment_id

    def validate_post_id(self, post_id: int):
        is_valid_post_id = Post.objects.filter(id=post_id).exists()
        is_invalid_post_id = not is_valid_post_id
        if is_invalid_post_id:
            raise InvalidPostId

    def create_post(self, user_id: int,
                    post_content: str) -> int:

        post = Post.objects.create(user_id=user_id,
                                   post_content=post_content)
        post_id = post.id
        return post_id

    def get_post_reaction_dtos(self, post_id: int) -> \
            PostReactionDto:
        reactions = Reactions.objects.filter(post_id=post_id)
        user_ids = []
        reaction_dtos = []
        for reaction in reactions:
            if reaction.user_id not in user_ids:
                user_ids.append(reaction.user_id)
            reaction_dto = self._convert_post_reaction_object_to_dto(reaction)
            reaction_dtos.append(reaction_dto)

        return PostReactionDto(
            user_ids=user_ids,
            reaction_dtos=reaction_dtos)

    def get_posts_with_more_positive_reactions(self) -> List[int]:
        positive_reactions = [ReactionType.LIKE.value, ReactionType.WOW.value,
                              ReactionType.HAHA.value]
        negative_reactions = [ReactionType.DISLIKE.value,
                              ReactionType.SAD.value,
                              ReactionType.ANGRY.value]

        positive_reactions_count = Count('reactions', filter=Q(
            reactions__reaction_type__in=positive_reactions))
        negative_reactions_count = Count('reactions', filter=Q(
            reactions__reaction_type__in=negative_reactions))

        post = Post.objects.annotate(
            positive_reactions_count=positive_reactions_count). \
            annotate(negative_reactions_count=negative_reactions_count)

        posts = post.filter(
            positive_reactions_count__gt=F('negative_reactions_count'))

        post_ids_query_set = posts.values_list('id', flat=True)
        post_ids = []
        for post_id in post_ids_query_set:
            post_ids.append(post_id)
        return post_ids

    def validate_post_reaction_if_exists_get_reaction_type(
            self,
            user_id: int,
            post_id: int) -> Optional[ReactionType]:

        try:
            reaction = Reactions.objects.get(user_id=user_id,
                                             post_id=post_id)
            return reaction.reaction_type
        except Reactions.DoesNotExist:
            raise ReactionDoesNotExist

    def undo_post_reaction(self,
                           user_id: int,
                           post_id: int):

        Reactions.objects.get(user_id=user_id,
                              post_id=post_id).delete()

    def update_post_reaction(self,
                             user_id: int,
                             post_id: int,
                             reaction_type: ReactionType):

        Reactions.objects.filter(user_id=user_id,
                                 post_id=post_id).update(
            reaction_type=reaction_type)

    def create_post_reaction(self,
                             user_id: int,
                             post_id: int,
                             reaction_type: ReactionType):

        Reactions.objects.create(user_id=user_id,
                                 post_id=post_id,
                                 reaction_type=reaction_type)

    def get_post_details_dto(self, post_id: int) -> PostDetailsDto:
        prefetch_reactions = Prefetch('reactions',
                                      queryset=Reactions.objects.filter(
                                          post_id=post_id))
        prefetch_comments = Prefetch(
            'comments', queryset=Comment.objects.
                prefetch_related(Prefetch('reactions')).
                prefetch_related('parent_comment__reactions')
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

        comment_reaction_dtos = self._merge_comment_reactions_and_reply_reaction(
            comment_reaction_dtos, reply_reaction_dtos)
        comment_dtos = self._merge_comment_dtos_and_reply_dtos(
            comment_dtos, reply_dtos)

        reaction_dtos = self._merge_post_reaction_dtos_and_comment_reaction_dtos(
            post_reaction_dtos, comment_reaction_dtos)

        post_details_dto = PostDetailsDto(post_dto=post_dto,
                                          reactions_dto=reaction_dtos,
                                          comments_dto=comment_dtos,
                                          user_ids=user_ids)
        return post_details_dto

    @staticmethod
    def _convert_post_obj_to_dto(post):
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
            post_reaction_dto = self._convert_post_reaction_object_to_dto(
                reaction)
            post_reaction_dtos.append(post_reaction_dto)
        return post_reaction_dtos

    def _convert_reaction_objects_to_dtos(self, replies):
        reaction_dtos = []
        for reply in replies:
            reaction_dto = self._convert_comment_reaction_object_to_dto(reply)
            reaction_dtos.append(reaction_dto)
        return reaction_dtos

    def _get_comment_details(self, comment, user_ids):
        comment_dtos = []
        comment_dto = self._convert_comment_obj_to_dto(comment)
        comment_dtos.append(comment_dto)

        if comment.user_id not in user_ids:
            user_ids.append(comment.user_id)

        comment_reactions = comment.reactions.all()
        comment_reaction_dtos = self._convert_reaction_objects_to_dtos(
            comment_reactions)

        return user_ids, comment_dtos, comment_reaction_dtos

    def _get_comments_details(self, comments, user_ids):
        comments_dtos = []
        comments_reaction_dtos = []

        for comment in comments:
            user_ids, comment_dto, comment_reaction_dto = \
                self._get_comment_details(comment, user_ids)
            comments_dtos += comment_dto
            comments_reaction_dtos += comment_reaction_dto

        return user_ids, comments_dtos, comments_reaction_dtos

    def _get_replies_details(self, comments, user_ids):
        reply_dtos = []
        reply_reaction_dtos = []

        for comment in comments:
            comment_dto, comment_reaction_dto, user_ids = self._get_reply_details(
                comment, user_ids=user_ids)
            reply_dtos += comment_dto
            reply_reaction_dtos += comment_reaction_dto

        return reply_dtos, reply_reaction_dtos, user_ids

    def _get_reply_dtos(self, replies):
        comment_dtos = []
        for reply in replies:
            comment_dto = self._convert_reply_object_to_dto(reply)
            comment_dtos.append(comment_dto)
        return comment_dtos

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
        replies = comment.comments.all()
        reply_dtos += self._get_reply_dtos(replies)

        for reply in replies:
            user_id = reply.user_id
            if user_id not in user_ids:
                user_ids.append(reply.user_id)

        reply_reaction_dtos += self._get_reply_reaction_dtos(replies)
        return reply_dtos, reply_reaction_dtos, user_ids

    @staticmethod
    def _merge_post_reaction_dtos_and_comment_reaction_dtos(
            post_reaction_dtos, comment_reaction_dtos):
        reaction_dtos = post_reaction_dtos + comment_reaction_dtos
        return reaction_dtos

    @staticmethod
    def _merge_comment_reactions_and_reply_reaction(
            comment_reaction_dtos, reply_reactions):
        comment_reaction_dtos = comment_reaction_dtos + reply_reactions
        return comment_reaction_dtos

    @staticmethod
    def _merge_comment_dtos_and_reply_dtos(comment_dtos, reply_dtos):
        comment_dtos = comment_dtos + reply_dtos
        return comment_dtos

    @staticmethod
    def _convert_post_reaction_object_to_dto(reaction):
        reaction_dto = ReactionDto(
            reaction_id=reaction.id,
            user_id=reaction.user_id,
            comment_id=reaction.comment,
            post_id=reaction.post.id,
            reaction_type=reaction.reaction_type)
        return reaction_dto

    @staticmethod
    def _convert_comment_reaction_object_to_dto(reaction):
        reaction_dto = ReactionDto(
            reaction_id=reaction.id,
            user_id=reaction.user_id,
            comment_id=reaction.comment.id,
            post_id=reaction.post,
            reaction_type=reaction.reaction_type)
        return reaction_dto

    @staticmethod
    def _convert_comment_obj_to_dto(comment):
        comment_dto = CommentDto(
            comment_id=comment.id,
            user_id=comment.user_id,
            post_id=comment.post.id,
            comment_content=comment.comment_text,
            pub_date_time=comment.pub_date_time.replace(tzinfo=None),
            parent_comment=comment.parent_comment)
        return comment_dto

    @staticmethod
    def _convert_reply_object_to_dto(reply):
        reply_dto = CommentDto(comment_id=reply.id,
                               parent_comment=reply.parent_comment.id,
                               pub_date_time=reply.pub_date_time.replace(
                                   tzinfo=None),
                               post_id=reply.post,
                               user_id=reply.user_id,
                               comment_content=reply.comment_text)
        return reply_dto

