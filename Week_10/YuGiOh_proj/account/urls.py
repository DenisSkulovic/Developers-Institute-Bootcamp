from django.urls import path, include
from .views import (
    Login, Register, ChangePicture,
    ChangePassword, viewcard, viewcards,
    logout, Account
)
from django.contrib.auth.views import LoginView


urlpatterns = [
    path('account/', Account.as_view(), name='account'),
    path('', include('django.contrib.auth.urls')),
    path('login/', Login.as_view(), name='login'),
    path('register/', Register.as_view(), name='register'),
    path('changepassword/', ChangePassword.as_view(), name='changepassword'),
    path('changepicture/', ChangePicture.as_view(), name='changepicture'),
    path('card/<int:id>', viewcard, name='viewcard'),
    path('cards/', viewcards, name='viewcards'),
    path('logout/', logout, name='logout')
]