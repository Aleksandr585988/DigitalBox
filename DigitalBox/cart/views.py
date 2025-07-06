from django.shortcuts import redirect, render, get_object_or_404
from models import Cart, CartItem
from DigitalBox.shop.models import Product

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

    return redirect('cart:detail')


def cart_detail(request):
    cart = get_cart(request)
    items = cart.items.select_related('product').all()

    total_price = sum(item.product.price * item.quantity for item in items)

    return render(request, 'cart/cart_detail.html', {
        'cart_items': items,
        'total_price': total_price,
    })

