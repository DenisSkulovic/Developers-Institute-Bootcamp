from django.urls import path
from . import views

urlpatterns = [
    path('', views.Homepage.as_view(), name='homepage'),
    path('addDirector', views.AddDirector.as_view(), name='AddDirector'),
    path('addFilm', views.AddFilm.as_view(), name='AddFilm'),
    # path('accounts', views.Homepage.as_view(), name='homepage'),    
]