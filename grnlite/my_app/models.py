from django.contrib.auth.models import AbstractUser
from django.db import models

class Reader(AbstractUser):
    # Add additional fields or methods if needed
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.username

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    published_date = models.DateField()

    def __str__(self):
        return self.title