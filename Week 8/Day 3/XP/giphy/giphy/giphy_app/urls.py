from django.urls import path
from . import views

urlpatterns = [
    path('gip', views.home, name='name'),
]
