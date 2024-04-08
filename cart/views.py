from django.shortcuts import render, get_object_or_404
from .cart import Cart
from store.models import Product
from django.http import JsonResponse


def cart_summary(request):
    #Ottengo il carrello
    cart = Cart(request)
    cart_products = cart.get_prods()
    return render(request, 'car_summary.html', {"car_products":cart_products})


def cart_add(request):
    #Ottengo il carrello
    cart = Cart(request)
    # test for POST
    if request.POST.get('action') == 'post':
        #ottengo la "roba"
        product_id = int(request.POST.get('product_id'))
        
        #Cerco il prodotto nel DB
        product = get_object_or_404(Product, id=product_id)
        
        #Salvataggio nella sessione
        cart.add(product=product)

        #Ottengo la quantità di oggetti contenuti nel carrello
        cart_quantity = cart.__len__()

        #Ritorno iul risultato
        #response = JsonResponse({'Product Name: ': product.name})
        response = JsonResponse({'qty': cart_quantity})
        return response



def cart_delete(request):
    pass


def cart_update(request):
    pass

