#!/usr/bin/env python3

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QWidget, QVBoxLayout, QHBoxLayout, QDialogButtonBox, \
    QGroupBox, QFormLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QFont
from functools import partial
import random
import requests
import sys
import json

STYLE_SHEET = {'app_window': 'background-color: #121212;',
               'button': 'background-color: #282828; font-weight: bold; color: #B3B3B3; border-radius: 10;',
               'button_hover': 'background-color: #282828; font-weight: bold; color: #FFFFFF; border-radius: 10;',
               'task_list_label': 'font-weight: bold; font-family: Verdana; color: #FFFFFF; font-size: 11pt',
               'task_list_widget': 'background-color: #282828; color: #B3B3B3; font-weight: bold; border-radius: 5;',
               'task_details_label': 'font-weight: bold; font-family: Verdana; color: #FFFFFF; font-size: 11pt',
               'task_details_widget': 'background-color: #B3B3B3; font-family: Courier;'
                                      ' font-style: italic; font-size: 10pt',
               'mot_quote': 'background-color: #800000; color: white; font-weight: bold; font-family:'
                            ' Courier; font-size: 8pt; border: 1px solid black;', }


class AppView(QMainWindow):
    """ Class responsible for rendering view of the app """
    def __init__(self):
        super().__init__()
        # Set main window's properties
        self.title = "Reminder alpha ver"
        self.x_position = 400
        self.y_position = 300
        self.width = 1065
        self.height = 575
        self.setWindowTitle(self.title)
        # TODO set proper window size and adjust the layout of the window widget
        self.setFixedSize(self.width, self.height)
        # self.setGeometry(self.x_position, self.y_position, self.width, self.height)
        self.setStyleSheet(STYLE_SHEET['app_window'])

        # Creation of the central widget and general layout
        self.generalLayout = QVBoxLayout()
        self._centralWidget = QWidget(self)
        self.setCentralWidget(self._centralWidget)
        self._centralWidget.setLayout(self.generalLayout)

        # Create child widgets
        self.first_widget = TaskListWidget()
        self.second_widget = TaskInfoWidget()
        self.third_widget = BottomWidget()

        self.render_view()

    def render_view(self):
        """ Creates layout of child widgets """
        minor_layout = QHBoxLayout()
        minor_layout.addWidget(self.first_widget)
        minor_layout.addStretch(1)
        minor_layout.addWidget(self.second_widget)
        self.generalLayout.addLayout(minor_layout)
        self.generalLayout.addStretch(1)
        self.generalLayout.addWidget(self.third_widget)


class TaskListWidget(QWidget):
    """ Renders view of task list widget """
    def __init__(self):
        super().__init__()
        self.width = 400
        self.height = 500
        self.main_layout = QVBoxLayout()
        self.task_list = None

        # Create inner widgets
        self.create_task_list_label()
        self.create_task_list_widget()
        self.create_buttons()

        self.setLayout(self.main_layout)

    def create_task_list_label(self):
        """ Sets up task list label and its properties """
        self.task_list_label = QtWidgets.QLabel(self)
        self.task_list_label.setAlignment(Qt.AlignCenter)
        self.task_list_label.setText("List of your current tasks")
        self.task_list_label.setStyleSheet(STYLE_SHEET['task_list_label'])
        self.task_list_label.adjustSize()
        self.main_layout.addWidget(self.task_list_label)

    def create_task_list_widget(self):
        """ Sets up task list widget and its properties """
        self.task_list_widget = QtWidgets.QListWidget(self)
        self.task_list_widget.setMinimumSize(250, 400)
        self.task_list_widget.setStyleSheet(STYLE_SHEET['task_list_widget'])
        self.main_layout.addWidget(self.task_list_widget)

    def create_buttons(self):
        """ Sets up widget's buttons and their properties """
        button_layout = QHBoxLayout()
        self.add_button = QtWidgets.QPushButton("Add task", self)
        self.add_button.setObjectName("add_button")
        self.add_button.setStyleSheet(f"#{self.add_button.objectName()}{{{STYLE_SHEET['button']}}} "
                                      f"#{self.add_button.objectName()}::hover {{{STYLE_SHEET['button_hover']}}}")
        self.add_button.setFixedWidth(100)
        self.add_button.setFixedHeight(30)
        button_layout.addWidget(self.add_button)

        self.update_button = QtWidgets.QPushButton("Update task", self)
        self.update_button.setObjectName("update_button")
        self.update_button.setStyleSheet(f"#{self.update_button.objectName()}{{{STYLE_SHEET['button']}}} "
                                         f"#{self.update_button.objectName()}::hover {{{STYLE_SHEET['button_hover']}}}")
        self.update_button.setFixedWidth(100)
        self.update_button.setFixedHeight(30)
        button_layout.addWidget(self.update_button)

        self.arch_button = QtWidgets.QPushButton("Archive task", self)
        self.arch_button.setObjectName("arch_button")
        self.arch_button.setStyleSheet(f"#{self.arch_button.objectName()}{{{STYLE_SHEET['button']}}} "
                                       f"#{self.arch_button.objectName()}::hover {{{STYLE_SHEET['button_hover']}}}")
        self.arch_button.setFixedWidth(100)
        self.arch_button.setFixedHeight(30)
        button_layout.addWidget(self.arch_button)

        self.main_layout.addStretch(1)
        self.main_layout.addLayout(button_layout)

    def show_tasks(self, task_list):
        """ Displays all tasks on task_list_widget """
        self.task_list_widget.clear()
        for task in task_list:
            for key in task:
                self.task_list_widget.addItem(key)


class TaskInfoWidget(QWidget):
    """ Renders view of task info widget """
    def __init__(self):
        super().__init__()
        self.width = 700
        self.height = 500
        self.setFixedWidth(self.width)
        self.setFixedHeight(self.height)
        self.main_layout = QVBoxLayout()

        # Create inner widgets
        self.create_task_details_label()
        self.create_task_details_widget()

        self.setLayout(self.main_layout)

    def create_task_details_label(self):
        """ Sets up task detail widget's label and its properties """
        self.task_details_label = QtWidgets.QLabel(self)
        self.task_details_label.setAlignment(Qt.AlignCenter)
        self.task_details_label.setText("Details of your task")
        self.task_details_label.setStyleSheet(STYLE_SHEET['task_details_label'])
        self.task_details_label.adjustSize()

        self.main_layout.addWidget(self.task_details_label)

    def create_task_details_widget(self):
        """ Sets up task detail widget and its properties """
        self.quest_text = QtWidgets.QTextBrowser(self)
        self.quest_text.append("Select a task to show its details here!")
        self.quest_text.setStyleSheet(STYLE_SHEET['task_details_widget'])

        self.main_layout.addWidget(self.quest_text)

    def update_quest_info(self, item_clicked):
        """ Method responsible for updating task detail widget's content """
        self.quest_text.setText("Details: {}".format(item_clicked))


class BottomWidget(QWidget):
    """ Renders view of bottom widget """
    def __init__(self):
        super().__init__()
        self.width = 700
        self.height = 50

        self.main_layout = QHBoxLayout()
        self.create_motivational_quote()
        self.create_close_button()

        self.setLayout(self.main_layout)

    def create_motivational_quote(self):
        """ Sets up motivational quote widget and its properties """
        self.mot_quote = QtWidgets.QLabel(self)
        self.mot_quote.setAlignment(Qt.AlignCenter)
        self.mot_quote.setStyleSheet(STYLE_SHEET['mot_quote'])
        self.mot_quote.adjustSize()

        self.main_layout.addWidget(self.mot_quote)

    def create_close_button(self):
        """ Sets up additional app's close button and its properties """
        self.close_button = QtWidgets.QPushButton("Close app", self)
        self.close_button.setObjectName("close_button")
        self.close_button.setStyleSheet(f"#{self.close_button.objectName()}{{{STYLE_SHEET['button']}}} "
                                        f"#{self.close_button.objectName()}::hover {{{STYLE_SHEET['button_hover']}}}")
        self.close_button.setFixedWidth(100)
        self.close_button.setFixedHeight(30)

        self.main_layout.addWidget(self.close_button)

    def set_motivational_quote(self, quote_dic):
        """ Method responsible for updating motivational quote widget's content """
        self.mot_quote.setText(quote_dic["text"] + " - " + quote_dic["author"])


class AddDialog(QDialog):
    """ Class used to create dialog window widgets """
    def __init__(self):
        super(AddDialog, self).__init__()
        self.setFixedWidth(500)
        self.setFixedHeight(300)

        self.main_layout = QVBoxLayout()
        self.create_form_group_box()
        self.create_button_box()
        self.setLayout(self.main_layout)

        self.setWindowTitle("Add new task to your list")

    def create_form_group_box(self):
        # TODO refactor dialog window
        self.form_group_box = QGroupBox("Task Information")
        self.task_title_label = QtWidgets.QLabel("Task title:")
        self.task_title_label.setStyleSheet("font-weight: bold")
        self.task_title_edit = QtWidgets.QLineEdit("Write your task here")
        self.task_details_label = QtWidgets.QLabel("Task details:")
        self.task_details_edit = QtWidgets.QTextEdit("Write tasks details here")
        layout = QFormLayout()
        layout.addRow(self.task_title_label, self.task_title_edit)
        layout.addRow(self.task_details_label, self.task_details_edit)
        self.form_group_box.setLayout(layout)

        self.main_layout.addWidget(self.form_group_box)

    def create_button_box(self):
        """ Sets up dialog's window bottom buttons and their properties """
        self.button_box = QDialogButtonBox(QDialogButtonBox.Save | QDialogButtonBox.Cancel)
        self.main_layout.addWidget(self.button_box)


class AppController:
    """ Mediates between model and view objects """
    def __init__(self, view, model):
        self._view = view
        self._model = model
        self._mot_model = MotivationalQuoteModel()
        self.update_task_list()
        self.update_motivational_quote()
        self._connect_signals()

    def _connect_signals(self):
        """ Method responsible for connecting main windows' signals with appropriate slot methods """
        self._view.first_widget.add_button.clicked.connect(self.add_task_window)
        self._view.first_widget.arch_button.clicked.connect(self.delete_task)
        self._view.third_widget.close_button.clicked.connect(self._close_the_app)
        self._view.first_widget.task_list_widget.itemClicked.connect(self.update_task_info)

    def _connect_dialog_signals(self):
        """ Method responsible for connecting dialog window's signals with appropriate slot methods """
        self._dialog.button_box.accepted.connect(self.accept_dialog)
        self._dialog.button_box.rejected.connect(self.reject_dialog)

    def _close_the_app(self):
        """ Saves changes into external file and closes the app """
        self._model.save_tasks()
        print("Closing the app...")
        sys.exit()

    def update_task_list(self):
        """ Updates task list widget's content with content of model's task list attribute """
        self._view.first_widget.show_tasks(self._model.task_list)

    def update_motivational_quote(self):
        """ Updates motivational quote widget's content with appropriate models' attribute """
        chosen_quote = self._mot_model.quote
        self._view.third_widget.set_motivational_quote(chosen_quote)

    @staticmethod
    def obtain_task_list_item(item_clicked):
        """ Returns clicked list widget's element as a string """
        item_clicked = str(item_clicked.text())
        return item_clicked

    def update_task_info(self, item_clicked):
        """ Updates task info widget's content """
        self.item_clicked = self.obtain_task_list_item(item_clicked)
        # searching through list of dictionaries
        task_det_dic = next(d for i, d in enumerate(self._model.task_list) if self.item_clicked in d)
        task_info = task_det_dic[self.item_clicked]
        self._view.second_widget.update_quest_info(task_info)

    def add_task_window(self):
        """ Creates a dialog window which can be used to add a task """
        self._dialog = AddDialog()
        self._connect_dialog_signals()
        self._dialog.show()

    def accept_dialog(self):
        """ Saves dialog window's entries to model's attribute and closes dialog window """
        key = self._dialog.task_title_edit.text()
        value = self._dialog.task_details_edit.toPlainText()
        self._model.add_task_to_list(key, value)
        self.update_task_list()
        self._dialog.close()
        print("Dialog form has been accepted. The task has been added. Closing the dialog window...")

    def reject_dialog(self):
        """ Closes dialog window without applying changes """
        self._dialog.close()
        print("Dialog form has been rejected. Closing the dialog window...")

    def delete_task(self):
        """ Method responsible for deleting a task from model's task list attribute and updating
            task list widget's view """
        item_to_delete = self.item_clicked
        self._model.delete_task_from_list(item_to_delete)
        print("task deleted successfully !")
        self.update_task_list()
        self._view.second_widget.update_quest_info("The task has been deleted!")


class TaskListModel:
    def __init__(self):
        self.task_list = self.retrieve_tasks()

    @staticmethod
    def retrieve_tasks():
        """ Retrieve tasks from external file """
        # TODO Handle an exception when there is not a single item in dictionary
        with open('task_list.txt', 'r') as read_file:
            data = json.load(read_file)
            # print(data['task list'])
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

    def update_task(self):
        """ Modifies self.task_list attribute by changing details of given item """
        pass

    def delete_task_from_list(self, task):
        """ Modifies self.task_list attribute by deleting given item """
        print(task)
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
        """ Gets random motivational quote from external file """
        with open('files/mot_quotes.txt', 'r') as read_file:
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


def main():
    """ Main function """
    # instance of 'QApplication'
    app = QApplication([])
    # instance of the model
    model = TaskListModel()
    # render the view
    view = AppView()
    view.show()
    # instance of the controller
    ctrl = AppController(view=view, model=model)

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
