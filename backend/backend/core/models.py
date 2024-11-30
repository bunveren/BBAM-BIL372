# This is an auto-generated Django model module.

# You'll have to do the following manually to clean this up:

#   * Rearrange models' order

#   * Make sure each model has one field with primary_key=True

#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior

#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table

# Feel free to rename the models, but don't rename db_table values or field names.

from django.db import models

class Albums(models.Model):

    album_id = models.BigAutoField(db_column='Album_ID', primary_key=True)  # Field name made lowercase.

    title = models.CharField(db_column='Title', max_length=100)  # Field name made lowercase.

    release_date = models.DateField(db_column='Release_date')  # Field name made lowercase.

    artist = models.ForeignKey('Artists', models.DO_NOTHING, db_column='Artist_ID')  # Field name made lowercase.



    class Meta:

        managed = False

        db_table = 'albums'





class Artists(models.Model):

    artist_id = models.BigAutoField(db_column='Artist_ID', primary_key=True)  # Field name made lowercase.

    name = models.CharField(db_column='Name', max_length=100)  # Field name made lowercase.

    biography = models.TextField(db_column='Biography', blank=True, null=True)  # Field name made lowercase.

    genre = models.CharField(db_column='Genre', max_length=50, blank=True, null=True)  # Field name made lowercase.



    class Meta:

        managed = False

        db_table = 'artists'





class Playlists(models.Model):

    playlist_id = models.BigAutoField(db_column='Playlist_ID', primary_key=True)  # Field name made lowercase.

    user = models.ForeignKey('Users', models.DO_NOTHING, db_column='User_ID')  # Field name made lowercase.

    name = models.CharField(db_column='Name', max_length=100)  # Field name made lowercase.

    created_at = models.DateField(db_column='Created_at', blank=True, null=True)  # Field name made lowercase.

    tracks = models.JSONField(db_column='Tracks', blank=True, null=True)  # Field name made lowercase.



    class Meta:

        managed = False

        db_table = 'playlists'





class RecentlyListened(models.Model):

    recently_listened_id = models.BigAutoField(db_column='Recently_Listened_ID', primary_key=True)  # Field name made lowercase.

    user = models.ForeignKey('Users', models.DO_NOTHING, db_column='User_ID')  # Field name made lowercase.

    track = models.ForeignKey('Tracks', models.DO_NOTHING, db_column='Track_ID')  # Field name made lowercase.

    timestamp = models.DateField(db_column='Timestamp', blank=True, null=True)  # Field name made lowercase.

    play_count = models.IntegerField(db_column='Play_count', blank=True, null=True)  # Field name made lowercase.



    class Meta:

        managed = False

        db_table = 'recently_listened'





class Tracks(models.Model):

    track_id = models.BigAutoField(db_column='Track_ID', primary_key=True)  # Field name made lowercase.

    title = models.CharField(db_column='Title', max_length=100)  # Field name made lowercase.

    duration = models.IntegerField(db_column='Duration')  # Field name made lowercase.

    album = models.ForeignKey(Albums, models.DO_NOTHING, db_column='Album_ID')  # Field name made lowercase.

    genre = models.CharField(db_column='Genre', max_length=50, blank=True, null=True)  # Field name made lowercase.

    file_path = models.CharField(db_column='File_Path', max_length=255)  # Field name made lowercase.

    artists_id = models.JSONField(db_column='Artists_ID')  # Field name made lowercase.

    play_count = models.IntegerField(db_column='Play_count', blank=True, null=True)  # Field name made lowercase.



    class Meta:

        managed = False

        db_table = 'tracks'





class UserFollowInteractions(models.Model):

    following = models.JSONField(db_column='Following')  # Field name made lowercase.

    followed_by = models.JSONField(db_column='Followed_By')  # Field name made lowercase.

    user_id = models.ForeignKey('Users', models.DO_NOTHING, db_column='User_ID', primary_key = True)  # Field name made lowercase.



    class Meta:

        managed = False

        db_table = 'user_follow_interactions'





class UserInteractions(models.Model):

    interaction_id = models.BigAutoField(db_column='Interaction_ID', primary_key=True)  # Field name made lowercase.

    user = models.ForeignKey('Users', models.DO_NOTHING, db_column='User_ID')  # Field name made lowercase.

    track = models.ForeignKey(Tracks, models.DO_NOTHING, db_column='Track_ID')  # Field name made lowercase.

    liked = models.IntegerField(db_column='Liked', blank=True, null=True)  # Field name made lowercase.

    timestamp = models.IntegerField(db_column='Timestamp', blank=True, null=True)  # Field name made lowercase.



    class Meta:

        managed = False

        db_table = 'user_interactions'





class Users(models.Model):
    user_id = models.BigAutoField(db_column='User_ID', primary_key=True)  # Field name made lowercase.
    username = models.CharField(db_column='Username', unique=True, max_length=50)  # Field name made lowercase.

    password = models.CharField(db_column='Password', max_length=50)  # Field name made lowercase.

    email = models.CharField(db_column='Email', unique=True, max_length=50)  # Field name made lowercase.

    subscription_type = models.CharField(db_column='Subscription_type', max_length=7)  # Field name made lowercase.

    created_at = models.DateField(db_column='Created_at', blank=True, null=True)  # Field name made lowercase.



    class Meta:
        managed = False
        db_table = 'users'