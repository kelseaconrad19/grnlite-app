from django.contrib.auth.models import User
from django.db import models
from django.utils.timezone import now
from django.utils import timezone


class User(models.Model):
    ROLE_CHOICES = [
        ('author', 'Author'),
        ('beta_reader', 'Beta Reader'),
        ('editor', 'Editor'),
    ]

    username = models.CharField(
        max_length=150,
        unique=True,
        null=False,
        help_text="Unique username"
    )
    email = models.EmailField(
        max_length=255,
        unique=True,
        null=False,
        help_text="Unique email"
    )
    password = models.CharField(
        max_length=255,
        null=False,
        help_text="User's password"
    )
    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default='author',
        null=False,
        help_text="Role of the user"
    )

    def __str__(self):
        return self.username


class Manuscript(models.Model):
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('submitted', 'Submitted'),
        ('in_review', 'In Review'),
        ('completed', 'Completed'),
    ]
    
    title = models.CharField(
        max_length=200, 
        null=False
    )
    author = models.ForeignKey(
        User, 
        on_delete=models.CASCADE
    ) # One to Many - one author can have many books 
    file_path = models.URLField(
        null=False
    )
    status = models.CharField(
        max_length=30, 
        choices=STATUS_CHOICES, 
        default='draft', 
        null=False, 
        help_text='Status of the manuscript'
    )

    def __str__(self):
        return self.title


class Genre(models.Model):
    genre_name = models.ForeignKey(
        Manuscript,
        on_delete=models.CASCADE, 
        related_name='manuscript'
    ) # One to Many - one manuscript can have many genres (Young Adult SciFi)

    def __str__(self):
        return self.genre_name


class FeedbackQuestion(models.Model):
    CATEGORY_CHOICES = [
        ('developmental', 'Developmental Edits'),
        ('line_editing', 'Line Editing'),
        ('copy_editing', 'Copy Editing'),
    ]

    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        null=False,
        help_text="Category of the feedback question"
    )
    question_text = models.TextField(
        null=False,
        help_text="The text of the feedback question"
    )
    is_active = models.BooleanField(
        default=True,
        help_text="Whether this question is currently in use"
    )

    def __str__(self):
        return f"{self.get_category_display()}: {self.question_text}"


class ManuscriptFeedbackPreference(models.Model):
    manuscript = models.ForeignKey(
        Manuscript, 
        on_delete=models.CASCADE, 
        related_name="feedback_preferences"
    )
    question = models.ForeignKey(
        FeedbackQuestion, 
        on_delete=models.CASCADE, 
        related_name="manuscript_preferences"
    )

    def __str__(self):
        return f"{self.manuscript.title} - {self.question.question_text}"

class FeedbackResponse(models.Model):
    manuscript = models.ForeignKey(
        Manuscript,
        on_delete=models.CASCADE,
        related_name="feedback_responses",
        help_text="The manuscript this feedback is for"
    )
    reader = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        limit_choices_to={'role': 'beta_reader'},
        related_name="feedback_given",
        help_text="The beta reader providing the feedback"
    )
    question = models.ForeignKey(
        FeedbackQuestion,
        on_delete=models.CASCADE,
        help_text="The specific feedback question being answered"
    )
    answer_text = models.TextField(
        null=True,
        blank=True,
        help_text="The beta reader's answer to the question"
    )
    review_date = models.DateTimeField(
        auto_now_add=True,
        help_text="When the feedback was submitted"
    )
    
    def __str__(self):
        return f"Feedback by {self.reader.username} for {self.manuscript.title} - Question: {self.question.id}"

