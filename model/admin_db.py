from model.directory_db import create__directory_table
from model.playing_back_next_db import create_playing_back_table, create_playing_next_table
from model.playlist_db import create_playlist_name_table
from model.queue_db import create_queue_table
from model.recently_played_db import create_recently_played_table
from model.songs_record_db import create_songs_table


class Admin:
    def __init__(self):
        self.create_tables()

    def create_tables(self):
        create_songs_table()
        create_recently_played_table()
        create_queue_table()
        create_playlist_name_table()
        create_playing_back_table()
        create_playing_next_table()
        create__directory_table()
