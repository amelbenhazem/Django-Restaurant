# Django Restaurant Reservation

## Description

Django Restaurant Reservation est une application web permettant aux utilisateurs de :  
- Consulter la liste des restaurants et leurs tables disponibles  
- Réserver une table  
- Gérer les données via l’interface d’administration Django  
- Protéger certaines pages via l’authentification  
- Consulter et manipuler les données via une API REST

L’application utilise : Django 5.2, Django REST Framework, HTML/Template, et SQLite (configurable PostgreSQL).

---

## Fonctionnalités

- Base de données pour stocker Restaurants, Tables et Réservations  
- Architecture MVT (Model-View-Template)  
- ORM et relations One-to-Many entre modèles  
- Templates HTML et formulaires Django (ModelForm)  
- Interface d’administration pour gérer les données  
- Authentification et gestion des permissions  
- CBV (Class-Based Views) pour les vues principales  
- REST API pour consulter et modifier les données  
- Gestion des sessions et sécurité par défaut de Django  

---

## Modèles

- **Restaurant** : nom, localisation  
- **Table** : numéro, nombre de places, relation avec Restaurant  
- **Reservation** : table, utilisateur, date et heure de réservation  

Relations :  

- Restaurant → Table : One-to-Many  
- Table → Reservation : One-to-Many  

---
Créer et activer un environnement virtuel :

python -m venv venv
venv\Scripts\activate   # Windows
# ou sur Linux/Mac
# source venv/bin/activate


Installer les dépendances :

pip install -r requirements.txt
# ou si pas de fichier requirements.txt
pip install django djangorestframework


Créer la base de données et appliquer les migrations :

python manage.py makemigrations
python manage.py migrate


Créer un superuser pour accéder à l’admin :

python manage.py createsuperuser


Lancer le serveur de développement :

python manage.py runserver

Utilisation

Page d’accueil : http://127.0.0.1:8000/
Affiche la liste des restaurants et tables.

Réserver une table : http://127.0.0.1:8000/reserve/
Accessible uniquement aux utilisateurs connectés.

Page de succès : http://127.0.0.1:8000/success/
Affichage après réservation réussie.

Admin : http://127.0.0.1:8000/admin/
Ajouter/modifier/supprimer Restaurants, Tables et Réservations.

API REST :

http://127.0.0.1:8000/api/restaurants/

http://127.0.0.1:8000/api/tables/

http://127.0.0.1:8000/api/reservations/ 
django_restaurant/
├── django_restaurant/       # Configuration du projet
├── restaurant/              # Application principale
│   ├── migrations/
│   ├── templates/restaurant/
│   │   ├── restaurant_list.html
│   │   ├── make_reservation.html
│   │   └── reservation_success.html
│   ├── admin.py
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   ├── serializers.py
│   └── api_views.py
├── db.sqlite3
├── manage.py
└── venv/

 
