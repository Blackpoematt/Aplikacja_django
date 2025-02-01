# Generated by Django 5.1.4 on 2025-01-31 15:49

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wyp_aut_app', '0002_rename_car_rezerwacje_auta'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rezerwacje',
            name='Auta',
        ),
        migrations.AddField(
            model_name='rezerwacje',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='rents', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rezerwacje',
            name='auta',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='rents', to='wyp_aut_app.auta'),
            preserve_default=False,
        ),
    ]
