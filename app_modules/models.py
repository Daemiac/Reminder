import random
import logging
import requests
import json
import datetime

from app_modules.db_handler import DatabaseHandler

logger = logging.getLogger(__name__)


class TaskListModel:
    def __init__(self):
        self.task_list = None
        self.db = None

        self.task_addition_date = datetime.datetime.now()

        self.retrieve_tasks_from_db()

    def retrieve_tasks_from_db(self):
        with DatabaseHandler() as self.db:
            self.db.create_table('tasks')
            self.db.select('tasks')
            self.task_list = self.db.cur.fetchall()

    def add_task_to_db(self, task, details, deadline):
        logger.debug('Tryout of addition of a "%s" task to database', task)
        with DatabaseHandler() as self.db:
            self.db.insert('tasks', task, details, self.task_addition_date.strftime("%d.%m.%Y"), deadline)
            logger.info('Task "%s" successfully added to a database', task)

    def update_task_data(self, task_name, new_task_name, new_details, new_deadline):
        with DatabaseHandler() as self.db:
            self.db.update('tasks', task_name, new_task_name, new_details, new_deadline)
            logger.info('Task "%s" details changed', task_name)

    def delete_task_from_db(self, task):
        logger.debug('Tryout of deletion of a "%s" task from a database', task)
        with DatabaseHandler() as self.db:
            self.db.delete('tasks', task)
            logger.info('Task "%s" successfully deleted from a database', task)

    def archive_task(self, task):
        logger.debug('Tryout of archiving of a "%s" task', task)
        with DatabaseHandler() as self.db:
            self.db.create_table('archive')
            self.db.transfer_data_between_tables('tasks', 'archive', task)
            logger.info('Task "%s" successfully archived', task)


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
            logger.exception("Connection couldn't be established...", exc_info=True)
            self.get_quote_from_file()

    def get_quote_from_file(self):
        """ Gets random motivational quote from external file in case of connection or timeout error """
        with open('data/mot_quotes.txt', 'r') as read_file:
            data = json.load(read_file)
            self.quote = random.choice(data["quotes"])
            while not self.is_quote_valid():
                self.quote = random.choice(data["quotes"])

    def is_quote_valid(self):
        """ Checks if quote's text length isn't bigger than 85 characters """
        if len(self.quote["text"]) > 85:
            logger.debug("Text too long to be displayed, trying again...")
            return False
        else:
            if self.quote["author"] is None or self.quote["author"] == "" or self.quote["author"] == "null":
                logger.debug("Author data doesn't exist, setting it to 'Unknown'... ")
                self.quote['author'] = 'Unknown'
            return True


class Archive:
    def __init__(self):
        self.archived_tasks = None
        self.db = None

    def retrieve_tasks_from_db(self):
        with DatabaseHandler() as self.db:
            self.db.create_table('archive')
            self.db.select('archive')
            self.archived_tasks = self.db.cur.fetchall()
            print(self.archived_tasks)

    def dump_archive(self):
        with DatabaseHandler() as self.db:
            self.db.drop_table('archive')
