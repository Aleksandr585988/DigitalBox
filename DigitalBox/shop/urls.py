from django.urls import path
from . import views

urlpatterns = [
    path('', views.digital_box, name='home'),
    path('laptopsAndComputer/', views.laptops_and_computers, name='laptops_and_computers'),
    path('category/<slug:slug>/', views.products_by_category, name='products_by_category'),
    path('category/<slug:category_slug>/<slug:product_slug>/', views.product_detail, name='product_detail'),
    ]
    