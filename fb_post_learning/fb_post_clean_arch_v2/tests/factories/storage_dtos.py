"""
Created on 03/07/20

@author: revanth
"""
import datetime
import factory
from fb_post_clean_arch_v2.adapters.dtos import UserDTO
from fb_post_clean_arch_v2.interactors.storage_interfaces.dtos import \
    PostDto, CommentDto, ReactionDto
from fb_post_clean_arch_v2.constants.enums import ReactionType

reaction_types = [reaction_type.value for reaction_type in ReactionType]


class UserDTOFactory(factory.Factory):
    class Meta:
        model = UserDTO

    user_id = factory.Sequence(lambda n: n + 1)
    name = factory.Sequence(lambda n: "user_{0}".format(n + 1))
    profile_pic_url = factory.Sequence(lambda n: "profile_{0}".format(n + 1))


class PostDtoFactory(factory.Factory):
    class Meta:
        model = PostDto

    user_id = factory.Sequence(lambda n: n + 1)
    post_content = factory.Sequence(lambda n: "post_content_{0}".format(n + 1))
    post_id = factory.Sequence(lambda n: n + 1)
    pub_date_time = factory.LazyFunction(datetime.datetime.now)


class CommentDtoFactory(factory.Factory):
    class Meta:
        model = CommentDto

    comment_id = factory.Sequence(lambda n: n + 1)
    user_id = factory.Sequence(lambda n: n + 1)
    post_id = factory.Sequence(lambda n: n + 1)
    comment_content = factory.Sequence(
        lambda n: "comment_content_{0}".format(n + 1))
    pub_date_time = factory.LazyFunction(datetime.datetime.now)
    parent_comment = factory.Sequence(lambda n: n + 1)


class ReactionDtoFactory(factory.Factory):
    class Meta:
        model = ReactionDto

    reaction_id = factory.Sequence(lambda n: n + 1)
    comment_id = factory.Sequence(lambda n: n + 1)
    post_id = factory.Sequence(lambda n: n + 1)
    user_id = factory.Sequence(lambda n: n + 1)
    reaction_type = factory.Iterator(reaction_types)
