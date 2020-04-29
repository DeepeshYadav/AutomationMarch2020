from django.db import models

# Create your models here.

class Album(models.Model):
    album_name = models.CharField(max_length=250)
    album_title = models.CharField(max_length=250)
    artist = models.CharField(max_length=200)
    songs = models.CharField(max_length=400)

