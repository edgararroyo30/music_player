"""
A queue is created each time a song is played.
The queue stores all the songs id's in the playing path.
Playing next id > current song id 
Playing back id < current song id 
"""


from model.db_conection import ConnectDB
from model.songs_record_db import get_song


def create_queue_table():
    """
    Creates the table that stores the queue.

    Values:
    id: integer, primary key, autoincrement
    song_in_queue: Varchar (100)
    """

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


def add_to_queue():
    """
    Cleans the table if has data in it.
    Creates the queue by accesing the id's in the path.
    Using the method get_song() from songs_record_db.
    """

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
    """
    Returns all the id's in the table.
    """

    connect = ConnectDB()

    sql = '''SELECT id FROM queue'''

    connect.cursor.execute(sql)
    queue = connect.cursor.fetchall()
    connect.close()

    return queue


def get_playing_song_id(song_name):
    """
    Return the given song's id.

    Argument:
    song_name -> Str
    """

    connect = ConnectDB()

    sql = f''' SELECT id FROM queue WHERE song_in_queue = '{song_name}' '''
    connect.cursor.execute(sql)
    song_id = connect.cursor.fetchone()
    connect.close()

    return song_id


def get_playing_next_song(song_id):
    """
    Return the song name for a given id.

    Argument:
    song_id -> Int
    """

    connect = ConnectDB()

    sql = f''' SELECT song_in_queue FROM queue WHERE id = '{song_id}' '''

    connect.cursor.execute(sql)
    song_name = connect.cursor.fetchone()
    connect.close()

    return song_name
