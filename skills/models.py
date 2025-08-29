from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.
class Skill(models.Model):
    LEVEL_CHOICES = [
        ('BEGINNER', 'Beginner'),
        ('INTERMEDIATE', 'Intermediate'),
        ('ADVANCED', 'Advanced'),
    ]
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='skills')
    name = models.CharField(max_length=120)
    level = models.CharField(max_length=13, choices=LEVEL_CHOICES, default='BEGINNER')
    started_at = models.DateField(null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('user', 'name')
        ordering = ['name']

    def __str__(self):
        return f"{self.name} ({self.user.username})"

class SkillProgress(models.Model):
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE, related_name='progress_logs')
    percent = models.PositiveIntegerField(default=0)
    note = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.skill.name} - {self.percent}%"
