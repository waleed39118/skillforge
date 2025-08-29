# skills/api_views.py
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from .models import Skill, SkillProgress
from .serializers import SkillSerializer, SkillProgressSerializer

class SkillViewSet(viewsets.ModelViewSet):
    serializer_class = SkillSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Skill.objects.all()
        return Skill.objects.filter(user=user)

    def get_serializer_context(self):
        ctx = super().get_serializer_context()
        ctx['request'] = self.request
        return ctx

    @action(detail=True, methods=['post'])
    def add_progress(self, request, pk=None):
        skill = self.get_object()
        serializer = SkillProgressSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        SkillProgress.objects.create(skill=skill, **serializer.validated_data)
        return Response({'status': 'progress added'})