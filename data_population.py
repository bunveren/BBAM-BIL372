import mysql.connector
import random
import json
import time
from datetime import datetime, timedelta

# MySQL bağlantısı
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="melis",
    database="bbam"
)

cursor = db.cursor()

# Rastgele tarih üretme fonksiyonu
def random_date(start, end):
    delta = end - start
    random_days = random.randint(0, delta.days)
    return start + timedelta(days=random_days)

# Kullanıcı verisi oluşturma
def generate_users(num_users):
    users = []
    for i in range(num_users):
        username = f'user_{i + 1}_{random.randint(1000, 9999)}'
        password = f'password_{i + 1}'
        email = f'user_{i + 1}_{random.randint(1000, 9999)}@example.com'
        subscription_type = random.choice(['Free', 'Premium'])
        created_at = random_date(datetime(2020, 1, 1), datetime(2024, 11, 27)).strftime('%Y-%m-%d')
        users.append((username, password, email, subscription_type, created_at))
    return users

# Sanatçı verisi oluşturma
def generate_artists(num_artists):
    artists = []
    for i in range(num_artists):
        name = f'Artist {i + 1}'
        biography = f'Biography of Artist {i + 1}'
        genre = random.choice(['Rock', 'Pop', 'Jazz', 'Classical'])
        songs = json.dumps([f'Song {random.randint(1, 100)}' for _ in range(random.randint(1, 5))])
        artists.append((name, biography, genre, songs))
    return artists

# Albüm verisi oluşturma
def generate_albums(num_albums, artist_ids):
    albums = []
    for i in range(num_albums):
        title = f'Album {i + 1}'
        release_date = random_date(datetime(2020, 1, 1), datetime(2024, 11, 27)).strftime('%Y-%m-%d')
        artist_id = random.choice(artist_ids)
        albums.append((title, release_date, artist_id))
    return albums

# Parça verisi oluşturma
def generate_tracks(num_tracks, album_ids, artist_ids):
    tracks = []
    for i in range(num_tracks):
        title = f'Track {i + 1}'
        duration = random.randint(120, 300)  # Süre saniye cinsinden
        album_id = random.choice(album_ids)
        genre = random.choice(['Rock', 'Pop', 'Jazz', 'Classical'])
        file_path = f'/path/to/track{i + 1}.mp3'
        artists_id = json.dumps(random.sample(artist_ids, random.randint(1, 3)))
        play_count = random.randint(0, 10000)
        tracks.append((title, duration, album_id, genre, file_path, artists_id, play_count))
    return tracks

# Playlist verisi oluşturma
def generate_playlists(num_playlists, user_ids):
    playlists = []
    for i in range(num_playlists):
        user_id = random.choice(user_ids)
        name = f'Playlist {i + 1}'
        created_at = random_date(datetime(2020, 1, 1), datetime(2024, 11, 27)).strftime('%Y-%m-%d')
        tracks = json.dumps(random.sample(range(1, 100), 5))  # Playlist içeriği
        playlists.append((user_id, name, created_at, tracks))
    return playlists



# Rastgele UNIX timestamp üretme fonksiyonu
def random_unix_timestamp(start, end):
    """Belirtilen tarih aralığında rastgele bir UNIX timestamp döndürür."""
    random_datetime = random_date(start, end)
    return int(time.mktime(random_datetime.timetuple()))

# Kullanıcı etkileşimleri verisi oluşturma
def generate_user_interactions(num_interactions, user_ids, track_ids):
    interactions = []
    for _ in range(num_interactions):
        user_id = random.choice(user_ids)
        track_id = random.choice(track_ids)
        liked = random.choice([True, False])
        timestamp = random_unix_timestamp(datetime(2020, 1, 1), datetime(2024, 11, 27))  # UNIX timestamp (saniye)
        interactions.append((user_id, track_id, liked, timestamp))
    return interactions

# User Interactions verilerini ekleme
def insert_user_interactions(interactions):
    query = "INSERT INTO User_Interactions (User_ID, Track_ID, Liked, Timestamp) VALUES (%s, %s, %s, %s)"
    cursor.executemany(query, interactions)
    db.commit()


# Recently listened verisi oluşturma
def generate_recently_listened(num_entries, user_ids, track_ids):
    entries = []
    for _ in range(num_entries):
        user_id = random.choice(user_ids)
        track_id = random.choice(track_ids)
        timestamp = random_date(datetime(2020, 1, 1), datetime(2024, 11, 27)).strftime('%Y-%m-%d %H:%M:%S')
        play_count = random.randint(1, 100)
        entries.append((user_id, track_id, timestamp, play_count))
    return entries

# Tablolara veri ekleme fonksiyonları
def insert_users(users):
    query = "INSERT INTO Users (Username, Password, Email, Subscription_type, Created_at) VALUES (%s, %s, %s, %s, %s)"
    cursor.executemany(query, users)
    db.commit()

def insert_artists(artists):
    query = "INSERT INTO Artists (Name, Biography, Genre, Songs) VALUES (%s, %s, %s, %s)"
    cursor.executemany(query, artists)
    db.commit()

def insert_albums(albums):
    query = "INSERT INTO Albums (Title, Release_date, Artist_ID) VALUES (%s, %s, %s)"
    cursor.executemany(query, albums)
    db.commit()

def insert_tracks(tracks):
    query = "INSERT INTO Tracks (Title, Duration, Album_ID, Genre, File_Path, Artists_ID, Play_Count) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    cursor.executemany(query, tracks)
    db.commit()

def insert_playlists(playlists):
    query = "INSERT INTO Playlists (User_ID, Name, Created_at, Tracks) VALUES (%s, %s, %s, %s)"
    cursor.executemany(query, playlists)
    db.commit()

def insert_user_interactions(interactions):
    query = "INSERT INTO User_Interactions (User_ID, Track_ID, Liked, Timestamp) VALUES (%s, %s, %s, %s)"
    cursor.executemany(query, interactions)
    db.commit()

def insert_recently_listened(entries):
    query = "INSERT INTO Recently_Listened (User_ID, Track_ID, Timestamp, Play_Count) VALUES (%s, %s, %s, %s)"
    cursor.executemany(query, entries)
    db.commit()

# Veri üretimi ve ekleme
users = generate_users(50)
insert_users(users)

cursor.execute("SELECT User_ID FROM Users")
user_ids = [row[0] for row in cursor.fetchall()]

artists = generate_artists(20)
insert_artists(artists)

cursor.execute("SELECT Artist_ID FROM Artists")
artist_ids = [row[0] for row in cursor.fetchall()]

albums = generate_albums(15, artist_ids)
insert_albums(albums)

cursor.execute("SELECT Album_ID FROM Albums")
album_ids = [row[0] for row in cursor.fetchall()]

tracks = generate_tracks(100, album_ids, artist_ids)
insert_tracks(tracks)

cursor.execute("SELECT Track_ID FROM Tracks")
track_ids = [row[0] for row in cursor.fetchall()]

playlists = generate_playlists(30, user_ids)
insert_playlists(playlists)

interactions = generate_user_interactions(50, user_ids, track_ids)
insert_user_interactions(interactions)

recently_listened = generate_recently_listened(50, user_ids, track_ids)
insert_recently_listened(recently_listened)

# Bağlantıyı kapat
db.close()
