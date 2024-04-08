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
    def add(self, product):
        product_id = str(product.id)
        
        if product_id in self.cart:
            pass
        else:
            self.cart[product_id] = {'price': str(product.price)}

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
        