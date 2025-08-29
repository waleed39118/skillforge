from django.db import models
from django.contrib.auth.models import User


def avatar_upload_to(instance, filename):
    return f"avatars/{instance.user.username}/{filename}"


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(blank=True)
    avatar = models.ImageField(upload_to=avatar_upload_to, blank=True, null=True)

    def __str__(self):
        return f"Profile({self.user.username})"