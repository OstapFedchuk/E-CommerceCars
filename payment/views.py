from django.shortcuts import render, redirect
from cart.cart import Cart
from payment.forms import ShippingForm
from payment.models import ShippingAddress
from django.contrib import messages


def billing_info(request):
    if request.POST:
        #Ottengo il carrello
        cart = Cart(request)
        cart_products = cart.get_prods()
        quantities = cart.get_quants()
        totals = cart.cart_total()

        shipping_form = request.POST
        return render(request, 'payment/billing_info.html', {"cart_products":cart_products, "quantities":quantities, "totals": totals, "shipping_form": shipping_form})
    else:
        messages.success(request, "Access Denied")
        return redirect('home');
   

def checkout(request):
    #Ottengo il carrello
    cart = Cart(request)
    cart_products = cart.get_prods()
    quantities = cart.get_quants()
    totals = cart.cart_total()

    if request.user.is_authenticated:
        #Login In Checkout
        #Ottenimento dei dati di Shipping dell'User corrente
        shipping_user = ShippingAddress.objects.get(user__id=request.user.id)
        #Shipping Form
        shipping_form = ShippingForm(request.POST or None, instance=shipping_user)
        return render(request, 'payment/checkout.html', {"cart_products":cart_products, "quantities":quantities, "totals": totals, "shipping_form": shipping_form})
    else:
        #Guest Checkout
        shipping_form = ShippingForm(request.POST or None)
        return render(request, 'payment/checkout.html', {"cart_products":cart_products, "quantities":quantities, "totals": totals, "shipping_form": shipping_form})


def payment_success(request):
    return render(request, 'payment/payment_success.html', {})