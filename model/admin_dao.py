from model.db_conection import ConnectDB
from tkinter import messagebox


def create_table():
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
