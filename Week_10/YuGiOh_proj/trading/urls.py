from django.urls import path
from . import views


urlpatterns = [
    path('offer/<int:pk>', views.TradingDetailView.as_view(), name='trading_detail'),
    path('', views.TradingListView.as_view(), name='trading_list'),
    path('offer/create/<str:type>', views.TradingCreateView.as_view(), name = 'trading_create'),
    path('offer/<int:pk>/edit/', views.TradingUpdateView.as_view(), name='trading_update'),
    path('offer/<int:pk>/delete/', views.TradingDeleteView.as_view(), name='trading_delete'),
]