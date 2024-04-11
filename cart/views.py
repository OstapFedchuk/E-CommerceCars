from django.shortcuts import render, get_object_or_404
from .cart import Cart
from store.models import Product
from django.http import JsonResponse


#Visualizzazione del Carrello
def cart_summary(request):
    #Ottengo il carrello
    cart = Cart(request)
    cart_products = cart.get_prods()
    quantities = cart.get_quants()
    return render(request, 'cart_summary.html', {"cart_products":cart_products, "quantities":quantities})

#Aggiunta dei prodotto al carrello, insieme alla quantità
def cart_add(request):
    #Ottengo il carrello
    cart = Cart(request)
    # test for POST
    if request.POST.get('action') == 'post':
        #ottengo la "roba"
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))
        
        #Cerco il prodotto nel DB
        product = get_object_or_404(Product, id=product_id)
        
        #Salvataggio nella sessione
        cart.add(product=product, quantity=product_qty)

        #Ottengo la quantità di oggetti contenuti nel carrello
        cart_quantity = cart.__len__()

        #Ritorno iul risultato
        #response = JsonResponse({'Product Name: ': product.name})
        response = JsonResponse({'qty': cart_quantity})
        return response


#Rimozione del prodotto dal carrello
def cart_delete(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        #ottengo la "roba"
        product_id = int(request.POST.get('product_id'))
        #Richiamo la funzione di rimozione del prodotto dal carrello
        cart.delete(product=product_id)

        response = JsonResponse({'product':product_id})
        return response


#Aggiornamento quantià del prodotto desiderato
def cart_update(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        #ottengo la "roba"
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))

        cart.update(product=product_id, quantity=product_qty)

        response = JsonResponse({'qty':product_qty})
        return response
        #return redirect('cart_summary')


