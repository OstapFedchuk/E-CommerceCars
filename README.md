Installazione
1. Scaricare il file zip(il progetto) esempio di percorso: "C:\Users\nomeUser\Desktop\ecomm-django.zip"
2. Estrarre tutto il contenuto fuori dalla cartella zip scaricata, esempio "C:\Users\nomeUser\Desktop\"
3. Aprire la cartella con un editor di codice, VSCode preferibilmente.
4. Navigare nella directory del progetto, esempio "C:\Users\ostap\Desktop\ecom-django", usare il comando "cd ecom-django"
5. Verificare la versione di python con: py --version (se non è scaricalo su https://www.python.org/downloads/)
6. Installare Django: pip install django
7. Creare un ambiente virtuale: python -3 -m venv virt
8. Attivare l'ambiente virtuale:
   Su Windows: .\virt\Scripts\activate
   Su macOS e Linux: source virt/bin/activate
9. Installare Pillow: python -m pip install Pillow
10. Avviare il server di sviluppo: python manage.py runserver
11. Accedere all'applicazione su http://localhost:8000
12. Per accedere alla pagina di administration(quindi per accedere al DB) occorre andare su http://localhost:8000/admin e poi come credenziali mettere User:admin, pass:admin

GRUPPO: 
1. Fedchuk Ostap(CapoGruppo): creazione base del WebApp, codice in python per le funzionalità/features del sito, gestione DB e Admin Page (estrazione/importazione dati), parte Front-End e Back-End del sito
2. Lazzaro Michael: scelta stile del sito, parte di HTML e CSS, creazione del file "models.py" con poi eventuali aiuti da parte del CapoGruppo
3. Susino Giacomo: scelta stile del sito, parte di HTML e CSS, creazione del file forms.py" con poi eventuali aiuti da parte del CapoGruppo
4. Delponte Giuseppe: scelta stile del sito, parte di HTML e CSS, creazione del file "urls.py" con poi eventuali aiuti da parte del CapoGruppo
