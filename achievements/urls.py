from django.urls import path
from .views import AchievementCreateView
from . import views

app_name = 'achievements'

urlpatterns = [
    path('create/<int:skill_id>/', AchievementCreateView.as_view(), name='create'),
]