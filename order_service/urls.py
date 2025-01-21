# orders/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.place_order, name='create_order'),  # Trigger order creation
    path('process/', views.order_success, name='order_success'),  # Endpoint for Azure Function
    path('order-failure/', views.order_failure, name='order_failure'),

]
