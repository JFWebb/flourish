from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

T_UNITS = (
    ('s', 'Seconds'),
    ('m', 'Minutes'),
    ('h', 'Hours')
)


# Create your models here.
class Post(models.Model):
    time_int = models.IntegerField()
    time_unit = models.CharField(
        max_length=10,
        choices = T_UNITS,
        default=T_UNITS[0][0])
    time_stamp = models.DateTimeField(auto_now_add=True)
    desc = models.CharField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Photo_Pair(models.Model):
    ref_url = models.CharField(max_length=250)
    art_url = models.CharField(max_length=250)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
