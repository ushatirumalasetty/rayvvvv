from django.db import models


class Post(models.Model):
    user_id = models.IntegerField()
    pub_date_time = models.DateTimeField(auto_now=True)
    post_content = models.CharField(max_length=250)

    def __str__(self):
        return "%s %s" % (self.user_id, self.post_content)
