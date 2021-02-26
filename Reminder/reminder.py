#!/usr/bin/env python3

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QFont
import sys
import requests
import json
import random

STYLE_SHEET = {'app_window': 'background-color: #DCDCDC;',
               'quest_list_label': 'font-weight: bold; font-family: Verdana; color: #8B0000; font-size: 11pt',
               'quest_details': 'font-weight: bold; font-family: Verdana; color: #8B0000; font-size: 11pt',
               'quest_info': 'background-color: white; font-family: Courier; font-style: italic; font-size: 10pt',
               'mot_quote': 'background-color: #800000; color: white; font-weight: bold; font-family:'
                            ' Courier; font-size: 8pt; border: 1px solid black;',
               'close_button': 'font-weight: bold; color:red;'}

TASKS = {'task list': [{'Back to home': 'Going back to home for a weekend'},
                       {'Buy potatoes': 'You are short on potatoes. You can\'t make french fries without them!'},
                       {'Clean your room': 'Your environment is messy. Dustin\' time'},
                       {'Try if any errors occur': 'Testing json method'}], }


class AppView(QMainWindow):
    """ Main window of the app """
    def __init__(self):
        super().__init__()
        # Set main window's properties
        self.title = "Reminder alpha ver"
        self.x_position = 400
        self.y_position = 300
        self.width = 1100
        self.height = 600
        self.setWindowTitle(self.title)
        self.setGeometry(self.x_position, self.y_position, self.width, self.height)
        self.setStyleSheet(STYLE_SHEET['app_window'])

        # Set the central widget and general layout
        self.generalLayout = QVBoxLayout()
        self._centralWidget = QWidget(self)
        self.setCentralWidget(self._centralWidget)
        self._centralWidget.setLayout(self.generalLayout)

        # Create child widgets
        self.first_widget = QuestListTab()
        self.second_widget = QuestInfoTab()
        self.third_widget = BottomWidget()

        self.render_view()

        # signal transfer methods
        self.first_widget.quest_info_update.connect(self.second_widget.update_quest_info)

    def render_view(self):
        """ layout objects """
        minor_layout = QHBoxLayout()
        minor_layout.addWidget(self.first_widget)
        minor_layout.addStretch(1)
        minor_layout.addWidget(self.second_widget)
        self.generalLayout.addLayout(minor_layout)
        self.generalLayout.addStretch(1)
        self.generalLayout.addWidget(self.third_widget)


class QuestListTab(QWidget):

    quest_info_update = QtCore.pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.width = 400
        self.height = 500
        self.main_layout = QVBoxLayout()
        self.task_list = None
        # Create widgets
        self.create_label()
        self.create_list_widget()
        self.create_buttons()

        self.setLayout(self.main_layout)

    def create_label(self):
        self.quest_list_label = QtWidgets.QLabel(self)
        self.quest_list_label.setAlignment(Qt.AlignCenter)
        self.quest_list_label.setText("List of your current tasks")
        self.quest_list_label.setStyleSheet(STYLE_SHEET['quest_list_label'])
        self.quest_list_label.adjustSize()
        self.main_layout.addWidget(self.quest_list_label)

    def create_list_widget(self):
        self.quest_list = QtWidgets.QListWidget(self)
        #for task in TASKS:
            #self.quest_list.addItem(task)
        self.quest_list.setMinimumSize(250, 400)
        self.quest_list.setStyleSheet('background-color: #BDB76B; color: #B22222; font-weight: bold;')
        self.quest_list.itemClicked.connect(self.show_quest_info)
        self.main_layout.addWidget(self.quest_list)
        self.retrieve_tasks()

    def create_buttons(self):
        button_layout = QHBoxLayout()
        self.add_button = QtWidgets.QPushButton("Add task", self)
        self.add_button.setStyleSheet(STYLE_SHEET['close_button'])
        self.add_button.setFixedWidth(100)
        self.add_button.setFixedHeight(30)
        button_layout.addWidget(self.add_button)

        self.del_button = QtWidgets.QPushButton("Change details", self)
        self.del_button.setStyleSheet(STYLE_SHEET['close_button'])
        self.del_button.setFixedWidth(100)
        self.del_button.setFixedHeight(30)
        button_layout.addWidget(self.del_button)

        self.arch_button = QtWidgets.QPushButton("Archive task", self)
        self.arch_button.setStyleSheet(STYLE_SHEET['close_button'])
        self.arch_button.setFixedWidth(100)
        self.arch_button.setFixedHeight(30)
        button_layout.addWidget(self.arch_button)

        self.main_layout.addStretch(1)
        self.main_layout.addLayout(button_layout)

    def retrieve_tasks(self):
        with open('task_list.txt', 'r') as tasks:
            data = json.load(tasks)
        self.task_list = data['task list']
        for task in self.task_list:
            for key in task:
                self.quest_list.addItem(key)

    def show_quest_info(self, item):
        self.quest_info_update.emit(str(item.text()))


class QuestInfoTab(QWidget):
    def __init__(self):
        super().__init__()
        self.width = 700
        self.height = 500
        self.setFixedWidth(self.width)
        self.setFixedHeight(self.height)

        self.main_layout = QVBoxLayout()
        # Create widgets
        self.create_label()
        self.create_info_widget()

        self.setLayout(self.main_layout)

    def create_label(self):
        self.quest_details = QtWidgets.QLabel(self)
        self.quest_details.setAlignment(Qt.AlignCenter)
        self.quest_details.setText("Details of your task")
        self.quest_details.setStyleSheet(STYLE_SHEET['quest_details'])
        self.quest_details.adjustSize()

        self.main_layout.addWidget(self.quest_details)

    def create_info_widget(self):
        self.quest_text = QtWidgets.QTextBrowser(self)
        self.quest_text.append("Quest info here!")
        self.quest_text.setStyleSheet(STYLE_SHEET['quest_info'])

        self.main_layout.addWidget(self.quest_text)

    def update_quest_info(self, message):
        #self.quest_text.setText(TASKS[message])
        pass


class BottomWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.width = 700
        self.height = 50

        self.main_layout = QHBoxLayout()
        self.create_motivational_quote()
        self.create_close_button()

        self.setLayout(self.main_layout)

    def create_motivational_quote(self):
        self.mot_quote = QtWidgets.QLabel(self)
        self.mot_quote.setAlignment(Qt.AlignCenter)
        self.get_motivational_quote()
        self.mot_quote.setStyleSheet(STYLE_SHEET['mot_quote'])
        self.mot_quote.adjustSize()

        self.main_layout.addWidget(self.mot_quote)

    def create_close_button(self):
        self.close_button = QtWidgets.QPushButton("Close app", self)
        self.close_button.setStyleSheet(STYLE_SHEET['close_button'])
        self.close_button.setFixedWidth(100)
        self.close_button.setFixedHeight(30)
        self.close_button.clicked.connect(self.close_button_clicked)

        self.main_layout.addWidget(self.close_button)

    def set_layout(self):
        hbox = QHBoxLayout()
        hbox.addWidget(self.mot_quote)
        hbox.stretch(1)
        hbox.addWidget(self.close_button)
        self.setLayout(hbox)

    def get_motivational_quote(self):
        # url = "https://type.fit/api/quotes?fbclid=IwAR066CVqn2qdvUIEBui3J2r-xre3ZcaQrfKJkqJmf4Drj2FH-qgW1DgcD4c"
        # response = requests.get(url)
        # if response.status_code == 200:
        #     quote_list = response.json()
        #     chosen_quote = random.choice(quote_list)
        #     while len(chosen_quote['text']) > 90:
        #         chosen_quote = random.choice(quote_list)
        #     if chosen_quote['author'] is None:
        #         chosen_quote['author'] = 'Anonymous'
        #     self.mot_quote.setText(chosen_quote['text'] + " - " + chosen_quote['author'])
        # else:
        self.mot_quote.setText("Be better than yesterday and worse than tomorrow! - Daemiac")

    @staticmethod
    def close_button_clicked():
        with open('task_list.txt', 'w') as outfile:
            json.dump(TASKS, outfile, indent=2)
        sys.exit()


class AppController:
    def __init__(self, view, model):
        self._view = view
        self._model = model


class AppModel:
    def __init__(self):
        self.task_list = None

    def retrieve_tasks(self):
        with open('task_list.txt', 'r') as read_file:
            data = json.load(read_file)
            self.task_list = data['task list']

    def save_tasks(self):
        data = {"task list": self.task_list}
        with open('task_list.txt', 'w') as outfile:
            json.dump(data, outfile, ident=2)


def main():
    """ Main function """
    # instance of 'QApplication'
    app = QApplication([])
    # instance of the model
    model = AppModel()
    # render the view
    view = AppView()
    view.show()
    # instance of the controller
    AppController(view=view, model=model)

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
