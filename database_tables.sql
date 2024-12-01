USE bbam;

-- Users Tablosu
CREATE TABLE Users (
    User_ID SERIAL PRIMARY KEY,                -- PRIMARY KEY zaten indekslidir
    Username VARCHAR(50) NOT NULL UNIQUE,      -- UNIQUE otomatik olarak indeks oluşturur
    Password VARCHAR(50) NOT NULL,
    Email VARCHAR(50) NOT NULL UNIQUE,         -- UNIQUE otomatik olarak indeks oluşturur
    Subscription_type ENUM('Free', 'Premium') NOT NULL,
    Created_at DATE DEFAULT '2024-11-27'
);
CREATE INDEX idx_subscription_type ON Users(Subscription_type); -- Üyelik tipi filtreleme

-- Artists Tablosu
CREATE TABLE Artists (
    Artist_ID SERIAL PRIMARY KEY,              -- PRIMARY KEY zaten indekslidir
    Name VARCHAR(100) NOT NULL,
    Biography TEXT,
    Genre VARCHAR(50)
);
CREATE INDEX idx_artist_genre ON Artists(Genre); -- Sanatçı türüne göre filtreleme

-- Albums Tablosu
CREATE TABLE Albums (
    Album_ID SERIAL PRIMARY KEY,               -- PRIMARY KEY zaten indekslidir
    Title VARCHAR(100) NOT NULL,
    Release_date DATE NOT NULL,
    Artist_ID BIGINT UNSIGNED NOT NULL,
    FOREIGN KEY (Artist_ID) REFERENCES Artists(Artist_ID) ON DELETE CASCADE
);

-- Artist_ID üzerinde indeks
CREATE INDEX idx_artist_id ON Albums(Artist_ID);

-- Tracks Tablosu
CREATE TABLE Tracks (
    Track_ID SERIAL PRIMARY KEY,               -- PRIMARY KEY zaten indekslidir
    Title VARCHAR(100) NOT NULL,
    Duration INT NOT NULL,
    Album_ID BIGINT UNSIGNED NOT NULL,
    Genre VARCHAR(50),
    File_Path VARCHAR(255) NOT NULL,
    Artists_ID JSON NOT NULL,
    Play_count INT DEFAULT 0,
    FOREIGN KEY (Album_ID) REFERENCES Albums(Album_ID) ON DELETE CASCADE
);

-- Album_ID ve Genre üzerinde indeksler
CREATE INDEX idx_album_id ON Tracks(Album_ID);
CREATE INDEX idx_genre ON Tracks(Genre);

-- Playlists Tablosu
CREATE TABLE Playlists (
    Playlist_ID SERIAL PRIMARY KEY,            -- PRIMARY KEY zaten indekslidir
    User_ID BIGINT UNSIGNED NOT NULL,
    Name VARCHAR(100) NOT NULL,
    Created_at DATE,
    Tracks JSON,
    FOREIGN KEY (User_ID) REFERENCES Users(User_ID) ON DELETE CASCADE
);

-- User_ID üzerinde indeks
CREATE INDEX idx_user_id ON Playlists(User_ID);

-- Recently_Listened Tablosu
CREATE TABLE Recently_Listened (
    Recently_Listened_ID SERIAL PRIMARY KEY,   -- PRIMARY KEY zaten indekslidir
    User_ID BIGINT UNSIGNED NOT NULL,
    Track_ID BIGINT UNSIGNED NOT NULL,
    Timestamp DATE,
    Play_count INT DEFAULT 0,
    FOREIGN KEY (User_ID) REFERENCES Users(User_ID) ON DELETE CASCADE,
    FOREIGN KEY (Track_ID) REFERENCES Tracks(Track_ID) ON DELETE CASCADE
);

-- User_ID ve Track_ID üzerinde indeksler
CREATE INDEX idx_recently_user_id ON Recently_Listened(User_ID);
CREATE INDEX idx_recently_track_id ON Recently_Listened(Track_ID);

-- User_Follow_Interactions Tablosu
CREATE TABLE User_Follow_Interactions (
    Following JSON NOT NULL,
    Followed_By JSON NOT NULL,
    User_ID BIGINT UNSIGNED NOT NULL,
    FOREIGN KEY (User_ID) REFERENCES Users(User_ID) ON DELETE CASCADE
);

-- User_ID üzerinde indeks
CREATE INDEX idx_follow_user_id ON User_Follow_Interactions(User_ID);

-- User_Interactions Tablosu
CREATE TABLE User_Interactions (
    Interaction_ID SERIAL PRIMARY KEY,         -- PRIMARY KEY zaten indekslidir
    User_ID BIGINT UNSIGNED NOT NULL,
    Track_ID BIGINT UNSIGNED NOT NULL,
    Liked BOOLEAN DEFAULT FALSE,
    Timestamp INT DEFAULT 0,
    FOREIGN KEY (User_ID) REFERENCES Users(User_ID) ON DELETE CASCADE,
    FOREIGN KEY (Track_ID) REFERENCES Tracks(Track_ID) ON DELETE CASCADE
);

-- User_ID ve Track_ID üzerinde indeksler
CREATE INDEX idx_interactions_user_id ON User_Interactions(User_ID);
CREATE INDEX idx_interactions_track_id ON User_Interactions(Track_ID);
CREATE INDEX idx_liked ON User_Interactions(Liked);
