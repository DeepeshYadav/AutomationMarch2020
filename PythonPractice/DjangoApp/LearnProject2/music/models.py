from django.db import models

# Create your models here.

class Album(models.Model):
    artist = models.CharField(max_length=250)
    album_title = models.CharField(max_length=250)
    genre = models.CharField(max_length=300)

    def __str__(self):
        return self.album_title +" . "+self.artist

class songs(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    filetype = models.CharField(max_length=30)
    song_title = models.CharField(max_length=400)
