from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Reservation


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['table', 'date', 'time', 'guests', 'special_requests']
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
        labels = {
            'table': 'Table',
            'date': 'Date',
            'time': 'Heure',
            'guests': 'Nombre de personnes',
            'special_requests': 'Demandes spéciales',
        }


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Email'
    }))
    first_name = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Prénom'
    }))
    last_name = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Nom'
    }))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Nom d'utilisateur"
            }),
        }

    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Mot de passe'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Confirmer le mot de passe'})
