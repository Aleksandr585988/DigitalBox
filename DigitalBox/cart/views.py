from django.shortcuts import redirect, render, get_object_or_404
from .models import Cart, CartItem
from shop.models import Product

from orders.models import Order
from django.db import transaction
from .forms import OrderCreateForm

CART_DETAIL_URL = 'cart:detail'


def get_cart(request):
    if request.user.is_authenticated:
        cart, _ = Cart.objects.get_or_create(user=request.user)
    else:
        session_key = request.session.session_key
        if not session_key:
            request.session.create()
            session_key = request.session.session_key
        cart, _ = Cart.objects.get_or_create(session_key=session_key)
    return cart



def add_to_cart(request, product_id):
    cart = get_cart(request)
    product = get_object_or_404(Product, id=product_id)

    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        cart_item.quantity += 1
    cart_item.save()

    return redirect(CART_DETAIL_URL)


def cart_detail(request):
    cart = get_cart(request)
    items = cart.items.select_related('product').all()

    total_price = sum(item.product.price * item.quantity for item in items)

    return render(request, 'cart/cart_detail.html', {
        'cart_items': items,
        'total_price': total_price,
    })


@transaction.atomic
def order_create(request):
    cart  = get_cart(request)
    items = cart.items.select_related('product')

    if not items.exists():
        return redirect(CART_DETAIL_URL)

    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data

            created_orders = []
            for item in items:
                o = Order.objects.create(
                    product        = item.product,
                    quantity       = item.quantity,
                    customer_name  = cd['customer_name'],
                    customer_email = cd['customer_email'],
                )
                created_orders.append(o)

            items.delete()

            # ➡ куда редиректить
            if len(created_orders) == 1:
                return redirect('order:order_success',
                                order_id=created_orders[0].id)
            else:
                return redirect('order:my_orders')
    else:
        form = OrderCreateForm()

    total = sum(i.product.price * i.quantity for i in items)
    return render(request, 'cart/checkout.html', {
        'cart_items':  items,
        'total_price': total,
        'form':        form,
    })


def cart_remove(request, product_id):
    cart = get_cart(request)
    product = get_object_or_404(Product, id=product_id)
    CartItem.objects.filter(cart=cart, product=product).delete()
    return redirect(CART_DETAIL_URL)
