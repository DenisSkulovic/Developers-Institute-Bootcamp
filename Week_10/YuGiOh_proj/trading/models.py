from django.db import models
from mainpage.models import (
    Type, Race, Archetype, Cardset, 
    Image, CardPrice, Attribute, Card,
    )
from account.models import Profile




class SellOffer(models.Model):
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    price = models.FloatField()
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    
    
class BuyOffer(models.Model):
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    price = models.FloatField()
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)    