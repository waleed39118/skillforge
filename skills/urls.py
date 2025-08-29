# skills/urls.py
from django.urls import path
from .views import (
    SkillListView, SkillDetailView, SkillCreateView, SkillUpdateView,
    SkillProgressCreateView, ReportDownloadView
)

app_name = 'skills'

urlpatterns = [
    path('', SkillListView.as_view(), name='list'),
    path('create/', SkillCreateView.as_view(), name='create'),
    path('<int:pk>/', SkillDetailView.as_view(), name='detail'),
    path('<int:pk>/edit/', SkillUpdateView.as_view(), name='edit'),
    path('<int:pk>/progress/add/', SkillProgressCreateView.as_view(), name='progress_add'),
    path('report/download/', ReportDownloadView.as_view(), name='report_download'),
]