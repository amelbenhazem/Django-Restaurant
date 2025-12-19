from django.views.generic.edit import CreateView
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Reservation, Restaurant
from .forms import ReservationForm, UserRegistrationForm


# Restaurant List View
class RestaurantListView(ListView):
    model = Restaurant
    template_name = 'restaurant/restaurant_list.html'
    context_object_name = 'restaurants'

    def get_queryset(self):
        return Restaurant.objects.prefetch_related('tables').all()


# Reservation Create View
class ReservationCreateView(LoginRequiredMixin, CreateView):
    model = Reservation
    form_class = ReservationForm
    template_name = 'restaurant/make_reservation.html'
    success_url = reverse_lazy('reservation_success')
    login_url = reverse_lazy('login')

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, 'Votre réservation a été confirmée avec succès !')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Une erreur est survenue. Veuillez vérifier les informations.')
        return super().form_invalid(form)


# Reservation Success View
def reservation_success(request):
    return render(request, 'restaurant/reservation_success.html')


# User Dashboard View
@login_required(login_url='login')
def user_dashboard(request):
    reservations = Reservation.objects.filter(user=request.user).select_related(
        'table', 'table__restaurant'
    ).order_by('-date', '-time')

    return render(request, 'restaurant/dashboard.html', {
        'reservations': reservations
    })


# Cancel Reservation View
@login_required(login_url='login')
def cancel_reservation(request, reservation_id):
    reservation = get_object_or_404(Reservation, id=reservation_id, user=request.user)

    if request.method == 'POST':
        if reservation.status in ['pending', 'confirmed']:
            reservation.status = 'cancelled'
            reservation.save()
            messages.success(request, 'Votre réservation a été annulée.')
        else:
            messages.error(request, 'Cette réservation ne peut pas être annulée.')

    return redirect('user_dashboard')


# Custom Login View
class CustomLoginView(LoginView):
    template_name = 'restaurant/login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('restaurant_list')

    def form_valid(self, form):
        messages.success(self.request, f'Bienvenue, {form.get_user().username} !')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Nom d\'utilisateur ou mot de passe incorrect.')
        return super().form_invalid(form)


# User Registration View
def register(request):
    if request.user.is_authenticated:
        return redirect('restaurant_list')

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'Bienvenue, {user.username} ! Votre compte a été créé avec succès.')
            return redirect('restaurant_list')
        else:
            messages.error(request, 'Veuillez corriger les erreurs ci-dessous.')
    else:
        form = UserRegistrationForm()

    return render(request, 'restaurant/register.html', {'form': form})
