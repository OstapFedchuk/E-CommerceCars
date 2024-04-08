from .cart import Cart

#Creazione context processor cosi il nostro carrello funzioni in tutte le pagine
def cart(request):
    #ritorno della data default dal nostro carrello
    return {'cart': Cart(request)}