from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import LoginForm, RegisterForm, RentForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data["username"], password=form.cleaned_data["password"])
            if user:
                login(request, user)
                return redirect("Auta")


    form = LoginForm()
    return render(request,"wyp_aut_app/Logowanie.html", {"form": form})


def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = User(email=form.cleaned_data["email"],
                        username=form.cleaned_data["username"])
            user.set_password(form.cleaned_data["password"])
            user.save()
            return redirect("logowanie")
    else:
        print("Wejście na strone")

    form = RegisterForm()
    return render(request, "wyp_aut_app/Rejestracja.html", {"form": form})


@login_required
def cars_view(request):
    error_message = ""
    if request.method == "POST":
        form = RentForm(request.POST)
        if form.is_valid():
            car = form.cleaned_data["auta"]
            if form.cleaned_data["date_end"] < form.cleaned_data["date_start"]:
                error_message = "Nieprawidłowa data, sprawdź to"
            elif not car.is_selected_days_reserved(form.cleaned_data["date_start"], form.cleaned_data["date_end"]):
                form.instance.user = request.user
                form.save()
                return redirect("Rezerwacje")
            else:
                error_message = "Auto niedostępne w tym terminie"
    else:
        form = RentForm()
    return render(request, "wyp_aut_app/Auta.html", {"form": form, "error_message": error_message})


@login_required
def rents_view(request):
     return render(request,"wyp_aut_app/Rezerwacje.html")

def user_logout(request):
    logout(request)
    return redirect("wyp_aut_app/Logowanie.html")