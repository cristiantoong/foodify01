# post_save -> this is the signal that fired after the object save
from django.db.models.signals import post_save

# User -> sender
from django.contrib.auth.models import User

# receiver
from django.dispatch import receiver

from .models import UserProfile

# We want User profile to be created for each new user
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(profile_name=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
