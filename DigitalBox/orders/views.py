from django.shortcuts import render, get_object_or_404
from .models import Order
from django.contrib.auth.decorators import login_required

def order_success(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'order/order_success.html', {'order': order})

@login_required
def my_orders(request):
    orders = Order.objects.filter(customer_email=request.user.email)  # если нет поля customer с FK на User
    # Или, если у тебя есть поле customer = models.ForeignKey(User), то:
    # orders = Order.objects.filter(customer=request.user)
    return render(request, 'order/my_orders.html', {'orders': orders})