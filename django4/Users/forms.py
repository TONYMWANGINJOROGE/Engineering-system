from django.contrib.auth.forms import UserCreationForm
from django.forms import forms


class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms . EmailField ()
    password = forms.CharField(widget=forms . PasswordInput)