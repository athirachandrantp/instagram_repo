from .models import Posts
from django.forms import ModelForm

class PostForm(ModelForm):
    class Meta:
        model = Posts
        fields = ['post_image', 'post_caption']
        exclude = ['post_user', 'post_created']