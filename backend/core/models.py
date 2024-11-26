from django.db import models

# Create your models here.

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
    Duration = models.IntegerField(default=0, max_length=1000)
    File_Path = models.CharField(max_length=255)
    Play_count = models.IntegerField(default=0)
