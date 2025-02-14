# Generated by Django 5.1.4 on 2025-02-14 18:49

from django.db import migrations, models
import django.contrib.auth.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ("my_app", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="user",
            field=models.OneToOneField(
                to=settings.AUTH_USER_MODEL,  # ✅ Ensures the correct user model is referenced
                on_delete=models.CASCADE,
            ),
        ),
    ]
