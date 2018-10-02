from django.shortcuts import render
from pymongo import MongoClient
from .models import *

# Create your views here.
def index(request):
	return render(request, 'MusicDownload/index.html',{})
def track_list(request):

    all_tracks = Tracks.objects.all() 
    context = {"all_tracks" : all_tracks}
    # count = 1
    # for song in Tracks.objects.all():
	   #  track = {"track_name":song.track_name,"track_image":song.track_image,"track_length":song.track_length,"track_album":song.track_album,"track_artist":song.track_artist}
	   #  all_tracks[count] = track
	   #  count=count+1
    print(all_tracks)   		    
    return render(request, 'MusicDownload/track-list.html',context)
def track(request):
	return render(request, 'MusicDownload/track.html',{})
def genre(request):
	return render(request, 'MusicDownload/genre.html',{})

	