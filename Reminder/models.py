import random
import requests
import json


class TaskListModel:
    def __init__(self):
        self.task_list = self.retrieve_tasks()

    @staticmethod
    def retrieve_tasks():
        """ Retrieves tasks from external file """
        try:
            with open('task_list.txt', 'r') as read_file:
                data = json.load(read_file)
                # print(data['task list'])
        except FileNotFoundError:
            data = {"task list": []}

        finally:
            return data['task list']

    def save_tasks(self):
        """ Saves made changes to external file """
        data = {"task list": self.task_list}
        with open('task_list.txt', 'w') as outfile:
            json.dump(data, outfile, indent=2)
        print("Tasks imported to task.txt file")

    def add_task_to_list(self, title, details):
        """ Modifies self.task_list attribute by adding given item """
        task = {title: details}
        self.task_list.append(task)
        print("A task has been added to list!")

    def update_task_details(self, old_title, old_details, title, details):
        """ Modifies self.task_list attribute by changing details of given item """
        item = {old_title: old_details}
        updated_item = {title: details}
        print(item, updated_item)
        self.task_list[:] = [updated_item if element == item else element for element in self.task_list]

    def delete_task_from_list(self, task):
        """ Modifies self.task_list attribute by deleting given item """
        task_det = next(i for i, d in enumerate(self.task_list) if task in d)
        del self.task_list[task_det]


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
