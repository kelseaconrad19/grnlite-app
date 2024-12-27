from django.shortcuts import redirect, render, get_object_or_404
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from .forms import ManuscriptSubmissionForm
from django.views.generic import ListView
from django.http import JsonResponse
from .models import Manuscript, Feedback
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

# from rest_framework.decorators import api_view, permission_classes
from social_django.utils import load_strategy
from social_core.backends.google import GoogleOAuth2
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.decorators import login_required


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
    BetaReader,
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
    ManuscriptFeedbackPreferenceSerializer,
)


# Home View
def home(request):
    return render(request, "main.html")


def signup(request):
    return render(request, "signup.html")


def signin(request):
    return render(request, "signin.html")


def login(request):
    return render(request, "login.html")


def logout(request):
    return render(request, "logout.html")


# Reader Dashboard Views
# def reader_dashboard(request):
#     return render(request, "reader-dashboard.html")


def reader_dashboard(request):
    return render(request, "reader-dashboard.html")


def available_manuscripts(request):
    return render(request, "Reader_Dashboard/available-manuscripts.html")


def reader_feedback(request):
    return render(request, "Reader_Dashboard/reader-feedback.html")


def reader_profile(request):
    return render(request, "Reader_Dashboard/reader-profile.html")


def reader_resource_library(request):
    return render(request, "Reader_Dashboard/reader-resource-library.html")


def beta_reader_training(request):
    return render(request, "Reader_Dashboard/beta-reader-training.html")


def beta_reader_performance_metrics(request):
    return render(request, "Reader_Dashboard/beta-reader-performance-metrics.html")


def reader_payment_page(request):
    return render(request, "Reader_Dashboard/reader-payment-page.html")


def reader_settings(request):
    return render(request, "Reader_Dashboard/reader-settings.html")


# Author Dashboard Views
def author_dashboard(request):
    return render(request, "author-dashboard.html")


def my_manuscripts(request):
    return render(request, "Author_Dashboard/my-manuscripts.html")


def get_manuscripts(request):
    manuscripts = Manuscript.objects.all().values(
        "id", "title", "genre", "length", "chapters", "description", "cover"
    )
    return JsonResponse(list(manuscripts), safe=False)


def get_manuscripts(request):
    manuscripts = Manuscript.objects.all().values("id", "title", "description", "cover")
    return JsonResponse(list(manuscripts), safe=False)


def find_beta_readers(request):
    return render(request, "Author_Dashboard/beta-reader-list.html")


def beta_reader_list(request):
    return render(request, "Author_Dashboard/beta-reader-list.html")


def manuscript_submission(request):
    return render(request, "Author_Dashboard/manuscript-submission.html")


def manuscript_success(request):
    return render(request, "Author_Dashboard/manuscript-success.html")


def my_books(request):
    return render(request, "Author_Dashboard/my-books.html")


@login_required
def create_manuscript(request):
    if request.method == "POST":
        form = ManuscriptSubmissionForm(request.POST, request.FILES)
        if form.is_valid():
            manuscript = form.save(commit=False)  # Prevent immediate database save
            manuscript.author = request.user  # Set the author to the logged-in user
            manuscript.save()  # Save to the database
            form.save_m2m()  # Save many-to-many relationships like keywords
            return redirect("my_app:manuscript-success")  # Redirect to the dashboard
    else:
        form = ManuscriptSubmissionForm()

    return render(
        request, "Author_Dashboard/manuscript-submission2.html", {"form": form}
    )


def feedback_form(request, manuscript_id):
    manuscript = get_object_or_404(Manuscript, id=manuscript_id)

    if request.method == "POST":
        feedback_data = request.POST  # Get all POST data

        # Create a new Feedback instance
        feedback = Feedback.objects.create(
            manuscript=manuscript,
            user=request.user,
            plot=feedback_data.get("plot"),
            characters=feedback_data.get("characters"),
            pacing=feedback_data.get("pacing"),
            worldbuilding=feedback_data.get("worldbuilding"),
            comments=feedback_data.get("comments"),
            # ... any other fields you want to save ...
        )

        # Process inManuscriptComments (assuming it's a JSON string)
        in_manuscript_comments = feedback_data.get("inManuscriptComments")
        if in_manuscript_comments:
            # ... logic to parse and store inManuscriptComments ...
            # (This depends on your data structure and how you want to store it)
            pass

        # Option 1: Redirect to a success page
        return redirect("feedback_success")

        # Option 2: Return a JSON response (for AJAX)
        # return JsonResponse({'success': True})

    return render(request, "reader_feedback.html", {"manuscript": manuscript})


@csrf_exempt
@login_required
def submit_feedback(request):
    if request.method == "POST":
        manuscript_id = request.POST.get("manuscript")
        plot_feedback = request.POST.get("plot")
        characters_feedback = request.POST.get("characters")
        pacing_feedback = request.POST.get("pacing")
        worldbuilding_feedback = request.POST.get("worldbuilding")
        additional_comments = request.POST.get("comments")

        manuscript = Manuscript.objects.get(id=manuscript_id)
        feedback = Feedback.objects.create(
            manuscript=manuscript,
            reader=request.user,
            plot=plot_feedback,
            characters=characters_feedback,
            pacing=pacing_feedback,
            worldbuilding=worldbuilding_feedback,
            comments=additional_comments,
        )
        return JsonResponse({"success": True})
    return JsonResponse({"success": False}, status=400)


def feedback_success(request):
    return render(request, "feedback_success.html")


def get_manuscripts(request):
    manuscripts = Manuscript.objects.all()
    manuscript_list = [
        {"id": manuscript.id, "title": manuscript.title} for manuscript in manuscripts
    ]
    return JsonResponse(manuscript_list, safe=False)


def feedback_summary(request):
    return render(request, "Author_Dashboard/feedback-summary.html")


def author_resource_library(request):
    return render(request, "Author_Dashboard/author-resource-library.html")


def author_community_groups(request):
    return render(request, "Author_Dashboard/author-community-groups.html")


def author_profile(request):
    return render(request, "Author_Dashboard/author-profile.html")


def author_payment_page(request):
    return render(request, "Author_Dashboard/author-payment-page.html")


def author_settings(request):
    return render(request, "Author_Dashboard/author-settings.html")


# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
def protected_view(request):
    return Response({"message": "This is a protected view."})


# Google Login View
class GoogleLoginView(APIView):
    def post(self, request):
        token = request.data.get("token")
        if not token:
            return Response({"error": "Token not provided"}, status=400)

        try:
            strategy = load_strategy(request)
            backend = GoogleOAuth2(strategy=strategy)
            user_data = backend.user_data(token)

            # Get or create the user
            user, created = User.objects.get_or_create(
                email=user_data["email"], defaults={"username": user_data["email"]}
            )

            # Generate JWT token
            refresh = RefreshToken.for_user(user)
            return Response(
                {"access": str(refresh.access_token), "refresh": str(refresh)}
            )

        except Exception as e:
            return Response({"error": str(e)}, status=400)


# User Profile View
class MyAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        return Response(
            {
                "id": user.id,
                "username": user.username,
                "email": user.email,
            }
        )


class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        return Response(
            {
                "id": user.id,
                "username": user.username,
                "email": user.email,
            }
        )


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


class BetaReaderListCreateView(ListView):
    model = BetaReader
    template_name = "beta-reader-list.html"


class BetaReaderApplicationListCreateView(generics.ListCreateAPIView):
    queryset = BetaReaderApplication.objects.all()
    serializer_class = BetaReaderApplicationSerializer


class BetaReaderApplicationDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BetaReaderApplication.objects.all()
    serializer_class = BetaReaderApplicationSerializer
