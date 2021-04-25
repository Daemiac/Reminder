import random
import requests
import json
import os

from app_modules.db_handler import DatabaseHandler


class TaskListModel:
    def __init__(self):
        self.task_list = None
        self.db = None

        self.retrieve_tasks_from_db()

    def retrieve_tasks_from_db(self):
        with DatabaseHandler() as self.db:
            self.db.create_table('tasks')
            self.db.select('tasks')
            self.task_list = self.db.cur.fetchall()

    def add_task_to_db(self, task, details):
        print("Adding task to database tryout")
        with DatabaseHandler() as self.db:
            self.db.insert('tasks', task, details)

    def update_task_data(self, task_name, new_task_name, new_details):
        with DatabaseHandler() as self.db:
            self.db.update('tasks', task_name, new_task_name, new_details)

    def delete_task_from_db(self, task):
        print("Let's try to delete task from db!")
        with DatabaseHandler() as self.db:
            self.db.delete('tasks', task)
            print("A task has been deleted from db!")

    def archive_task(self, task):
        pass


class MotivationalQuoteModel:
    def __init__(self):
        self.quote = None
        self.get_quote_from_api()

    def get_quote_from_api(self):
        """ Gets random motivational quote from api """
        url = "https://type.fit/api/quotes?fbclid=IwAR066CVqn2qdvUIEBui3J2r-xre3ZcaQrfKJkqJmf4Drj2FH-qgW1DgcD4c"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                self.quote = random.choice(data)
                while not self.is_quote_valid():
                    self.quote = random.choice(data)
        except (requests.ConnectionError, requests.Timeout):
            print("Connection couldnt be done...")
            self.get_quote_from_file()

    def get_quote_from_file(self):
        """ Gets random motivational quote from external file in case of connection or timeout error """
        with open('data/mot_quotes.txt', 'r') as read_file:
            data = json.load(read_file)
            self.quote = random.choice(data["quotes"])
            while not self.is_quote_valid():
                self.quote = random.choice(data["quotes"])

    def is_quote_valid(self):
        """ Checks if quote's text length isn't bigger than 90 characters """
        if len(self.quote["text"]) > 90:
            return False
        else:
            if self.quote["author"] is None or self.quote["author"] == "":
                self.quote['author'] = 'Unknown'
            return True
