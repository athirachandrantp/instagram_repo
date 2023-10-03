from django.db import models
from django.contrib.auth.models import User
import uuid
from django.db.models.signals import post_save

# Create your models here.

# Create your models here.
class Profile(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE, null=True,
                              blank=True)
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=500, blank=True, null=True)
    profile_photo = models.ImageField(null=True, blank=True,
                                      upload_to='images/',
                                      default="images/aman.jpeg")
    created = models.DateTimeField(auto_now_add=True)

    followers = models.IntegerField(default=0, null=True, blank=True)
    following = models.IntegerField(default=0, null=True, blank=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True,
                          editable=False)

    def __str__(self):
        return self.name

def createProfile(sender, instance, created, **kwargs):
    print('profile signal triggered')
    if created:
        user = instance
        profile = Profile.objects.create(
            owner=user,
            name=user.username
        )


post_save.connect(createProfile, sender=User)
