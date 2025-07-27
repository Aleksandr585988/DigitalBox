from django.shortcuts import render, get_object_or_404
from .models import Product, Category

def digital_box(request):
    categories = Category.objects.all()
    return render(request, 'shop/DigitalBox.html', {'categories': categories})

def laptops_and_computers(request):
    categories = Category.objects.all()
    return render(request, 'shop/laptops_and_computers.html', {
        'categories': categories
    })

def products_by_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = Product.objects.filter(category=category, available=True)
    return render(request, 'shop/products_by_category.html', {
        'category': category,
        'products': products
    })


def product_detail(request, category_slug, product_slug):
    category = get_object_or_404(Category, slug=category_slug)
    product = get_object_or_404(Product, slug=product_slug, category=category, available=True)
    return render(request, 'shop/product_detail.html', {
        'category': category,
        'product': product
    })