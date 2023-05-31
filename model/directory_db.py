"""
Methods for directory interaction.
create_directory_table: Creates the table
save_directory: Save a given directory path
check_existance: Check if a directory exists in the table
get_directory: Retrieves the directory path
"""

from model.db_conection import ConnectDB


def create__directory_table():
    """
    Creates the directory table.

    Elements:
    id_directory: Autoincrement, primary key
    directory_path: Path of the directory

    """
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
    """
    Save a given directory path to the table and asigns an id.

    Arguments:
    directory: The direcotry path
    """

    connect = ConnectDB()

    sql = f"""INSERT INTO music_directory (directory_path) VALUES ('{directory}')"""

    connect.cursor.execute(sql)
    connect.close()


def check_existance():
    """
    Check if the table is not empty.

    Values:
    If is empty return False, if not return True
    """

    connect = ConnectDB()

    sql = 'SELECT * FROM music_directory'

    connect.cursor.execute(sql)
    directory = connect.cursor.fetchone()
    connect.close()

    if directory is None:
        return False
    return True


def get_directory():
    """
    Retrieves the first value in the directory table
    """

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


def edit_directory(old_directory, new_directory):
    """
    Updates a directory
    """
    connect = ConnectDB()

    sql = 'UPDATE music_directory SET directory_path = ? WHERE directory_path = ?'

    connect.cursor.execute(sql, (new_directory, old_directory,))
    connect.close()
