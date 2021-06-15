import sqlite3
import os
import logging
from dotenv import load_dotenv

logger = logging.getLogger(__name__)

load_dotenv(r'D:\Programy do nauki\Projekty Python\Reminder\.env')

DB_LOCATION = os.getenv("DB_LOCATION")


class DatabaseHandler:
    #TODO Remodeling this class to be more redundant
    __DB_LOCATION = DB_LOCATION

    def __init__(self, db_location=None):
        """ Initialize db class variables """
        if db_location is not None:
            """ Allows to set db location through argument """
            self.connection = sqlite3.connect(db_location)
        else:
            self.connection = sqlite3.connect(DatabaseHandler.__DB_LOCATION)
        self.cur = self.connection.cursor()

    def select(self, table_name):
        self.cur.execute(f"SELECT * FROM {table_name};")

    def insert(self, table_name, task_name, task_details, task_addition_date, task_deadline):
        self.cur.execute(f"INSERT INTO {table_name} VALUES (:task, :details, :add_date, :deadline);",
                         {'task': task_name, 'details': task_details, 'add_date': task_addition_date,
                          'deadline': task_deadline})

    def delete(self, table_name, record):
        self.cur.execute(f"DELETE FROM {table_name} WHERE TaskName=(:item);",
                         {'item': record})

    def update(self, table_name, task_name, new_task_name, new_task_details, new_task_deadline):
        self.cur.execute(f"UPDATE {table_name} SET TaskName=(:new_name), TaskDetails=(:new_details), \
                            TaskDeadline=(:new_deadline) WHERE TaskName=(:old_name);",
                         {'new_name': new_task_name, 'new_details': new_task_details, 'new_deadline': new_task_deadline,
                          'old_name': task_name})

    def create_table(self, table_name):
        self.cur.execute(f""" CREATE TABLE IF NOT EXISTS {table_name}(  TaskName text, \
                                                                        TaskDetails text, \
                                                                        AdditionDate text, \
                                                                        TaskDeadline text)""")

    def transfer_data_between_tables(self, table1_name, table2_name, key_value):
        self.cur.execute(f"INSERT INTO {table2_name} SELECT * FROM {table1_name} WHERE TaskName=(:value);",
                         {'value': key_value})
        self.delete(table1_name, key_value)

    def drop_table(self, table_name):
        self.cur.execute(f"DROP TABLE IF EXISTS {table_name}")
        print(f"Dropped the {table_name} table")

    def __enter__(self):
        return self

    def __exit__(self, ext_type, exc_value, traceback):
        self.cur.close()
        if isinstance(exc_value, Exception):
            self.connection.rollback()
        else:
            self.connection.commit()
        self.connection.close()
