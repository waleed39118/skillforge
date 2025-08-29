from rest_framework import serializers
from .models import Goal

class GoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goal
        fields = ('id', 'skill', 'title', 'description', 'status', 'due_date', 'created_at')
        read_only_fields = ('id', 'created_at')

    def validate(self, attrs):
        # Ensure only owner can set a skill they own
        request = self.context.get('request')
        skill = attrs.get('skill') or getattr(self.instance, 'skill', None)
        if request and skill and skill.user != request.user and not request.user.is_staff:
            raise serializers.ValidationError('Not allowed to use this skill.')
        return attrs