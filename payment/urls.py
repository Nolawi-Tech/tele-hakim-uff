from django.urls import path
from .views import home, payment_with_cart, payment_with_express, success, cancel, ipn

urlpatterns = [
    path('', home, name='home'),
    path('with-express/', payment_with_express, name='express-payment'),
    path('with-cart/', payment_with_cart, name='cart-payment'),
    path('success/', success, name='success'),
    path('cancel/', cancel, name='cancel'),
    path('ipn/', ipn, name='ipn')
]



# from django.urls import path

# from . import views

# app_name = "billing"

# urlpatterns = [
# path('order_confirm/<str:order_id>/', views.order_confirm, name='order_confirm'),
# path('order_complete/', views.order_complete, name='order_complete'),
# path('success/<str:order_id>/', views.success, name='success'),
# ]

