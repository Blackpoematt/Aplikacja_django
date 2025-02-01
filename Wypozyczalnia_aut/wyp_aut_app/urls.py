from django.urls import path
from . import views

urlpatterns = [
    path("logowanie", views.login_view, name="logowanie"),
    path("rejestracja", views.register_view, name="Rejestracja"),
    path("rezerwacje", views.rents_view, name="Rezerwacje"),
    path("auta", views.cars_view, name="Auta"),
    path("", views.login_view, name="Logowanie"),
    path("logout", views.login_view, name="logout"),


]
