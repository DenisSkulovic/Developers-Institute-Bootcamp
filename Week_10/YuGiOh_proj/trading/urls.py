from django.urls import path
from . import views


urlpatterns = [
    path('', views.Trading.as_view(), name='trading'),
    path('buy/<int:page>', views.BuyOfferView.as_view(), name='trading_buy'),
    path('sell/<int:page>', views.SellOfferView.as_view(), name='trading_sell'),
    path('buy_all/<int:page>', views.BuyOfferViewAll.as_view(), name='trading_buy_all'),
    path('sell_all/<int:page>', views.SellOfferViewAll.as_view(), name='trading_sell_all'),
]