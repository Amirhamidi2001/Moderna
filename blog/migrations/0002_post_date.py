# Generated by Django 4.1.3 on 2022-11-14 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="post", name="date", field=models.DateField(auto_now=True),
        ),
    ]