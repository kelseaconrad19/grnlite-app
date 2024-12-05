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

class Profile(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        help_text="User who owns the profile"
    )
    profile_img = models.ImageField(
        upload_to='profile_images/',
        null=True,
        blank=True,
        help_text="User's profile picture"
    )
    bio = models.TextField(
        null=True,
        blank=True,
        help_text="Short biography for the user"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text="When the user account was created"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        help_text="When the user account was last updated"
    )

class Genre(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True,
        null=False,
        help_text="Unique name of the genre"
    )

    def __str__(self):
        return self.name
    
class Keyword(models.Model):
    name = models.CharField(
        max_length=100,
        null=False,
        help_text="Keyword for tagging manuscripts"
    )
    CATEGORY_CHOICES = [
        ('genre', 'Genre'),
        ('theme', 'Theme'),
    ]
    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        null=False,
        help_text="Category of the keyword"
    )

    def __str__(self):
        return f"{self.name} ({self.get_category_display()})"

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
    )
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
    keywords = models.ManyToManyField(
        Keyword,
        related_name="manuscripts",
        blank=True,
        help_text="Keywords associated with the manuscript"
    )

    def __str__(self):
        return self.title


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
    

class AuthorSettings(models.Model):
    author = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="settings",
        help_text="The author this settings configuration belongs to"
    )
    feedback_preferences = models.JSONField(
        default=dict,
        blank=True,
        help_text="Customizable preferences for the type of feedback the author wants"
    )
    notification_preferences = models.JSONField(
        default=dict,
        blank=True,
        help_text="Notification settings for the author"
    )
    default_genre = models.ForeignKey(
        Genre,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        help_text="Default genre for new manuscripts"
    )
    profile_visibility = models.BooleanField(
        default=True,
        help_text="Whether the author's profile is public or private"
    )
    auto_submit_feedback = models.BooleanField(
        default=False,
        help_text="Automatically submit feedback requests when manuscripts are uploaded"
    )
    created_at = models.DateTimeField(
        default=now,
        help_text="Timestamp of when the settings were created"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        help_text="Timestamp of when the settings were last updated"
    )

    def __str__(self):
        return f"Settings for {self.author.username}"

class Resource(models.Model):
    title = models.CharField(
        max_length=150,
        null=False,
        help_text="Title of the resource"
    )
    description = models.TextField(
        null=True,
        blank=True,
        help_text="Description of the resource"
    )
    file_path = models.FileField(
        upload_to="resources/",
        null=False,
        help_text="Path to the uploaded resource file"
    )
    category = models.CharField(
        max_length=50,
        null=True,
        blank=True,
        help_text="Category of the resource (e.g., 'Templates', 'Guides')"
    )
    tags = models.TextField(
        null=True,
        blank=True,
        help_text="Comma-separated tags for search and categorization"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text="Timestamp when the resource was uploaded"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        help_text="Timestamp when the resource was last updated"
    )

    def __str__(self):
        return self.title
    
class ResourceInteraction(models.Model):
    resource = models.ForeignKey(
        Resource, 
        on_delete=models.CASCADE, 
        related_name="interactions"
    )
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name="resource_interactions"
    )
    interaction_type = models.CharField(
        max_length=50, 
        choices=[("download", "Download"), ("favorite", "Favorite")], 
        help_text="Type of user interaction"
    )
    timestamp = models.DateTimeField(auto_now_add=True, help_text="Timestamp of the interaction")

    def __str__(self):
        return f"{self.user.username} - {self.interaction_type} - {self.resource.title}"
    
class Notification(models.Model):
    STATUS_CHOICES = [
        ('read', 'Read'),
        ('not_read', 'Not Read'),
    ]
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        help_text="User notification is sent to"
    )
    message = models.TextField(
        null=False,
        help_text="Message of the notification"
        )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        null=False,
        help_text="Read status of the notification",
        default='not_read'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text="Timestamp when the notification was sent"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        help_text="Timestamp when the notification was read"
    )
