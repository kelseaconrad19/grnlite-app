from django.core.management.base import BaseCommand
from my_app.models import Profile, Manuscript, AuthorSettings


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        Profile.objects.create(name="Default Profile", genre="Fiction")
        Manuscript.objects.create(
            title="Default Manuscript", content="This is a default manuscript."
        )
        AuthorSettings.objects.create(
            author_name="Default Author", bio="This is a default bio."
        )
