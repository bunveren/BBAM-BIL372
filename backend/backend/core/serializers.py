from rest_framework import serializers
from .models import (
    Albums, Playlists, UserInteractions, RecentlyListened, 
    Users, UserFollowInteractions, Artists, Tracks
)

class PlaylistsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playlists
        fields = '__all__'


class UserInteractionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInteractions
        fields = '__all__'


class RecentlyListenedSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecentlyListened
        fields = '__all__'


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'


class UserFollowInteractionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserFollowInteractions
        fields = '__all__'


class ArtistsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artists
        fields = '__all__'


class TracksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tracks
        fields = '__all__'

class AlbumsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Albums
        fields = '__all__'

        artist = ArtistsSerializer(source='Artist_ID',
            read_only=True)  # Use the ForeignKey 'Artist_ID' to retrieve artist data
