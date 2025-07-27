from decimal import Decimal
from django.db import models
from shop.models import Product


class Order(models.Model):
    product         = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="orders")
    quantity        = models.PositiveIntegerField(default=1)
    unit_price      = models.DecimalField(max_digits=10, decimal_places=2, editable=False)
    total_price     = models.DecimalField(max_digits=12, decimal_places=2, editable=False)
    order_date      = models.DateTimeField(auto_now_add=True)
    customer_name   = models.CharField(max_length=100)
    customer_email  = models.EmailField()
    status          = models.CharField(
        max_length=20,
        choices=[('new', 'Новый'), ('paid', 'Оплачен'), ('shipped', 'Отгружен')],
        default='new',
    )

    def save(self, *args, **kwargs):
        # если создаём новый заказ, фиксируем текущую цену товара
        if not self.pk:
            self.unit_price = self.product.price
        # пересчитываем итог каждый раз (на случай изменения quantity)
        self.total_price = (self.unit_price or Decimal('0.00')) * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        if self.pk:
            return f"Order #{self.pk} — {self.product.model_name} × {self.quantity}"
        return f"New Order — {self.product.model_name} × {self.quantity}"