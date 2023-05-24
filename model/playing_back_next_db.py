from model.db_conection import ConnectDB


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

    sql = '''INSERT INTO playing_back(song) VALUES (?)'''
    play_back_song = str(play_back_song)
    play_back_song = play_back_song.strip("()")
    play_back_song = play_back_song.strip(",")
    play_back_song = play_back_song.strip("'")
    play_back_song = play_back_song.strip()
    print(play_back_song)
    connect.cursor.execute(sql, (play_back_song,))
    connect.close()


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
