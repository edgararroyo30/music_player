"""
Table for the albums names.
"""

from model.db_conection import ConnectDB
from classes.format_string import FormatString

give_format = FormatString()


def create_album_table():
    """
    Creates the table for the albums names.
    """
    connect = ConnectDB()

    sql = """
    create table if not exists album(
    id integer,
    album_name varchar(100),
    artist_id integer,
    primary key(id autoincrement)
    )
    """

    connect.cursor.execute(sql)
    connect.close()


def album_existance(album_name):
    """
    Check if the given album is already in the table
    """

    connect = ConnectDB()

    sql = 'select album_name from album where album_name = ?;'

    connect.cursor.execute(sql, (album_name,))
    existance = connect.cursor.fetchone()
    connect.close()

    if existance is None:

        return False

    return True


def add_album(album_name):
    """
    Add the given album to the album table
    """
    connect = ConnectDB()

    if album_existance(album_name) is False:

        sql = 'insert into album(album_name) values (?);'

        connect.cursor.execute(sql, (album_name,))
        connect.close()
        return True

    return False


def album_id(album_name):
    """
    Returns the album id
    """
    connect = ConnectDB()

    sql = 'SELECT id FROM album WHERE album_name = ?'
    connect.cursor.execute(sql, (album_name,))
    id = connect.cursor.fetchone()
    connect.close()

    return id


def asign_album(song_name, album_name):
    """
    Asign the given album id to a given song
    """
    connect = ConnectDB()

    if add_album(album_name) is True:
        given_id = album_id(album_name)
        given_id = give_format.format(given_id, 4)
        sql = 'UPDATE songs_record SET album_id = ?  WHERE song_name = ? ;'
        connect.cursor.execute(sql, (given_id, song_name.lower()))
        connect.close()

    else:
        given_id = album_id(album_name)
        given_id = give_format.format(given_id, 4)
        sql = 'UPDATE songs_record SET album_id = ?  WHERE song_name = ? ;'
        connect.cursor.execute(sql, (given_id, song_name.lower()))
        connect.close()


def get_album_name(given_id):
    """
    Give the album name for a given id
    """
    connect = ConnectDB()
    given_id = give_format.format(given_id, 4)

    sql = 'SELECT album_name FROM album WHERE id = ?'
    connect.cursor.execute(sql, (given_id,))
    name = connect.cursor.fetchone()
    connect.close()

    name = give_format.format(name, 4)

    return name
