from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    name = models.CharField(max_length=50)
    profile_pic_url = models.CharField(max_length=50)

    def __str__(self):
        return "%s %s" % (self.name, self.profile_pic_url)
