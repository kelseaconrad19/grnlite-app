from django.core.management.base import BaseCommand
from my_app.models import FeedbackQuestion

class Command(BaseCommand):
    help = 'Add predefined feedback questions'

    def handle(self, *args, **kwargs):
        questions = [
            'What did you think about the pacing of the manuscript?',
            'Were the characters relatable?',
            'What are your thoughts on the world-building?',
            'Did the dialogue feel natural?',
            'Would you recommend this manuscript to others?',
        ]
        for question_text in questions:
            FeedbackQuestion.objects.get_or_create(question_text=question_text, is_active=True)
        self.stdout.write(self.style.SUCCESS('Feedback questions added successfully!'))
