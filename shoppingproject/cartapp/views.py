from django.shortcuts import render, redirect, get_object_or_404
from shopapp . models import product
from .models import Cart, CartItem
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
def cart_id(request):
    cart=request.session.session_key
    if not cart:
        cart=request.session.create()
    return cart

def cart_item(request,product_id):
    produ=product.objects.get(id=product_id)
    try:
        cart=Cart.objects.get(cart_id=cart_id(request))
    except Cart.DoesNotExist:
        cart=Cart.objects.create(
            cart_id=cart_id(request)
        )
        cart.save(),
    try:
        cart_item=CartItem.objects.get(products=produ,cart=cart)
        if cart_item.quantity < cart_item.products.stock:
            cart_item.quantity += 1
        cart_item.save(),
    except CartItem.DoesNotExist:
        cart_item=CartItem.objects.create(
            products=produ,
            quantity=1,
            cart=cart
        )
        cart_item.save()
    return redirect('cartapp:cart_detail')

def cart_detail(request,total=0,counter=0,cart_items=None):
    try:
        cart=Cart.objects.get(cart_id=cart_id(request))
        cart_items=CartItem.objects.filter(cart=cart,active=True)
        for p in cart_items:
            total += p.products.price * p.quantity
            counter += p.quantity
    except ObjectDoesNotExist:
        pass
    return render(request,'cart.html',dict(cart_items=cart_items,total=total,counter=counter))

def cart_remove(request,product_id):
    cart=Cart.objects.get(cart_id=cart_id(request))
    Product=get_object_or_404(product,id=product_id)
    cart_item=CartItem.objects.get(products=Product,cart=cart)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('cartapp:cart_detail')

def full_remove(request,product_id):
    cart = Cart.objects.get(cart_id=cart_id(request))
    produc = get_object_or_404(product, id=product_id)
    cart_item = CartItem.objects.get(products=produc, cart=cart)
    cart_item.delete()
    return redirect('cartapp:cart_detail')