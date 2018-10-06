from djongo import models
from pymongo import MongoClient
from gridfs import GridFSBucket
import os

class Tracks(models.Model):
    track_name = models.CharField(max_length=100)
    track_artist = models.CharField(max_length=100)
    track_album = models.CharField(max_length=100)
    track_length = models.FloatField()
    track_genre = models.CharField(max_length = 100)
    track_language = models.CharField(max_length = 50)
    track_number = models.IntegerField()
    track_image = models.FileField()
    actual_track = models.FileField()

    def __str__(self):
       return self.track_name

    def save(self):
        #Save to the database
        super(Tracks,self).save()

        #if genre doesn't exist add it
        try:
            genre_object = Genres.objects.get(genre_name = self.track_genre)
        except:
            genre_object = Genres.objects.create(genre_name = self.track_genre)
            genre_object.save()

        #Upload music to Gridfs using pymongo commands
        print("Uploading to GridFS")
        db = MongoClient().MusicDB
        fs = GridFSBucket(db)
        music_file = open(self.actual_track.path,'rb')		#open the file in binary mode
        fs.upload_from_stream(self.track_name ,music_file.read())	#upload to gridfs 

class Genres(models.Model):
    genre_name = models.CharField(max_length = 50)

    def __str__(self):
        return self.genre_name