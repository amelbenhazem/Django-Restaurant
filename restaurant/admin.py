from django.contrib import admin
from .models import Restaurant
from .models import Table
from .models import Reservation

# Enregistrer le modèle Restaurant
admin.site.register(Restaurant)
admin.site.register(Table)
admin.site.register(Reservation)
