Installazione
1. Scaricare il file zip(il progetto) esempio di percorso: "C:\Users\nomeUser\Desktop\ecomm-django.zip"
2. Estrarre tutto il contenuto fuori dalla cartella zi scaricata, esempio ""C:\Users\ostap\Desktop\"
3. Aprire la cartella con un editor di codice, VSCode preferibilmente.
4. Navigare nella directory del progetto: cd django-ecommerce
5. Creare un ambiente virtuale: python -m venv env
6. Attivare l'ambiente virtuale:
7. Su Windows: .\env\Scripts\activate
   Su macOS e Linux: source env/bin/activate
8. Installare le dipendenze: pip install -r requirements.txt
9. Eseguire le migrazioni: python manage.py migrate
10. Creare un superuser: python manage.py createsuperuser
11. Avviare il server di sviluppo: python manage.py runserver
12. Accedere all'applicazione su http://localhost:8000
