import mysql.connector
import random
import json
from datetime import datetime, timedelta

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="melis", 
    database="bbam" #musicstreamingdb
)

cursor = db.cursor()

artist_names = [
    "Taylor Swift", "Ed Sheeran", "Adele", "Drake", "Beyoncé",
    "Coldplay", "Ariana Grande", "Bruno Mars", "Lady Gaga", "Eminem",
    "The Weeknd", "Justin Bieber", "Rihanna", "Kanye West", "Dua Lipa",
    "Billie Eilish", "Harry Styles", "Selena Gomez", "Kendrick Lamar", "Shawn Mendes"
]

album_titles = [
    "Fearless", "Divide", "25", "Scorpion", "Lemonade",
    "Parachutes", "Sweetener", "Unorthodox Jukebox", "Chromatica", "Revival",
    "After Hours", "Justice", "Anti", "Donda", "Future Nostalgia",
    "Happier Than Ever", "Fine Line", "Rare", "DAMN.", "Illuminate"
]

track_titles = [
    "Love Story", "Shape of You", "Hello", "God's Plan", "Formation",
    "Yellow", "No Tears Left to Cry", "Treasure", "Shallow", "Lose Yourself",
    "Blinding Lights", "Peaches", "Diamonds", "Stronger", "Levitating",
    "Bad Guy", "Watermelon Sugar", "Hands to Myself", "HUMBLE.", "Treat You Better",
    "As It Was", "Daylight", "Counting Stars", "Senorita", "Uptown Funk",
    "Someone Like You", "Umbrella", "We Found Love", "Can't Feel My Face", "Late Night Talking"
    "Bad Guy", "Watermelon Sugar", "Hands to Myself", "HUMBLE.", "Treat You Better",
    "As It Was", "Daylight", "Counting Stars", "Senorita", "Uptown Funk",
    "Someone Like You", "Umbrella", "We Found Love", "Can't Feel My Face", "Late Night Talking"
]

playlist_names = [
    "Chill Vibes", "Workout Mix", "Top Hits 2024", "Throwback Classics", "Relax & Unwind",
    "Party Anthems", "Road Trip", "Focus Beats", "Love Songs", "Indie Pop Gems",
    "Rock Legends", "Hip Hop Hits", "Pop Essentials", "Jazz Nights", "Morning Motivation",
    "Evening Acoustic", "Study Session", "Dance Floor", "Soulful Sundays", "Fresh Finds", "Chill Vibes", "Workout Mix", "Top Hits 2024", "Throwback Classics", "Relax & Unwind",
    "Party Anthems", "Road Trip", "Focus Beats", "Love Songs", "Indie Pop Gems",
]

def random_date(start, end):
    delta = end - start
    random_days = random.randint(0, delta.days)
    return start + timedelta(days=random_days)

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

def generate_artists(num_artists):
    artists = []
    selected_artists = random.sample(artist_names, num_artists)
    for name in selected_artists:
        biography = f"{name} is an internationally acclaimed artist."
        genre = random.choice(['Pop', 'Rock', 'Hip Hop', 'Jazz', 'Classical'])
        # songs = random.sample(track_titles, random.randint(3, 7))
        artists.append((name, biography, genre))
    return artists

def generate_albums(num_albums, artist_ids):
    albums = []
    selected_albums = random.sample(album_titles, num_albums)
    for i, title in enumerate(selected_albums):
        release_date = random_date(datetime(2010, 1, 1), datetime(2024, 11, 27)).strftime('%Y-%m-%d')
        artist_id = random.choice(artist_ids)
        albums.append((title, release_date, artist_id))
    return albums

def generate_tracks(num_tracks, album_ids, album_artist_map, all_artist_ids):
    tracks = []
    selected_tracks = random.choices(track_titles, k=num_tracks)
    for i, title in enumerate(selected_tracks):
        duration = random.randint(120, 300)  # Süre saniye cinsinden
        album_id = random.choice(album_ids)
        primary_artist_id  = album_artist_map[album_id]
        other_artist_ids = random.sample(all_artist_ids, random.randint(0, 3))
        if primary_artist_id not in other_artist_ids:
            other_artist_ids.append(primary_artist_id) 
        genre = random.choice(['Pop', 'Rock', 'Hip Hop', 'Jazz', 'Classical'])
        file_path = f'/tracks/{title.replace(" ", "_").lower()}.mp3'
        artists_id = json.dumps(list(set(other_artist_ids)))  #json.dumps(random.sample(artist_ids, random.randint(1, 3)))
        play_count = random.randint(0, 10000)
        tracks.append((title, duration, album_id, genre, file_path, artists_id, play_count))
    return tracks

def generate_playlists(num_playlists, user_ids):
    playlists = []
    selected_playlists = random.sample(playlist_names, num_playlists)
    for i, name in enumerate(selected_playlists):
        user_id = random.choice(user_ids)
        created_at = random_date(datetime(2020, 1, 1), datetime(2024, 11, 27)).strftime('%Y-%m-%d')
        contained_items = json.dumps(random.sample(range(1, 100), 5))
        playlists.append((user_id, name, created_at, contained_items))
    return playlists

def generate_recently_listened(user_ids, track_ids, track_play_counts, tracks_per_user=10):
    recently_listened = []
    for user_id in user_ids:
        selected_tracks = random.sample(track_ids, tracks_per_user)
        
        for track_id in selected_tracks:
            global_play_count = track_play_counts[track_id]
            user_play_count = random.randint(1, max(global_play_count - 1, 1))
            timestamp = random_date(datetime(2020, 1, 1), datetime.now()).strftime('%Y-%m-%d %H:%M:%S')
            recently_listened.append((user_id, track_id, timestamp, user_play_count))
    
    return recently_listened

def generate_user_interactions(user_ids, track_data):
    user_interactions = []
    for user_id in user_ids:
        selected_tracks = random.sample(track_data, random.randint(5, 15))
        for track_id, duration in selected_tracks:
            liked = random.choice([True, False])
            timestamp = random.randint(0, duration - 1)
            user_interactions.append((user_id, track_id, liked, timestamp))
    return user_interactions







def generate_user_follow_interactions(user_ids):
    """
    Generates consistent Following and Followed_By relationships for users only.
    """
    # Initialize relationships for all users
    follow_interactions = {user_id: {"Following": set(), "Followed_By": set()} for user_id in user_ids}

    # Generate Following and Followed_By relationships
    for user_id in user_ids:
        # Randomly select other users to follow (excluding self)
        following_users = random.sample(
            [uid for uid in user_ids if uid != user_id], random.randint(0, 5)
        )

        # Add to Following and update Followed_By for the followed users
        follow_interactions[user_id]["Following"].update(following_users)
        for followed_user in following_users:
            follow_interactions[followed_user]["Followed_By"].add(user_id)

    # Convert sets to JSON-compatible lists for database insertion
    all_follow_interactions = []
    for user_id, relations in follow_interactions.items():
        all_follow_interactions.append((
            user_id,
            json.dumps(list(relations["Following"])),
            json.dumps(list(relations["Followed_By"]))
        ))

    return all_follow_interactions






def insert_users(users):
    query = "INSERT INTO Users (Username, Password, Email, Subscription_type, Created_at) VALUES (%s, %s, %s, %s, %s)"
    cursor.executemany(query, users)
    db.commit()

def insert_artists(artists):
    query = "INSERT INTO Artists (Name, Biography, Genre) VALUES (%s, %s, %s)"
    query = "INSERT INTO Artists (Name, Biography, Genre) VALUES (%s, %s, %s)"
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

def insert_recently_listened(recently_listened_data):
    query = "INSERT INTO Recently_Listened (User_ID, Track_ID, Timestamp, Play_Count) VALUES (%s, %s, %s, %s)"
    cursor.executemany(query, recently_listened_data)
    db.commit()

def insert_user_interactions(user_interactions):
    query = "INSERT INTO User_Interactions (User_ID, Track_ID, Liked, Timestamp) VALUES (%s, %s, %s, %s)"
    cursor.executemany(query, user_interactions)
    db.commit()
    
def insert_user_follow_interactions(user_follow_interactions):
    """
    User_Follow_Interactions tablosuna veri ekler.
    """
    query = """
    INSERT INTO User_Follow_Interactions (User_ID, Following, Followed_By)
    VALUES (%s, %s, %s)
    """
    cursor.executemany(query, user_follow_interactions)
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

cursor.execute("SELECT Album_ID, Artist_ID FROM Albums")
album_artist_map = {row[0]: row[1] for row in cursor.fetchall()}

cursor.execute("SELECT Artist_ID FROM Artists")
all_artist_ids = [row[0] for row in cursor.fetchall()]

tracks = generate_tracks(100, album_ids, album_artist_map, all_artist_ids)
cursor.execute("SELECT Album_ID, Artist_ID FROM Albums")
album_artist_map = {row[0]: row[1] for row in cursor.fetchall()}

cursor.execute("SELECT Artist_ID FROM Artists")
all_artist_ids = [row[0] for row in cursor.fetchall()]

tracks = generate_tracks(100, album_ids, album_artist_map, all_artist_ids)
insert_tracks(tracks)

cursor.execute("SELECT Track_ID FROM Tracks")
track_ids = [row[0] for row in cursor.fetchall()]

playlists = generate_playlists(30, user_ids)
insert_playlists(playlists)

cursor.execute("SELECT Track_ID, Play_Count FROM Tracks")
track_data = cursor.fetchall()
track_ids_for_RL = [row[0] for row in track_data]
track_play_counts = {row[0]: row[1] for row in track_data}
recently_listened_data = generate_recently_listened(user_ids, track_ids_for_RL, track_play_counts, tracks_per_user=10)
insert_recently_listened(recently_listened_data)

cursor.execute("SELECT Track_ID, Duration FROM Tracks")
track_data_duration = cursor.fetchall()
user_interactions = generate_user_interactions(user_ids, track_data_duration)
insert_user_interactions(user_interactions)

# Kullanıcılar ve sanatçılar için takip ilişkisi oluşturma
user_follow_interactions = generate_user_follow_interactions(user_ids)
# Takip ilişkisini tabloya ekleme
insert_user_follow_interactions(user_follow_interactions)

#close
db.close()
