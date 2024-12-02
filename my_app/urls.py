from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    # Author URLs
    path('authors/', views.AuthorListCreateView.as_view(), name='author-list'),
    path('authors/<int:pk>/', views.AuthorDetailView.as_view(), name='author-detail'),

    # Book URLs
    path('books/', views.BookListCreateView.as_view(), name='book-list'),
    path('books/<int:pk>/', views.BookDetailView.as_view(), name='book-detail'),

    # Novel URLs
    path('novels/', views.NovelListCreateView.as_view(), name='novel-list'),
    path('novels/<int:pk>/', views.NovelDetailView.as_view(), name='novel-detail'),

    # Reader URLs
    path('readers/', views.ReaderListCreateView.as_view(), name='reader-list'),
    path('readers/<int:pk>/', views.ReaderDetailView.as_view(), name='reader-detail'),

    # Review URLs
    path('reviews/', views.ReviewListCreateView.as_view(), name='review-list'),
    path('reviews/<int:pk>/', views.ReviewDetailView.as_view(), name='review-detail'),
]

