Installazione
1. Scaricare il file zip(il progetto) esempio di percorso: "C:\Users\nomeUser\Desktop\ecomm-django.zip"
2. Estrarre tutto il contenuto fuori dalla cartella zi scaricata, esempio "C:\Users\ostap\Desktop\"
3. Aprire la cartella con un editor di codice, VSCode preferibilmente.
4. Navigare nella directory del progetto, esempio "C:\Users\ostap\Desktop\", usare il comando "cd ecom-django"
5. Verificare la versione di python con: py --version (se non è scaricalo su https://www.python.org/downloads/)
6. Installare Django: pip install django
7. Creare un ambiente virtuale: python -3 -m venv virt
8. Attivare l'ambiente virtuale:
   Su Windows: .\virt\Scripts\activate
   Su macOS e Linux: source env/bin/activate
9. Entrare nela cartella ecom: cd ecom
10. Eseguire le migrazioni: python manage.py migrate
11. Creare un superuser: python manage.py createsuperuser
12. Avviare il server di sviluppo: python manage.py runserver
13. Accedere all'applicazione su http://localhost:8000
