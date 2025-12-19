from django.contrib import admin
from .models import Restaurant, Table, Reservation


# Restaurant Admin
@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ['name', 'cuisine_type', 'address', 'phone', 'rating', 'created_at']
    list_filter = ['cuisine_type', 'rating', 'created_at']
    search_fields = ['name', 'address', 'cuisine_type']
    ordering = ['-rating', 'name']


# Table Admin
@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ['restaurant', 'number', 'capacity', 'is_available']
    list_filter = ['restaurant', 'is_available', 'capacity']
    search_fields = ['restaurant__name', 'number']
    list_editable = ['is_available']
    ordering = ['restaurant', 'number']


# Reservation Admin
@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ['user', 'table', 'date', 'time', 'guests', 'status', 'created_at']
    list_filter = ['status', 'date', 'created_at']
    search_fields = ['user__username', 'user__email', 'table__restaurant__name']
    list_editable = ['status']
    ordering = ['-date', '-time']
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
