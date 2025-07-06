from django.db import models
from django.conf import settings
from shop.models import Product


class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    # session_key можно оставить, если хочешь поддерживать анонимных пользователей
    session_key = models.CharField(max_length=40, unique=True, null=True, blank=True)

    def __str__(self):
        if self.user:
            return f"Cart of {self.user.username}"
        return f"Cart with session {self.session_key}"


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
