from django.urls import path
from account import views

urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup'),
]

# Password resetting is done via built-in views and urls,
# so integrate the /account/password_reset/ and so on

# If the templates are in "registration" and are named properly,
# they are available to Django (they replace Django's default templates)
