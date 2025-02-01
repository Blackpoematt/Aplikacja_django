from django import forms
from .models import Rezerwacje

class LoginForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(max_length=30, widget=forms.PasswordInput)

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=50)
    email = forms.EmailField()
    password = forms.CharField(max_length=50, widget=forms.PasswordInput)

class RentForm(forms.ModelForm):
    date_start = forms.DateField(widget=forms.DateInput(attrs={"type": "date"}), required=False)
    date_end = forms.DateField(widget=forms.DateInput(attrs={"type": "date"}), required=False)

    class Meta:
        model = Rezerwacje
        fields = ["date_start", "date_end", "auta"]

