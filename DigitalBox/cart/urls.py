
from django.urls import path, include
from . import views

app_name = "cart"

urlpatterns = [
    path("", views.cart_detail,  name="detail"),
    path("add/<int:product_id>/", views.add_to_cart, name="add"),
    path('remove/<int:product_id>/', views.cart_remove, name='remove'),
    path('checkout/', views.order_create, name='checkout'),
]