from model.db_conection import ConnectDB


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


def add_to_playing_next(play_back_song):
    connect = ConnectDB()

    sql_existance = '''SELECT * FROM playing_next'''
    connect.cursor.execute(sql_existance)
    exists = connect.cursor.fetchone()

    if exists is None:
        for song in play_back_song:
            song = str(song)
            song = song.strip("()")
            song = song.strip(",")
            song = song.strip("'")
            song = song.strip()

            sql = f'''INSERT INTO playing_next(song) VALUES ('{song}')'''
            connect.cursor.execute(sql)
        connect.close()

    else:

        sql_delete = '''DELETE FROM playing_next'''
        connect.cursor.execute(sql_delete)

        sql_delete_back = '''DELETE FROM playing_back'''
        connect.cursor.execute(sql_delete_back)

        for song in play_back_song:
            song = str(song)
            song = song.strip("()")
            song = song.strip(",")
            song = song.strip("'")
            song = song.strip()

            sql = f'''INSERT INTO playing_next(song) VALUES ('{song}')'''
            connect.cursor.execute(sql)
        connect.close()


def play_next(curent_song):
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

    add_to_playing_back(curent_song)

    return playing_next_song


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


def add_to_playing_back(play_back_song):
    connect = ConnectDB()

    play_back_song = str(play_back_song)
    play_back_song = play_back_song.strip("()")
    play_back_song = play_back_song.strip(",")
    play_back_song = play_back_song.strip("'")
    play_back_song = play_back_song.strip()

    sql = f'''INSERT INTO playing_back(song, id) VALUES ('{play_back_song}', (SELECT COALESCE(MAX(id), 0) - 1 FROM playing_back))'''
    connect.cursor.execute(sql)
    connect.close()


def move_to_playing_next(play_back_song):
    connect = ConnectDB()

    play_back_song = str(play_back_song)
    play_back_song = play_back_song.strip("()")
    play_back_song = play_back_song.strip(",")
    play_back_song = play_back_song.strip("'")
    play_back_song = play_back_song.strip()

    sql = f'''INSERT INTO playing_next(song) VALUES ('{play_back_song}')'''
    connect.cursor.execute(sql)
    connect.close()


def play_back():
    connect = ConnectDB()

    sql = '''SELECT song
        FROM playing_back
        ORDER BY id
        LIMIT 1'''

    connect.cursor.execute(sql)
    playing_back_song = connect.cursor.fetchone()

    sql_delete = '''
        DELETE FROM playing_back
        WHERE id = (
        SELECT id
        FROM playing_back
        ORDER BY id
        LIMIT 1)
    '''

    connect.cursor.execute(sql_delete)
    connect.close()

    move_to_playing_next(playing_back_song)

    return playing_back_song
