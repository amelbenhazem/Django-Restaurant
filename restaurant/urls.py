from django.urls import path
from .views import ReservationCreateView, RestaurantListView
from . import views

urlpatterns = [
    path('', RestaurantListView.as_view(), name='restaurant_list'),  # page d'accueil
    path('reserve/', ReservationCreateView.as_view(), name='make_reservation'),
    path('success/', views.reservation_success, name='reservation_success'),
]
