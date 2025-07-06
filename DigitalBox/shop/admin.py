from django.contrib import admin
from .models import Content, Category, Product

@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "category", "price", "available")
    list_filter = ("available", "category")
    search_fields = ("name", "description")
