from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .api_views import SkillViewSet

router = DefaultRouter()
router.register(r'skills', SkillViewSet, basename='skill')

urlpatterns = [
    path('', include(router.urls)),
]