from django.contrib import admin
from .models import Order

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "product", "quantity", "order_date", "customer_name", "customer_email")
    list_filter = ("order_date",)
    search_fields = ("customer_name", "customer_email", "product__model_name")
