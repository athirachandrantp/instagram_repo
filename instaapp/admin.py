from django.contrib import admin
from .models import Posts, likePost, CommentPost

# Register your models here.
admin.site.register(Posts)
admin.site.register(likePost)
admin.site.register(CommentPost)
