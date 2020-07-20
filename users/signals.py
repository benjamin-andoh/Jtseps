from django.db.models.signals import post_save
# the sender
from django.contrib.auth.models import User
# the receiver
from django.dispatch import receiver
from .models import Profile


# we want a user profile to be created for each new user
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        instance.profile.save()

