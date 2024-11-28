"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from .core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/admin/', admin.site.urls),
    path('api/users/', views.users_list, name='users_list'),
    path('api/users/<int:pk>/', views.user_detail, name='user_detail'),

    path('api/user-follow/<int:pk>/', views.user_following, name='user_following'),
    path('api/user-follow/<int:pk>/', views.user_followed_by, name='user_followed_by'),

    path('api/artists/', views.artists_list, name='artists_list'),
    path('api/artists/<int:pk>/', views.artist_detail, name='artist_detail'),

    path('api/tracks/', views.tracks_list, name='tracks_list'),
    path('api/tracks/<int:pk>/', views.track_detail, name='track_detail'),

    path('api/albums/', views.all_albums, name='all-albums'),
    path('api/albums/<int:album_id>/', views.album_detail, name='album-detail'),
    path('api/albums/artists/<int:artist_id>/', views.artist_albums, name='artist-albums'),

    path('api/playlists/users/<int:user_id>/', views.all_user_playlists, name='all-user-playlists'),
    path('api/playlists/users/<int:user_id>/<int:playlist_id>/', views.playlist_detail, name='playlist-detail'),
    
    path('api/user_interactions/<int:user_id>/<int:track_id>/', views.user_interaction, name='user-interaction'),
    path('api/recently_listened/<int:user_id>/<int:track_id>/', views.recently_listened, name='recently-listened')
]
