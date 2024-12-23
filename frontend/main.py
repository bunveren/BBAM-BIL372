# import backend.core.views
# todo add play-pause buttons for visual
# todo make search tab useful????
from datetime import datetime

from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QPushButton,
    QLabel, QWidget, QListWidget, QStackedWidget,
    QSplitter, QLineEdit, QMessageBox, QScrollArea
)
from PyQt5.QtGui import QFont, QIcon, QPixmap
from PyQt5.QtCore import Qt, QSize, QPropertyAnimation
import os

import api


class MainWindow(QMainWindow):
    _user_id = -1
    start_screen = None

    def start_screen_func(self, user_id):
        username = api.get_user(user_id)['username']
        username_label = QLabel(f"Tekrar hoş geldin {username}!")
        username_label.setStyleSheet("font-family: Arial; font-size: 35px; font-weight: bold;")

        basedir = (os.path.dirname(os.path.abspath(__file__)))

        followed_by = api.get_followed_by(self._user_id)
        following = api.get_following(self._user_id)

        followers_num = len(following)
        followed_by_num = len(followed_by)
        followers_button = QPushButton(f"Takipçiler ({followers_num})")
        following_button = QPushButton(f"Takip Edilenler ({followed_by_num})")
        followers_button.setIcon(QIcon(os.path.join(basedir, "resources", "follower-svgrepo-com.svg")))
        following_button.setIcon(QIcon(os.path.join(basedir, "resources", "following-svgrepo-com.svg")))
        followers_button.setFixedSize(170, 40)
        following_button.setFixedSize(170, 40)
        followers_button.setStyleSheet("text-align: left;")
        following_button.setStyleSheet("text-align: left;")

        followers_button.clicked.connect(lambda: self.show_list_screen("Takipçiler", following, False, False, False))
        following_button.clicked.connect(lambda: self.show_list_screen("Takip Edilenler", followed_by, False, False, False))

        profile_layout = QHBoxLayout()
        profile_details = api.get_user(self._user_id)
        profile_details_text = "E-mail: "+profile_details["email"]+"\n"+"Abonelik türü: "+profile_details["subscription_type"]+"\n"+"Hesap oluşturma tarihi "+profile_details["created_at"]
        profile_layout.addWidget(QLabel(profile_details_text))
        profile_layout.addWidget(followers_button)
        profile_layout.addWidget(following_button)
        profile_layout.addStretch()
        profile_layout.setSpacing(10)

        main_layout = QVBoxLayout()
        main_layout.addWidget(username_label)
        main_layout.addLayout(profile_layout)
        main_layout.addStretch()

        continue_label = QLabel("Kaldığın yerden devam et...")
        continue_label.setStyleSheet("font-size: 18px; color: gray; text-align: center;")
        continue_button = QPushButton("Devam Et")
        continue_button.setFixedSize(170, 40)
        continue_button.clicked.connect(lambda: self.show_recent_screen())

        continue_layout = QHBoxLayout()
        continue_layout.addWidget(continue_label)
        continue_layout.addWidget(continue_button)
        continue_layout.setSpacing(10)

        main_layout.addLayout(continue_layout)

        container = QWidget()
        container.setLayout(main_layout)
        self.start_screen = container
        self.stack.setCurrentWidget(container)

    def create_login_screen(self):
        login_layout = QVBoxLayout()

        login_label = QLabel("Hoş geldiniz! Lütfen giriş yapın.")
        login_label.setAlignment(Qt.AlignCenter)
        login_label.setStyleSheet("""
            padding: 10px;
            font-size: 18px;
            margin-bottom: 10px;""")
        login_layout.addStretch()
        login_layout.addWidget(login_label)

        # Username input
        username_input = QLineEdit()
        username_input.setPlaceholderText("Kullanıcı Adı")
        username_input.setFixedWidth(200)
        username_input.setStyleSheet("""
            padding: 10px;
            font-size: 14px;
            border: 2px solid #ccc;
            border-radius: 8px;
            margin-bottom: 10px;
        """)
        login_layout.addWidget(username_input, alignment=Qt.AlignHCenter)

        # Password input
        password_input = QLineEdit()
        password_input.setPlaceholderText("Şifre")
        password_input.setEchoMode(QLineEdit.Password)
        password_input.setFixedWidth(200)
        password_input.setStyleSheet("""
            padding: 10px;
            font-size: 14px;
            border: 2px solid #ccc;
            border-radius: 8px;
            margin-bottom: 10px;
        """)
        login_layout.addWidget(password_input, alignment=Qt.AlignHCenter)

        # Error label
        error_label = QLabel("")
        error_label.setStyleSheet("color: red; font-size: 12px;")
        error_label.setAlignment(Qt.AlignCenter)
        error_label.hide()
        login_layout.addWidget(error_label)

        # Login button with a HBox layout to align it with inputs
        button_layout = QHBoxLayout()
        login_button = QPushButton("Giriş Yap")
        login_button.setStyleSheet("background-color: #1DB954; color: white; padding: 10px;")
        login_button.setFixedWidth(200)
        button_layout.addWidget(login_button)
        button_layout.setAlignment(Qt.AlignHCenter)

        # Add the button layout to the main login layout
        login_layout.addLayout(button_layout)

        login_layout.addStretch()

        # Set up the final login widget
        login_widget = QWidget()
        login_widget.setLayout(login_layout)
        self.setCentralWidget(login_widget)

        def validate_login():
            username = username_input.text()
            password = password_input.text()
            is_valid = self.check_credentials(username, password)
            if is_valid != -1:
                self.create_after_login(is_valid)
            else:
                error_label.setText("Yanlış username veya password. Tekrar deneyin.")
                error_label.show()

        login_button.clicked.connect(validate_login)

    def check_credentials(self, username, password):
        for user in api.get_users():
            if user["username"] == username and user["password"] == password:
                return user["user_id"]
            else:
                if user["username"] == username and user["password"] != password:
                    return -1
        return -1

    def create_after_login(self, user_id):
        self._user_id = user_id  # for future use
        self.main_splitter = QSplitter(Qt.Horizontal)

        menu_layout = QVBoxLayout()
        self.profile_button = QPushButton("Ana Sayfa")
        self.playlist_button = QPushButton("Playlist'lerim")
        self.artist_button = QPushButton("Sanatçılar")
        self.settings_button = QPushButton("Ayarlar")

        basedir = (os.path.dirname(os.path.abspath(__file__)))

        self.profile_button.setIcon(QIcon(os.path.join(basedir, "resources", "profile-svgrepo-com.svg")))
        self.playlist_button.setIcon(QIcon(os.path.join(basedir, "resources", "music-player-svgrepo-com.svg")))
        self.artist_button.setIcon(QIcon(os.path.join(basedir, "resources", "musician.svg")))
        self.settings_button.setIcon(QIcon(os.path.join(basedir, "resources", "settings-svgrepo-com.svg")))

        self.profile_button.setStyleSheet("text-align: left;")
        self.playlist_button.setStyleSheet("text-align: left;")
        self.artist_button.setStyleSheet("text-align: left;")
        self.settings_button.setStyleSheet("text-align: left;")

        self.profile_button.setIconSize(QSize(24, 24))
        self.playlist_button.setIconSize(QSize(24, 24))
        self.artist_button.setIconSize(QSize(24, 24))
        self.settings_button.setIconSize(QSize(24, 24))

        menu_layout.addWidget(self.profile_button)
        menu_layout.addWidget(self.playlist_button)
        menu_layout.addWidget(self.artist_button)
        menu_layout.addWidget(self.settings_button)
        menu_layout.addStretch()

        menu_container = QWidget()
        menu_container.setLayout(menu_layout)

        self.stack = QStackedWidget()

        self.start_screen_func(user_id)

        self.playlist_screen = self.create_playlists_screen(user_id)

        self.artists_data = api.get_artists()

        self.artist_screen = self.create_artist_screen(self.artists_data)

        self.settings_screen = self.create_settings_screen()

        self.stack.addWidget(self.start_screen)
        self.stack.addWidget(self.playlist_screen)
        self.stack.addWidget(self.artist_screen)
        self.stack.addWidget(self.settings_screen)

        self.main_splitter.addWidget(menu_container)
        self.main_splitter.addWidget(self.stack)

        self.main_splitter.setStretchFactor(0, 1)
        self.main_splitter.setStretchFactor(1, 4)

        container = QWidget()
        layout = QHBoxLayout()
        layout.addWidget(self.main_splitter)
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.profile_button.clicked.connect(lambda: self.start_screen_func(self._user_id))
        self.playlist_button.clicked.connect(lambda: self.stack.setCurrentWidget(self.playlist_screen))
        self.artist_button.clicked.connect(lambda: self.stack.setCurrentWidget(self.artist_screen))
        self.settings_button.clicked.connect(lambda: self.stack.setCurrentWidget(self.settings_screen))

    def __init__(self):
        super().__init__()
        self.setWindowTitle("BBAM Music Player")
        self.setGeometry(100, 100, 1024, 768)
        self.font = QFont("Arial", 12, QFont.Normal)

        self.animation = QPropertyAnimation(self, b"windowOpacity")
        self.animation.setDuration(500)
        self.animation.setStartValue(0)
        self.animation.setEndValue(1)
        self.animation.start()

        self.setStyleSheet("""
            QWidget {
                background-color: #121212;
                color: white;
                font-family: Arial;
                font-size: 12px;
            }
            QPushButton {
                background-color: #1DB954;
                color: white;
                font-size: 14px;
                border-radius: 5px;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #1ed760;
            }
            QLabel {
                color: #FFFFFF;
                font-size: 14px;
            }
            QListWidget {
                background-color: #181818;
                color: #B3B3B3;
                border: none;
            }
            QTableWidget {
                background-color: #181818;
                color: #FFFFFF;
                gridline-color: #282828;
                selection-background-color: #1DB954;
            }
            QHeaderView::section {
                background-color: #282828;
                color: #B3B3B3;
                font-weight: bold;
                border: none;
            }
            QScrollBar:vertical {
                background: #121212;
                width: 10px;
                margin: 0px 3px 0px 3px;
            }
            QScrollBar::handle:vertical {
                background: #1DB954;
                min-height: 25px;
            }
            QScrollBar::handle:vertical:hover {
                background: #1ed760;
            }
            QSplitter {
                background: #181818;
            }
            QSplitter::handle {
                background-color: #444444; 
                border: 1px solid #282828; 
                width: 6px; 
            }
            QSplitter::handle:pressed {
                background-color: #666666; 
            }
        """)

        self.create_login_screen()

    def create_settings_screen(self):
        setting_category_1 = ["a", "b", "c"]
        setting_category_2 = ["d", "e", "f"]
        settings = [("Category 1", setting_category_1), ("Category 2", setting_category_2)]
        basedir = (os.path.dirname(os.path.abspath(__file__)))

        layout = QVBoxLayout()
        for category_name, setting_list in settings:
            button = QPushButton(category_name)
            button.setIcon(QIcon(os.path.join(basedir, "resources", "musician-svgrepo-com.svg")))
            button.setStyleSheet("text-align: left; width: 100%;")
            button.clicked.connect(lambda _, s=setting_list: self.show_list_screen(category_name, s, False, False,True))
            layout.addWidget(button)
        layout.addStretch()
        home_button = QPushButton("Ana Sayfa")
        home_button.clicked.connect(lambda: self.create_after_login(self._user_id))
        layout.addWidget(home_button)
        container = QWidget()
        container.setLayout(layout)
        return container

    def show_recent_screen(self):

        # print(api.get_recently_listened(self._user_id))
        # [{'recently_listened_id': 1, 'timestamp': '2023-10-22', 'play_count': 155, 'user': 1, 'track': 59},
        layout = QVBoxLayout()
        list_widget = QListWidget()
        items = api.get_recently_listened(self._user_id)
        if items:
            for recently_listened_item in items:
                track = api.get_track(recently_listened_item["track"])
                timestamp = recently_listened_item["timestamp"]
                play_count = recently_listened_item["play_count"]
                track_title = track["title"]
                track_duration = track["duration"]
                track_genre = track["genre"]
                track_artists = ""

                for artist_id in track["artists_id"]:
                    track_artists += api.get_artist(artist_id)['name'] + ", "
                length = len(track_artists)
                track_artists = track_artists[:length - 2]
                list_widget.addItem(
                    f"{track_title} - {track_genre} - {track_artists} - {play_count} - {timestamp}"
                )
        else:
            layout.addWidget(QLabel("Playlist'iniz boş."))

        layout.addWidget(list_widget)
        home_button = QPushButton("Ana Sayfa")
        home_button.clicked.connect(lambda: self.create_after_login(self._user_id))
        layout.addWidget(home_button)
        container = QWidget()
        container.setLayout(layout)
        self.stack.addWidget(container)
        self.stack.setCurrentWidget(container)

    def create_artist_screen(self, artist_data):
        artist_buttons = []
        search_bar = QLineEdit()
        search_bar.setPlaceholderText("Sanatçı Ara...")
        search_bar.textChanged.connect(lambda query: self.search(search_query=query, artist_buttons=artist_buttons))

        layout = QVBoxLayout()
        layout.addWidget(search_bar)
        basedir = (os.path.dirname(os.path.abspath(__file__)))

        for artist in artist_data:
            albums = api.get_artist_albums(artist["artist_id"])
            artist_name = artist["name"]
            button = QPushButton(artist_name)
            button.setIcon(QIcon(os.path.join(basedir, "resources", "musician-svgrepo-com.svg")))
            button.setStyleSheet("text-align: left; width: 100%;")

            button.clicked.connect(lambda _, a=artist_name, s=albums: self.show_list_screen(a, s, False, True, False))
            layout.addWidget(button)
            artist_buttons.append((button, artist_name))

        layout.addStretch()

        home_button = QPushButton("Ana Sayfa")
        home_button.clicked.connect(lambda: self.create_after_login(self._user_id))
        layout.addWidget(home_button)

        container = QWidget()
        container.setLayout(layout)
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setWidget(container)
        return scroll_area

    def search(self, search_query, artist_buttons):
        search_query = search_query.strip().lower()
        for button, artist_name in artist_buttons:
            if search_query in artist_name.lower():
                button.show()
            else:
                button.hide()

    def create_playlists_screen(self, user_id):
        layout = QVBoxLayout()
        basedir = (os.path.dirname(os.path.abspath(__file__)))
        playlist_data = api.get_user_playlists(user_id)
        if type(playlist_data) is dict:
            label = QLabel("Henüz bir playlist oluşturulmamış. Eklemek ister misiniz?")
            layout.addWidget(label)
            create_playlist_button = QPushButton("Yeni Playlist")
            create_playlist_button.clicked.connect(self.new_playlist_screen)
            layout.addWidget(create_playlist_button)
            layout.addStretch()

            home_button = QPushButton("Ana Sayfa")
            home_button.clicked.connect(lambda: self.create_after_login(self._user_id))
            layout.addWidget(home_button)

            container = QWidget()
            container.setLayout(layout)
            return container

        for playlist in playlist_data:
            playlist_name = playlist["name"]
            playlist_created_at = playlist["created_at"]
            playlist_tracks = playlist["tracks"]

            button = QPushButton(playlist_name + " / " + playlist_created_at)
            button.setIcon(QIcon(os.path.join(basedir, "resources", "music-player-svgrepo-com.svg")))
            button.setStyleSheet("text-align: left; width: 100%;")
            button.setStyleSheet("text-align:")
            button.clicked.connect(
                lambda _, a=playlist_name, s=playlist_tracks: self.show_list_screen(a, s, True, False, False))

            layout.addWidget(button)
        layout.addStretch()
        create_playlist_button = QPushButton("Yeni Playlist")
        create_playlist_button.clicked.connect(self.new_playlist_screen)
        layout.addWidget(create_playlist_button)
        home_button = QPushButton("Ana Sayfa")
        home_button.clicked.connect(lambda: self.create_after_login(self._user_id))
        layout.addWidget(home_button)

        container = QWidget()
        container.setLayout(layout)
        return container

    def new_playlist_screen(self):
        playlist_name_input = QLineEdit()
        playlist_name_input.setPlaceholderText("Playlist Adı")
        playlist_name_input.setFixedWidth(200)
        playlist_name_input.setStyleSheet("""
                    padding: 10px;
                    font-size: 14px;
                    border: 2px solid #ccc;
                    border-radius: 8px;
                    margin-bottom: 10px;
                """)

        container = QWidget()
        label = QLabel(f"Playlist'inize bir isim verin:")
        layout = QVBoxLayout()
        layout.addWidget(playlist_name_input, alignment=Qt.AlignHCenter)
        layout.addWidget(label)
        add_playlist_button = QPushButton("Playlist'i Oluştur")
        layout.addWidget(add_playlist_button)
        layout.addStretch()
        home_button = QPushButton("Ana Sayfa")
        home_button.clicked.connect(lambda: self.create_after_login(self._user_id))
        layout.addWidget(home_button)
        container.setLayout(layout)
        self.stack.addWidget(container)
        self.stack.setCurrentWidget(container)
        add_playlist_button.clicked.connect(lambda: (
            self.create_playlist(playlist_name_input),
            self.create_after_login(self._user_id)
        ))

    def create_playlist(self, playlist_name_input):
        if not playlist_name_input.text():
            QMessageBox.warning(self, "Uyarı", "Lütfen bir playlist adı girin!")
            return
        playlist_data = {
            "playlist_id": 0,
            "name": playlist_name_input.text(),
            "created_at": datetime.now().strftime("%Y-%m-%d"),
            "tracks": [],
            "user": self._user_id
        }
        result = api.create_user_playlist(self._user_id, playlist_data)

    def show_list_screen(self, title, items, is_song, is_artist, is_setting):
        layout = QVBoxLayout()
        label = QLabel(title)
        label.setFont(QFont("Arial", 16))
        label.setAlignment(Qt.AlignCenter)
        list_widget = QListWidget()
        layout.addWidget(label)
        layout.addWidget(list_widget)
        if is_song:
            if items:
                for track_id in items:
                    track = api.get_track(track_id)
                    track_title = track["title"]
                    track_duration = track["duration"]
                    track_genre = track["genre"]
                    track_artists = ""

                    for artist_id in track["artists_id"]:
                        track_artists += api.get_artist(artist_id)['name'] + ", "
                    length = len(track_artists)
                    track_artists = track_artists[:length - 2]
                    list_widget.addItem(track_title)
            else:
                layout.addWidget(QLabel("Playlist'iniz boş."))
        if is_artist:
            if type(items) != dict:
                for album in items:
                    list_widget.addItem(album["title"] + " / " + album["release_date"])
            else:
                layout.addWidget(QLabel("Sanatçının albümü bulunmamakta."))
        if is_setting:
            layout.addWidget(QLabel("Uygulamanız güncel."))
        else: # takipci - takip edilen
            if items:
                for person_id in items:
                    person_details = api.get_user(person_id)
                    person_name = person_details["username"]
                    person_following = api.get_following(person_id)
                    person_followed_by = api.get_followed_by(person_id)
                    button = QPushButton(person_name)
                    button.setStyleSheet("text-align: left; width: 100%;")
                    button.clicked.connect(
                        lambda _, pid=person_id, details=person_details: self.on_person_clicked(pid, details))
                    layout.addWidget(button)

            else:
                layout.addWidget(QLabel("Kimse yok."))

        home_button = QPushButton("Ana Sayfa")
        home_button.clicked.connect(lambda: self.create_after_login(self._user_id))
        layout.addWidget(home_button)

        container = QWidget()
        container.setLayout(layout)
        self.stack.addWidget(container)
        self.stack.setCurrentWidget(container)

    def on_person_clicked(self, person_id, person_details):
        container = QWidget()
        person_name = person_details["username"]
        person_following = api.get_following(person_id)
        person_followed_by = api.get_followed_by(person_id)
        basedir = (os.path.dirname(os.path.abspath(__file__)))
        followers_num = len(person_followed_by)
        followed_by_num = len(person_following)
        followers_button = QPushButton(f"Takipçiler ({followers_num})")
        following_button = QPushButton(f"Takip Edilenler ({followed_by_num})")
        followers_button.setIcon(QIcon(os.path.join(basedir, "resources", "follower-svgrepo-com.svg")))
        following_button.setIcon(QIcon(os.path.join(basedir, "resources", "following-svgrepo-com.svg")))
        followers_button.setFixedSize(170, 40)
        following_button.setFixedSize(170, 40)
        followers_button.setStyleSheet("text-align: left;")
        following_button.setStyleSheet("text-align: left;")

        followers_button.clicked.connect(lambda: self.show_list_screen("Takipçiler", person_followed_by, False, False, False))
        following_button.clicked.connect(
            lambda: self.show_list_screen("Takip Edilenler", person_following, False, False, False))

        profile_layout = QHBoxLayout()
        profile_details = api.get_user(person_id)
        name_label = QLabel(person_name)
        name_label.setStyleSheet("font-size: 24px; color: gray; text-align: center;")
        profile_layout.addWidget(name_label)
        profile_details_text = "E-mail: " + profile_details["email"] + "\n" + "Abonelik türü: " + profile_details[
            "subscription_type"] + "\n" + "Hesap oluşturma tarihi " + profile_details["created_at"]
        profile_layout.addWidget(QLabel(profile_details_text))
        profile_layout.addWidget(followers_button)
        profile_layout.addWidget(following_button)
        profile_layout.addStretch()
        profile_layout.setSpacing(10)
        profile_layout.addStretch()
        home_button = QPushButton("Ana Sayfa")
        home_button.clicked.connect(lambda: self.create_after_login(self._user_id))
        profile_layout.addWidget(home_button)
        container.setLayout(profile_layout)
        self.stack.addWidget(container)
        self.stack.setCurrentWidget(container)



# todo

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
