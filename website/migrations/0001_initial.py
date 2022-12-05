# Generated by Django 4.1.3 on 2022-11-09 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Contact",
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
                ("name", models.CharField(max_length=60)),
                ("email", models.EmailField(max_length=254)),
                ("subject", models.CharField(max_length=60)),
                ("message", models.TextField()),
                ("created_date", models.DateTimeField(auto_now_add=True)),
            ],
            options={"ordering": ["-created_date"],},
        ),
        migrations.CreateModel(
            name="Newsletter",
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
                ("email", models.EmailField(max_length=254)),
            ],
        ),
    ]
