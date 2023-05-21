import sqlite3


class ConnectDB:
    def __init__(self):
        self.data_base = 'database/directory.db'
        self.conection = sqlite3.connect(self.data_base)
        self.cursor = self.conection.cursor()

    def close(self):
        self.conection.commit()
        self.conection.close()
