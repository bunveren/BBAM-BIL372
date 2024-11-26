from rest_framework import serializers
from .models import (
    Albums, Playlists, User_Interactions, Recently_Listened, 
    Users, User_Follow_Interactions, Artists, Tracks
)

class AlbumsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Albums
        fields = '__all__'


class PlaylistsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playlists
        fields = '__all__'


class UserInteractionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_Interactions
        fields = '__all__'


class RecentlyListenedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recently_Listened
        fields = '__all__'


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'


class UserFollowInteractionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_Follow_Interactions
        fields = '__all__'


class ArtistsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artists
        fields = '__all__'


class TracksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tracks
        fields = '__all__'