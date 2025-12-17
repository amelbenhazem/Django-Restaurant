from django.views.generic.edit import CreateView
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Reservation, Restaurant
from .forms import ReservationForm
from django.shortcuts import render

# Page pour créer une réservation


class ReservationCreateView(LoginRequiredMixin, CreateView):
    model = Reservation
    form_class = ReservationForm
    template_name = 'restaurant/make_reservation.html'
    success_url = reverse_lazy('reservation_success')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

# Page pour afficher la liste des restaurants


class RestaurantListView(ListView):
    model = Restaurant
    template_name = 'restaurant/restaurant_list.html'
    context_object_name = 'restaurants'

# Page de succès après réservation


def reservation_success(request):
    return render(request, 'restaurant/reservation_success.html')
