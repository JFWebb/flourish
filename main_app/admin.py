from django.contrib import admin

# Register your models here.
from .models import Post, Photo_Pair

admin.site.register(Post)
admin.site.register(Photo_Pair)