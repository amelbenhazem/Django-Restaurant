"""
Script to populate the database with sample restaurant data
Run this with: python manage.py shell < populate_data.py
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_restaurant.settings')
django.setup()

from restaurant.models import Restaurant, Table
from datetime import time

# Sample restaurant data
restaurants_data = [
    {
        'name': 'Le Gourmet Parisien',
        'address': '15 Rue de la Paix, 75002 Paris',
        'phone': '+33 1 42 61 23 45',
        'description': 'Restaurant gastronomique français proposant une cuisine raffinée dans un cadre élégant. Nos chefs préparent des plats traditionnels avec une touche moderne.',
        'cuisine_type': 'Français',
        'opening_time': time(12, 0),
        'closing_time': time(23, 0),
        'rating': 4.8,
        'image': 'https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?w=800',
    },
    {
        'name': 'Sushi Zen',
        'address': '28 Avenue des Champs-Élysées, 75008 Paris',
        'phone': '+33 1 45 62 78 90',
        'description': 'Expérience authentique de sushi japonais avec des ingrédients frais importés directement du Japon. Bar à sushi et tables privées disponibles.',
        'cuisine_type': 'Japonais',
        'opening_time': time(11, 30),
        'closing_time': time(22, 30),
        'rating': 4.9,
        'image': 'https://images.unsplash.com/photo-1579584425555-c3ce17fd4351?w=800',
    },
    {
        'name': 'Trattoria Bella',
        'address': '42 Rue de Rivoli, 75004 Paris',
        'phone': '+33 1 48 87 12 34',
        'description': 'Trattoria italienne familiale servant des pâtes fraîches, pizzas au feu de bois et vins italiens sélectionnés.',
        'cuisine_type': 'Italien',
        'opening_time': time(12, 0),
        'closing_time': time(23, 30),
        'rating': 4.6,
        'image': 'https://images.unsplash.com/photo-1555396273-367ea4eb4db5?w=800',
    },
    {
        'name': 'La Brasserie du Coin',
        'address': '8 Boulevard Saint-Germain, 75005 Paris',
        'phone': '+33 1 43 54 67 89',
        'description': 'Brasserie parisienne traditionnelle avec terrasse, proposant des plats classiques français dans une ambiance conviviale.',
        'cuisine_type': 'Brasserie',
        'opening_time': time(8, 0),
        'closing_time': time(1, 0),
        'rating': 4.5,
        'image': 'https://images.unsplash.com/photo-1414235077428-338989a2e8c0?w=800',
    },
    {
        'name': 'Taj Mahal',
        'address': '33 Rue de la Huchette, 75005 Paris',
        'phone': '+33 1 43 26 89 01',
        'description': 'Restaurant indien proposant des currys authentiques, tandooris et naans fraîchement préparés. Ambiance chaleureuse et colorée.',
        'cuisine_type': 'Indien',
        'opening_time': time(11, 0),
        'closing_time': time(23, 0),
        'rating': 4.7,
        'image': 'https://images.unsplash.com/photo-1552566626-52f8b828add9?w=800',
    },
]

print("Creating restaurants...")
for data in restaurants_data:
    restaurant, created = Restaurant.objects.get_or_create(
        name=data['name'],
        defaults=data
    )
    if created:
        print(f"✓ Created: {restaurant.name}")

        # Create tables for each restaurant
        table_configs = [
            (1, 2), (2, 2), (3, 4), (4, 4), (5, 6), (6, 6), (7, 8)
        ]

        for number, capacity in table_configs:
            Table.objects.get_or_create(
                restaurant=restaurant,
                number=number,
                defaults={'capacity': capacity, 'is_available': True}
            )
        print(f"  → Added {len(table_configs)} tables")
    else:
        print(f"○ Already exists: {restaurant.name}")

print("\n✅ Database population complete!")
print("You can now run: python manage.py runserver")
