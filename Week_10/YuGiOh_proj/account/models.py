from django.db import models
from mainpage.models import Card
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    picture = models.URLField(max_length=200, null=True, default = 'https://secure.gravatar.com/avatar/fcd55da13e2825cfeca3ed77022745ff?s=256&d=mm&r=g')
    cards = models.ManyToManyField(Card, default=None, blank=True)
    balance = models.FloatField(default=0)
    def __repr__(self):
        return f'{self.username}'
    def __str__(self):
        return f'{self.username}'
    