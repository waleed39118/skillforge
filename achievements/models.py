from django.db import models
from skills.models import Skill

# Create your models here.
def achievement_upload_to(instance, filename):
    return f"achievements/{instance.skill.user.username}/{instance.skill.name}/{filename}"

class Achievement(models.Model):
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE, related_name='achievements')
    title = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    file = models.FileField(upload_to=achievement_upload_to, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title
