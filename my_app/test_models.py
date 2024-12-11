import django
django.setup()

from django.test import TestCase
from my_app.models import Profile, Manuscript, Genre  
from django.contrib.auth.models import User
from django.apps import apps

class TestProfileModel(TestCase):
    def setUp(self):
        Manuscript.objects.filter(title="Test Manuscript").delete()
        # Ensure Django apps are fully loaded
        apps.check_apps_ready() 

        # Create a user
        self.user = User.objects.create_user(username="testuser", password="testpass")

        # Create a profile
        self.profile = Profile.objects.create(user=self.user, profile_img="path/to/image.jpg")

        # Create a genre
        self.genre = Genre.objects.create(name="Science Fiction")

        # Create a manuscript
        self.manuscript = Manuscript.objects.create(
            author=self.user, title="Test Manuscript", file_path="/path/to/file", status="draft"
        )

    def test_profile_creation(self):
        profiles = Profile.objects.all()
        self.assertEqual(profiles.count(), 1)
        self.assertEqual(profiles[0].user.username, "testuser")

    def test_genre_creation(self):
        genres = Genre.objects.all()
        self.assertEqual(genres.count(), 1)
        self.assertEqual(genres[0].name, "Science Fiction")

    def test_manuscript_creation(self):  # New test for Manuscript model
        # Fix: Provide a valid author
        Manuscript = Manuscript.objects.create(
            author=self.user, title="Test Manuscript", file_path="/path/to/file", status="draft"
        )
        manuscripts = Manuscript.objects.all()
        self.assertEqual(manuscripts.count(), 2)  # The original one and the one created in the test
