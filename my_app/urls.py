from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='home'),

    path('signin/', views.signin_view, name='signin'),
    path('signup/', views.signup_view, name='signup'),

    # Profile URLs
    path('profiles/', views.ProfileListCreateView.as_view(), name='profile-list'),
    path('profiles/', views.profile_list, name='profile-list-html'),
    path('profiles/<int:pk>/', views.ProfileDetailView.as_view(), name='profile-detail'),

    # Author Setting URLs
    path('author-settings/', views.AuthorSettingListCreateView.as_view(), name='author-setting-list'),
    path('author-settings/<int:pk>/', views.AuthorSettingDetailView.as_view(), name='author-setting-detail'),

    # Notification URLs
    path('notifications/', views.NotificationListCreateView.as_view(), name='notification-list'),
    path('notifications/<int:pk>/', views.NotificationDetailView.as_view(), name='notification-detail'),

    # Manuscript URLs
    path('manuscripts/', views.ManuscriptListCreateView.as_view(), name='manuscript-list'),
    path('manuscripts/<int:pk>/', views.ManuscriptDetailView.as_view(), name='manuscript-detail'),

    # Manuscript Keyword URLs
    path('manuscript-keywords/', views.ManuscriptKeywordListCreateView.as_view(), name='manuscript-keyword-list'),
    path('manuscript-keywords/<int:pk>/', views.ManuscriptKeywordDetailView.as_view(), name='manuscript-keyword-detail'),

    # Genre URLs
    path('genres/', views.GenreListCreateView.as_view(), name='genre-list'),
    path('genres/<int:pk>/', views.GenreDetailView.as_view(), name='genre-detail'),

    # Beta Reader Application URLs
    path('beta-reader-applications/', views.BetaReaderApplicationListCreateView.as_view(), name='beta-reader-application-list'),
    path('beta-reader-applications/<int:pk>/', views.BetaReaderApplicationDetailView.as_view(), name='beta-reader-application-detail'),

    # Feedback URLs
    path('feedbacks/', views.FeedbackListCreateView.as_view(), name='feedback-list'),
    path('feedbacks/<int:pk>/', views.FeedbackDetailView.as_view(), name='feedback-detail'),
]
