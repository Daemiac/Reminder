import unittest

import json
import os.path


def retrieve_tasks():
    """ Retrieve tasks from external file """
    try:
        with open('task_file.txt', 'r') as read_file:
            data = json.load(read_file)
            print(data['task list'])
            return data['task list']
    except FileNotFoundError:
        create_empty_task_list()


def create_empty_task_list():
    json_template = {"task_list": []}
    with open('task_list.txt', 'w') as write_file:
        json.dump(json_template, write_file, indent=2)


def delete_empty_task_list():
    if os.path.isfile("task_list.txt"):
        os.remove("task_list.txt")


class TestFileCreation(unittest.TestCase):

    def test_create_empty_task_list(self):
        create_empty_task_list()
        self.assertTrue(os.path.isfile("task_list.txt"))

    def test_delete_empty_task_list(self):
        delete_empty_task_list()
        self.assertFalse(os.path.isfile("task_list.txt"))


if __name__ == '__main__':
    unittest.main()
