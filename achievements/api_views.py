from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Achievement
from .serializers import AchievementSerializer

class AchievementViewSet(viewsets.ModelViewSet):
    serializer_class = AchievementSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Achievement.objects.all()
        return Achievement.objects.filter(skill__user=user)

    def get_serializer_context(self):
        ctx = super().get_serializer_context()
        ctx['request'] = self.request
        return ctx