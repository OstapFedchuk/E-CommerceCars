from store.models import Product, Profile

class Cart():
    def __init__(self, request):
        self.session = request.session
        #Ottengo la richiesta
        self.request = request
        #Otteniamo la key della sessione nel caso esista
        cart = self.session.get('session_key')

        #se user è nuovo, non si ha la session key! Creare una nuova!
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}

        #Controllo se il carrello sia accessibile da tutte le pagine del sito
        self.cart = cart
    
    '''Funzione che aggiunge all'interno del DB il prodotto della sessione corrente
    Permettendo cosi di salvare i prodotti nel carrello dell'utente anche dopo il logout
    Essendo che vengono salvati l'ID e quantità dei prodotti all'interno del DB e il programma andrà
    solamente a recuperare da li dentro questi dati per mostrarti sul sito'''
    def db_add(self, product, quantity):
        product_id = str(product)
        product_qty = str(quantity)
        
        if product_id in self.cart:
            pass
        else:
            #self.cart[product_id] = {'price': str(product.price)}
            self.cart[product_id] = int(product_qty)

        self.session.modified = True

        #Controllo se l'utente è loggato
        if self.request.user.is_authenticated:
            #Ottenimento dell'user corrente
            current_user = Profile.objects.filter(user__id=self.request.user.id)
            # Converto la Query es. da  {'3':1, '2': 3} a {"3":1, "2": 3}
            carty = str(self.cart)
            carty = carty.replace("\'", "\"")
            #Salvo carty nel Profile Model
            current_user.update(old_cart=str(carty))
    #Funzione che aggiunge il prodotto all'interno della sessione corrente
    def add(self, product, quantity):
        product_id = str(product.id)
        product_qty = str(quantity)
        
        if product_id in self.cart:
            pass
        else:
            #self.cart[product_id] = {'price': str(product.price)}
            self.cart[product_id] = int(product_qty)

        self.session.modified = True

        #Controllo se l'utente è loggato
        if self.request.user.is_authenticated:
            #Ottenimento dell'user corrente
            current_user = Profile.objects.filter(user__id=self.request.user.id)
            # Converto la Query es. da  {'3':1, '2': 3} a {"3":1, "2": 3}
            carty = str(self.cart)
            carty = carty.replace("\'", "\"")
            #Salvo carty nel Profile Model
            current_user.update(old_cart=str(carty))

    def cart_total(self):
        #Ottengo ID del prodotto
        product_ids = self.cart.keys()
        #Cerco "quelle" keys nel nostro modello dei prodotti all'interno del DB
        products = Product.objects.filter(id__in=product_ids)
        #Ottengo le quantità dei prodotti
        quantities = self.cart
        #Contatore del totale
        total = 0
        for key, value in quantities.items():
            #Converto la string key in un int cosi da poter eseguire i calcoli
            key = int(key)
            for product in products:
                if product.id == key:
                    if product.is_sale:
                        total = total + (product.sale_price * value)
                    else:
                        total = total + (product.price * value)

        return total 
    



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

        if self.request.user.is_authenticated:
            #Ottenimento dell'user corrente
            current_user = Profile.objects.filter(user__id=self.request.user.id)
            # Converto la Query es. da  {'3':1, '2': 3} a {"3":1, "2": 3}
            carty = str(self.cart)
            carty = carty.replace("\'", "\"")
            #Salvo carty nel Profile Model
            current_user.update(old_cart=str(carty))

        thing = self.cart
        return thing   
    
    def delete(self, product):
        product_id = str(product)
        #RImozione dal carrello
        if product_id in self.cart:
            del self.cart[product_id]
        
        self.session.modified = True

        if self.request.user.is_authenticated:
            #Ottenimento dell'user corrente
            current_user = Profile.objects.filter(user__id=self.request.user.id)
            # Converto la Query es. da  {'3':1, '2': 3} a {"3":1, "2": 3}
            carty = str(self.cart)
            carty = carty.replace("\'", "\"")
            #Salvo carty nel Profile Model
            current_user.update(old_cart=str(carty))
        