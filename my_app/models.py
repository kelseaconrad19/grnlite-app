from django.contrib.auth.models import User
from django.db import models


class Author(models.Model):
    author_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)  # Renamed for clarity
    book_name = models.CharField(max_length=100, null=True, blank=True)
    date = models.DateField(auto_now_add=True)  # Automatically set the date


    def __str__(self):
        return self.name


class Book(models.Model):
    book_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    author_id = models.ForeignKey(Author, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.title


class Novel(models.Model):
    novel_id = models.AutoField(primary_key=True)
    title = models.ForeignKey(Book, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.title


class Reader(models.Model):
    user_id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='reader_profile')  # Renamed
    user_signup_date = models.DateField(auto_now_add=True)  # Automatically set the signup date
    previously_completed_reviews =  models.IntegerField(default=0)

    def __str__(self):
        return self.user.username


class Review(models.Model):
    reader_id = models.ForeignKey(Reader, on_delete=models.CASCADE)
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
    rating = models.IntegerField()
    review = models.TextField()
    review_date = models.DateField(auto_now_add=True)  # Automatically set the review date

    def __str__(self):
        return f"{self.reader.user.username} - {self.book.title}"


class AuthorBook(models.Model):
    author_id = models.ForeignKey(Author, on_delete=models.CASCADE)
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.author.name} - {self.book.title}"

class BookNovel(models.Model):
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
    novel_id = models.ForeignKey(Novel, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.book.title} - {self.novel.title}"

class ReaderNovel(models.Model):
    user_id = models.ForeignKey(Reader, on_delete=models.CASCADE)
    novel_id = models.ForeignKey(Novel, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.reader.user.username} - {self.novel.title}"
