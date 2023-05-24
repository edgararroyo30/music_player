from model.db_conection import ConnectDB


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
