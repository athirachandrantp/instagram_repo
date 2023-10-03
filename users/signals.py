from .models import Profile
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.conf import settings



# def createProfile(sender, instance, created, **kwargs):
#     print('profile signal triggered')
#     if created:
#         user = instance
#         profile = Profile.objects.create(
#             user=user,
#             username=user.name,
#         )


# post_save.connect(createProfile, sender=User)
#
# @receiver(post_save, sender=User)
# def create_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)