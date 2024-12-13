import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "grnlite.settings")
django.setup()

from django.test import TestCase
from my_app.models import Profile, Manuscript, Genre
from django.contrib.auth.models import User


class TestProfileModel(TestCase):
    def setUp(self):
        # Delete any existing "Test Manuscript" to avoid conflicts
        Manuscript.objects.filter(title="Test Manuscript").delete()

        # Create a user
        self.user = User.objects.create_user(username="testuser", password="testpass")

        # Create a profile
        self.profile = Profile.objects.create(
            user=self.user, profile_img="path/to/image.jpg"
        )

        # Create a genre
        self.genre = Genre.objects.create(name="Science Fiction")

        # Create a manuscript
        self.manuscript = Manuscript.objects.create(
            author=self.user,
            title="Initial Manuscript",
            file_path="/path/to/file",
            status="draft",
        )

    def test_profile_creation(self):
        profiles = Profile.objects.all()
        self.assertEqual(profiles.count(), 1)
        self.assertEqual(profiles[0].user.username, "testuser")

    def test_genre_creation(self):
        genres = Genre.objects.all()
        self.assertEqual(genres.count(), 1)
        self.assertEqual(genres[0].name, "Science Fiction")

    def test_manuscript_creation(self):
        # Create a new manuscript within the test
        Manuscript.objects.create(
            author=self.user,
            title="Test Manuscript",
            file_path="/path/to/file",
            status="draft",
        )
        manuscripts = Manuscript.objects.all()
        self.assertEqual(manuscripts.count(), 3)

    def test_manuscript_deletion(self):
        # Create a new manuscript specifically for this test
        manuscript_to_delete = Manuscript.objects.create(
            author=self.user,
            title="Manuscript to Delete",
            file_path="/path/to/file",
            status="draft",
        )

        manuscript_to_delete.delete()
        manuscripts = Manuscript.objects.all()

        # Expect 2 manuscripts remaining: the one from setUp() and the one from test_manuscript_creation()
        self.assertEqual(manuscripts.count(), 2)

    def test_profile_update(self):
        self.profile.bio = "Updated bio"
        self.profile.save()
        updated_profile = Profile.objects.get(user=self.user)
        self.assertEqual(updated_profile.bio, "Updated bio")

    def test_genre_update(self):
        self.genre.description = "Updated description"
        self.genre.save()
        updated_genre = Genre.objects.get(name="Science Fiction")
        self.assertEqual(updated_genre.description, "Updated description")

    def test_manuscript_update(self):
        self.manuscript.title = "Updated Manuscript"
        self.manuscript.save()
        updated_manuscript = Manuscript.objects.get(id=self.manuscript.id)
        self.assertEqual(updated_manuscript.title, "Updated Manuscript")

    def test_profile_deletion(self):
        self.profile.delete()
        profiles = Profile.objects.all()
        self.assertEqual(profiles.count(), 0)

    def test_genre_deletion(self):
        self.genre.delete()
        genres = Genre.objects.all()
        self.assertEqual(genres.count(), 0)
