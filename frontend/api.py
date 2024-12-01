import requests

BASE_URL = "http://127.0.0.1:8000/api/"

# GET all users
def get_users():
    response = requests.get(f"{BASE_URL}users/")
    if response.status_code == 200:
        return response.json()
    return {"error": "Unable to fetch users"}

# POST a new user
def create_user(user_data):
    response = requests.post(f"{BASE_URL}users/", data=user_data)
    if response.status_code == 201:
        return response.json()
    return {"error": "Unable to create user"}

# GET a specific user by ID
def get_user(user_id):
    response = requests.get(f"{BASE_URL}users/{user_id}/")
    if response.status_code == 200:
        return response.json()
    return {"error": "User not found"}

# PUT (Update) a user
def update_user(user_id, user_data):
    response = requests.put(f"{BASE_URL}users/{user_id}/", data=user_data)
    if response.status_code == 200:
        return response.json()
    return {"error": "Unable to update user"}

# DELETE a user
def delete_user(user_id):
    response = requests.delete(f"{BASE_URL}users/{user_id}/")
    if response.status_code == 204:
        return {"message": "User deleted successfully"}
    return {"error": "Unable to delete user"}

# GET the users the user is following
def get_following(user_id):
    response = requests.get(f"{BASE_URL}user_following/{user_id}/")
    if response.status_code == 200:
        return response.json()
    return {"error": "Unable to fetch following"}

# PUT (Add) a user to following
def follow_user(user_id, follow_data):
    response = requests.put(f"{BASE_URL}user_following/{user_id}/", data=follow_data)
    if response.status_code == 200:
        return response.json()
    return {"error": "Unable to add following"}

# DELETE (Remove) a user from following
def unfollow_user(user_id, follow_data):
    response = requests.delete(f"{BASE_URL}user_following/{user_id}/", data=follow_data)
    if response.status_code == 200:
        return response.json()
    return {"error": "Unable to remove following"}

# GET the users followers
def get_followed_by(user_id):
    response = requests.get(f"{BASE_URL}user_followed_by/{user_id}/")
    if response.status_code == 200:
        return response.json()
    return {"error": "Unable to fetch followers"}

# PUT (Add) a user to followers
def add_follower(user_id, follow_data):
    response = requests.put(f"{BASE_URL}user_followed_by/{user_id}/", data=follow_data)
    if response.status_code == 200:
        return response.json()
    return {"error": "Unable to add follower"}

# DELETE (Remove) a user from followers
def unfollow_user(user_id, follow_data):
    response = requests.delete(f"{BASE_URL}user_followed_by/{user_id}/", data=follow_data)
    if response.status_code == 200:
        return response.json()
    return {"error": "Unable to remove follower"}

# GET all artists
def get_artists():
    response = requests.get(f"{BASE_URL}artists/")
    if response.status_code == 200:
        return response.json()
    return {"error": "Unable to fetch artists"}

# PUT (Add) an artist
def create_artist(artist_data):
    response = requests.put(f"{BASE_URL}artists/", json=artist_data)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error" : "Unable to add artist"}

# GET a specific artist by ID
def get_artist(artist_id):
    response = requests.get(f"{BASE_URL}artists/{artist_id}/")
    if response.status_code == 200:
        return response.json()
    return {"error": "Artist not found"}

# POST (Update) an artist
def update_artist(artist_id, artist_data):
    response = requests.put(f"{BASE_URL}artists/{artist_id}/", data=artist_data)
    if response.status_code == 200:
        return response.json()
    return {"error": "Unable to update artist"}

# DELETE (Remove) an artist
def delete_artist(artist_id):
    response = requests.delete(f"{BASE_URL}artists/{artist_id}/")
    if response.status_code == 204:
        return response.json()
    else:
        {"error": "Unable to delete artist"}

# GET all albums
def get_albums():
    response = requests.get(f"{BASE_URL}albums/")
    if response.status_code == 200:
        return response.json()
    return {"error": "Unable to fetch albums"}

# PUT (create) an album
def create_album(album_data):
    response = requests.put(f"{BASE_URL}albums/", json=album_data)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error" : "Unable to add album"}

# GET albums by a specific artist
def get_artist_albums(artist_id):
    response = requests.get(f"{BASE_URL}albums/artists/{artist_id}/")
    if response.status_code == 200:
        return response.json()
    return {"error": "No albums found for this artist"}

# POST (update) an album
def update_album_detail(album_id, album_data):
    response = requests.post(f"{BASE_URL}albums/{album_id}/", json=album_data)
    if response.status_code == 200:
        return response.json()
    return {"error": "Unable to update album"}

# DELETE (remove) an album
def delete_album(album_id):
    response = requests.delete(f"{BASE_URL}albums/{album_id}/")
    if response.status_code == 204:
        return response.json()
    else:
        {"error": "Unable to delete album"}

# GET all albums of an artist
def get_artist_albums(artist_id):
    response = requests.get(f"{BASE_URL}albums/artists/{artist_id}/")
    if response.status_code == 200:
        return response.json()
    return {"error": "Unable to fetch albums of the artist"}

# GET all tracks
def get_tracks():
    response = requests.get(f"{BASE_URL}tracks/")
    if response.status_code == 200:
        return response.json()
    return {"error": "Unable to fetch tracks"}

# PUT (add) a track
def create_track(track_data):
    response = requests.put(f"{BASE_URL}tracks/", json=track_data)
    if response.status_code == 201:
        return response.json()
    else:
        return {"error": "Unable to add track"}

# GET a specific track by ID
def get_track(track_id):
    response = requests.get(f"{BASE_URL}tracks/{track_id}/")
    if response.status_code == 200:
        return response.json()
    return {"error": "Track not found"}

# POST (update) a track
def update_track(track_id, track_data):
    response = requests.post(f"{BASE_URL}tracks/{track_id}/", json=track_data)
    if response.status_code == 200:
        return response.json()
    return {"error": "Unable to update found"}

# DELETE (remove) a track
def delete_track(track_id):
    response = requests.delete(f"{BASE_URL}tracks/{track_id}/")
    if response.status_code == 204:
        return response.json()
    else:
        {"error": "Unable to delete track"}

# GET all playlists for a user
def get_user_playlists(user_id):
    response = requests.get(f"{BASE_URL}playlists/users/{user_id}/")
    if response.status_code == 200:
        return response.json()
    return {"error": "Unable to fetch playlists"}

# POST (create) a new playlist for user
def create_user_playlist(user_id, playlist_data):
    response = requests.post(f"{BASE_URL}playlists/users/{user_id}/", json=playlist_data)
    if response.status_code in [200, 201]:
        return response.json()
    return {"error": "Unable to add playlist"}

# GET playlist details of a user
def get_playlist_detail(user_id, playlist_id):
    response = requests.get(f"{BASE_URL}playlists/users/{user_id}/{playlist_id}/")
    if response.status_code == 200:
        return response.json()
    return {"error": "Unable to get playlist details"}

# PUT (update) a playlist for a user
def create_playlist(user_id, playlist_id, playlist_data):
    response = requests.post(f"{BASE_URL}playlists/users/{user_id}/{playlist_id}/", data=playlist_data)
    if response.status_code == 200:
        return response.json()
    return {"error": "Unable to update playlist"}

# DELETE a playlist of a user
def delete_playlist(user_id, playlist_id):
    response = requests.delete(f"{BASE_URL}playlists/users/{user_id}/{playlist_id}/")
    if response.status_code == 204:
        return response.json()
    else:
        {"error": "Unable to delete playlist"}

# GET user interactions
def get_user_interaction(user_id, track_id):
    response = requests.get(f"{BASE_URL}user_interactions/{user_id}/{track_id}/")
    if response.status_code == 200:
        return response.json()
    return {"error": "Unable to get user interactions"}

# POST (update) user interaction
def update_user_interaction(user_id, track_id, interaction_data):
    response = requests.post(f"{BASE_URL}user_interactions/{user_id}/{track_id}/", json=interaction_data)
    if response.status_code == 200:
        return response.json()
    return {"error": "Unable to update user interaction"}

# DELETE user interaction
def delete_user_interaction(user_id, track_id):
    response = requests.delete(f"{BASE_URL}user_interactions/{user_id}/{track_id}/")
    if response.status_code == 204:
        return response.json()
    else:
        {"error": "Unable to delete user interaction"}

# GET recently listened tracks for a user
def get_recently_listened(user_id):
    response = requests.get(f"{BASE_URL}recently_listened/{user_id}/")
    if response.status_code == 200:
        return response.json()
    return {"error": "Unable to fetch recently listened tracks"}

# POST (update) a recently listened track for a user
def add_recently_listened(user_id, track_data):
    response = requests.post(f"{BASE_URL}recently_listened/{user_id}/", data=track_data)
    if response.status_code == 201:
        return response.json()
    return {"error": "Unable to add recently listened track"}

# DELETE recently listened
def delete_recently_listened(user_id, track_id):
    response = requests.delete(f"{BASE_URL}recently_listened/{user_id}/")
    if response.status_code == 204:
        return response.json()
    else:
        {"error": "Unable to delete recently listened track"}

