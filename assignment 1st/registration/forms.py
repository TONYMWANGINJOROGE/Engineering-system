from django import forms
from .models import Register
from .models import employeekin


class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Register
        fields = ['first_name', 'last_name', 'phone_no', 'password']


class employeekinForm(forms.ModelForm):
    class Meta:
        model = employeekin
        fields = ['full_name', 'employee_name', 'ID_no', 'phone_no']
