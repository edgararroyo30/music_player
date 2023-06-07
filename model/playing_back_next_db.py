"""
Create tables that stores the songs that would be played next and back for the current playing song.
The tables are updated everytime the user skip backwards or forward, 
change the current playing song or the queue
"""

from model.db_conection import ConnectDB
import sqlite3


def song_existance(song):
    """
    Check if the song that is being given already exists in the table.
    If the song exists return True.
    If not return False.

    Argument:
    song -> Str
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


def create_playing_next_table():
    """
    Creates the table that stores the playin next songs.

    Values:
    id: primary key, autpincrement
    song: song name
    """

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
    """
    Add songs to the playing next table.

    First empty the table if it has values.
    Then insert the playing next song.

    Argument:
    Playing next songs -> List
    """

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
    """
    Returns the first song on playing next table.
    Then delete this song from the table.
    Lastly send the current song to play back table.

    Arguments:
    current_song -> Str
    """

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

    if curent_song is None:
        pass

    else:
        move_to_playing_back(curent_song)

    if playing_next_song is None:
        print("No song")
        return None

    return playing_next_song


def create_playing_back_table():
    """
    Creates the table that stores the playin back songs.

    Values:
    id: primary key, autpincrement
    song: song name
    """
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
    """
    Add songs to the playing back table.

    First empty the table if it has values.
    Then insert the playing back song.

    Argument:
    Playing back songs -> List
    """
    try:
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
                sql = f'''INSERT INTO playing_back(song, id) VALUES ('{song}', (SELECT COALESCE(MAX(id), 0) - 1 FROM playing_back))'''
                connect.cursor.execute(sql)
            connect.close()

        else:

            sql_delete_back = '''DELETE FROM playing_back'''
            connect.cursor.execute(sql_delete_back)

            for song in play_back_song:
                song = str(song)
                song = song.strip("()")
                song = song.strip(",")
                song = song.strip("'")
                song = song.strip()
                sql = f'''INSERT INTO playing_back(song, id) VALUES ('{song}', (SELECT COALESCE(MAX(id), 0) - 1 FROM playing_back))'''
                connect.cursor.execute(sql)
            connect.close()

    except sqlite3.IntegrityError as e:
        print("UNIQUE constraint violation:", e)
        connect.close()


def move_to_playing_next(play_back_song):
    """
    Moves the played back song to the play next table

    ONLY FOR USE BETWEEN TABLES

    Arguments:

    Play_back_song -> Sr
    """

    connect = ConnectDB()
    play_back_song = str(play_back_song)
    play_back_song = play_back_song.strip("()")
    play_back_song = play_back_song.strip(",")
    play_back_song = play_back_song.strip("'")
    play_back_song = play_back_song.strip()

    try:
        sql = f'''INSERT INTO playing_next(song) VALUES ('{play_back_song}')'''
        connect.cursor.execute(sql)
        connect.close()

    except sqlite3.IntegrityError as e:
        print("UNIQUE constraint violation:", e)


def move_to_playing_back(play_back_song):
    """
    Moves the played song to the play back table

    ONLY FOR USE BETWEEN TABLES

    Arguments:

    Play_back_song -> Str
    """

    connect = ConnectDB()

    play_back_song = str(play_back_song)
    play_back_song = play_back_song.strip("()")
    play_back_song = play_back_song.strip(",")
    play_back_song = play_back_song.strip("'")
    play_back_song = play_back_song.strip()

    try:

        sql = f'''INSERT INTO playing_back(song, id) VALUES ('{play_back_song}', (SELECT COALESCE(MAX(id), 0) - 1 FROM playing_back))'''
        connect.cursor.execute(sql)
        connect.close()

    except sqlite3.IntegrityError as e:
        print("UNIQUE constraint violation:", e)
        connect.close()


def play_back():
    """
    Returns the first song on playing back table.
    Then delete this song from the table.
    Lastly send the current song to play next table.

    """
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
