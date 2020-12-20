from django.urls import path
from . import views


urlpatterns = [
    path('', views.mainpage, name='mainpage')
    path('card_detail/<int:pk>', views.CardDetailView.as_view(), name='card_detail'),
    path('card_list/', views.CardListView.as_view(), name='card_list'),
]