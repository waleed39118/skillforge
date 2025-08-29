from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .api_views import GoalViewSet

router = DefaultRouter()
router.register(r'goals', GoalViewSet, basename='goal')

urlpatterns = [
    path('', include(router.urls)),
]