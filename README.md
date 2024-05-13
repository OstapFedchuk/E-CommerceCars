Installazione
Scaricare il file zip(il progetto) esempio di percorso: "C:\Users\nomeUser\Desktop\ecomm-django.zip"
Estrarre tutto il contenuto fuori dalla cartella zi scaricata, esempio ""C:\Users\ostap\Desktop\"
Aprire la cartella con un editor di codice, VSCode preferibilmente.
Navigare nella directory del progetto: cd django-ecommerce
Creare un ambiente virtuale: python -m venv env
Attivare l'ambiente virtuale:
Su Windows: .\env\Scripts\activate
Su macOS e Linux: source env/bin/activate
Installare le dipendenze: pip install -r requirements.txt
Eseguire le migrazioni: python manage.py migrate
Creare un superuser: python manage.py createsuperuser
Avviare il server di sviluppo: python manage.py runserver
Accedere all'applicazione su http://localhost:8000
