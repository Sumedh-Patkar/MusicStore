from django.shortcuts import render
from pymongo import MongoClient
from .models import Tracks, Genres
from django.http import HttpResponse
from pymongo import MongoClient
from gridfs import GridFSBucket
import os

# Create your views here.
def index(request):
	return render(request, 'MusicDownload/index.html',{})

def track_list(request):
    all_tracks = Tracks.objects.all() 
    all_genres = Genres.objects.all()
    context = {
        "all_tracks" : all_tracks,
        "all_genres" : all_genres,
    }

    return render(request, 'MusicDownload/track-list.html',context)

def track(request, pk):
    selected_track = Tracks.objects.get(pk = pk)
    all_genres = Genres.objects.all()
    context = {
        "selected_track" : selected_track,
        "all_genres" : all_genres,
    }
    return render(request, 'MusicDownload/track.html',context)

def genre(request, pk):
    genre_name = Genres.objects.get(pk = pk)
    all_genres = Genres.objects.all()
    genre_track_list = Tracks.objects.filter(track_genre = genre_name)
    context = {
        "genre_track_list" : genre_track_list,
        "all_genres" : all_genres,
    }
    return render(request, 'MusicDownload/genre.html',context)

def download(request, pk):
    selected_track = Tracks.objects.get(pk = pk)
    print("Downloaded")
    db = MongoClient().MusicDB
    fs = GridFSBucket(db)
    music_file_stream = fs.open_download_stream_by_name(selected_track.track_name)
    response = HttpResponse(music_file_stream.read(), content_type = 'content_type: audio/mpeg')
    response['Content-Disposition'] = 'attachment; filename=' + (str)(selected_track.actual_track)
    return response
