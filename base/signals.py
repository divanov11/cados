from django.db.models.signals import post_save, post_delete

from django.contrib.auth.models import User 
from .models import Profile

def createProfile(sender, instance, created, **kwargs):
    if created:
        user = instance
        profile = Profile.objects.create(
            user=user
        )


post_save.connect(createProfile, sender=User)