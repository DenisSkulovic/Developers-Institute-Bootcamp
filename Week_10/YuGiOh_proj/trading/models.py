from django.db import models
from mainpage.models import (
    Type, Race, Archetype, Cardset, 
    Image, CardPrice, Attribute, Card,
    )
from account.models import Profile
from django.urls import reverse




class SellOffer(models.Model):
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    price = models.FloatField()
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.card.name} - {self.profile.nickname}'
    def get_absolute_url(self):
        return reverse('trading_sell_detail', args=[str(self.id)])
    
class BuyOffer(models.Model):
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    price = models.FloatField()
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)    
    def __str__(self):
        return f'{self.card.name} - {self.profile.nickname}'
    def get_absolute_url(self):
        return reverse('trading_buy_detail', args=[str(self.id)])
    