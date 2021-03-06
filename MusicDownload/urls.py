"""MusicDownload URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, re_path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'MusicDownload'

urlpatterns = [
    path('', views.home, name = "home"),
    path('track-list/',views.track_list, name = "track-list"),
    re_path(r'^track/(?P<pk>\d+)/$',views.track, name = "track"),
    re_path(r'^genre/(?P<pk>\d+)/$',views.genre, name = "genre"),
    re_path(r'^download/(?P<pk>\d+)/$', views.download, name="download"),
    re_path(r'^stream/(?P<pk>\d+)/$', views.stream, name="stream"),
]
