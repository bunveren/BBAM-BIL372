from django.db import models

class Albums(models.Model):
    Album_ID = models.AutoField(primary_key = True)
    Title = models.CharField(max_length = 100)
    Release_date = models.DateField()
    Artist_ID = models.ForeignKey(
        'Artists',
        on_delete = models.CASCADE
    )

class Playlists(models.Model):
    Playlist_ID = models.AutoField(primary_key = True)
    User_ID = models.ForeignKey(
        'Users',
        on_delete = models.CASCADE
    )
    Name = models.CharField(max_length = 100)
    Created_at = models.DateField()
    Tracks = models.JSONField(default = list)


class User_Interactions:
    Interaction_ID = models.AutoField(primary_key = True)
    User_ID = models.ForeignKey(
        'Users',
        on_delete = models.CASCADE
    )
    Track_ID = models.ForeignKey(
        'Tracks',
        on_delete = models.CASCADE
    )
    Liked = models.BooleanField()
    Timestamp = models.IntegerField(default = 0, max_length = 1000)

class Recently_Listened:
    Recently_Listened_ID = models.AutoField(primary_key = True)
    User_ID = models.ForeignKey(
        'Users',
        on_delete = models.CASCADE
    )
    Track_ID = models.ForeignKey(
        'Tracks',
        on_delete = models.CASCADE
    )
    Timestamp = models.IntegerField(default = 0, max_length = 1000)
    Play_count = models.IntegerField()

class Users(models.Model):
    User_ID = models.AutoField(primary_key=True)
    Username = models.CharField(max_length=100)
    Password = models.CharField(max_length=100)
    Email = models.EmailField()
    Subscription_type = models.IntegerField(default=0)
    Created_at = models.DateTimeField(auto_now_add=True)

class User_Follow_Interactions(models.Model):
    User_ID = models.ForeignKey('Users', on_delete=models.CASCADE)
    Following = models.JSONField(default=list)
    Followed_by = models.JSONField(default=list)

class Artists(models.Model):
    Artist_ID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=100)
    Biography = models.TextField()
    Genre = models.TextField(max_length=100)
    Songs = models.JSONField(default=list)

class Tracks(models.Model):
    Track_ID = models.AutoField(primary_key=True)
    Artists_ID = models.JSONField(default=list)
    Album_ID = models.ForeignKey('Albums', on_delete=models.CASCADE)
    Title = models.CharField(max_length=100)
    Genre = models.TextField(max_length=100)
    Duration = models.IntegerField(default=0)
    File_Path = models.CharField(max_length=255)
    Play_count = models.IntegerField(default=0)
