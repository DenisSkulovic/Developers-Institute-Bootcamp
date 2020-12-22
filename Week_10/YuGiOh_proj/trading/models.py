from django.db import models
from mainpage.models import (
    Type, Race, Archetype, Cardset, 
    Image, CardPrice, Attribute, Card,
    )
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()



class Offer(models.Model):
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    price = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=5, choices=(('Sell', 'Sell'), ('Buy','Buy')))
    def __str__(self):
        return f'{self.type} - {self.card.name} - {self.user.username}'
    def get_absolute_url(self):
        return reverse('trading_detail', args=[str(self.id)])