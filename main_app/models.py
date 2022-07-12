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
        choices=T_UNITS,
        default=T_UNITS[0][0])
    time_stamp = models.DateTimeField(auto_now_add=True)
    desc = models.CharField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.desc

    def get_absolute_url(self):
        return reverse('detail', kwargs={'post_id': self.id})

class Photo_Pair(models.Model):
    ref_url = models.CharField(max_length=250)
    art_url = models.CharField(max_length=250)
    ref_cred = models.CharField(max_length=250)
    post = models.OneToOneField(
        Post,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    def __str__(self):
        return f"photos for post_id: {self.post} @{self.ref_url} and @{self.art_url}"
