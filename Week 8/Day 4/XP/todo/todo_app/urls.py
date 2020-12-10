from django.urls import path
from . import views

urlpatterns = [
    path('todo', views.todo_view, name='todo_view'),
    path('', views.display_todos, name='display_todos'),
]