# import backend.core.views
# todo add play-pause buttons for visual
# todo make search tab useful????

from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QPushButton,
    QLabel, QWidget, QListWidget, QStackedWidget,
    QSplitter, QLineEdit
)
from PyQt5.QtGui import QFont, QIcon, QPixmap
from PyQt5.QtCore import Qt, QSize, QPropertyAnimation
import os
import api


class MainWindow(QMainWindow):
    _user_id = -1

    def create_login_screen(self):
        login_layout = QVBoxLayout()

        login_label = QLabel("Hoş geldiniz! Lütfen giriş yapın.")
        login_label.setAlignment(Qt.AlignCenter)
        login_label.setStyleSheet("font-size: 18px; font-weight: bold;")
        login_layout.addStretch()
        login_layout.addWidget(login_label)
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
        login_layout.addStretch()
        error_label = QLabel("")
        error_label.setStyleSheet("color: red; font-size: 12px;")
        error_label.setAlignment(Qt.AlignCenter)
        error_label.hide()
        login_layout.addWidget(error_label)

        login_button = QPushButton("Login")
        login_button.setStyleSheet("background-color: #1DB954; color: white; padding: 10px;")
        login_layout.addWidget(login_button)

        login_widget = QWidget()
        login_widget.setLayout(login_layout)
        self.setCentralWidget(login_widget)

        def validate_login():
            username = username_input.text()
            password = password_input.text()
            user_id = 0
            is_valid = self.check_credentials(username, password)
            if is_valid != -1:
                self.create_after_login(is_valid)
            else:
                error_label.setText("Invalid username or password. Please try again.")
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
        _user_id = user_id  # for future use
        self.main_splitter = QSplitter(Qt.Horizontal)

        menu_layout = QVBoxLayout()
        self.profile_button = QPushButton("Ana Sayfa")
        self.playlist_button = QPushButton("Playlist'lerim")
        self.artist_button = QPushButton("Sanatçılarım")
        self.search_button = QPushButton("Arama")
        self.settings_button = QPushButton("Ayarlar")

        basedir = (os.path.dirname(os.path.abspath(__file__)))

        self.profile_button.setIcon(QIcon(os.path.join(basedir, "resources", "profile-svgrepo-com.svg")))
        self.playlist_button.setIcon(QIcon(os.path.join(basedir, "resources", "music-player-svgrepo-com.svg")))
        self.artist_button.setIcon(QIcon(os.path.join(basedir, "resources", "musician.svg")))
        self.search_button.setIcon(QIcon(os.path.join(basedir, "resources", "search-svgrepo-com.svg")))
        self.settings_button.setIcon(QIcon(os.path.join(basedir, "resources", "settings-svgrepo-com.svg")))

        self.profile_button.setStyleSheet("text-align: left;")
        self.playlist_button.setStyleSheet("text-align: left;")
        self.artist_button.setStyleSheet("text-align: left;")
        self.search_button.setStyleSheet("text-align: left;")
        self.settings_button.setStyleSheet("text-align: left;")

        self.profile_button.setIconSize(QSize(24, 24))
        self.playlist_button.setIconSize(QSize(24, 24))
        self.artist_button.setIconSize(QSize(24, 24))
        self.search_button.setIconSize(QSize(24, 24))
        self.settings_button.setIconSize(QSize(24, 24))

        menu_layout.addWidget(self.profile_button)
        menu_layout.addWidget(self.playlist_button)
        menu_layout.addWidget(self.artist_button)
        menu_layout.addWidget(self.search_button)
        menu_layout.addWidget(self.settings_button)
        menu_layout.addStretch()

        menu_container = QWidget()
        menu_container.setLayout(menu_layout)

        self.stack = QStackedWidget()

        self.start_screen = self.start_screen(user_id)

        self.playlist_screen = self.create_playlists_screen(user_id)

        artists_data = {
            # tamamı
        }

        self.artist_screen = self.create_artist_screen(artists_data)
        self.search_screen = self.create_search_screen()
        self.settings_screen = self.create_settings_screen()

        self.stack.addWidget(self.start_screen)
        self.stack.addWidget(self.playlist_screen)
        self.stack.addWidget(self.artist_screen)
        self.stack.addWidget(self.search_screen)
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

        self.profile_button.clicked.connect(lambda: self.stack.setCurrentWidget(self.start_screen))
        self.playlist_button.clicked.connect(lambda: self.stack.setCurrentWidget(self.playlist_screen))
        self.artist_button.clicked.connect(lambda: self.stack.setCurrentWidget(self.artist_screen))
        self.search_button.clicked.connect(lambda: self.stack.setCurrentWidget(self.search_screen))
        self.settings_button.clicked.connect(lambda: self.stack.setCurrentWidget(self.settings_screen))

    def __init__(self):
        super().__init__()
        self.setWindowTitle("spotify çakması ui")
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
            button.clicked.connect(lambda _, s=setting_list: self.show_list_screen(category_name, s, False, True,
                                                                                   False))  # setting verince hata
            layout.addWidget(button)

        layout.addStretch()

        home_button = QPushButton("Ana Sayfa")
        home_button.clicked.connect(lambda: self.stack.setCurrentWidget(self.start_screen))
        layout.addWidget(home_button)

        container = QWidget()
        container.setLayout(layout)
        return container

    def show_recent_screen(self):
        layout = QVBoxLayout()

        new_screen_label = QLabel("Yakın zamanda dinlenenler burada görünecek.")
        new_screen_label.setAlignment(Qt.AlignCenter)
        new_screen_label.setFont(QFont("Arial", 18))

        back_button = QPushButton("Ana Sayfa")
        back_button.clicked.connect(lambda: self.stack.setCurrentWidget(self.start_screen))

        layout.addWidget(new_screen_label)
        layout.addWidget(back_button)

        continue_container = QWidget()
        continue_container.setLayout(layout)

        self.stack.addWidget(continue_container)
        self.stack.setCurrentWidget(continue_container)

    def start_screen(self, user_id):
        username = api.get_user(user_id)['username'];
        username_label = QLabel(f"Tekrar hoş geldin {username}!")
        username_label.setStyleSheet("font-family: Arial; font-size: 35px; font-weight: bold;")

        profile_picture = QLabel()
        pixmap = QPixmap("resources/thispersondoesnotexist.jpg")
        profile_picture.setPixmap(pixmap.scaled(100, 100))
        basedir = (os.path.dirname(os.path.abspath(__file__)))
        """
        #followers_num = len(following)
        #followed_by_num = len(followed_by)
        #followers_button = QPushButton(f"Takipçiler ({followers_num})")
        #following_button = QPushButton(f"Takip Edilenler ({followed_by_num})")
        followers_button.setIcon(QIcon(os.path.join(basedir, "resources", "follower-svgrepo-com.svg")))
        following_button.setIcon(QIcon(os.path.join(basedir, "resources", "following-svgrepo-com.svg")))
        followers_button.setFixedSize(170, 40)
        following_button.setFixedSize(170, 40)
        followers_button.setStyleSheet("text-align: left;")
        following_button.setStyleSheet("text-align: left;")

        followers_button.clicked.connect(lambda: self.show_list_screen("Takipçiler", following, False, False, False))
        following_button.clicked.connect(lambda: self.show_list_screen("Takip Edilenler", followed_by, False, False, False))
        """
        profile_layout = QHBoxLayout()
        profile_layout.addWidget(profile_picture)
        # profile_layout.addWidget(followers_button)
        # profile_layout.addWidget(following_button)
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
        return container

    def create_artist_screen(self, artist_data):
        layout = QVBoxLayout()
        basedir = (os.path.dirname(os.path.abspath(__file__)))

        for artist, songs in artist_data.items():
            button = QPushButton(artist)
            button.setIcon(QIcon(os.path.join(basedir, "resources", "musician-svgrepo-com.svg")))
            button.setStyleSheet("text-align: left; width: 100%;")

            button.clicked.connect(lambda _, a=artist, s=songs: self.show_list_screen(a, s, False, True, False))
            layout.addWidget(button)

        layout.addStretch()

        home_button = QPushButton("Ana Sayfa")
        home_button.clicked.connect(lambda: self.stack.setCurrentWidget(self.start_screen))
        layout.addWidget(home_button)

        container = QWidget()
        container.setLayout(layout)
        return container

    def create_playlists_screen(self, user_id):
        layout = QVBoxLayout()
        basedir = (os.path.dirname(os.path.abspath(__file__)))
        playlist_data = api.get_user_playlists(user_id)
        for playlist in playlist_data:
            playlist_name = playlist["name"]
            playlist_created_at = playlist["created_at"]
            playlist_tracks = playlist["tracks"]

            button = QPushButton(playlist_name + " " + playlist_created_at)
            button.setIcon(QIcon(os.path.join(basedir, "resources", "music-player-svgrepo-com.svg")))
            button.setStyleSheet("text-align: left; width: 100%;")

            button.setStyleSheet("text-align:")
            button.clicked.connect(
                lambda _, a=playlist_name, s=playlist_tracks: self.show_list_screen(a, s, True, False, False))

            layout.addWidget(button)
        layout.addStretch()

        home_button = QPushButton("Ana Sayfa")
        home_button.clicked.connect(lambda: self.stack.setCurrentWidget(self.start_screen))
        layout.addWidget(home_button)

        container = QWidget()
        container.setLayout(layout)
        return container

    def create_search_screen(self):
        layout = QVBoxLayout()
        search_label = QLabel("Arama özelliği aktif değil..")
        search_label.setFont(QFont("Arial", 16))
        search_label.setAlignment(Qt.AlignCenter)

        layout.addWidget(search_label)
        home_button = QPushButton("Ana Sayfa")
        home_button.clicked.connect(lambda: self.stack.setCurrentWidget(self.start_screen))
        layout.addWidget(home_button)
        container = QWidget()
        container.setLayout(layout)
        return container

    def show_list_screen(self, title, items, is_song, is_artist, is_setting):
        layout = QVBoxLayout()

        label = QLabel(title)
        label.setFont(QFont("Arial", 16))
        label.setAlignment(Qt.AlignCenter)
        list_widget = QListWidget()
        layout.addWidget(label)
        layout.addWidget(list_widget)

        if is_song:
            # list_widget.itemClicked.connect(self.on_song_clicked)
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
        if is_setting:
            list_widget.itemClicked.connect(self.start_screen)
        if is_artist:
            list_widget.itemClicked.connect(self.on_person_clicked)  # todo change
        else:
            list_widget.itemClicked.connect(self.on_person_clicked)

        home_button = QPushButton("Ana Sayfa")
        home_button.clicked.connect(lambda: self.stack.setCurrentWidget(self.start_screen))
        layout.addWidget(home_button)

        container = QWidget()
        container.setLayout(layout)
        self.stack.addWidget(container)
        self.stack.setCurrentWidget(container)

    def on_song_clicked(self, item):
        text = item.text()
        container = QWidget()
        label = QLabel(f"'{text}' için şarkılar burada görünecek.")
        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addStretch()
        home_button = QPushButton("Ana Sayfa")
        home_button.clicked.connect(lambda: self.stack.setCurrentWidget(self.start_screen))
        layout.addWidget(home_button)
        container.setLayout(layout)
        self.stack.addWidget(container)
        self.stack.setCurrentWidget(container)

    def on_person_clicked(self, item):
        text = item.text()
        container = QWidget()
        label = QLabel(f"'{text}' için profil burada görünecek.")
        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addStretch()
        home_button = QPushButton("Ana Sayfa")
        home_button.clicked.connect(lambda: self.stack.setCurrentWidget(self.start_screen))
        layout.addWidget(home_button)
        container.setLayout(layout)
        self.stack.addWidget(container)
        self.stack.setCurrentWidget(container)


# todo

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()

    print(api.get_user(1))

