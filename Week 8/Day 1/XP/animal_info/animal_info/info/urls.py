from django.urls import path
from . import views


urlpatterns = [
    path('', views.animals, name='info_manager'),
    path('animals', views.animals, name='animals'),
    path('family/<int:id>', views.family, name='family'),
    path('animal/<int:id>', views.animal, name='animal')

]