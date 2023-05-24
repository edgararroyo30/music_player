from model.db_conection import ConnectDB
from tkinter import messagebox


def create__directory_table():
    connect = ConnectDB()

    sql = '''
    CREATE TABLE IF NOT EXISTS music_directory(
    id_directory INTEGER,
    directory_path VARCHAR(200),
    PRIMARY KEY(id_directory AUTOINCREMENT)
    )
    '''

    connect.cursor.execute(sql)
    connect.close()


def save_directory(directory):
    connect = ConnectDB()
    # escaped_directory = directory.replace("'", "''")

    sql = f"""INSERT INTO music_directory (directory_path) VALUES ('{directory}')"""

    try:
        connect.cursor.execute(sql)
        connect.close()

    except Exception as e:
        print(e)
        titulo = 'Database connection'
        mensaje = 'No table in the database'
        messagebox.showerror(titulo, mensaje)


def check_existance():
    connect = ConnectDB()

    sql = 'SELECT * FROM music_directory'

    connect.cursor.execute(sql)
    directory = connect.cursor.fetchone()
    connect.close()

    if directory is None:
        return False
    return True


def get_directory():
    connect = ConnectDB()

    sql = 'SELECT (directory_path)  FROM music_directory'

    connect.cursor.execute(sql)
    directory = connect.cursor.fetchone()
    connect.close()

    directory = str(directory)
    directory = directory.strip("()")
    directory = directory.strip("'")
    directory = directory.strip(",")
    directory = directory[:-1]

    return directory


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


def create_recently_played_table():
    connection = ConnectDB()

    sql = '''
        CREATE TABLE IF NOT EXISTS recently_played(
        id INTEGER,
        recently_played_song VARCHAR(100),
        PRIMARY KEY(id AUTOINCREMENT)
        )
    '''

    connection.cursor.execute(sql)
    connection.close()


def add_recently_played_song(song):
    connect = ConnectDB()

    sql = f"""INSERT INTO recently_played(recently_played_song) VALUES ('{song}')"""

    connect.cursor.execute(sql)
    connect.close()


def get_recently_played_songs():
    connect = ConnectDB()

    sql = """ SELECT recently_played_song FROM recently_played"""

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


def create_playlist_name_table():
    connect = ConnectDB()

    sql = '''
        CREATE TABLE IF NOT EXISTS  playlist_name_storage(
        id INTEGER,
        playlist_name VARCHAR(200),
        PRIMARY KEY(id AUTOINCREMENT)
        )
    '''
    connect.cursor.execute(sql)
    connect.close()


def add_playlist_name(playlist_name):
    connect = ConnectDB()

    sql = f'''
        INSERT INTO playlist_name_storage(playlist_name) VALUES ('{playlist_name}')
    '''
    connect.cursor.execute(sql)
    connect.close()


def create_queue_table():
    connect = ConnectDB()

    sql = '''
        CREATE TABLE IF NOT EXISTS queue(
        id INTEGER,
        song_in_queue VARCHAR(100), 
        PRIMARY KEY(id AUTOINCREMENT)
        )
    '''

    connect.cursor.execute(sql)
    connect.close()


def add_song_to_playlist(song_name, playlist_name):
    connect = ConnectDB()

    sql_id = f'''
        SELECT id FROM playlist_name_storage WHERE playlist_name = '{playlist_name}'
    '''
    connect.cursor.execute(sql_id)
    playlist_id = connect.cursor.fetchone()
    connect.close()
    playlist_id = str(playlist_id)
    playlist_id = playlist_id.strip("()")
    playlist_id = playlist_id.strip(",")

    sql = f'''
        UPDATE songs_record 
        SET playlist_id ={playlist_id}
        WHERE song_name = '{song_name}';
    '''

    connect.cursor.execute(sql)
    connect.close()


def add_to_queue():
    connect = ConnectDB()

    sql = '''SELECT * FROM queue'''

    connect.cursor.execute(sql)
    exists = connect.cursor.fetchone()

    if exists is None:
        for song in get_song():
            sql_add = f'''INSERT INTO queue(song_in_queue) VALUES ('{song}')'''
            connect.cursor.execute(sql_add)
        connect.close()

    else:
        sql_delete = '''DELETE FROM queue'''
        connect.cursor.execute(sql_delete)

        for song in get_song():
            sql_add = f'''INSERT INTO queue(song_in_queue) VALUES ('{song}')'''
            connect.cursor.execute(sql_add)
        connect.close()


def get_queue_songs_id():
    connect = ConnectDB()

    sql = '''SELECT id FROM queue'''

    connect.cursor.execute(sql)
    queue = connect.cursor.fetchall()
    connect.close()

    return queue


def get_playing_song_id(song_name):
    connect = ConnectDB()

    sql = f''' SELECT id FROM queue WHERE song_in_queue = '{song_name}' '''
    connect.cursor.execute(sql)
    song_id = connect.cursor.fetchone()
    connect.close()

    return song_id


def get_playing_next_song(id):
    connect = ConnectDB()

    sql = f''' SELECT song_in_queue FROM queue WHERE id = '{id}' '''

    connect.cursor.execute(sql)
    song_name = connect.cursor.fetchone()
    connect.close()

    return song_name


def create_playing_back_table():
    connect = ConnectDB()

    sql = '''
    CREATE TABLE IF NOT EXISTS playing_back(
    id INTEGER,
    song VARCHAR(100),
    PRIMARY KEY(id AUTOINCREMENT)
    )
    '''
    connect.cursor.execute(sql)
    connect.close()


def create_playing_next_table():
    connect = ConnectDB()

    sql = '''
    CREATE TABLE IF NOT EXISTS playing_next(
    id INTEGER,
    song VARCHAR(100),
    PRIMARY KEY(id AUTOINCREMENT)
    )
    '''
    connect.cursor.execute(sql)
    connect.close()


def add_to_playing_next(play_next_song):
    connect = ConnectDB()

    sql = f'''INSERT INTO playing_next(song) VALUES ('{play_next_song}')'''
    print(play_next_song)

    connect.cursor.execute(sql)
    connect.close()


def add_to_playing_back(play_back_song):
    connect = ConnectDB()

    sql = '''INSERT INTO playing_back(song) VALUES (?)'''
    play_back_song = str(play_back_song)
    play_back_song = play_back_song.strip("()")
    play_back_song = play_back_song.strip(",")
    play_back_song = play_back_song.strip("'")
    play_back_song = play_back_song.strip()
    print(play_back_song)
    connect.cursor.execute(sql, (play_back_song,))
    connect.close()


def play_next():
    connect = ConnectDB()

    sql = '''SELECT song
        FROM playing_next
        ORDER BY id
        LIMIT 1'''

    connect.cursor.execute(sql)
    playing_next_song = connect.cursor.fetchone()

    sql_delete = '''
        DELETE FROM playing_next
        WHERE id = (
        SELECT id
        FROM playing_next
        ORDER BY id
        LIMIT 1)
    '''

    connect.cursor.execute(sql_delete)
    connect.close()

    add_to_playing_back(f'{playing_next_song}')

    return playing_next_song


def play_back():
    connect = ConnectDB()

    sql = ''' 
        SELECT song
        FROM playing_back
        ORDER BY song
        LIMIT 1
    '''

    connect.cursor.execute(sql)
    playing_back_song = connect.cursor.fetchone()

    sql_delete = '''
        DELETE FROM playing_back
        WHERE id = (
        SELECT id
        FROM playing_next
        ORDER BY id
        LIMIT 1)
    '''

    connect.cursor.execute(sql_delete)
    connect.close()

    add_to_playing_next(playing_back_song)

    return playing_back_song
