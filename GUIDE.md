# 📚 Guide Technique Complet - Django Restaurant Reservation

## Table des Matières
1. [Introduction à Django](#1-introduction-à-django)
2. [Architecture du Projet](#2-architecture-du-projet)
3. [Technologies Utilisées](#3-technologies-utilisées)
4. [Modèles de Données](#4-modèles-de-données)
5. [Vues et Templates](#5-vues-et-templates)
6. [Formulaires](#6-formulaires)
7. [Système d'Authentification](#7-système-dauthentification)
8. [Interface d'Administration](#8-interface-dadministration)
9. [API REST](#9-api-rest)
10. [Frontend et CSS](#10-frontend-et-css)
11. [Base de Données et Migrations](#11-base-de-données-et-migrations)
12. [Sécurité](#12-sécurité)
13. [Concepts Avancés](#13-concepts-avancés)

---

## 1. Introduction à Django

### Qu'est-ce que Django ?

Django est un **framework web Python** de haut niveau qui encourage le développement rapide et la conception propre et pragmatique. Il a été créé en 2003 et est maintenu par la Django Software Foundation.

### Philosophie de Django

**"Don't Repeat Yourself" (DRY)** - Ne vous répétez pas
- Réduire la duplication du code
- Réutiliser les composants
- Maintenir un code propre et maintenable

**"Convention over Configuration"** - Convention plutôt que configuration
- Moins de décisions à prendre
- Structure de projet standardisée
- Démarrage rapide

### Architecture MVT (Model-View-Template)

Django utilise le pattern MVT, une variante du MVC (Model-View-Controller) :

```
┌─────────────────────────────────────────────────┐
│                   UTILISATEUR                    │
└─────────────────┬───────────────────────────────┘
                  │
                  ▼
┌─────────────────────────────────────────────────┐
│              URLS (urls.py)                      │
│  Route les requêtes HTTP vers les bonnes vues   │
└─────────────────┬───────────────────────────────┘
                  │
                  ▼
┌─────────────────────────────────────────────────┐
│              VIEWS (views.py)                    │
│  Logique métier et traitement des données       │
└─────────┬───────────────────────┬───────────────┘
          │                       │
          ▼                       ▼
┌──────────────────┐    ┌──────────────────────┐
│  MODELS          │    │   TEMPLATES          │
│  (models.py)     │    │   (HTML + Django)    │
│  Base de données │    │   Présentation       │
└──────────────────┘    └──────────────────────┘
```

**Model (Modèle)** : Représente la structure des données et interagit avec la base de données
**View (Vue)** : Contient la logique métier et traite les requêtes
**Template** : Définit la présentation HTML et l'interface utilisateur

### Pourquoi Django ?

✅ **Batteries incluses** - Tout ce dont vous avez besoin est intégré :
- Système d'authentification
- Interface d'administration automatique
- ORM (Object-Relational Mapping)
- Gestion des formulaires
- Protection CSRF
- Gestion des sessions

✅ **Sécurité** - Protection intégrée contre :
- Injection SQL
- Cross-Site Scripting (XSS)
- Cross-Site Request Forgery (CSRF)
- Clickjacking

✅ **Scalabilité** - Utilisé par Instagram, Pinterest, Mozilla, NASA

✅ **Documentation excellente** - https://docs.djangoproject.com/

---

## 2. Architecture du Projet

### Structure Complète

```
Django-Restaurant/
│
├── django_restaurant/              # Configuration du projet Django
│   ├── __init__.py                 # Package Python
│   ├── settings.py                 # Configuration globale
│   ├── urls.py                     # URLs principales
│   ├── asgi.py                     # Configuration ASGI (async)
│   └── wsgi.py                     # Configuration WSGI (déploiement)
│
├── restaurant/                     # Application principale
│   ├── migrations/                 # Historique des modifications BDD
│   │   ├── __init__.py
│   │   ├── 0001_initial.py
│   │   ├── 0002_table.py
│   │   ├── 0003_reservation.py
│   │   └── 0004_alter_reservation_options_...py
│   │
│   ├── static/                     # Fichiers statiques
│   │   └── restaurant/
│   │       ├── css/
│   │       │   └── style.css       # Styles CSS personnalisés
│   │       ├── js/                 # JavaScript (optionnel)
│   │       └── images/             # Images du site
│   │
│   ├── templates/                  # Templates HTML
│   │   └── restaurant/
│   │       ├── base.html           # Template de base
│   │       ├── restaurant_list.html
│   │       ├── make_reservation.html
│   │       ├── reservation_success.html
│   │       ├── dashboard.html
│   │       ├── login.html
│   │       └── register.html
│   │
│   ├── __init__.py                 # Package Python
│   ├── admin.py                    # Configuration interface admin
│   ├── apps.py                     # Configuration de l'app
│   ├── models.py                   # Modèles de données
│   ├── views.py                    # Vues (logique métier)
│   ├── forms.py                    # Formulaires Django
│   ├── urls.py                     # URLs de l'application
│   ├── serializers.py              # Sérialiseurs pour l'API
│   ├── api_views.py                # Vues API REST
│   ├── api_urls.py                 # URLs de l'API
│   └── tests.py                    # Tests unitaires
│
├── venv/                           # Environnement virtuel Python
├── db.sqlite3                      # Base de données SQLite
├── manage.py                       # Script de gestion Django
├── populate_data.py                # Script de données d'exemple
├── requirements.txt                # Dépendances Python
├── .gitignore                      # Fichiers à ignorer par Git
└── README.md                       # Documentation utilisateur
```

### Flux de Données

```
1. REQUÊTE HTTP
   └─> urls.py (routing)
       └─> views.py (traitement)
           ├─> models.py (accès BDD)
           │   └─> ORM Django
           │       └─> Base de données
           └─> templates/ (rendu HTML)
               └─> RÉPONSE HTTP
```

---

## 3. Technologies Utilisées

### Backend

#### Python 3.9+
```python
# Langage de programmation principal
# Caractéristiques :
- Syntaxe claire et lisible
- Typage dynamique
- Orienté objet
- Large écosystème de bibliothèques
```

#### Django 5.2
```python
# Framework web principal
# Fonctionnalités utilisées :
- ORM (Object-Relational Mapping)
- Système de templates
- Middleware de sécurité
- Gestion des sessions
- Système d'authentification
- Interface d'administration
```

#### Django REST Framework
```python
# Extension pour créer des APIs REST
# Permet :
- Sérialisation des données
- Vues API
- Authentification API
- Pagination
- Filtrage
```

### Base de Données

#### SQLite (développement)
```sql
-- Base de données embarquée
-- Avantages :
- Pas de serveur nécessaire
- Fichier unique (db.sqlite3)
- Parfait pour le développement
- Configuration zéro
```

#### PostgreSQL (production recommandée)
```sql
-- Base de données relationnelle robuste
-- Avantages :
- Performance supérieure
- Transactions ACID complètes
- Meilleure concurrence
- Fonctionnalités avancées
```

### Frontend

#### HTML5
```html
<!-- Structure sémantique -->
- Balises sémantiques (<section>, <article>, <nav>)
- Formulaires HTML5 (type="date", type="time")
- Accessibilité (labels, aria-*)
```

#### CSS3
```css
/* Design moderne et responsive */
- Variables CSS (--primary-color)
- Flexbox et Grid
- Animations et transitions
- Media queries (responsive)
- Gradients
```

#### JavaScript (Vanilla)
```javascript
// Validation côté client
// Interactions utilisateur
// Améliorations progressives
```

### Outils de Développement

```bash
# Git - Contrôle de version
# pip - Gestionnaire de paquets Python
# venv - Environnement virtuel
# Django Debug Toolbar (optionnel)
# pytest (tests)
```

---

## 4. Modèles de Données

### Concept de l'ORM Django

L'**ORM (Object-Relational Mapping)** permet de manipuler la base de données avec des objets Python au lieu de SQL brut.

```python
# Au lieu d'écrire :
cursor.execute("SELECT * FROM restaurant WHERE id = 1")

# On écrit :
restaurant = Restaurant.objects.get(id=1)
```

### Modèle Restaurant

**Fichier** : `restaurant/models.py`

```python
from django.db import models
from django.utils import timezone

class Restaurant(models.Model):
    # Champs du modèle
    name = models.CharField(max_length=100)
    # CharField = Texte court (jusqu'à max_length)

    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)

    description = models.TextField(blank=True, null=True)
    # TextField = Texte long, blank=True permet champ vide

    image = models.URLField(blank=True, null=True,
                           help_text="URL de l'image du restaurant")
    # URLField = Validation automatique d'URL

    cuisine_type = models.CharField(max_length=50, blank=True, null=True)
    # Type de cuisine (Français, Italien, etc.)

    opening_time = models.TimeField(blank=True, null=True)
    closing_time = models.TimeField(blank=True, null=True)
    # TimeField = Heure (HH:MM:SS)

    rating = models.DecimalField(
        max_digits=3,
        decimal_places=1,
        blank=True,
        null=True,
        default=4.5
    )
    # DecimalField = Nombre décimal précis (ex: 4.5)

    created_at = models.DateTimeField(default=timezone.now)
    # DateTimeField = Date et heure complète

    def __str__(self):
        # Représentation en chaîne de caractères
        return self.name

    class Meta:
        # Métadonnées du modèle
        ordering = ['-rating', 'name']
        # Tri par défaut : rating décroissant, puis nom
```

**Explication des types de champs** :

| Type de champ | Utilisation | Type SQL |
|--------------|-------------|----------|
| `CharField` | Texte court | VARCHAR |
| `TextField` | Texte long | TEXT |
| `IntegerField` | Nombre entier | INTEGER |
| `DecimalField` | Nombre décimal précis | DECIMAL |
| `DateField` | Date | DATE |
| `TimeField` | Heure | TIME |
| `DateTimeField` | Date et heure | DATETIME |
| `BooleanField` | Vrai/Faux | BOOLEAN |
| `URLField` | URL validée | VARCHAR |
| `ForeignKey` | Relation Many-to-One | INTEGER (clé étrangère) |

### Modèle Table

```python
class Table(models.Model):
    restaurant = models.ForeignKey(
        Restaurant,
        on_delete=models.CASCADE,
        related_name='tables'
    )
    # ForeignKey = Relation Many-to-One
    # on_delete=CASCADE : si restaurant supprimé, tables supprimées aussi
    # related_name='tables' : permet restaurant.tables.all()

    number = models.IntegerField()
    # Numéro de la table

    capacity = models.IntegerField()
    # Nombre de places

    is_available = models.BooleanField(default=True)
    # Disponibilité de la table

    def __str__(self):
        return f"Table {self.number} ({self.capacity} places)"

    class Meta:
        unique_together = ['restaurant', 'number']
        # Contrainte : pas deux tables avec le même numéro dans un restaurant
        ordering = ['number']
```

**Relations entre modèles** :

```
Restaurant (1) ←──── (N) Table
     │
     │ Un restaurant a plusieurs tables
     │ Une table appartient à un restaurant
     │
     └─> restaurant.tables.all()  # Récupère toutes les tables
```

### Modèle Reservation

```python
class Reservation(models.Model):
    STATUS_CHOICES = [
        ('pending', 'En attente'),
        ('confirmed', 'Confirmée'),
        ('cancelled', 'Annulée'),
        ('completed', 'Terminée'),
    ]
    # Choices = Liste de valeurs prédéfinies

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='reservations'
    )
    # Relation avec le modèle User de Django

    table = models.ForeignKey(
        Table,
        on_delete=models.CASCADE,
        related_name='reservations'
    )

    date = models.DateField()
    time = models.TimeField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending'
    )
    # Le champ n'accepte que les valeurs dans STATUS_CHOICES

    guests = models.IntegerField(default=2)
    special_requests = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    # auto_now=True : mise à jour automatique à chaque save()

    def __str__(self):
        return f"{self.user.username} - Table {self.table.number} on {self.date} at {self.time}"

    class Meta:
        ordering = ['-date', '-time']
        # Tri par date et heure décroissantes
```

**Schéma de base de données généré** :

```sql
-- Table restaurant_restaurant
CREATE TABLE restaurant_restaurant (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(100) NOT NULL,
    address VARCHAR(200) NOT NULL,
    phone VARCHAR(20) NOT NULL,
    description TEXT,
    image VARCHAR(200),
    cuisine_type VARCHAR(50),
    opening_time TIME,
    closing_time TIME,
    rating DECIMAL(3, 1),
    created_at DATETIME NOT NULL
);

-- Table restaurant_table
CREATE TABLE restaurant_table (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    restaurant_id INTEGER NOT NULL REFERENCES restaurant_restaurant(id),
    number INTEGER NOT NULL,
    capacity INTEGER NOT NULL,
    is_available BOOLEAN NOT NULL DEFAULT 1,
    UNIQUE(restaurant_id, number)
);

-- Table restaurant_reservation
CREATE TABLE restaurant_reservation (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL REFERENCES auth_user(id),
    table_id INTEGER NOT NULL REFERENCES restaurant_table(id),
    date DATE NOT NULL,
    time TIME NOT NULL,
    status VARCHAR(20) NOT NULL DEFAULT 'pending',
    guests INTEGER NOT NULL DEFAULT 2,
    special_requests TEXT,
    created_at DATETIME NOT NULL,
    updated_at DATETIME NOT NULL
);
```

### Opérations CRUD avec l'ORM

```python
# CREATE - Créer un restaurant
restaurant = Restaurant.objects.create(
    name="Le Gourmet",
    address="15 Rue de la Paix",
    phone="+33 1 23 45 67 89",
    cuisine_type="Français",
    rating=4.8
)

# READ - Lire les données
# Tous les restaurants
all_restaurants = Restaurant.objects.all()

# Un restaurant spécifique
restaurant = Restaurant.objects.get(id=1)

# Filtrer
french_restaurants = Restaurant.objects.filter(cuisine_type="Français")
good_restaurants = Restaurant.objects.filter(rating__gte=4.5)  # >= 4.5

# UPDATE - Mettre à jour
restaurant = Restaurant.objects.get(id=1)
restaurant.rating = 4.9
restaurant.save()

# Ou en une ligne
Restaurant.objects.filter(id=1).update(rating=4.9)

# DELETE - Supprimer
restaurant = Restaurant.objects.get(id=1)
restaurant.delete()

# Ou en une ligne
Restaurant.objects.filter(id=1).delete()
```

**Requêtes avancées** :

```python
# Jointures automatiques
# Récupérer toutes les réservations avec les infos de table et restaurant
reservations = Reservation.objects.select_related(
    'table',
    'table__restaurant'
).all()

# Évite les requêtes N+1
restaurants = Restaurant.objects.prefetch_related('tables').all()

# Agrégation
from django.db.models import Count, Avg
Restaurant.objects.aggregate(
    total=Count('id'),
    avg_rating=Avg('rating')
)

# Annotation
from django.db.models import Count
restaurants = Restaurant.objects.annotate(
    num_tables=Count('tables')
)
```

---

## 5. Vues et Templates

### Types de Vues Django

#### 1. Function-Based Views (FBV)

**Fichier** : `restaurant/views.py`

```python
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

# Vue fonction simple
def reservation_success(request):
    """
    Affiche la page de succès après une réservation

    Args:
        request: Objet HttpRequest contenant les données de la requête

    Returns:
        HttpResponse avec le template rendu
    """
    return render(request, 'restaurant/reservation_success.html')

# Vue avec décorateur de sécurité
@login_required(login_url='login')
def user_dashboard(request):
    """
    Affiche le tableau de bord utilisateur avec ses réservations
    Nécessite une authentification
    """
    # Récupérer les réservations de l'utilisateur connecté
    reservations = Reservation.objects.filter(
        user=request.user
    ).select_related(
        'table',
        'table__restaurant'
    ).order_by('-date', '-time')

    # Passer les données au template
    context = {
        'reservations': reservations
    }

    return render(request, 'restaurant/dashboard.html', context)

# Vue avec traitement POST
@login_required(login_url='login')
def cancel_reservation(request, reservation_id):
    """
    Annule une réservation
    """
    # get_object_or_404 retourne 404 si non trouvé
    reservation = get_object_or_404(
        Reservation,
        id=reservation_id,
        user=request.user  # Sécurité : vérifier que c'est bien sa réservation
    )

    if request.method == 'POST':
        if reservation.status in ['pending', 'confirmed']:
            reservation.status = 'cancelled'
            reservation.save()
            messages.success(request, 'Votre réservation a été annulée.')
        else:
            messages.error(request, 'Cette réservation ne peut pas être annulée.')

    return redirect('user_dashboard')
```

#### 2. Class-Based Views (CBV)

```python
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

# Vue basée sur une classe pour lister
class RestaurantListView(ListView):
    """
    Affiche la liste des restaurants
    ListView automatise :
    - Récupération des objets
    - Pagination
    - Passage au template
    """
    model = Restaurant
    template_name = 'restaurant/restaurant_list.html'
    context_object_name = 'restaurants'

    def get_queryset(self):
        """
        Personnaliser la requête
        Précharge les tables pour optimisation
        """
        return Restaurant.objects.prefetch_related('tables').all()

# Vue pour créer des objets
class ReservationCreateView(LoginRequiredMixin, CreateView):
    """
    Crée une réservation
    CreateView automatise :
    - Affichage du formulaire
    - Validation
    - Sauvegarde
    - Redirection
    """
    model = Reservation
    form_class = ReservationForm
    template_name = 'restaurant/make_reservation.html'
    success_url = reverse_lazy('reservation_success')
    login_url = reverse_lazy('login')

    def form_valid(self, form):
        """
        Appelé quand le formulaire est valide
        Permet de modifier l'objet avant sauvegarde
        """
        # Assigner l'utilisateur connecté à la réservation
        form.instance.user = self.request.user

        # Message de succès
        messages.success(
            self.request,
            'Votre réservation a été confirmée avec succès !'
        )

        return super().form_valid(form)

    def form_invalid(self, form):
        """
        Appelé quand le formulaire est invalide
        """
        messages.error(
            self.request,
            'Une erreur est survenue. Veuillez vérifier les informations.'
        )
        return super().form_invalid(form)
```

**Comparaison FBV vs CBV** :

| Aspect | FBV | CBV |
|--------|-----|-----|
| **Lisibilité** | Plus explicite | Plus concise |
| **Réutilisabilité** | Moins | Plus (héritage) |
| **Flexibilité** | Total | Structure imposée |
| **Apprentissage** | Plus facile | Courbe d'apprentissage |
| **CRUD** | Code répétitif | Automatisé |

### Système de Templates Django

#### Template de Base

**Fichier** : `restaurant/templates/restaurant/base.html`

```django
{% load static %}
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    {# Block pour le titre personnalisé #}
    <title>{% block title %}Restaurant Reservation{% endblock %}</title>

    {# Chargement du CSS #}
    <link rel="stylesheet" href="{% static 'restaurant/css/style.css' %}">

    {# Block pour CSS supplémentaire #}
    {% block extra_css %}{% endblock %}
</head>
<body>
    {# Navigation #}
    <nav class="navbar">
        <div class="container">
            <a href="{% url 'restaurant_list' %}" class="navbar-brand">
                <span>🍽️</span> Restaurant Reservation
            </a>
            <ul class="navbar-menu">
                <li><a href="{% url 'restaurant_list' %}">Accueil</a></li>

                {# Affichage conditionnel selon authentification #}
                {% if user.is_authenticated %}
                    <li><a href="{% url 'user_dashboard' %}">Mes Réservations</a></li>
                    <li><a href="{% url 'make_reservation' %}" class="btn btn-primary">Réserver</a></li>
                    <li><a href="{% url 'logout' %}">Déconnexion ({{ user.username }})</a></li>
                {% else %}
                    <li><a href="{% url 'login' %}">Connexion</a></li>
                    <li><a href="{% url 'register' %}" class="btn btn-primary">S'inscrire</a></li>
                {% endif %}
            </ul>
        </div>
    </nav>

    {# Messages flash #}
    {% if messages %}
        <div class="container" style="margin-top: 2rem;">
            {% for message in messages %}
                <div class="alert alert-{{ message.tags }}">
                    {{ message }}
                </div>
            {% endfor %}
        </div>
    {% endif %}

    {# Contenu principal #}
    <main>
        {% block content %}{% endblock %}
    </main>

    {# Footer #}
    <footer class="footer">
        <div class="container">
            <p>&copy; 2024 Restaurant Reservation. Tous droits réservés.</p>
        </div>
    </footer>

    {# Block pour JavaScript supplémentaire #}
    {% block extra_js %}{% endblock %}
</body>
</html>
```

**Tags de Template Django** :

```django
{# Commentaire - non visible dans le HTML généré #}

{{ variable }}
{# Affiche une variable #}

{% tag %}
{# Exécute une balise de template #}

{% if condition %}
    ...
{% elif autre_condition %}
    ...
{% else %}
    ...
{% endif %}
{# Structure conditionnelle #}

{% for item in liste %}
    {{ item }}
    {% empty %}
    <p>Liste vide</p>
{% endfor %}
{# Boucle for #}

{% url 'nom_url' %}
{# Génère une URL à partir de son nom #}

{% static 'chemin/fichier.css' %}
{# Génère l'URL d'un fichier statique #}

{% block nom_block %}{% endblock %}
{# Définit un block pour héritage #}

{% extends 'base.html' %}
{# Hérite d'un template parent #}

{% include 'partial.html' %}
{# Inclut un autre template #}

{% load static %}
{# Charge un module de tags #}
```

#### Template avec Héritage

**Fichier** : `restaurant/templates/restaurant/restaurant_list.html`

```django
{% extends 'restaurant/base.html' %}

{% block title %}Restaurants - Restaurant Reservation{% endblock %}

{% block content %}
{# Hero Section #}
<section class="hero">
    <div class="container">
        <h1>🍽️ Découvrez nos Restaurants</h1>
        <p>Réservez une table dans les meilleurs restaurants en quelques clics</p>
    </div>
</section>

{# Liste des restaurants #}
<section class="container">
    {% if restaurants %}
        <div class="restaurants-grid">
            {% for restaurant in restaurants %}
            <div class="restaurant-card">
                {# Image conditionnelle #}
                {% if restaurant.image %}
                    <img src="{{ restaurant.image }}" alt="{{ restaurant.name }}" class="restaurant-image">
                {% else %}
                    <div class="restaurant-image" style="display: flex; align-items: center; justify-content: center; font-size: 4rem;">
                        🍽️
                    </div>
                {% endif %}

                <div class="restaurant-info">
                    <h2 class="restaurant-name">{{ restaurant.name }}</h2>

                    {# Filtres de template #}
                    {% if restaurant.description %}
                        <p>{{ restaurant.description|truncatewords:20 }}</p>
                    {% endif %}

                    <p>📍 {{ restaurant.address }}</p>
                    <p>📞 {{ restaurant.phone }}</p>

                    {# Formatage de date/heure #}
                    {% if restaurant.opening_time and restaurant.closing_time %}
                        <p>🕐 {{ restaurant.opening_time|time:"H:i" }} - {{ restaurant.closing_time|time:"H:i" }}</p>
                    {% endif %}

                    {# Relation Many-to-One #}
                    {% if restaurant.tables.all %}
                        <div class="tables-list">
                            <h4>Tables disponibles</h4>
                            {% for table in restaurant.tables.all %}
                                {% if table.is_available %}
                                    <span class="table-item">
                                        Table {{ table.number }} ({{ table.capacity }} places)
                                    </span>
                                {% endif %}
                            {% endfor %}
                        </div>
                    {% endif %}

                    {# Génération d'URL #}
                    <a href="{% url 'make_reservation' %}" class="btn btn-primary">
                        Réserver une table
                    </a>
                </div>
            </div>
            {% endfor %}
        </div>
    {% else %}
        {# État vide #}
        <div class="empty-state">
            <h3>Aucun restaurant disponible</h3>
            <p>Revenez bientôt pour découvrir nos restaurants partenaires!</p>
        </div>
    {% endif %}
</section>
{% endblock %}
```

**Filtres de Template Communs** :

```django
{{ value|lower }}           {# Minuscules #}
{{ value|upper }}           {# Majuscules #}
{{ value|title }}           {# Titre (première lettre en majuscule) #}
{{ value|truncatewords:20 }} {# Tronquer à 20 mots #}
{{ value|date:"d/m/Y" }}    {# Formater une date #}
{{ value|time:"H:i" }}      {# Formater une heure #}
{{ value|default:"N/A" }}   {# Valeur par défaut si vide #}
{{ value|length }}          {# Longueur #}
{{ value|first }}           {# Premier élément #}
{{ value|last }}            {# Dernier élément #}
{{ value|join:", " }}       {# Joindre avec séparateur #}
{{ value|safe }}            {# Marquer comme HTML sûr #}
```

### Context Processors

Les context processors ajoutent automatiquement des variables à tous les templates :

```python
# Disponibles par défaut :
{{ user }}          # Utilisateur connecté
{{ request }}       # Objet request
{{ messages }}      # Messages flash
{{ perms }}         # Permissions
```

---

## 6. Formulaires

### Formulaires Django

#### FormModel de base

**Fichier** : `restaurant/forms.py`

```python
from django import forms
from .models import Reservation

class ReservationForm(forms.ModelForm):
    """
    Formulaire basé sur le modèle Reservation
    ModelForm génère automatiquement les champs à partir du modèle
    """

    class Meta:
        model = Reservation
        fields = ['table', 'date', 'time', 'guests', 'special_requests']

        # Widgets personnalisés pour le rendu HTML
        widgets = {
            'date': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control',
                'placeholder': 'Sélectionnez une date'
            }),
            'time': forms.TimeInput(attrs={
                'type': 'time',
                'class': 'form-control',
                'placeholder': 'Sélectionnez une heure'
            }),
            'table': forms.Select(attrs={
                'class': 'form-control'
            }),
            'guests': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre de personnes',
                'min': '1',
                'max': '20'
            }),
            'special_requests': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Demandes spéciales (allergies, occasion spéciale, etc.)',
                'rows': '3'
            }),
        }

        # Labels personnalisés
        labels = {
            'table': 'Table',
            'date': 'Date',
            'time': 'Heure',
            'guests': 'Nombre de personnes',
            'special_requests': 'Demandes spéciales',
        }
```

#### Formulaire d'Inscription

```python
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegistrationForm(UserCreationForm):
    """
    Formulaire d'inscription utilisateur
    Étend UserCreationForm de Django
    """

    # Champs supplémentaires
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Email'
        })
    )

    first_name = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Prénom'
        })
    )

    last_name = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Nom'
        })
    )

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
        ]
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Nom d'utilisateur"
            }),
        }

    def __init__(self, *args, **kwargs):
        """
        Constructeur pour personnaliser les champs hérités
        """
        super(UserRegistrationForm, self).__init__(*args, **kwargs)

        # Personnaliser les champs password
        self.fields['password1'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Mot de passe'
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Confirmer le mot de passe'
        })

    def clean_email(self):
        """
        Validation personnalisée pour l'email
        """
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Cet email est déjà utilisé.')
        return email
```

### Validation de Formulaires

```python
class ReservationForm(forms.ModelForm):
    # ... (champs précédents)

    def clean_date(self):
        """
        Validation personnalisée pour la date
        """
        date = self.cleaned_data.get('date')

        # Vérifier que la date n'est pas dans le passé
        from datetime import date as dt_date
        if date < dt_date.today():
            raise forms.ValidationError(
                'La date de réservation ne peut pas être dans le passé.'
            )

        return date

    def clean_guests(self):
        """
        Validation pour le nombre de personnes
        """
        guests = self.cleaned_data.get('guests')

        if guests < 1:
            raise forms.ValidationError(
                'Le nombre de personnes doit être au moins 1.'
            )

        if guests > 20:
            raise forms.ValidationError(
                'Le nombre maximum de personnes est 20.'
            )

        return guests

    def clean(self):
        """
        Validation globale du formulaire
        """
        cleaned_data = super().clean()
        date = cleaned_data.get('date')
        time = cleaned_data.get('time')
        table = cleaned_data.get('table')

        # Vérifier si la table est déjà réservée
        if date and time and table:
            existing = Reservation.objects.filter(
                table=table,
                date=date,
                time=time,
                status__in=['pending', 'confirmed']
            ).exists()

            if existing:
                raise forms.ValidationError(
                    'Cette table est déjà réservée à cette date et heure.'
                )

        return cleaned_data
```

### Rendu de Formulaire dans Template

```django
<form method="post">
    {% csrf_token %}

    {# Erreurs non liées à un champ spécifique #}
    {% if form.non_field_errors %}
        <div class="alert alert-error">
            {{ form.non_field_errors }}
        </div>
    {% endif %}

    {# Méthode 1 : Rendu automatique #}
    {{ form.as_p }}

    {# Méthode 2 : Rendu personnalisé #}
    <div class="form-group">
        <label for="{{ form.date.id_for_label }}">
            {{ form.date.label }}
        </label>
        {{ form.date }}
        {% if form.date.errors %}
            <div class="alert alert-error">
                {{ form.date.errors }}
            </div>
        {% endif %}
    </div>

    <button type="submit" class="btn btn-primary">
        Soumettre
    </button>
</form>
```

---

## 7. Système d'Authentification

### Vue de Connexion Personnalisée

```python
from django.contrib.auth.views import LoginView
from django.contrib import messages

class CustomLoginView(LoginView):
    """
    Vue de connexion personnalisée
    Hérite de LoginView de Django
    """
    template_name = 'restaurant/login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        """
        URL de redirection après connexion réussie
        """
        return reverse_lazy('restaurant_list')

    def form_valid(self, form):
        """
        Appelé quand le formulaire est valide
        """
        username = form.get_user().username
        messages.success(
            self.request,
            f'Bienvenue, {username} !'
        )
        return super().form_valid(form)

    def form_invalid(self, form):
        """
        Appelé quand le formulaire est invalide
        """
        messages.error(
            self.request,
            'Nom d\'utilisateur ou mot de passe incorrect.'
        )
        return super().form_invalid(form)
```

### Vue d'Inscription

```python
from django.contrib.auth import login

def register(request):
    """
    Vue d'inscription utilisateur
    """
    # Si déjà connecté, rediriger
    if request.user.is_authenticated:
        return redirect('restaurant_list')

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            # Créer l'utilisateur
            user = form.save()

            # Connecter automatiquement après inscription
            login(request, user)

            messages.success(
                request,
                f'Bienvenue, {user.username} ! Votre compte a été créé avec succès.'
            )
            return redirect('restaurant_list')
        else:
            messages.error(
                request,
                'Veuillez corriger les erreurs ci-dessous.'
            )
    else:
        form = UserRegistrationForm()

    return render(request, 'restaurant/register.html', {'form': form})
```

### Décorateurs d'Authentification

```python
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Function-Based View
@login_required(login_url='login')
def user_dashboard(request):
    # Accessible uniquement si connecté
    pass

# Class-Based View
class ReservationCreateView(LoginRequiredMixin, CreateView):
    login_url = 'login'
    # Accessible uniquement si connecté
    pass
```

### Gestion des Permissions

```python
from django.contrib.auth.decorators import permission_required

@permission_required('restaurant.can_manage_reservations')
def manage_reservations(request):
    # Accessible uniquement avec la permission
    pass

# Dans le template
{% if perms.restaurant.can_manage_reservations %}
    <a href="{% url 'manage_reservations' %}">Gérer</a>
{% endif %}
```

---

## 8. Interface d'Administration

### Configuration Admin Avancée

**Fichier** : `restaurant/admin.py`

```python
from django.contrib import admin
from .models import Restaurant, Table, Reservation

@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    """
    Configuration personnalisée de l'admin Restaurant
    """

    # Colonnes affichées dans la liste
    list_display = [
        'name',
        'cuisine_type',
        'address',
        'phone',
        'rating',
        'created_at'
    ]

    # Filtres dans la sidebar
    list_filter = [
        'cuisine_type',
        'rating',
        'created_at'
    ]

    # Champs de recherche
    search_fields = [
        'name',
        'address',
        'cuisine_type'
    ]

    # Tri par défaut
    ordering = ['-rating', 'name']

    # Champs en lecture seule
    readonly_fields = ['created_at']

    # Organisation des champs dans le formulaire
    fieldsets = (
        ('Informations de base', {
            'fields': ('name', 'cuisine_type', 'rating')
        }),
        ('Contact', {
            'fields': ('address', 'phone')
        }),
        ('Détails', {
            'fields': ('description', 'image', 'opening_time', 'closing_time'),
            'classes': ('collapse',)  # Section repliable
        }),
        ('Informations système', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        }),
    )

@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    """
    Configuration admin Table
    """
    list_display = [
        'restaurant',
        'number',
        'capacity',
        'is_available'
    ]

    list_filter = [
        'restaurant',
        'is_available',
        'capacity'
    ]

    search_fields = [
        'restaurant__name',
        'number'
    ]

    # Champs modifiables directement dans la liste
    list_editable = ['is_available']

    ordering = ['restaurant', 'number']

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    """
    Configuration admin Reservation
    """
    list_display = [
        'user',
        'table',
        'date',
        'time',
        'guests',
        'status',
        'created_at'
    ]

    list_filter = [
        'status',
        'date',
        'created_at'
    ]

    search_fields = [
        'user__username',
        'user__email',
        'table__restaurant__name'
    ]

    list_editable = ['status']

    ordering = ['-date', '-time']

    # Navigation par date
    date_hierarchy = 'date'

    fieldsets = (
        ('Informations de base', {
            'fields': ('user', 'table', 'date', 'time')
        }),
        ('Détails de la réservation', {
            'fields': ('guests', 'status', 'special_requests')
        }),
        ('Informations système', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    readonly_fields = ('created_at', 'updated_at')

    # Actions personnalisées
    actions = ['mark_as_confirmed', 'mark_as_cancelled']

    def mark_as_confirmed(self, request, queryset):
        """
        Action pour confirmer plusieurs réservations
        """
        updated = queryset.update(status='confirmed')
        self.message_user(
            request,
            f'{updated} réservation(s) confirmée(s).'
        )
    mark_as_confirmed.short_description = "Marquer comme confirmée"

    def mark_as_cancelled(self, request, queryset):
        """
        Action pour annuler plusieurs réservations
        """
        updated = queryset.update(status='cancelled')
        self.message_user(
            request,
            f'{updated} réservation(s) annulée(s).'
        )
    mark_as_cancelled.short_description = "Marquer comme annulée"
```

### Personnalisation du Site Admin

```python
# Dans admin.py
admin.site.site_header = "Administration Restaurant Reservation"
admin.site.site_title = "Restaurant Admin"
admin.site.index_title = "Bienvenue dans l'administration"
```

---

## 9. API REST

### Sérialiseurs

**Fichier** : `restaurant/serializers.py`

```python
from rest_framework import serializers
from .models import Restaurant, Table, Reservation

class RestaurantSerializer(serializers.ModelSerializer):
    """
    Sérialiseur pour le modèle Restaurant
    Convertit les objets Python en JSON et vice-versa
    """

    class Meta:
        model = Restaurant
        fields = '__all__'  # Tous les champs
        # Ou spécifier : fields = ['id', 'name', 'address', ...]

class TableSerializer(serializers.ModelSerializer):
    """
    Sérialiseur pour le modèle Table
    """
    # Inclure des informations du restaurant
    restaurant_name = serializers.CharField(
        source='restaurant.name',
        read_only=True
    )

    class Meta:
        model = Table
        fields = [
            'id',
            'restaurant',
            'restaurant_name',
            'number',
            'capacity',
            'is_available'
        ]

class ReservationSerializer(serializers.ModelSerializer):
    """
    Sérialiseur pour le modèle Reservation
    """
    # Champs en lecture seule
    user_username = serializers.CharField(
        source='user.username',
        read_only=True
    )
    table_number = serializers.IntegerField(
        source='table.number',
        read_only=True
    )
    restaurant_name = serializers.CharField(
        source='table.restaurant.name',
        read_only=True
    )

    class Meta:
        model = Reservation
        fields = [
            'id',
            'user',
            'user_username',
            'table',
            'table_number',
            'restaurant_name',
            'date',
            'time',
            'status',
            'guests',
            'special_requests',
            'created_at',
            'updated_at'
        ]
        read_only_fields = ['created_at', 'updated_at']
```

### Vues API

**Fichier** : `restaurant/api_views.py`

```python
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Restaurant, Table, Reservation
from .serializers import (
    RestaurantSerializer,
    TableSerializer,
    ReservationSerializer
)

class RestaurantViewSet(viewsets.ModelViewSet):
    """
    ViewSet pour les opérations CRUD sur Restaurant

    GET /api/restaurants/        - Liste tous les restaurants
    POST /api/restaurants/       - Crée un restaurant
    GET /api/restaurants/{id}/   - Détails d'un restaurant
    PUT /api/restaurants/{id}/   - Met à jour un restaurant
    DELETE /api/restaurants/{id}/ - Supprime un restaurant
    """
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class TableViewSet(viewsets.ModelViewSet):
    """
    ViewSet pour les opérations CRUD sur Table
    """
    queryset = Table.objects.all()
    serializer_class = TableSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class ReservationViewSet(viewsets.ModelViewSet):
    """
    ViewSet pour les opérations CRUD sur Reservation
    """
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        """
        Filtrer les réservations par utilisateur si authentifié
        """
        queryset = super().get_queryset()
        if self.request.user.is_authenticated:
            # L'utilisateur voit seulement ses réservations
            return queryset.filter(user=self.request.user)
        return queryset.none()
```

### Configuration des URLs API

**Fichier** : `restaurant/api_urls.py`

```python
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_views import (
    RestaurantViewSet,
    TableViewSet,
    ReservationViewSet
)

# Le router génère automatiquement les URLs
router = DefaultRouter()
router.register(r'restaurants', RestaurantViewSet)
router.register(r'tables', TableViewSet)
router.register(r'reservations', ReservationViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
```

**Exemples de requêtes API** :

```bash
# GET - Liste des restaurants
curl http://127.0.0.1:8000/api/restaurants/

# POST - Créer un restaurant
curl -X POST http://127.0.0.1:8000/api/restaurants/ \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Le Nouveau Restaurant",
    "address": "123 Rue Example",
    "phone": "+33 1 23 45 67 89",
    "cuisine_type": "Français"
  }'

# GET - Détails d'un restaurant
curl http://127.0.0.1:8000/api/restaurants/1/

# PUT - Mettre à jour
curl -X PUT http://127.0.0.1:8000/api/restaurants/1/ \
  -H "Content-Type: application/json" \
  -d '{"rating": 4.9}'

# DELETE - Supprimer
curl -X DELETE http://127.0.0.1:8000/api/restaurants/1/
```

---

## 10. Frontend et CSS

### Architecture CSS

```css
/* Variables CSS pour cohérence */
:root {
    --primary-color: #ff6b6b;      /* Rouge pour boutons principaux */
    --secondary-color: #4ecdc4;    /* Teal pour accents */
    --dark-color: #2c3e50;         /* Texte principal */
    --light-color: #ecf0f1;        /* Arrière-plans clairs */
    --text-color: #333;            /* Texte normal */
    --border-radius: 12px;         /* Rayon des bordures */
    --transition: all 0.3s ease;   /* Transitions fluides */
}

/* Réinitialisation */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

/* Typographie de base */
body {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    line-height: 1.6;
    color: var(--text-color);
    background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
    min-height: 100vh;
}
```

### Système de Grid Responsive

```css
/* Grid pour les cartes restaurant */
.restaurants-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
    gap: 2rem;
    padding: 2rem 0;
}

/* Media queries pour responsive */
@media (max-width: 768px) {
    .restaurants-grid {
        grid-template-columns: 1fr;
    }

    .navbar-menu {
        flex-direction: column;
    }
}
```

### Animations et Transitions

```css
/* Effets de survol sur les cartes */
.restaurant-card {
    transition: var(--transition);
}

.restaurant-card:hover {
    transform: translateY(-10px);
    box-shadow: 0 10px 30px rgba(0,0,0,0.2);
}

/* Animation de chargement */
@keyframes spin {
    to { transform: rotate(360deg); }
}

.loading {
    animation: spin 1s ease-in-out infinite;
}
```

### Système de Boutons

```css
.btn {
    padding: 0.7rem 1.5rem;
    border: none;
    border-radius: var(--border-radius);
    cursor: pointer;
    font-size: 1rem;
    font-weight: 600;
    transition: var(--transition);
}

.btn-primary {
    background: var(--primary-color);
    color: white;
}

.btn-primary:hover {
    background: #ff5252;
    transform: translateY(-2px);
    box-shadow: 0 5px 15px rgba(255, 107, 107, 0.3);
}
```

---

## 11. Base de Données et Migrations

### Qu'est-ce qu'une Migration ?

Les migrations sont le système de **versionnement de schéma de base de données** de Django. Elles permettent de :
- Propager les changements de modèles à la base de données
- Maintenir un historique des modifications
- Synchroniser la base de données entre développeurs
- Déployer les changements en production

### Workflow des Migrations

```bash
# 1. Créer une migration après modification des modèles
python manage.py makemigrations

# 2. Voir le SQL généré (optionnel)
python manage.py sqlmigrate restaurant 0004

# 3. Appliquer les migrations
python manage.py migrate

# 4. Voir l'état des migrations
python manage.py showmigrations
```

### Fichier de Migration

**Fichier** : `restaurant/migrations/0004_alter_reservation_options_...py`

```python
from django.db import migrations, models
import django.utils.timezone

class Migration(migrations.Migration):
    """
    Migration générée automatiquement
    """

    dependencies = [
        ('restaurant', '0003_reservation'),
    ]

    operations = [
        # Ajouter un champ
        migrations.AddField(
            model_name='restaurant',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),

        # Modifier un champ
        migrations.AlterField(
            model_name='reservation',
            name='status',
            field=models.CharField(
                choices=[
                    ('pending', 'En attente'),
                    ('confirmed', 'Confirmée'),
                    ('cancelled', 'Annulée'),
                    ('completed', 'Terminée')
                ],
                default='pending',
                max_length=20
            ),
        ),

        # Ajouter une contrainte
        migrations.AlterUniqueTogether(
            name='table',
            unique_together={('restaurant', 'number')},
        ),
    ]
```

### Migration de Données

```python
from django.db import migrations

def populate_ratings(apps, schema_editor):
    """
    Migration de données pour définir les ratings par défaut
    """
    Restaurant = apps.get_model('restaurant', 'Restaurant')
    for restaurant in Restaurant.objects.filter(rating__isnull=True):
        restaurant.rating = 4.5
        restaurant.save()

class Migration(migrations.Migration):
    dependencies = [
        ('restaurant', '0004_...'),
    ]

    operations = [
        migrations.RunPython(populate_ratings),
    ]
```

---

## 12. Sécurité

### Protection CSRF

Django protège automatiquement contre les attaques CSRF (Cross-Site Request Forgery) :

```django
<form method="post">
    {% csrf_token %}
    <!-- Le token CSRF est obligatoire pour les formulaires POST -->
</form>
```

### Protection XSS

Django échappe automatiquement les variables dans les templates :

```django
{{ user_input }}  <!-- Automatiquement échappé -->
{{ user_input|safe }}  <!-- Désactiver l'échappement (attention !) -->
```

### Protection SQL Injection

L'ORM Django protège contre les injections SQL :

```python
# ✅ SÛR - Requête paramétrée
Restaurant.objects.filter(name=user_input)

# ❌ DANGEREUX - SQL brut sans paramètres
Restaurant.objects.raw(f"SELECT * FROM restaurant WHERE name = '{user_input}'")

# ✅ SÛR - SQL brut avec paramètres
Restaurant.objects.raw("SELECT * FROM restaurant WHERE name = %s", [user_input])
```

### Hachage de Mots de Passe

Django utilise PBKDF2 par défaut :

```python
from django.contrib.auth.models import User

# Créer un utilisateur (mot de passe haché automatiquement)
user = User.objects.create_user(
    username='john',
    password='secret123'
)

# Vérifier un mot de passe
user.check_password('secret123')  # True
```

### Configuration de Sécurité

**Fichier** : `django_restaurant/settings.py`

```python
# ❌ Développement
DEBUG = True
ALLOWED_HOSTS = []

# ✅ Production
DEBUG = False
ALLOWED_HOSTS = ['votredomaine.com', 'www.votredomaine.com']

# Secret key (utiliser variables d'environnement)
import os
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'dev-key-only')

# HTTPS
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# Sécurité supplémentaire
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'DENY'
```

---

## 13. Concepts Avancés

### Signaux Django

Les signaux permettent d'exécuter du code automatiquement lors d'événements :

```python
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail

@receiver(post_save, sender=Reservation)
def send_reservation_email(sender, instance, created, **kwargs):
    """
    Envoyer un email après création d'une réservation
    """
    if created:
        send_mail(
            'Confirmation de réservation',
            f'Votre réservation pour le {instance.date} est confirmée.',
            'noreply@restaurant.com',
            [instance.user.email],
        )
```

### Middleware Personnalisé

```python
class RequestLoggingMiddleware:
    """
    Middleware pour logger toutes les requêtes
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Code avant la vue
        print(f"Request: {request.method} {request.path}")

        response = self.get_response(request)

        # Code après la vue
        print(f"Response: {response.status_code}")

        return response
```

### Context Processors

```python
def restaurant_count(request):
    """
    Ajoute le nombre de restaurants à tous les templates
    """
    from restaurant.models import Restaurant
    return {
        'restaurant_count': Restaurant.objects.count()
    }

# Dans settings.py
TEMPLATES = [{
    'OPTIONS': {
        'context_processors': [
            # ... processeurs par défaut
            'restaurant.context_processors.restaurant_count',
        ],
    },
}]
```

### Custom Template Tags

```python
# restaurant/templatetags/restaurant_tags.py
from django import template

register = template.Library()

@register.filter
def stars(rating):
    """
    Convertit un rating en étoiles
    Usage: {{ restaurant.rating|stars }}
    """
    full_stars = int(rating)
    return '⭐' * full_stars

@register.simple_tag
def available_tables_count(restaurant):
    """
    Compte les tables disponibles
    Usage: {% available_tables_count restaurant %}
    """
    return restaurant.tables.filter(is_available=True).count()
```

### Commandes de Management

```python
# restaurant/management/commands/send_reminders.py
from django.core.management.base import BaseCommand
from datetime import date, timedelta
from restaurant.models import Reservation

class Command(BaseCommand):
    help = 'Envoie des rappels pour les réservations du lendemain'

    def handle(self, *args, **options):
        tomorrow = date.today() + timedelta(days=1)
        reservations = Reservation.objects.filter(
            date=tomorrow,
            status='confirmed'
        )

        for reservation in reservations:
            # Envoyer email de rappel
            print(f"Rappel envoyé à {reservation.user.email}")

        self.stdout.write(
            self.style.SUCCESS(
                f'{reservations.count()} rappels envoyés'
            )
        )

# Utilisation :
# python manage.py send_reminders
```

---

## 🎓 Résumé des Concepts Clés

### Django en 10 Points

1. **MVT** : Modèles (données) → Vues (logique) → Templates (présentation)
2. **ORM** : Manipuler la BDD avec Python au lieu de SQL
3. **Migrations** : Versionnement du schéma de base de données
4. **Forms** : Validation et rendu automatique de formulaires
5. **Admin** : Interface d'administration auto-générée
6. **Auth** : Système d'authentification complet intégré
7. **Templates** : Langage de template avec héritage et filtres
8. **URLs** : Routing basé sur des patterns
9. **Sécurité** : Protection CSRF, XSS, SQL injection par défaut
10. **DRY** : Don't Repeat Yourself - code réutilisable

### Architecture de Notre Projet

```
Requête HTTP
    ↓
urls.py (routing)
    ↓
views.py (logique)
    ↓
├─→ models.py (BDD)
│       ↓
│   ORM Django
│       ↓
│   SQLite/PostgreSQL
│
└─→ forms.py (validation)
    ↓
templates/ (rendu)
    ↓
Réponse HTTP
```

### Technologies du Stack

- **Backend** : Python 3.9 + Django 5.2
- **Base de données** : SQLite (dev) / PostgreSQL (prod)
- **Frontend** : HTML5 + CSS3 + JavaScript Vanilla
- **API** : Django REST Framework
- **Authentification** : Django Auth System
- **Admin** : Django Admin Interface

---

## 📚 Ressources pour Aller Plus Loin

### Documentation Officielle
- Django : https://docs.djangoproject.com/
- Django REST Framework : https://www.django-rest-framework.org/
- Python : https://docs.python.org/

### Tutoriels
- Django Girls Tutorial : https://tutorial.djangogirls.org/
- Real Python : https://realpython.com/tutorials/django/
- MDN Django Tutorial : https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django

### Livres Recommandés
- "Django for Beginners" par William S. Vincent
- "Two Scoops of Django" par Daniel Roy Greenfeld
- "Django for APIs" par William S. Vincent

---

**Bonne chance dans votre apprentissage de Django ! 🚀**
