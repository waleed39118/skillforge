from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


def avatar_upload_to(instance, filename):
    return f"avatars/{instance.user.username}/{filename}"


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(blank=True)
    avatar = models.ImageField(upload_to=avatar_upload_to, blank=True, null=True)

    def __str__(self):
        return f"Profile({self.user.username})"


# Signals to create or update Profile automatically
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    if hasattr(instance, 'profile'):
        instance.profile.save()
        