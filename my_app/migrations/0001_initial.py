# Generated by Django 5.1.4 on 2025-02-18 17:05

import django.contrib.auth.models
import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="FeedbackTopic",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="Keyword",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text="Keyword for tagging manuscripts", max_length=100
                    ),
                ),
                (
                    "category",
                    models.CharField(
                        choices=[("genre", "Genre"), ("theme", "Theme")],
                        help_text="Category of the keyword",
                        max_length=20,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="MyModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("field1", models.CharField(max_length=100)),
            ],
            options={
                "db_table": "my_table_name",
            },
        ),
        migrations.CreateModel(
            name="Resource",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "title",
                    models.CharField(help_text="Title of the resource", max_length=150),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True, help_text="Description of the resource", null=True
                    ),
                ),
                (
                    "file_path",
                    models.FileField(
                        help_text="Path to the uploaded resource file",
                        upload_to="resources/",
                    ),
                ),
                (
                    "category",
                    models.CharField(
                        blank=True,
                        help_text="Category of the resource (e.g., 'Templates', 'Guides')",
                        max_length=50,
                        null=True,
                    ),
                ),
                (
                    "tags",
                    models.TextField(
                        blank=True,
                        help_text="Comma-separated tags for search and categorization",
                        null=True,
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True,
                        help_text="Timestamp when the resource was uploaded",
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(
                        auto_now=True,
                        help_text="Timestamp when the resource was last updated",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="AuthorSettings",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "feedback_preferences",
                    models.JSONField(
                        blank=True,
                        default=dict,
                        help_text="Customizable preferences for the type of feedback the author wants",
                    ),
                ),
                (
                    "notification_preferences",
                    models.JSONField(
                        blank=True,
                        default=dict,
                        help_text="Notification settings for the author",
                    ),
                ),
                (
                    "profile_visibility",
                    models.BooleanField(
                        default=True,
                        help_text="Whether the author's profile is public or private",
                    ),
                ),
                (
                    "auto_submit_feedback",
                    models.BooleanField(
                        default=False,
                        help_text="Automatically submit feedback requests when manuscripts are uploaded",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        default=django.utils.timezone.now,
                        help_text="Timestamp of when the settings were created",
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(
                        auto_now=True,
                        help_text="Timestamp of when the settings were last updated",
                    ),
                ),
                (
                    "author",
                    models.OneToOneField(
                        help_text="The author this settings configuration belongs to",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="settings",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="CustomUser",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "username",
                    models.CharField(
                        error_messages={
                            "unique": "A user with that username already exists."
                        },
                        help_text="Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.",
                        max_length=150,
                        unique=True,
                        validators=[
                            django.contrib.auth.validators.UnicodeUsernameValidator()
                        ],
                        verbose_name="username",
                    ),
                ),
                (
                    "first_name",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="first name"
                    ),
                ),
                (
                    "last_name",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="last name"
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        blank=True, max_length=254, verbose_name="email address"
                    ),
                ),
                (
                    "is_staff",
                    models.BooleanField(
                        default=False,
                        help_text="Designates whether the user can log into this admin site.",
                        verbose_name="staff status",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True,
                        help_text="Designates whether this user should be treated as active. Unselect this instead of deleting accounts.",
                        verbose_name="active",
                    ),
                ),
                (
                    "date_joined",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="date joined"
                    ),
                ),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True, related_name="customuser_set", to="auth.group"
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True, related_name="customuser_set", to="auth.permission"
                    ),
                ),
            ],
            options={
                "verbose_name": "user",
                "verbose_name_plural": "users",
                "abstract": False,
            },
            managers=[
                ("objects", django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name="CustomUserGroup",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "custom_user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="my_app.customuser",
                    ),
                ),
                (
                    "group",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="auth.group"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="CustomUserPermission",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "custom_user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="my_app.customuser",
                    ),
                ),
                (
                    "permission",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="auth.permission",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="FeedbackQuestion",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "question_text",
                    models.TextField(help_text="The text of the feedback question"),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True,
                        help_text="Is this question active and selectable?",
                    ),
                ),
                (
                    "topic",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="questions",
                        to="my_app.feedbacktopic",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Manuscript",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=255)),
                ("file_path", models.FileField(upload_to="manuscripts/")),
                (
                    "status",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("draft", "Draft"),
                            ("submitted", "Submitted"),
                            ("in_review", "In Review"),
                            ("completed", "Completed"),
                        ],
                        default="draft",
                        help_text="Status of the manuscript",
                        max_length=30,
                    ),
                ),
                (
                    "budget",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=10, null=True
                    ),
                ),
                (
                    "beta_readers_needed",
                    models.PositiveIntegerField(blank=True, null=True),
                ),
                (
                    "cover_art",
                    models.ImageField(blank=True, null=True, upload_to="cover_art/"),
                ),
                ("nda_required", models.BooleanField(default=False)),
                (
                    "nda_file",
                    models.FileField(blank=True, null=True, upload_to="nda_files/"),
                ),
                ("plot_summary", models.TextField(blank=True, null=True)),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="manuscripts",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "feedback_topics",
                    models.ManyToManyField(blank=True, to="my_app.feedbacktopic"),
                ),
            ],
            options={
                "permissions": [
                    ("can_view_reader_dashboard", "Can view reader dashboard"),
                    ("can_view_author_dashboard", "Can view author dashboard"),
                ],
            },
        ),
        migrations.CreateModel(
            name="FeedbackResponse",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "answer_text",
                    models.TextField(
                        blank=True,
                        help_text="The beta reader's answer to the question",
                        null=True,
                    ),
                ),
                (
                    "review_date",
                    models.DateTimeField(
                        auto_now_add=True, help_text="When the feedback was submitted"
                    ),
                ),
                (
                    "question",
                    models.ForeignKey(
                        help_text="The specific feedback question being answered",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="my_app.feedbackquestion",
                    ),
                ),
                (
                    "reader",
                    models.ForeignKey(
                        help_text="The beta reader providing the feedback",
                        limit_choices_to={"groups__name": "beta_reader"},
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="feedback_given",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "manuscript",
                    models.ForeignKey(
                        help_text="The manuscript this feedback is for",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="feedback_responses",
                        to="my_app.manuscript",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Feedback",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("plot", models.TextField(blank=True, null=True)),
                ("characters", models.TextField(blank=True, null=True)),
                ("pacing", models.TextField(blank=True, null=True)),
                ("worldbuilding", models.TextField(blank=True, null=True)),
                ("comments", models.TextField(blank=True, null=True)),
                (
                    "reader",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "manuscript",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="feedbacks",
                        to="my_app.manuscript",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="BetaReaderApplication",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "reader_rating",
                    models.IntegerField(
                        blank=True,
                        help_text="Optional rating given to the beta reader for their application",
                        null=True,
                    ),
                ),
                (
                    "attachment",
                    models.FileField(
                        blank=True,
                        help_text="Optional attachment for the beta reader's application",
                        null=True,
                        upload_to="beta_reader_applications/",
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("applied", "Applied"),
                            ("approved", "Approved"),
                            ("rejected", "Rejected"),
                        ],
                        default="applied",
                        help_text="Status of the application",
                        max_length=10,
                    ),
                ),
                (
                    "application_date",
                    models.DateTimeField(
                        auto_now_add=True,
                        help_text="When the application was submitted",
                    ),
                ),
                (
                    "review_date",
                    models.DateTimeField(
                        blank=True,
                        help_text="When the application was reviewed by the author",
                        null=True,
                    ),
                ),
                (
                    "cover_letter",
                    models.TextField(
                        blank=True,
                        help_text="Optional message from the beta reader to the author",
                        null=True,
                    ),
                ),
                (
                    "beta_reader",
                    models.ForeignKey(
                        help_text="The beta reader submitting the application",
                        limit_choices_to={"groups__name": "beta_reader"},
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="applications",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "manuscript",
                    models.ForeignKey(
                        help_text="The manuscript this application is for",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="applications",
                        to="my_app.manuscript",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Manuscript_keywords",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "keyword",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="my_app.keyword"
                    ),
                ),
                (
                    "manuscript",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="my_app.manuscript",
                    ),
                ),
            ],
            options={
                "db_table": "my_app_manuscript_keywords",
            },
        ),
        migrations.AddField(
            model_name="manuscript",
            name="keywords",
            field=models.ManyToManyField(
                blank=True, through="my_app.Manuscript_keywords", to="my_app.keyword"
            ),
        ),
        migrations.CreateModel(
            name="ManuscriptFeedbackPreference",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "manuscript",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="feedback_preferences",
                        to="my_app.manuscript",
                    ),
                ),
                (
                    "question",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="manuscript_preferences",
                        to="my_app.feedbackquestion",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ManuscriptKeywords",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "keyword",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="my_app.keyword"
                    ),
                ),
                (
                    "manuscript",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="my_app.manuscript",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Notification",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("message", models.TextField(help_text="Message of the notification")),
                (
                    "status",
                    models.CharField(
                        choices=[("read", "Read"), ("not_read", "Not Read")],
                        default="not_read",
                        help_text="Read status of the notification",
                        max_length=20,
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True,
                        help_text="Timestamp when the notification was sent",
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(
                        auto_now=True,
                        help_text="Timestamp when the notification was read",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        help_text="The user receiving the notification",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="notifications",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Profile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "role",
                    models.CharField(
                        choices=[
                            ("author", "Author"),
                            ("beta_reader", "Beta Reader"),
                            ("admin", "Admin"),
                        ],
                        help_text="Role of the user",
                        max_length=20,
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        help_text="User who owns the profile",
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="BetaReader",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "experience",
                    models.TextField(
                        blank=True,
                        help_text="Summary of the beta reader's experience",
                        null=True,
                    ),
                ),
                (
                    "rating",
                    models.DecimalField(
                        blank=True,
                        decimal_places=2,
                        help_text="Average rating for this beta reader",
                        max_digits=3,
                        null=True,
                    ),
                ),
                (
                    "total_reviews",
                    models.PositiveIntegerField(
                        default=0,
                        help_text="Total number of reviews completed by the beta reader",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True,
                        help_text="When the beta reader profile was created",
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(
                        auto_now=True,
                        help_text="When the beta reader profile was last updated",
                    ),
                ),
                (
                    "keywords",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Keywords the beta reader is interested in",
                        related_name="beta_readers",
                        to="my_app.keyword",
                    ),
                ),
                (
                    "profile",
                    models.OneToOneField(
                        help_text="The profile associated with this beta reader",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="beta_reader_profile",
                        to="my_app.profile",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ReaderManuscript",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("in_progress", "In Progress"),
                            ("completed", "Completed"),
                        ],
                        default="in_progress",
                        max_length=50,
                    ),
                ),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "manuscript",
                    models.ForeignKey(
                        help_text="The manuscript chosen by the reader",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="readers",
                        to="my_app.manuscript",
                    ),
                ),
                (
                    "reader",
                    models.ForeignKey(
                        help_text="The reader associated with the manuscript",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="reader_manuscripts",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ResourceInteraction",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "interaction_type",
                    models.CharField(
                        choices=[("download", "Download"), ("favorite", "Favorite")],
                        help_text="Type of user interaction",
                        max_length=50,
                    ),
                ),
                (
                    "timestamp",
                    models.DateTimeField(
                        auto_now_add=True, help_text="Timestamp of the interaction"
                    ),
                ),
                (
                    "resource",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="interactions",
                        to="my_app.resource",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        help_text="The user interacting with the resource",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="resource_interactions",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
