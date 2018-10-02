from django.shortcuts import render
from pymongo import MongoClient

# Create your views here.
def index(request):
	return render(request, 'MusicDownload/index.html',{})
def track_list(request):
	return render(request, 'MusicDownload/track-list.html',{})
def track(request):
	return render(request, 'MusicDownload/track.html',{})
def genre(request):
	return render(request, 'MusicDownload/genre.html',{})