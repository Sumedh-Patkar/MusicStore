from djongo import models
from pymongo import MongoClient
from gridfs import GridFSBucket
import os

# dbname = "MusicDB"

class Tracks(models.Model):
    track_name = models.CharField(max_length=100)
    track_length = models.IntegerField()
    track_image = models.FileField()
    actual_track = models.FileField()
    track_album = models.CharField(max_length=100)
    track_artist = models.CharField(max_length=100)

    def __str__(self):
       return self.track_name

    def save(self):
        #Save to the database
        super(Tracks,self).save()

        #Upload to Gridfs using pymongo commands
        print("Saved")
        db = MongoClient().MusicDB
        fs = GridFSBucket(db)
        music_file = open(self.actual_track.path,'rb')		#open the file in binary mode
        fs.upload_from_stream(self.actual_track.path ,music_file.read())	#upload to gridfs
