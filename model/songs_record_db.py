"""
Stores all the song names.
Along with their given id,
Directory path id,
Song artist id,
Album id,
Playlist id (if apply)
"""

from model.db_conection import ConnectDB


def create_songs_table():
    """
    Create the table that stores all the data related to songs.

    Values:
    song_id: INTEGER
    song_name: VARCHAR(100)
    directory_id: INTEGER
    playlist_id: INTEGER
    artists_id: INTEGER
    album_id: INTEGER

    """
    connect = ConnectDB()

    sql = '''
    CREATE TABLE IF NOT EXISTS songs_record(
    song_id INTEGER,
    song_name VARCHAR(100),
    directory_id INTEGER,
    playlist_id INTEGER,
    artist_id INTEGER,
    album_id INTEGER,
    PRIMARY KEY(song_id AUTOINCREMENT)
    )
    '''

    connect.cursor.execute(sql)
    connect.close()


def song_existance(song):
    """
    Checks if a song already exists in the table.
    If exists returns True.
    If not returns False
    """

    connect = ConnectDB()

    sql = """SELECT song_name FROM songs_record"""

    connect.cursor.execute(sql)
    song_name = connect.cursor.fetchall()
    connect.close()

    song_name = str(song_name)
    song_name = song_name.strip("[]")

    if song in song_name:
        return True
    return False


def save_songs(songs, directory):
    """
    Saves a song with the given directory id.

    Arguments:
    songs -> List
    directory -> Str
    """

    connect = ConnectDB()
    sql_id = f''' SELECT id_directory FROM music_directory WHERE directory_path = '{directory}' '''
    connect.cursor.execute(sql_id)
    directory_id = connect.cursor.fetchone()
    directory_id = str(directory_id)
    directory_id = directory_id.strip("()")
    directory_id = directory_id.strip(",")

    for song in songs:
        if song_existance(song) is False:
            sql = f""" INSERT INTO songs_record (song_name, directory_id) VALUES ('{song}', {directory_id})"""
            connect.cursor.execute(sql)
    connect.close()


def get_song():
    """
    Returns a list with all the songs in the table
    """

    connect = ConnectDB()

    sql = """SELECT song_name FROM songs_record"""

    connect.cursor.execute(sql)
    song_name = connect.cursor.fetchall()
    connect.close()

    def iterate_song(song_name):
        result = []
        for song in song_name:
            song = str(song)
            song = song.strip("()")
            song = song.strip(",")
            song = song.strip("'")
            result.append(song)
        return result

    list_songs = iterate_song(song_name)
    return list_songs
