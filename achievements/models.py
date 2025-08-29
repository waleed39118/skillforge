from django.db import models
from django.utils.text import slugify
from skills.models import Skill


def achievement_upload_to(instance, filename):
    uname = slugify(instance.skill.user.username)
    sname = slugify(instance.skill.name)
    return f"achievements/{uname}/{sname}/{filename}"


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