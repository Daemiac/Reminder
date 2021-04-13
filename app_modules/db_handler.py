import sqlite3
import os

LOCATION_CONSTANT = ''


class DatabaseModifier:

    __DB_LOCATION = LOCATION_CONSTANT

    def __init__(self, db_location=None):
        """ Initialize db class variables """
        if db_location is not None:
            """ Allows to set db location through argument """
            self.connection = sqlite3.connect(db_location)
        else:
            self.connection = sqlite3.connect(DatabaseModifier.__DB_LOCATION)
        self.cur = self.connection.cursor()

    def close(self):
        """ Closes sqlite3 connection """
        self.connection.close()

    def execute(self, data):
        self.cur.execute(data)

    def executemany(self, data):
        self.cur.executemany(data)

    def create_table(self):
        self.cur.execute(f""" CREATE TABLE IF NOT EXISTS tasks( TaskID integer PRIMARY KEY, \
                                                                TaskName text, \
                                                                TaskDetails text, \
                                                                AdditionDate text, \
                                                                Deadline text, \
                                                                Status text)""")

    def __enter__(self):
        return self

    def __exit__(self, ext_type, exc_value, traceback):
        self.cur.close()
        if isinstance(exc_value, Exception):
            self.connection.rollback()
        else:
            self.connection.commit()
        self.connection.close()


if __name__ == "__main__":
    train_db = DatabaseModifier()
    train_db.create_table()

