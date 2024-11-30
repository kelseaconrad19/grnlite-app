from django.contrib.auth.models import AbstractUser
from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    # Add additional fields like bio, etc.

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)  # Connect to Author
    published_date = models.DateField()
    # Add fields for genre, cover image, etc.

    def __str__(self):
        return self.title

class Novel(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)  # Connect to Author
    published_date = models.DateField()
    # Add fields for genre, cover image, etc.

    def __str__(self):
        return self.title

class Reader(AbstractUser):
    # Inherit from AbstractUser for built-in user fields
    bio = models.TextField(blank=True, null=True)
    # Add additional fields as needed

    def __str__(self):
        return self.username

class Review(models.Model):
    reader = models.ForeignKey(Reader, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)  # Review for a Book
    # Add a similar field for Novel if needed
    rating = models.IntegerField()
    comment = models.TextField()
    # Add fields for date, etc.

    def __str__(self):
        return f"{self.reader.username} - {self.book.title}"