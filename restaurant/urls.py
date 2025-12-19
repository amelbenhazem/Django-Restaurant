from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import (
    ReservationCreateView,
    RestaurantListView,
    CustomLoginView,
    register,
    reservation_success,
    user_dashboard,
    cancel_reservation
)

urlpatterns = [
    # Home and restaurant pages
    path('', RestaurantListView.as_view(), name='restaurant_list'),

    # Reservation pages
    path('reserve/', ReservationCreateView.as_view(), name='make_reservation'),
    path('success/', reservation_success, name='reservation_success'),
    path('reservation/cancel/<int:reservation_id>/', cancel_reservation, name='cancel_reservation'),

    # User dashboard
    path('dashboard/', user_dashboard, name='user_dashboard'),

    # Authentication pages
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='restaurant_list'), name='logout'),
    path('register/', register, name='register'),
]
