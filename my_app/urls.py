from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    # User URLs
    path('users/', views.UserListCreateView.as_view(), name='user-list-create'),
    path('users/<int:pk>/', views.UserDetailView.as_view(), name='user-detail'),

    # Profile URLs
    path('profiles/', views.ProfileListCreateView.as_view(), name='profile-list-create'),
    path('profiles/<int:pk>/', views.ProfileDetailView.as_view(), name='profile-detail'),

    # Manuscript URLs
    path('manuscripts/', views.ManuscriptListCreateView.as_view(), name='manuscript-list-create'),
    path('manuscripts/<int:pk>/', views.ManuscriptDetailView.as_view(), name='manuscript-detail'),

    # Keyword URLs
    path('keywords/', views.KeywordListCreateView.as_view(), name='keyword-list'),
    path('keywords/<int:pk>/', views.KeywordDetailView.as_view(), name='keyword-detail'),

    # Feedback Question URLs
    path('feedback-questions/', views.FeedbackQuestionListCreateView.as_view(), name='feedback-question-list'),
    path('feedback-questions/<int:pk>/', views.FeedbackQuestionDetailView.as_view(), name='feedback-question-detail'),

    # Manuscript Feedback Preference URLs
    path('manuscript-feedback-preferences/', views.ManuscriptFeedbackPreferenceListCreateView.as_view(), name='manuscript-feedback-preference-list'),
    path('manuscript-feedback-preferences/<int:pk>/', views.ManuscriptFeedbackPreferenceDetailView.as_view(), name='manuscript-feedback-preference-detail'),

    # Feedback Response URLs
    path('feedback-responses/', views.FeedbackResponseListCreateView.as_view(), name='feedback-response-list'),
    path('feedback-responses/<int:pk>/', views.FeedbackResponseDetailView.as_view(), name='feedback-response-detail'),

    # Author Settings URLs
    path('author-settings/', views.AuthorSettingsListCreateView.as_view(), name='author-settings-list'),
    path('author-settings/<int:pk>/', views.AuthorSettingsDetailView.as_view(), name='author-settings-detail'),

    # Resource URLs
    path('resources/', views.ResourceListCreateView.as_view(), name='resource-list'),
    path('resources/<int:pk>/', views.ResourceDetailView.as_view(), name='resource-detail'),

    # Resource Interactions URLs
    path('resource-interactions/', views.ResourceInteractionListCreateView.as_view(), name='resource-interaction-list'),
    path('resource-interactions/<int:pk>/', views.ResourceInteractionDetailView.as_view(), name='resource-interaction-detail'),

    # Notification URLs
    path('notifications/', views.NotificationListCreateView.as_view(), name='notification-list'),
    path('notifications/<int:pk>/', views.NotificationDetailView.as_view(), name='notification-detail'),

    # Beta Reader Application URLs
    path('beta-reader-applications/', views.BetaReaderApplicationListCreateView.as_view(), name='beta-reader-application-list'),
    path('beta-reader-applications/<int:pk>/', views.BetaReaderApplicationDetailView.as_view(), name='beta-reader-application-detail'),
]


