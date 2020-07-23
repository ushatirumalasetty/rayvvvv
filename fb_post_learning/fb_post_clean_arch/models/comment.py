from django.db import models

from fb_post_clean_arch.models.post import Post


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name='comments', default=None, null=True)
    comment_text = models.CharField(max_length=250)
    pub_date_time = models.DateTimeField(auto_now=True)
    parent_comment = models.ForeignKey('self', on_delete=models.CASCADE,
                                       default=None, null=True,
                                       related_name='comments')
    user_id = models.IntegerField()
