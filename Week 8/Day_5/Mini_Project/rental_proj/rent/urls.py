from django.urls import path
from . import views

urlpatterns = [
    path('', views.mainpage, name='mainpage'),
    path('rental/', views.rental, name='rental'),
    path('rental/<int:id>', views.rental_id, name='rental_id'),
    path('rental/add', views.rental_add, name='rental_add'),
    path('customer/', views.customer, name='customer'),
    path('customer/<int:id>', views.customer_id, name='customer_id'),
    path('customer/add', views.customer_add, name='customer_add'),
    path('vehicle/', views.vehicle, name='vehicle'),
    path('vehicle/<int:id>', views.vehicle_id, name='vehicle_id'),
    path('vehicle/add', views.vehicle_add, name='vehicle/add'),
]