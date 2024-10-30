# Generated by Django 5.1 on 2024-10-29 20:52

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name="cliente",
            name="email",
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.CreateModel(
            name="Avaliacao",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "nota",
                    models.IntegerField(
                        choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]
                    ),
                ),
                ("comentario", models.TextField(blank=True)),
                (
                    "agendamento",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="avaliacao",
                        to="core.agendamento",
                    ),
                ),
                (
                    "cliente",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
