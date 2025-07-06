from django.urls import path
from . import views

urlpatterns = [
    path('', views.content_list, name='content'),
    path('laptopsAndComputer/', views.laptops_and_computers, name='laptops_and_computers'),
    path('category/<int:category_id>/', views.products_by_category, name='products_by_category'),
    path('productslist/', views.products_list, name='product_list'),
    path('productslaptop/', views.products_laptop, name='product_laptop'),
    ]
    