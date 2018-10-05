from django.shortcuts import render
from pymongo import MongoClient
from .models import *
from django.http import HttpResponse
from pymongo import MongoClient
from gridfs import GridFSBucket
import os

# Create your views here.
def index(request):
	return render(request, 'MusicDownload/index.html',{})

def track_list(request):

    all_tracks = Tracks.objects.all() 
    context = {"all_tracks" : all_tracks}
    return render(request, 'MusicDownload/track-list.html',context)

def track(request, pk):
    selected_track = Tracks.objects.get(pk = pk)
    context = { "selected_track" : selected_track }
    return render(request, 'MusicDownload/track.html',context)

def genre(request):
	return render(request, 'MusicDownload/genre.html',{})

def download(request, pk):
    selected_track = Tracks.objects.get(pk = pk)
    print("Downloaded")
    db = MongoClient().MusicDB
    fs = GridFSBucket(db)
    music_file_stream = fs.open_download_stream_by_name(selected_track.track_name)
    response = HttpResponse(music_file_stream.read(), content_type = 'content_type: audio/mpeg')
    response['Content-Disposition'] = 'attachment; filename=' + (str)(selected_track.actual_track)
    return response
