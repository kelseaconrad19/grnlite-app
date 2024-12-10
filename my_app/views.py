from django.shortcuts import render
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework.permissions import BasePermission, AllowAny, IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadOnly

from .models import (
    Profile,
    Keyword,
    Manuscript,
    FeedbackQuestion,
    FeedbackResponse,
    ManuscriptFeedbackPreference,
    AuthorSettings,
    Resource,
    ResourceInteraction,
    Notification,
    BetaReaderApplication,
)
from .serializers import (
    UserSerializer,
    ProfileSerializer,
    ManuscriptSerializer,
    KeywordSerializer,
    FeedbackQuestionSerializer,
    FeedbackResponseSerializer,
    AuthorSettingsSerializer,
    ResourceSerializer,
    ResourceInteractionSerializer,
    NotificationSerializer,
    BetaReaderApplicationSerializer,
    ManuscriptFeedbackPreferenceSerializer
)

# Home View
def home(request):
    return render(request, 'main.html')

def signup(request):
    return render(request, 'signup.html')

def signin(request):
    return render(request, 'signin.html')

def login(request):
    return render(request, 'login.html')

def logout(request):
    return render(request, 'logout.html')



# User Views

class UserListCreateView(generics.ListCreateAPIView):
    """
    GET: List all users.
    POST: Create a new user.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET: Retrieve user details.
    PUT/PATCH: Update user details.
    DELETE: Delete a user.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

# Profile Views
class ProfileListCreateView(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

class ProfileDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

# Manuscript Views
class ManuscriptListCreateView(generics.ListCreateAPIView):
    queryset = Manuscript.objects.all()
    serializer_class = ManuscriptSerializer

class ManuscriptDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Manuscript.objects.all()
    serializer_class = ManuscriptSerializer

# Keyword Views
class KeywordListCreateView(generics.ListCreateAPIView):
    queryset = Keyword.objects.all()
    serializer_class = KeywordSerializer

class KeywordDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Keyword.objects.all()
    serializer_class = KeywordSerializer

# Feedback Question Views
class FeedbackQuestionListCreateView(generics.ListCreateAPIView):
    queryset = FeedbackQuestion.objects.all()
    serializer_class = FeedbackQuestionSerializer

class FeedbackQuestionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = FeedbackQuestion.objects.all()
    serializer_class = FeedbackQuestionSerializer
    
# Manuscript Feedback Preference Views
class ManuscriptFeedbackPreferenceListCreateView(generics.ListCreateAPIView):
    queryset = ManuscriptFeedbackPreference.objects.all()
    serializer_class = ManuscriptFeedbackPreferenceSerializer

class ManuscriptFeedbackPreferenceDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ManuscriptFeedbackPreference.objects.all()
    serializer_class = ManuscriptFeedbackPreferenceSerializer

# Feedback Response Views
class FeedbackResponseListCreateView(generics.ListCreateAPIView):
    queryset = FeedbackResponse.objects.all()
    serializer_class = FeedbackResponseSerializer

class FeedbackResponseDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = FeedbackResponse.objects.all()
    serializer_class = FeedbackResponseSerializer

# Author Settings Views
class AuthorSettingsListCreateView(generics.ListCreateAPIView):
    queryset = AuthorSettings.objects.all()
    serializer_class = AuthorSettingsSerializer

class AuthorSettingsDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AuthorSettings.objects.all()
    serializer_class = AuthorSettingsSerializer

# Resource Views
class ResourceListCreateView(generics.ListCreateAPIView):
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer

class ResourceDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer

# Resource Interaction Views
class ResourceInteractionListCreateView(generics.ListCreateAPIView):
    queryset = ResourceInteraction.objects.all()
    serializer_class = ResourceInteractionSerializer

class ResourceInteractionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ResourceInteraction.objects.all()
    serializer_class = ResourceInteractionSerializer

# Notification Views
class NotificationListCreateView(generics.ListCreateAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer

class NotificationDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer

# Beta Reader Application Views
class BetaReaderApplicationListCreateView(generics.ListCreateAPIView):
    queryset = BetaReaderApplication.objects.all()
    serializer_class = BetaReaderApplicationSerializer

class BetaReaderApplicationDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BetaReaderApplication.objects.all()
    serializer_class = BetaReaderApplicationSerializer