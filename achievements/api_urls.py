from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .api_views import AchievementViewSet

router = DefaultRouter()
router.register(r'achievements', AchievementViewSet, basename='achievement')

urlpatterns = [
    path('', include(router.urls)),
]