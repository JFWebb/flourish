from django.forms import ModelForm

from .models import Post

class Post_Form(ModelForm):
    class Meta:
        model = Post
        fields = ['time_int', 'time_unit', 'desc']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

    


