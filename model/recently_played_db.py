from model.db_conection import ConnectDB


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
