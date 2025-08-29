from django.urls import path
from .views import GoalCreateView, GoalUpdateView

app_name = 'goals'

urlpatterns = [
    path('create/<int:skill_id>/', GoalCreateView.as_view(), name='create'),
    path('<int:pk>/edit/', GoalUpdateView.as_view(), name='edit'),
]