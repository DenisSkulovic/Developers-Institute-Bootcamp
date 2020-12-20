from django.urls import path
from . import views


urlpatterns = [
    path('', views.Forum.as_view(), name='forum'),
    path('addcomment/', views.CreateComment.as_view(), name='addcomment'),
]