from django.shortcuts import render, get_object_or_404
from .models import Product, Content, Category

def content_list(request):
    categories = Category.objects.all()
    content = Content.objects.all()
    return render(request, 'shop/content.html', {'content': content, 'categories': categories})

def laptops_and_computers(request):
    categories = Category.objects.all()
    return render(request, 'shop/laptops_and_computers.html', {
        'categories': categories
    })

def products_list(request):
    product = Product.objects.filter(available=True)
    return render(request, 'shop/product_list.html', {'products': product})

def products_laptop(request):
    product = Product.objects.filter(available=True)
    return render(request, 'shop/product_laptop.html', {'products': product})

def products_by_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    products = Product.objects.filter(category=category, available=True)
    return render(request, 'shop/products_by_category.html', {
        'category': category,
        'products': products
    })
