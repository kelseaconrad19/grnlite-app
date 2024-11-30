from django.contrib.auth.models import User
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

class Reader(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='reader_profile')
    # Add custom fields here
    favorite_books = models.ManyToManyField('Book', related_name='favorite_readers')

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