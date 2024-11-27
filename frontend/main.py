# import backend.core.views

#todo add play-pause buttons for visual
#todo make the other users' and artists' pages accessible
#todo make search tab useful????
#todo settings

from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QPushButton,
    QLabel, QWidget, QListWidget, QStackedWidget, QTableWidget, QTableWidgetItem,
    QSplitter, QSizePolicy
)
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import Qt, QSize

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("spotify çakması ui")
        self.setGeometry(100, 100, 1024, 768)
        self.font = QFont("Arial", 12, QFont.Normal)

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

        self.main_splitter = QSplitter(Qt.Horizontal)

        menu_layout = QVBoxLayout()
        self.profile_button = QPushButton("Profil")
        self.playlist_button = QPushButton("Playlist'lerim")
        self.artist_button = QPushButton("Sanatçılarım")
        self.search_button = QPushButton("Arama")
        self.settings_button = QPushButton("Ayarlar")

        self.profile_button.setIcon(QIcon("resources/profile-svgrepo-com.svg"))
        self.playlist_button.setIcon(QIcon("resources/music-player-svgrepo-com.svg"))
        self.artist_button.setIcon(QIcon("resources/musician.svg"))
        self.search_button.setIcon(QIcon("resources/search-svgrepo-com.svg"))
        self.settings_button.setIcon(QIcon("resources/settings-svgrepo-com.svg"))

        self.profile_button.setStyleSheet("text-align: left;")
        self.playlist_button.setStyleSheet("text-align: left;")
        self.artist_button.setStyleSheet("text-align: left;")
        self.search_button.setStyleSheet("text-align: left;")
        self.settings_button.setStyleSheet("text-align: left;")

        self.profile_button.setIconSize(QSize(24, 24))
        self.playlist_button.setIconSize(QSize(24, 24))
        self.artist_button.setIconSize(QSize(24, 24))
        self.search_button.setIconSize(QSize(24, 24))
        self.settings_button.setIconSize(QSize(24,24))

        menu_layout.addWidget(self.profile_button)
        menu_layout.addWidget(self.playlist_button)
        menu_layout.addWidget(self.artist_button)
        menu_layout.addWidget(self.search_button)
        menu_layout.addWidget(self.settings_button)
        menu_layout.addStretch()

        menu_container = QWidget()
        menu_container.setLayout(menu_layout)

        self.stack = QStackedWidget()

        self.profile_screen = self.create_profile_screen()
        self.playlist_screen = self.create_playlist_screen()
        self.artist_screen = self.create_artist_screen()
        self.search_screen = self.create_search_screen()
        self.settings_screen = self.create_settings_screen()

        self.stack.addWidget(self.profile_screen)
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

        self.profile_button.clicked.connect(lambda: self.stack.setCurrentWidget(self.profile_screen))
        self.playlist_button.clicked.connect(lambda: self.stack.setCurrentWidget(self.playlist_screen))
        self.artist_button.clicked.connect(lambda: self.stack.setCurrentWidget(self.artist_screen))
        self.search_button.clicked.connect(lambda: self.stack.setCurrentWidget(self.search_screen))
        self.settings_button.clicked.connect(lambda: self.stack.setCurrentWidget(self.settings_screen))

#todo setting screen
    def create_settings_screen(self):
        layout = QVBoxLayout()
        arb_button1 = QPushButton("a")
        arb_button2 = QPushButton("b")
        arb_button1.setIcon(QIcon("resources/mix-svgrepo-com.svg"))
        arb_button2.setIcon(QIcon("resources/musician-svgrepo-com.svg"))

        arb_button1.setStyleSheet("text-align: left;")
        arb_button2.setStyleSheet("text-align: left;")

        arb_button1.clicked.connect(lambda: self.show_list_screen("ayar1", ["a", "b", "c"]))
        arb_button2.clicked.connect(lambda: self.show_list_screen("ayar2", ["d", "e", "f"]))

        layout.addWidget(arb_button1)
        layout.addWidget(arb_button2)
        container = QWidget()
        container.setLayout(layout)
        return container

    def create_profile_screen(self):
        layout = QVBoxLayout()
        username_label = QLabel("Kullanıcı Adı: example_user")
        username_label.setFont(QFont("Arial", 14))
        username_label.setAlignment(Qt.AlignCenter)

        followers_button = QPushButton("Takipçiler (50)")
        following_button = QPushButton("Takip Edilenler (30)")
        followers_button.setIcon(QIcon("resources/follower-svgrepo-com.svg"))
        following_button.setIcon(QIcon("resources/following-svgrepo-com.svg"))
        followers_button.setStyleSheet("text-align: left;")
        following_button.setStyleSheet("text-align: left;")

        followers_button.clicked.connect(lambda: self.show_list_screen("Takipçiler", ["User1", "User2", "User3"]))
        following_button.clicked.connect(lambda: self.show_list_screen("Takip Edilenler", ["UserA", "UserB", "UserC"]))

        layout.addWidget(username_label)
        layout.addWidget(followers_button)
        layout.addWidget(following_button)

        container = QWidget()
        container.setLayout(layout)
        return container

    def create_playlist_screen(self):
        layout = QVBoxLayout()

        self.playlist_list = QListWidget()
        self.playlist_list.addItems(["Favoriler", "Çalışma Listesi", "Yaz Hiti"])

        self.playlist_list.itemClicked.connect(self.load_playlist_songs)

        self.song_table = QTableWidget(0, 3)
        self.song_table.setHorizontalHeaderLabels(["Şarkı Adı", "Sanatçı", "Süre"])

        self.song_table.setStyleSheet("""
                QTableWidget {
                    background-color: #181818;  
                    color: #FFFFFF;  
                    border: 1px solid #282828;  
                    selection-background-color: #1DB954;  
                }

                QTableWidget::item {
                    border-bottom: 1px solid #282828;  
                }

                QTableWidget::horizontalHeader {
                    background-color: #282828;  
                    color: #B3B3B3;  
                    font-weight: bold; 
                }

                QTableWidget::horizontalHeader::section {
                    border: none;  
                    padding: 10px;
                }

                QTableWidget::item:selected {
                    background-color: #1ed760;  
                }

                QTableWidget::verticalHeader {
                    background-color: #181818;  
                    color: #B3B3B3;  
                }

                QTableWidget::item:hover {
                    background-color: #444444; 
                }
            """)

        layout.addWidget(self.playlist_list)
        layout.addWidget(self.song_table)
        home_button = QPushButton("Ana Sayfa")
        home_button.clicked.connect(lambda: self.stack.setCurrentWidget(self.profile_screen))
        layout.addWidget(home_button)
        container = QWidget()
        container.setLayout(layout)
        return container

    def load_playlist_songs(self, item):
        playlist_songs = {
            "Favoriler": [["Şarkı 1", "Sanatçı A", "3:30"], ["Şarkı 2", "Sanatçı B", "4:00"]],
            "Çalışma Listesi": [["Şarkı 3", "Sanatçı C", "2:45"], ["Şarkı 4", "Sanatçı D", "3:50"]],
            "Yaz Hiti": [["Şarkı 5", "Sanatçı E", "3:15"], ["Şarkı 6", "Sanatçı F", "4:20"]]
        }

        songs = playlist_songs.get(item.text(), [])
        self.song_table.setRowCount(len(songs))
        for row, song in enumerate(songs):
            for col, value in enumerate(song):
                self.song_table.setItem(row, col, QTableWidgetItem(value))

    def create_artist_screen(self):
        layout = QVBoxLayout()
        artist_list = QListWidget()
        artist_list.addItems(["Sanatçı 1", "Sanatçı 2", "Sanatçı 3", "Sanatçı 4"])

        layout.addWidget(artist_list)
        home_button = QPushButton("Ana Sayfa")
        home_button.clicked.connect(lambda: self.stack.setCurrentWidget(self.profile_screen))
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
        home_button.clicked.connect(lambda: self.stack.setCurrentWidget(self.profile_screen))
        layout.addWidget(home_button)
        container = QWidget()
        container.setLayout(layout)
        return container

    def show_list_screen(self, title, items):
        layout = QVBoxLayout()

        label = QLabel(title)
        label.setFont(QFont("Arial", 16))
        label.setAlignment(Qt.AlignCenter)

        list_widget = QListWidget()
        list_widget.addItems(items)

        layout.addWidget(label)
        layout.addWidget(list_widget)

        home_button = QPushButton("Ana Sayfa")
        home_button.clicked.connect(lambda: self.stack.setCurrentWidget(self.profile_screen))
        layout.addWidget(home_button)

        container = QWidget()
        container.setLayout(layout)
        self.stack.addWidget(container)
        self.stack.setCurrentWidget(container)

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()