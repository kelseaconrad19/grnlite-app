from django.core.management.base import BaseCommand
from my_app.models import Manuscript


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        Manuscript.objects.create(
            title="Initial Manuscript",
            file_path="/path/to/file",
            status="draft",
            author_id=447,
            nda_required=False,
        )
        self.stdout.write("Manuscript created successfully.")


Manuscript.objects.all()
