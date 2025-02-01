from django.contrib.auth.models import User
from django.db import models
from django.db.models import Q


class Auta(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    car_type = models.CharField(max_length=20)

    def __str__(self):
        return self.brand + " " + self.model

    def is_selected_days_reserved(self, new_date_start, new_date_end):
        check = Auta.get_selected_days_reserved_filter(new_date_start, new_date_end)
        return Auta.objects.filter(check, id=self.id).exists()

    @staticmethod
    def get_selected_days_reserved_filter(new_date_start, new_date_end):
        return Q(rents__date_start__lt=new_date_end) & Q(rents__date_end__gt=new_date_start)

class Rezerwacje(models.Model):
    date_start = models.DateField()
    date_end = models.DateField()
    auta = models.ForeignKey(to=Auta, on_delete=models.CASCADE, related_name="rents")
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="rents")

    def __str__(self):
        return f"{self.date_start}-{self.date_end} ({self.auta}, {self.user})"
