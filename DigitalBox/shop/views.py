from django.shortcuts import render
from .models import Product, Content

def product_list(request):
    product = Product.objects.filter(available=True)
    return render(request, 'shop/product_list.html', {'products': product})

def content_list(request):
    content = Content.objects.filter()
    return render(request, 'shop/content.html', {'content': content})

def laptops_and_computers(request):
    return render(request, 'shop/laptops_and_computers.html')
