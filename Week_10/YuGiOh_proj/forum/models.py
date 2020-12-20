from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


class Comment(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    post_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
