from store.models import Product

class Cart():
    def __init__(self, request):
        self.session = request.session

        #Otteniamo la key della sessione nel caso esista
        cart = self.session.get('session_key')

        #se user è nuovo, non si ha la session key! Creare una nuova!
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}

        #Controllo se il carrello sia accessibile da tutte le pagine del sito
        self.cart = cart

    #Funzione che aggiunge il prodotto all'interno della sessione
    def add(self, product, quantity):
        product_id = str(product.id)
        product_qty = str(quantity)
        
        if product_id in self.cart:
            pass
        else:
            #self.cart[product_id] = {'price': str(product.price)}
            self.cart[product_id] = int(product_qty)

        self.session.modified = True

    #Funzione che restituisce la lunghezza del carrello, cioè la quantità degli oggetti contenenti in essa
    def __len__(self):
        return len(self.cart)
    
    #Funzione che permetterà di vedere cio che è presente nel carrello
    def get_prods(self):
        #Ottengo i ID dal carrello
        product_ids = self.cart.keys()
        #Utilizzo dei ID per cercarli nel DB
        products = Product.objects.filter(id__in=product_ids)
        #ritorno i prodotti cercati
        return products
    
    #Funzione che ritorna il numero di prodotti scelti
    def get_quants(self):
        quantities = self.cart
        return quantities
    
    def update(self, product, quantity):
        product_id = str(product)
        product_qty = int(quantity)

        #ottengo il carrello
        ourcart = self.cart
        #Update Dictionary/cart
        ourcart[product_id] = product_qty

        self.session.modified = True

        thing = self.cart
        return thing   
    
    def delete(self, product):
        product_id = str(product)
        #RImozione dal carrello
        if product_id in self.cart:
            del self.cart[product_id]
        
        self.session.modified = True
        