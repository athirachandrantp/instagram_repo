from .models import Posts, CommentPost
from django.forms import ModelForm

class PostForm(ModelForm):
    class Meta:
        model = Posts
        fields = ['post_image', 'post_caption', 'post_video']
        exclude = ['post_user', 'post_created']

class CommentForm(ModelForm):
    class Meta:
        model = CommentPost
        fields = ['body']