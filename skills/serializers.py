from rest_framework import serializers
from .models import Skill, SkillProgress

class SkillProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = SkillProgress
        fields = ('id', 'percent', 'note', 'created_at')

class SkillSerializer(serializers.ModelSerializer):
    progress_logs = SkillProgressSerializer(many=True, read_only=True)

    class Meta:
        model = Skill
        fields = ('id', 'name', 'level', 'started_at', 'updated_at', 'progress_logs')
        read_only_fields = ('id', 'updated_at')

    def create(self, validated_data):
        user = self.context['request'].user
        return Skill.objects.create(user=user, **validated_data)