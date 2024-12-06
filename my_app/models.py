from django.contrib.auth.models import User
from django.db import models
from django.utils.timezone import now


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    profile_image = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.user.username


class AuthorSetting(models.Model):
    author = models.OneToOneField(User, on_delete=models.CASCADE, related_name="author_setting")
    feedback_preferences = models.JSONField(null=True, blank=True)
    notification_preferences = models.JSONField(null=True, blank=True)

    def __str__(self):
        return self.author.username


class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notifications")
    message = models.TextField()
    status = models.CharField(max_length=20, choices=[("unread", "Unread"), ("read", "Read")], default="unread")
    created_at = models.DateTimeField(default=now)

    def __str__(self):
        return f"Notification for {self.user.username}"


class Manuscript(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="manuscripts")
    title = models.CharField(max_length=255)
    file_path = models.CharField(max_length=255)
    status = models.CharField(
        max_length=20,
        choices=[("draft", "Draft"), ("submitted", "Submitted"), ("in_review", "In Review"), ("complete", "Complete")],
        default="draft",
    )

    def __str__(self):
        return self.title


class ManuscriptKeyword(models.Model):
    manuscript = models.ForeignKey(Manuscript, on_delete=models.CASCADE, related_name="keywords")
    keyword = models.CharField(max_length=100)

    def __str__(self):
        return self.keyword


class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class BetaReaderApplication(models.Model):
    manuscript = models.ForeignKey(Manuscript, on_delete=models.CASCADE, related_name="beta_applications")
    beta_reader = models.ForeignKey(User, on_delete=models.CASCADE, related_name="beta_reader_applications")
    status = models.CharField(
        max_length=20,
        choices=[("applied", "Applied"), ("approved", "Approved"), ("rejected", "Rejected")],
        default="applied",
    )
    created_at = models.DateTimeField(default=now)

    def __str__(self):
        return f"{self.beta_reader.username} - {self.manuscript.title}"


class Feedback(models.Model):
    manuscript = models.ForeignKey(Manuscript, on_delete=models.CASCADE, related_name="feedbacks")
    beta_reader = models.ForeignKey(User, on_delete=models.CASCADE, related_name="feedbacks")
    feedback_text = models.TextField()

    def __str__(self):
        return f"Feedback by {self.beta_reader.username}"


class ResourceLibrary(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name
