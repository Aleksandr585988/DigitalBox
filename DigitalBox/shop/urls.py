from django.urls import path
from . import views

urlpatterns = [
    path('', views.content_list, name='content'),
    path('laptops/', views.laptops_and_computers, name='laptops_and_computers'),
    ]