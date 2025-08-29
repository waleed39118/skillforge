from django.contrib.auth.models import AbstractUser
from django.db import models

def avatar_upload_to(instance, filename):
    return f"avatars/{instance.username}/{filename}"

class CustomUser(AbstractUser):
    bio = models.TextField(blank=True)
    avatar = models.ImageField(upload_to=avatar_upload_to, blank=True, null=True)

    def __str__(self):
        return self.username