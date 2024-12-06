from django.shortcuts import render
from rest_framework import generics
from .models import (
    Profile, AuthorSetting, Notification, Manuscript,
    ManuscriptKeyword, Genre, BetaReaderApplication, Feedback
)
from .serializers import (
    ProfileSerializer, AuthorSettingSerializer, NotificationSerializer, ManuscriptSerializer,
    ManuscriptKeywordSerializer, GenreSerializer, BetaReaderApplicationSerializer, FeedbackSerializer
)
def profile_list(request):
    profiles = Profile.objects.all()
    return render(request, 'profiles.html', {'profiles': profiles})

def main(request):
    return render(request, 'main.html')

def signin_view(request):
    return render(request, 'signin.html')

def signup_view(request):
    return render(request, 'signup.html')

# Profile Views
class ProfileListCreateView(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class ProfileDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

# Author Setting Views
class AuthorSettingListCreateView(generics.ListCreateAPIView):
    queryset = AuthorSetting.objects.all()
    serializer_class = AuthorSettingSerializer

class AuthorSettingDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AuthorSetting.objects.all()
    serializer_class = AuthorSettingSerializer

# Notification Views
class NotificationListCreateView(generics.ListCreateAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer

class NotificationDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer

# Manuscript Views
class ManuscriptListCreateView(generics.ListCreateAPIView):
    queryset = Manuscript.objects.all()
    serializer_class = ManuscriptSerializer

class ManuscriptDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Manuscript.objects.all()
    serializer_class = ManuscriptSerializer

# Manuscript Keyword Views
class ManuscriptKeywordListCreateView(generics.ListCreateAPIView):
    queryset = ManuscriptKeyword.objects.all()
    serializer_class = ManuscriptKeywordSerializer

class ManuscriptKeywordDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ManuscriptKeyword.objects.all()
    serializer_class = ManuscriptKeywordSerializer

# Genre Views
class GenreListCreateView(generics.ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

class GenreDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

# Beta Reader Application Views
class BetaReaderApplicationListCreateView(generics.ListCreateAPIView):
    queryset = BetaReaderApplication.objects.all()
    serializer_class = BetaReaderApplicationSerializer

class BetaReaderApplicationDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BetaReaderApplication.objects.all()
    serializer_class = BetaReaderApplicationSerializer

# Feedback Views
class FeedbackListCreateView(generics.ListCreateAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer

class FeedbackDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
