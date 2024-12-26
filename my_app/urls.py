from django.urls import path, include, re_path
from . import views
from .views import GoogleLoginView, UserProfileView, BetaReaderListCreateView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

app_name = "my_app"

urlpatterns = [
    path("", views.home, name="home"),
    # User URLs
    path("signin/", views.signin, name="signin"),
    path("signup/", views.signup, name="signup"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("users/", views.UserListCreateView.as_view(), name="user-list-create"),
    path("users/<int:pk>/", views.UserDetailView.as_view(), name="user-detail"),
    path("auth/", include("djoser.urls")),
    path("auth/", include("djoser.urls.jwt")),
    path("auth/", include("social_django.urls", namespace="social")),
    # Google OAuth2 URLs
    path("admin/", admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path("auth/google/", GoogleLoginView.as_view(), name="google-login"),
    path("auth/profile/", UserProfileView.as_view(), name="user-profile"),
    # Profile URLs
    path(
        "profiles/", views.ProfileListCreateView.as_view(), name="profile-list-create"
    ),
    path(
        "profiles/<int:pk>/", views.ProfileDetailView.as_view(), name="profile-detail"
    ),
    # Manuscript URLs
    path(
        "manuscrtipt-submission/",
        views.manuscript_submission,
        name="manuscript-submission-html",
    ),
    path(
        "manuscripts/",
        views.ManuscriptListCreateView.as_view(),
        name="manuscript-list-create",
    ),
    path(
        "manuscripts/<int:pk>/",
        views.ManuscriptDetailView.as_view(),
        name="manuscript-detail",
    ),
    # Keyword URLs
    path("keywords/", views.KeywordListCreateView.as_view(), name="keyword-list"),
    path(
        "keywords/<int:pk>/", views.KeywordDetailView.as_view(), name="keyword-detail"
    ),
    # Feedback Question URLs
    path(
        "feedback-questions/",
        views.FeedbackQuestionListCreateView.as_view(),
        name="feedback-question-list",
    ),
    path(
        "feedback-questions/<int:pk>/",
        views.FeedbackQuestionDetailView.as_view(),
        name="feedback-question-detail",
    ),
    # Manuscript Feedback Preference URLs
    path(
        "manuscript-feedback-preferences/",
        views.ManuscriptFeedbackPreferenceListCreateView.as_view(),
        name="manuscript-feedback-preference-list",
    ),
    path(
        "manuscript-feedback-preferences/<int:pk>/",
        views.ManuscriptFeedbackPreferenceDetailView.as_view(),
        name="manuscript-feedback-preference-detail",
    ),
    # Feedback Response URLs
    path(
        "feedback-responses/",
        views.FeedbackResponseListCreateView.as_view(),
        name="feedback-response-list",
    ),
    path(
        "feedback-responses/<int:pk>/",
        views.FeedbackResponseDetailView.as_view(),
        name="feedback-response-detail",
    ),
    # Author Settings URLs
    path(
        "author-settings-view/",
        views.AuthorSettingsListCreateView.as_view(),
        name="author-settings-list",
    ),
    path(
        "author-settings/<int:pk>/",
        views.AuthorSettingsDetailView.as_view(),
        name="author-settings-detail",
    ),
    # Resource URLs
    path("resources/", views.ResourceListCreateView.as_view(), name="resource-list"),
    path(
        "resources/<int:pk>/",
        views.ResourceDetailView.as_view(),
        name="resource-detail",
    ),
    # Resource Interactions URLs
    path(
        "resource-interactions/",
        views.ResourceInteractionListCreateView.as_view(),
        name="resource-interaction-list",
    ),
    path(
        "resource-interactions/<int:pk>/",
        views.ResourceInteractionDetailView.as_view(),
        name="resource-interaction-detail",
    ),
    # Notification URLs
    path(
        "notifications/",
        views.NotificationListCreateView.as_view(),
        name="notification-list",
    ),
    path(
        "notifications/<int:pk>/",
        views.NotificationDetailView.as_view(),
        name="notification-detail",
    ),
    # Beta Reader Application URLs
    path(
        "beta_reader_list/",
        BetaReaderListCreateView.as_view(),
        name="beta-reader-list-html",
    ),
    path(
        "beta-reader-applications/<int:pk>/",
        views.BetaReaderApplicationDetailView.as_view(),
        name="beta-reader-application-detail",
    ),
    # Reader Dashboard URLs
    re_path(
        r"^reader-dashboard\.html$",
        views.reader_dashboard,
        name="reader-dashboard-html",
    ),
    path("available-books/", views.available_books, name="available-books-html"),
    path("reader-feedback/", views.reader_feedback, name="reader-feedback-html"),
    path("reader-profile/", views.reader_profile, name="reader-profile-html"),
    path("reader-dashboard/", views.reader_dashboard, name="reader-dashboard-html"),
    path(
        "reader-resource-library/",
        views.reader_resource_library,
        name="reader-resource-library-html",
    ),
    path(
        "beta-reader-training/",
        views.beta_reader_training,
        name="beta-reader-training-html",
    ),
    path(
        "beta-reader-performance-metrics/",
        views.beta_reader_performance_metrics,
        name="beta-reader-performance-metrics-html",
    ),
    path(
        "reader-payment-page/",
        views.reader_payment_page,
        name="reader-payment-page-html",
    ),
    path("reader-settings/", views.reader_settings, name="reader-settings-html"),
    # Author Dashboard URLs
    re_path(
        r"^author-dashboard\.html$",
        views.author_dashboard,
        name="author-dashboard-html",
    ),
    path("my-books/", views.my_books, name="my-books-html"),
    path("find-beta-readers/", views.find_beta_readers, name="find-beta-readers-html"),
    path("author-profile/", views.author_profile, name="author-profile-html"),
    path("feedback-summary/", views.feedback_summary, name="feedback-summary-html"),
    path("manuscript-submission/", views.create_manuscript, name="create_manuscript"),
    path("manuscript-success/", views.manuscript_success, name="manuscript-success"),
    path(
        "author-resource-library/",
        views.author_resource_library,
        name="author-resource-library-html",
    ),
    path(
        "author-community-groups/",
        views.author_community_groups,
        name="author-community-groups-html",
    ),
    path(
        "author-payment-page/",
        views.author_payment_page,
        name="author-payment-page-html",
    ),
    path("author-settings/", views.author_settings, name="author-settings-html"),
    path("find-beta-readers/", views.find_beta_readers, name="find-beta-readers-html"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
