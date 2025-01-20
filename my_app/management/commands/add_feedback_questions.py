from django.core.management.base import BaseCommand
from my_app.models import FeedbackQuestion, FeedbackTopic


class Command(BaseCommand):
    help = 'Add feedback questions to the database'

    def handle(self, *args, **kwargs):
        # Define your feedback topics and associated questions
        data = {
            "Dialogue": [
                "Was the dialogue realistic and engaging?",
                "Did the dialogue reflect the characters' personalities?",
                "Were there any instances where the dialogue felt unnatural or forced?",
            ],
            "Overall Impressions": [
                "What was your overall impression of the manuscript?",
                "What stood out to you the most about the story?",
                "Are there any areas where you think the manuscript could improve?",
            ],
        }

        # Add feedback topics and questions
        for topic_name, questions in data.items():
            # Create or get the feedback topic
            topic, created = FeedbackTopic.objects.get_or_create(name=topic_name)

            for question_text in questions:
                FeedbackQuestion.objects.get_or_create(
                    topic=topic,
                    question_text=question_text,
                    is_active=True,  # Mark questions as active by default
                )

        self.stdout.write(self.style.SUCCESS('New feedback questions added successfully!'))