from django.urls import path
from . import views

urlpatterns = [
    path('phonenumber/<str:phone_number>', views.phonenumber, name='phonenumber'),
    path('name/<str:name>', views.name, name='name')
]