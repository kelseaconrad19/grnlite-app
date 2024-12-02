from django.contrib.auth.models import User
from django.db import models
from django.utils.timezone import now
from django.utils import timezone


class Author(models.Model):
    name = models.CharField(max_length=100)
    book_name = models.CharField(max_length=100, null=True, blank=True)
    date = models.DateField(default='2023-01-01')

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Novel(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Reader(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='reader_profile')
    user_signup_date = models.DateTimeField(default=timezone.now)
    previously_completed_reviews = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username


class Review(models.Model):
    reader = models.ForeignKey(Reader, on_delete=models.CASCADE, default=1)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    rating = models.IntegerField()
    review = models.TextField()
    review_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.reader.user.username} - {self.book.title}"


class AuthorBook(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, default=1)  # Assuming Author with ID 1 exists
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.author.name} - {self.book.title}"


class BookNovel(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    novel = models.ForeignKey(Novel, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.book.title} - {self.novel.title}"


class ReaderNovel(models.Model):
    reader = models.ForeignKey(Reader, on_delete=models.CASCADE, default=1)  # Assuming Reader with ID 1 exists
    novel = models.ForeignKey(Novel, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.reader.user.username} - {self.novel.title}"
