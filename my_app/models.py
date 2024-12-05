from django.contrib.auth.models import User
from django.db import models
from django.utils.timezone import now
from django.utils import timezone


class User(models.Model):
    ROLE_CHOICES = [
        ('author', 'Author'),
        ('beta_reader', 'Beta Reader'),
        ('editor', 'Editor'),
    ]

    username = models.CharField(
        max_length=150,
        unique=True,
        null=False,
        help_text="Unique username"
    )
    email = models.EmailField(
        max_length=255,
        unique=True,
        null=False,
        help_text="Unique email"
    )
    password = models.CharField(
        max_length=255,
        null=False,
        help_text="User's password"
    )
    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default='author',
        null=False,
        help_text="Role of the user"
    )

    def __str__(self):
        return self.username


class Manuscript(models.Model):
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('submitted', 'Submitted'),
        ('in_review', 'In Review'),
        ('completed', 'Completed'),
    ]
    
    title = models.CharField(
        max_length=200, 
        null=False
    )
    author = models.ForeignKey(
        User, 
        on_delete=models.CASCADE
    ) # One to Many - one author can have many books 
    file_path = models.URLField(
        null=False
    )
    status = models.CharField(
        max_length=30, 
        choices=STATUS_CHOICES, 
        default='draft', 
        null=False, 
        help_text='Status of the manuscript'
    )

    def __str__(self):
        return self.title


class Genre(models.Model):
    genre_name = models.ForeignKey(
        Manuscript,
        on_delete=models.CASCADE, 
        related_name='manuscript'
    ) # One to Many - one manuscript can have many genres (Young Adult SciFi)

    def __str__(self):
        return self.genre_name


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
