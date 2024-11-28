from rest_framework import status
from .models import Users, UserFollowInteractions, Artists, Albums, Tracks, Playlists, UserInteractions, \
    RecentlyListened
from .serializers import UsersSerializer, UserFollowInteractionsSerializer, ArtistsSerializer, AlbumsSerializer, \
    TracksSerializer, PlaylistsSerializer, UserInteractionsSerializer, RecentlyListenedSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

import json
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from django.core.exceptions import ValidationError

@api_view(['GET', 'POST'])
def users_list(request):
    if request.method == 'GET':
        users = Users.objects.all()
        serializer = UsersSerializer(users, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = UsersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def user_detail(request, user_id):
    try:
        user = Users.objects.get(user_id=user_id)
    except Users.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UsersSerializer(user)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = UsersSerializer(user, data=request.data)  # Validates incoming data
        if serializer.is_valid():  # Ensures incoming data is valid
            serializer.save()  # Saves the validated data to the database
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#todo ask @betulls

@api_view(['GET', 'PUT', 'DELETE'])
def user_following(request, user_id):
    try:
        following = UserFollowInteractions.objects.values_list('following', flat=True).get(user_id=pk)
    except UserFollowInteractions.DoesNotExist:
        return Response({'error': 'User_Follow_Interactions not found.'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        return Response({'following': following}, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        new_following = request.data.get('following', None)
        if new_following is not None:
            user_interaction.following = new_following
            user_interaction.save()
            return Response({'message': 'following updated successfully.'}, status=status.HTTP_200_OK)

        return Response({'error': 'Invalid data provided.'}, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        user_interaction.following.delete()
        return Response({'message': 'User_Follow_Interactions:Following deleted successfully.'}, status=status.HTTP_200_OK)


@api_view(['GET', 'PUT', 'DELETE'])
def user_followed_by(request, user_id):
    try:
        followed_by = UserFollowInteractions.objects.values_list('followed_by', flat=True).get(user_id=pk)
    except UserFollowInteractions.DoesNotExist:
        return Response({'error': 'User_Follow_Interactions not found.'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        return Response({'followed_by': followed_by}, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        new_followed = request.data.get('followed_by', None)
        if new_followed is not None:
            user_interaction.followed_by = new_followed
            user_interaction.save()
            return Response({'message': 'Followed by updated successfully.'}, status=status.HTTP_200_OK)

        return Response({'error': 'Invalid data provided.'}, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        user_interaction.followed_by.delete()
        return Response({'message': 'User_Follow_Interactions:Followed_by deleted successfully.'}, status=status.HTTP_200_OK)


@api_view(['GET', 'POST'])
def artists_list(request):
    if request.method == 'GET':
        artists = Artists.objects.all()
        serializer = ArtistsSerializer(artists, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ArtistsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def artist_detail(request, artist_id):
    try:
        artist = Artists.objects.get(artist_id=artist_id)
    except Artists.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ArtistsSerializer(artist)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ArtistsSerializer(artist, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        artist.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def tracks_list(request):
    if request.method == 'GET':
        tracks = Tracks.objects.all()
        serializer = TracksSerializer(tracks, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = TracksSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def track_detail(request, track_id):
    try:
        track = Tracks.objects.get(track_id=track_id)
    except Tracks.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TracksSerializer(track)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = TracksSerializer(track, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        track.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Albums

@api_view(['GET', 'POST'])  # /api/albums
def all_albums(request):
    if request.method == 'GET':
        albums = Albums.objects.all()
        serializer = AlbumsSerializer(albums, many=True)
        return Response(serializer.data, status=200)

    elif request.method == 'POST':
        serializer = AlbumsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])  # /api/albums/{album_id}
def album_detail(request, album_id):
    try:
        album = Albums.objects.get(album_id=album_id)
    except Albums.DoesNotExist:
        return Response({"error": "Album not found"}, status=404)

    if request.method == 'GET':
        serializer = AlbumsSerializer(album)
        return Response(serializer.data, status=200)

    elif request.method == 'PUT':
        serializer = AlbumsSerializer(album, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        album.delete()
        return Response({"message": "Album deleted successfully"}, status=204)


@api_view(['GET'])  # /api/albums/artists/{artist_id}
def artist_albums(request, artist_id):
    try:
        albums = Albums.objects.filter(artist_id=artist_id)
        if not albums.exists():
            return Response({"error": "No albums found for this artist"}, status=404)
        serializer = AlbumsSerializer(albums, many=True)
        return Response(serializer.data, status=200)
    except Exception as e:
        return Response({"error": str(e)}, status=500)

    # Playlists


#todo bunları anlamadım
"""
/api/users/<int:user_id>/playlists/

    GET: List all playlists of a user.
    PUT: Add a new playlist for the user.
    DELETE: Delete a user’s playlist.

/api/users/<int:user_id>/playlists/<int:playlist_id>/

    GET: Retrieve a specific playlist for a user.
    POST: Update a playlist (e.g., tracks, name).
"""


@api_view(['GET', 'POST'])  # /api/playlists/users/{user_id}
def all_user_playlists(request, user_id):
    if request.method == 'GET':
        playlists = Playlists.objects.filter(user_id=user_id)
        if playlists.exists():
            serializer = PlaylistsSerializer(playlists, many=True)
            return Response(serializer.data, status=200)
        return Response({"error": "No playlists found for this user"}, status=status.HTTP_404_NOT_FOUND)

    elif request.method == 'POST':
        data = request.data
        data['user_id'] = user_id
        serializer = PlaylistsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])  # /api/playlists/users/{user_id}/{playlist_id}
def playlist_detail(request, user_id, playlist_id):
    try:
        playlist = Playlists.objects.get(user_id=user_id, playlist_id=playlist_id)
    except Playlists.DoesNotExist:
        return Response({"error": "Playlist not found"}, status=404)

    if request.method == 'GET':
        serializer = PlaylistsSerializer(playlist)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PlaylistsSerializer(playlist, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        playlist.delete()
        return Response({"message": "Playlist deleted successfully"}, status=204)


# User_Interactions
# todo parametre post ama iceride put var
@api_view(['GET', 'POST', 'DELETE'])  # api/user_interactions/{user_id}/{track_id}
def user_interaction(request, user_id, track_id):
    try:
        interaction = UserInteractions.objects.get(user_id=user_id, track_id=track_id)
    except UserInteractions.DoesNotExist:
        return Response({"error": "Interaction not found"}, status=404)

    if request.method == 'GET':
        # Retrieve the interaction
        serializer = UserInteractionsSerializer(interaction)
        return Response(serializer.data)

    elif request.method == 'PUT':
        # Update the interaction
        serializer = UserInteractionsSerializer(interaction, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        # Delete the interaction
        interaction.delete()
        return Response({"message": "Interaction deleted successfully"}, status=204)


# Recently_Listened
@api_view(['GET', 'POST', 'DELETE'])  # /api/recently_listened/{user_id}/{track_id}
def recently_listened(request, user_id):
    try:
        recently_listened_entry = RecentlyListened.objects.get(user_id=user_id)
    except RecentlyListened.DoesNotExist:
        return Response({"error": "Recently listened entry not found"}, status=404)

    if request.method == 'GET':
        # Retrieve the recently listened entry
        serializer = RecentlyListenedSerializer(recently_listened_entry)
        return Response(serializer.data)

    elif request.method == 'POST':
        # Update or add the recently listened entry (e.g., play count or timestamp)
        serializer = RecentlyListenedSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        # Delete the recently listened entry
        recently_listened_entry.delete()
        return Response({"message": "Recently listened entry deleted successfully"}, status=204)
