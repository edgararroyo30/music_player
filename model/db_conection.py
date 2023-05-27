"""
Grant access to the database through the class ConnectDB
"""

import sqlite3


class ConnectDB:
    """
    Stablish the connection to the database.
    .cursor() creates the cursor for the DB
    The .close() method calls commit and close
    """

    def __init__(self):
        self.data_base = 'database/directory.db'
        self.conection = sqlite3.connect(self.data_base)
        self.cursor = self.conection.cursor()

    def close(self):
        """
        Commit and close the database at once
        """
        self.conection.commit()
        self.conection.close()
