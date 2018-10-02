from djongo import models

class Tracks(models.Model):
    track_name = models.CharField(max_length=100)
    track_length = models.IntegerField()
    track_image = models.ImageField(upload_to = "MusicDownload/static/MusicDownload/images/")
    track_album = models.CharField(max_length=100)
    track_artist = models.CharField(max_length=100)
	
    def __str__(self):
       return self.track_name

