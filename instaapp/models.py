from django.db import models
import uuid
from users.models import Profile


# Create your models here.
class Posts(models.Model):
    post_user = models.ForeignKey(Profile, null=True, blank=True,
                                  on_delete=models.CASCADE)
    post_name = models.CharField(max_length=50, null=True, blank=True)
    post_image = models.ImageField(null=True, blank=True, default="aman.jpeg")
    post_caption = models.TextField(null=True, blank=True)
    post_created = models.DateTimeField(auto_now_add=True)
    post_likes = models.IntegerField(default=0)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.post_user.name
class likePost(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE,
                             related_name="user_like")
    post = models.ForeignKey(Posts, on_delete=models.CASCADE,
                                 related_name="post_like")


