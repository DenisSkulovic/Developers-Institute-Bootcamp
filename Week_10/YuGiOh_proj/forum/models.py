from django.db import models
from django.contrib.auth import get_user_model
from account.models import CustomUser
from django.urls import reverse


class Comment(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    post_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('comment_detail', args=[str(self.id)])