"""
Table for the artists names.
"""

from model.db_conection import ConnectDB
from classes.format_string import FormatString

give_format = FormatString()


def create_artist_table():
    """
    Creates the table for the artists names.
    """
    connect = ConnectDB()

    sql = """
    create table if not exists artist(
    id integer,
    artists_name varchar(100),
    primary key(id autoincrement)
    )
    """

    connect.cursor.execute(sql)
    connect.close()


def artist_existance(artist_name):
    """
    Check if the given artist is already in the table
    """

    connect = ConnectDB()

    sql = 'select artists_name from artist where artists_name = ?;'

    connect.cursor.execute(sql, (artist_name,))
    existance = connect.cursor.fetchone()
    connect.close()

    if existance is None:

        return False

    return True


def add_artist(artist_name):
    """
    Add the given artist to the artist table
    """
    connect = ConnectDB()

    if artist_existance(artist_name) is False:

        sql = 'insert into artist(artists_name) values (?);'

        connect.cursor.execute(sql, (artist_name,))
        connect.close()
        return True

    return False


def artist_id(artist_name):
    """
    Returns the artist id
    """
    connect = ConnectDB()

    sql = 'SELECT id FROM artist WHERE artists_name = ?'
    connect.cursor.execute(sql, (artist_name,))
    id = connect.cursor.fetchone()
    connect.close()

    return id


def asign_artist(song_name, artist_name):
    """
    Asign the given artist id to a given song
    """
    connect = ConnectDB()

    if add_artist(artist_name) is True:
        given_id = artist_id(artist_name)
        given_id = give_format.format(given_id, 4)
        sql = 'UPDATE songs_record SET artist_id = ?  WHERE song_name = ?; '
        connect.cursor.execute(sql, (given_id, song_name.lower()))
        connect.close()

    else:
        given_id = artist_id(artist_name)
        given_id = give_format.format(given_id, 4)
        sql = 'UPDATE songs_record SET artist_id = ?  WHERE song_name = ?; '
        connect.cursor.execute(sql, (given_id, song_name.lower()))
        connect.close()


def get_artist_name(given_id):
    """
    Give the artist name for a given id
    """
    connect = ConnectDB()

    given_id = give_format.format(given_id, 4)

    sql = 'SELECT artists_name FROM artist WHERE id = ?'
    connect.cursor.execute(sql, (given_id,))
    name = connect.cursor.fetchone()
    connect.close()

    name = give_format.format(name, 4)

    return name
