from django.db import models
from mainpage.models import Type, Race, Archetype, Cardset, Image, CardPrice, Attribute, Card
from django.contrib.auth import get_user_model
User = get_user_model()



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = models.URLField(max_length=200, default = 'https://secure.gravatar.com/avatar/fcd55da13e2825cfeca3ed77022745ff?s=256&d=mm&r=g')
    nickname = models.CharField(max_length=50, unique=True, null=False)
    cards = models.ManyToManyField(Card, null=True, default=None, blank=True)
    balance = models.FloatField(default=0)
    def __repr__(self):
        return f'{self.nickname} - {self.user.username}'
    def __str__(self):
        return f'{self.nickname} - {self.user.username}'
    
    
        
