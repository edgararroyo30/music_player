from model.db_conection import ConnectDB


def create_songs_table():
    connect = ConnectDB()

    sql = '''
    CREATE TABLE IF NOT EXISTS songs_record(
    song_id INTEGER,
    song_name VARCHAR(100),
    directory_id INTEGER,
    playlist_id INTEGER,
    PRIMARY KEY(song_id AUTOINCREMENT)
    )
    '''

    connect.cursor.execute(sql)
    connect.close()


def song_existance(song):
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
    connect = ConnectDB()
    sql_id = f''' SELECT id_directory FROM music_directory WHERE directory_path = '{directory}' '''
    connect.cursor.execute(sql_id)
    directory_id = connect.cursor.fetchone()
    connect.close()
    directory_id = str(directory_id)
    directory_id = directory_id.strip("()")
    directory_id = directory_id.strip(",")

    for song in songs:
        if song_existance(song) is False:
            sql = f""" INSERT INTO songs_record (song_name, directory_id) VALUES ('{song}', {directory_id})"""
            connect.cursor.execute(sql)
            connect.close()


def get_song():
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
