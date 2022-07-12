from django.forms import ModelForm
from .models import Post, Photo_Pair

class Post_Form(ModelForm):
    class Meta:
        model = Post
        fields = ['time_int', 'time_unit', 'desc']

class Photo_Form(ModelForm):
    class Meta:
        model = Photo_Pair
        fields = ['ref_url', 'art_url']
