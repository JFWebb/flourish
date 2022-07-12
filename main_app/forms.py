from django.forms import ModelForm
from .models import Post

class Post_Form(ModelForm):
    class Meta:
        model = Post
        fields = ['time_int', 'time_unit', 'desc']


