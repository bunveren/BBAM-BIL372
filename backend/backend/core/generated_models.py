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


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class CoreAlbums(models.Model):
    album_id = models.AutoField(db_column='Album_ID', primary_key=True)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=100)  # Field name made lowercase.
    release_date = models.DateField(db_column='Release_date')  # Field name made lowercase.
    artist_id = models.ForeignKey('CoreArtists', models.DO_NOTHING, db_column='Artist_ID_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'core_albums'


class CoreArtists(models.Model):
    artist_id = models.AutoField(db_column='Artist_ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100)  # Field name made lowercase.
    biography = models.TextField(db_column='Biography')  # Field name made lowercase.
    genre = models.TextField(db_column='Genre')  # Field name made lowercase.
    songs = models.JSONField(db_column='Songs')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'core_artists'


class CorePlaylists(models.Model):
    playlist_id = models.AutoField(db_column='Playlist_ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100)  # Field name made lowercase.
    created_at = models.DateField(db_column='Created_at')  # Field name made lowercase.
    tracks = models.JSONField(db_column='Tracks')  # Field name made lowercase.
    user_id = models.ForeignKey('CoreUsers', models.DO_NOTHING, db_column='User_ID_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'core_playlists'


class CoreTracks(models.Model):
    track_id = models.AutoField(db_column='Track_ID', primary_key=True)  # Field name made lowercase.
    artists_id = models.JSONField(db_column='Artists_ID')  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=100)  # Field name made lowercase.
    genre = models.TextField(db_column='Genre')  # Field name made lowercase.
    duration = models.IntegerField(db_column='Duration')  # Field name made lowercase.
    file_path = models.CharField(db_column='File_Path', max_length=255)  # Field name made lowercase.
    play_count = models.IntegerField(db_column='Play_count')  # Field name made lowercase.
    album_id = models.ForeignKey(CoreAlbums, models.DO_NOTHING, db_column='Album_ID_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'core_tracks'


class CoreUserFollowInteractions(models.Model):
    id = models.BigAutoField(primary_key=True)
    following = models.JSONField(db_column='Following')  # Field name made lowercase.
    followed_by = models.JSONField(db_column='Followed_by')  # Field name made lowercase.
    user_id = models.ForeignKey('CoreUsers', models.DO_NOTHING, db_column='User_ID_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'core_user_follow_interactions'


class CoreUsers(models.Model):
    user_id = models.AutoField(db_column='User_ID', primary_key=True)  # Field name made lowercase.
    username = models.CharField(db_column='Username', max_length=100)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=100)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=254)  # Field name made lowercase.
    subscription_type = models.IntegerField(db_column='Subscription_type')  # Field name made lowercase.
    created_at = models.DateTimeField(db_column='Created_at')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'core_users'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


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
    user = models.ForeignKey('Users', models.DO_NOTHING, db_column='User_ID')  # Field name made lowercase.

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
