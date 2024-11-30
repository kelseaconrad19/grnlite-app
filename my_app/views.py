from django.shortcuts import render
from rest_framework import generics
from .models import Author, Book, Novel, Reader, Review
from .serializers import (
    AuthorSerializer, BookSerializer, NovelSerializer, ReaderSerializer, ReviewSerializer
)

def index(request):
    return render(request, 'index.html')

# Author Views
class AuthorListCreateView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class AuthorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

# Book Views
class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# Novel Views
class NovelListCreateView(generics.ListCreateAPIView):
    queryset = Novel.objects.all()
    serializer_class = NovelSerializer

class NovelDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Novel.objects.all()
    serializer_class = NovelSerializer

# Reader Views
class ReaderListCreateView(generics.ListCreateAPIView):
    queryset = Reader.objects.all()
    serializer_class = ReaderSerializer

class ReaderDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reader.objects.all()
    serializer_class = ReaderSerializer

# Review Views
class ReviewListCreateView(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class ReviewDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
