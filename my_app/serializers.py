from rest_framework import serializers
from .models import (
    Profile, AuthorSetting, Notification, Manuscript, ManuscriptKeyword,
    Genre, BetaReaderApplication, Feedback
)

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

class AuthorSettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthorSetting
        fields = '__all__'

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'

class ManuscriptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manuscript
        fields = '__all__'

class ManuscriptKeywordSerializer(serializers.ModelSerializer):
    class Meta:
        model = ManuscriptKeyword
        fields = '__all__'

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'

class BetaReaderApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = BetaReaderApplication
        fields = '__all__'

class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = '__all__'