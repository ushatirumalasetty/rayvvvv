"""
Created on 03/07/20

@author: revanth
"""

import datetime

import factory
from fb_post_clean_arch_v2.models import Post, Comment, Reaction
from fb_post_clean_arch_v2.constants.enums import ReactionType
reaction_types = [reaction_type.value for reaction_type in ReactionType]


class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Post

    user_id = factory.Sequence(lambda n: n + 1)
    pub_date_time = factory.LazyFunction(datetime.datetime.now)
    post_content = factory.Sequence(lambda n: "post_content_{0}".format(n + 1))


class CommentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Comment

    post = factory.SubFactory(PostFactory)
    comment_text = factory.Sequence(
        lambda n: "comment_content_{0}".format(n + 1))
    pub_date_time = factory.LazyFunction(datetime.datetime.now)
    parent_comment = factory.Sequence(lambda n: n + 1)
    user_id = factory.Sequence(lambda n: n + 1)


class ReactionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Reaction
    comment = factory.SubFactory(CommentFactory)
    post = factory.SubFactory(PostFactory)
    user_id = factory.Sequence(lambda n: n + 1)
    reaction_type = factory.Iterator(reaction_types)


class ReplyFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Comment

    user_id = factory.Sequence(lambda n: n)
    comment_text = factory.Sequence(lambda n: "NiceComment %03d" % n)
    parent_comment = factory.SubFactory(CommentFactory)
