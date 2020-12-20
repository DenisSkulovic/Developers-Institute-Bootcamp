from django.urls import path
from . import views


urlpatterns = [
    path('', views.Trading.as_view(), name='trading'),
    path('sell/<int:pk>', views.TradingSellDetailView.as_view(), name='trading_sell_detail'),
    path('buy/<int:pk>', views.TradingBuyDetailView.as_view(), name='trading_buy_detail'),
    path('buy/all/<int:page>', views.TradingBuyListView.as_view(), name='trading_buy_list'),
    path('sell/all/<int:page>', views.TradingSellListView.as_view(), name='trading_sell_list'),
    path('buy/create/', views.TradingBuyCreateView.as_view(), name = 'trading_buy_create'),
    path('sell/create/', views.TradingSellCreateView.as_view(), name = 'trading_sell_create'),
    path('buy/<int:pk>/edit/', views.TradingBuyUpdateView.as_view(), name='trading_buy_update'),
    path('sell/<int:pk>/edit', views.TradingSellUpdateView.as_view(), name='trading_sell_update'),
]