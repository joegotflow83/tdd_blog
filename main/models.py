from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    user = models.ForeignKey(User)
    title = models.CharField(max_length=32)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
