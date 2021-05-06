import sqlite3
import os
import json

LOCATION_CONSTANT = os.path.relpath(r'data/task_list.sqlite')


class DatabaseHandler:
    #TODO Remodeling this class to be more redundant
    __DB_LOCATION = LOCATION_CONSTANT

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

    def insert(self, table_name, task_name, task_details, task_deadline):
        self.cur.execute(f"INSERT INTO {table_name} VALUES (:task, :details, :deadline);",
                         {'task': task_name, 'details': task_details, 'deadline': task_deadline})

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


if __name__ == "__main__":

    with DatabaseHandler() as train_db:
        train_db.create_table('tasks')
        train_db.drop_table('archive')
        train_db.create_table('archive')

    path = os.path.relpath(r'../data/task_list.txt')

    with open(f'{path}', 'r') as json_list:
        task_list = json.load(json_list)
        data = task_list['task list']

    print(data)

    with DatabaseHandler() as train_db:
        # for num, item in enumerate(data):
        #     for key in item:
        #         print(num, key, item[key])
        #         train_db.insert("tasks", key, item[key])
        train_db.select('tasks')
        rows = train_db.cur.fetchall()
        print(rows)
        train_db.update('tasks', 'Clean up the mess', 'Clean up', 'You should clean up your kitchen!')
        train_db.transfer_data_between_tables('tasks', 'archive', 'Clean up')
