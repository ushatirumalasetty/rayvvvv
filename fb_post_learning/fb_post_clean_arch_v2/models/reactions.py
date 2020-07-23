from django.db import models


def validate_reaction_type(value):
    from fb_post_clean_arch_v2.constants.enums import ReactionType
    if value not in ReactionType.get_list_of_values():
        from django.core.exceptions import ValidationError
        from fb_post_clean_arch_v2.constants.constants import \
            INVALID_REACTION_TYPE
        raise ValidationError(INVALID_REACTION_TYPE.format(value))


class Reaction(models.Model):
    from fb_post_clean_arch_v2.models.comment import Comment
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE,
                                default=None, null=True,
                                related_name="reactions")
    from fb_post_clean_arch_v2.models.post import Post
    post = models.ForeignKey(Post, on_delete=models.CASCADE, default=None,
                             null=True, related_name="reactions")
    user_id = models.IntegerField()
    reaction_type = models.CharField(max_length=10, default=None, null=True,
                                     validators=[validate_reaction_type])

    def __str__(self):
        return self.reaction_type
