USE bbam;

-- constraint kontrolleri için trigger kullanıldı
DELIMITER ;
DELIMITER //


CREATE TRIGGER validate_artists_in_json
BEFORE INSERT ON Tracks
FOR EACH ROW
BEGIN
    DECLARE album_artist_id INT;

    -- Albüm sanatçısının ID'sini al
    SELECT Artist_ID INTO album_artist_id
    FROM Albums
    WHERE Album_ID = NEW.Album_ID;

    -- Artists_ID içinde albüm sanatçısının bulunup bulunmadığını kontrol et (sayı olarak arama yap)
    IF JSON_CONTAINS(NEW.Artists_ID, CAST(album_artist_id AS CHAR)) = 0 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Artists_ID must contain the Artist_ID of the album.';
    END IF;
END;
//

DELIMITER //
CREATE TRIGGER validate_artists_in_json_update
BEFORE UPDATE ON Tracks
FOR EACH ROW
BEGIN
    DECLARE album_artist_id INT;

    -- Albüm sanatçısının ID'sini al
    SELECT Artist_ID INTO album_artist_id
    FROM Albums
    WHERE Album_ID = NEW.Album_ID;

    -- Artists_ID içinde albüm sanatçısının bulunup bulunmadığını kontrol et (sayı olarak arama yap)
    IF JSON_CONTAINS(NEW.Artists_ID, CAST(album_artist_id AS CHAR)) = 0 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Artists_ID must contain the Artist_ID of the album.';
    END IF;
END;
//

DELIMITER ;
DELIMITER \\
CREATE TRIGGER validate_playlist_created_at
BEFORE INSERT ON Playlists
FOR EACH ROW
BEGIN
    DECLARE user_created_at DATE;

    -- Kullanıcının Created_at değerini al
    SELECT Created_at INTO user_created_at
    FROM Users
    WHERE User_ID = NEW.User_ID;

    -- Eğer Created_at uygun aralıkta değilse hata ver
    IF NEW.Created_at < user_created_at OR NEW.Created_at > CURRENT_DATE THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Created_at must be between the user creation date and today.';
    END IF;
END;
//

DELIMITER ;

DELIMITER //

CREATE TRIGGER validate_playlist_created_at_update
BEFORE UPDATE ON Playlists
FOR EACH ROW
BEGIN
    DECLARE user_created_at DATE;

    -- Kullanıcının Created_at değerini al
    SELECT Created_at INTO user_created_at
    FROM Users
    WHERE User_ID = NEW.User_ID;

    -- Eğer Created_at uygun aralıkta değilse hata ver
    IF NEW.Created_at < user_created_at OR NEW.Created_at > CURRENT_DATE THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Created_at must be between the user creation date and today.';
    END IF;
END;
//

DELIMITER ;
DELIMITER //

CREATE TRIGGER validate_play_count_insert
BEFORE INSERT ON Recently_Listened
FOR EACH ROW
BEGIN
    DECLARE track_play_count INT;

    -- Tracks tablosundan Play_count değerini al
    SELECT Play_count INTO track_play_count
    FROM Tracks
    WHERE Track_ID = NEW.Track_ID;

    -- Eğer Recently_Listened'daki Play_count, Tracks'deki Play_count'tan büyükse hata ver
    IF NEW.Play_count > track_play_count THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Play_count in Recently_Listened must be less than or equal to the Track Play_count.';
    END IF;
END;
//

DELIMITER ;

DELIMITER //

CREATE TRIGGER validate_play_count_update
BEFORE UPDATE ON Recently_Listened
FOR EACH ROW
BEGIN
    DECLARE track_play_count INT;

    -- Tracks tablosundan Play_count değerini al
    SELECT Play_count INTO track_play_count
    FROM Tracks
    WHERE Track_ID = NEW.Track_ID;

    -- Eğer Recently_Listened'daki Play_count, Tracks'deki Play_count'tan büyükse hata ver
    IF NEW.Play_count > track_play_count THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Play_count in Recently_Listened must be less than or equal to the Track Play_count.';
    END IF;
END;
//

DELIMITER ;
DELIMITER //

CREATE TRIGGER validate_timestamp_insert
BEFORE INSERT ON User_Interactions
FOR EACH ROW
BEGIN
    DECLARE track_duration INT;

    -- Tracks tablosundan Track_ID'ye karşılık gelen Duration değerini al
    SELECT Duration INTO track_duration
    FROM Tracks
    WHERE Track_ID = NEW.Track_ID;

    -- Eğer Timestamp, Duration'dan büyükse hata ver
    IF NEW.Timestamp > track_duration THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Timestamp must be less than or equal to the track duration.';
    END IF;
END;
//

DELIMITER ;

DELIMITER //

CREATE TRIGGER validate_timestamp_update
BEFORE UPDATE ON User_Interactions
FOR EACH ROW
BEGIN
    DECLARE track_duration INT;

    -- Tracks tablosundan Track_ID'ye karşılık gelen Duration değerini al
    SELECT Duration INTO track_duration
    FROM Tracks
    WHERE Track_ID = NEW.Track_ID;

    -- Eğer Timestamp, Duration'dan büyükse hata ver
    IF NEW.Timestamp > track_duration THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Timestamp must be less than or equal to the track duration.';
    END IF;
END;
//

DELIMITER ;
DELIMITER //

CREATE TRIGGER validate_recently_listened_insert
BEFORE INSERT ON Recently_Listened
FOR EACH ROW
BEGIN
    DECLARE album_release_date DATE;
    DECLARE user_created_at DATE;

    -- Albümün çıkış tarihini al
    SELECT a.Release_date INTO album_release_date
    FROM Tracks t
    JOIN Albums a ON t.Album_ID = a.Album_ID
    WHERE t.Track_ID = NEW.Track_ID;

    -- Kullanıcının kayıt tarihini al
    SELECT Created_at INTO user_created_at
    FROM Users
    WHERE User_ID = NEW.User_ID;

    -- Doğrulama
    IF NEW.Timestamp < album_release_date OR NEW.Timestamp < user_created_at THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Timestamp must be after the album release date and user created date.';
    END IF;
END;
//

DELIMITER ;
DELIMITER //

CREATE TRIGGER validate_recently_listened_update
BEFORE UPDATE ON Recently_Listened
FOR EACH ROW
BEGIN
    DECLARE album_release_date DATE;
    DECLARE user_created_at DATE;

    -- Albümün çıkış tarihini al
    SELECT a.Release_date INTO album_release_date
    FROM Tracks t
    JOIN Albums a ON t.Album_ID = a.Album_ID
    WHERE t.Track_ID = NEW.Track_ID;

    -- Kullanıcının kayıt tarihini al
    SELECT Created_at INTO user_created_at
    FROM Users
    WHERE User_ID = NEW.User_ID;

    -- Doğrulama
    IF NEW.Timestamp < album_release_date OR NEW.Timestamp < user_created_at THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Timestamp must be after the album release date and user created date.';
    END IF;
END;
//

DELIMITER ;