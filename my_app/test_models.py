from django.test import TestCase
from .models import Profile, Manuscript, Genre
from django.contrib.auth.models import User

class TestProfileModel(TestCase):  # Class name starts with Test
    def setUp(self):
        # Create a user
        self.user = User.objects.create_user(username="testuser", password="testpass")

        # Create a profile
        self.profile = Profile.objects.create(user=self.user, profile_image="path/to/image.jpg")

        # Create a genre
        self.genre = Genre.objects.create(name="Science Fiction")

        # Create a manuscript
        self.manuscript = Manuscript.objects.create(author=self.user, title="My Manuscript", file_path="/path/to/file", status="draft")

    def test_profile_creation(self):
        profiles = Profile.objects.all()
        self.assertEqual(profiles.count(), 1)
        self.assertEqual(profiles[0].user.username, "testuser")

    def test_genre_creation(self):
        genres = Genre.objects.all()
        self.assertEqual(genres.count(), 1)
        self.assertEqual(genres[0].name, "Science Fiction")
