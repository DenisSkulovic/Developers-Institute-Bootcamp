from django.contrib import admin
from trading.models import SellOffer, BuyOffer


admin.site.register(SellOffer)
admin.site.register(BuyOffer)