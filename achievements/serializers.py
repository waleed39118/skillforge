from rest_framework import serializers
from .models import Achievement
from skills.models import Skill

class AchievementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Achievement
        fields = ('id', 'skill', 'title', 'description', 'file', 'created_at')
        read_only_fields = ('id', 'created_at')

    def validate_skill(self, value):
        request = self.context.get('request')
        if request and value.user != request.user and not request.user.is_staff:
            raise serializers.ValidationError('Not allowed to use this skill.')
        return value