from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QFont
import sys
import requests
import random

STYLE_SHEET = {"quest_list_label": "font-weight: bold; font-family: Verdana; font-style: italic; font-size: 10pt",
               'mot_quote': 'font-weight: bold; font-family: Courier; font-size: 8pt; border: 1px solid black;'}


class AppWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.title = "Reminder alpha ver"
        self.x_position = 400
        self.y_position = 300
        self.width = 1100
        self.height = 600

        self.first_widget = QuestListTab()
        self.second_widget = QuestInfoTab()
        self.third_widget = BottomWidget()

        self.init_ui()

    def init_ui(self):

        """ layout objects """
        vbox = QVBoxLayout()
        hbox = QHBoxLayout()
        hbox.addWidget(self.first_widget)
        hbox.stretch(1)
        hbox.addWidget(self.second_widget)
        vbox.addLayout(hbox)
        vbox.addStretch(1)
        vbox.addWidget(self.third_widget)
        self.setLayout(vbox)

        self.setWindowTitle(self.title)
        self.setGeometry(self.x_position, self.y_position, self.width, self.height)
        # self.setWindowIcon(QIcon('python.png'))


class QuestListTab(QWidget):
    def __init__(self):
        super().__init__()
        self.width = 400
        self.height = 500

        self.task_list = ["My first task", "My second task", "My third task"]

        self.quest_list_label = QtWidgets.QLabel(self)
        self.quest_list_label.setAlignment(Qt.AlignCenter)
        self.quest_list_label.setText("List of your current tasks")
        self.quest_list_label.setStyleSheet(STYLE_SHEET['quest_list_label'])
        self.quest_list_label.adjustSize()

        self.quest_list = QtWidgets.QListWidget(self)
        for task in self.task_list:
            self.quest_list.addItem(task)
        self.quest_list.adjustSize()

        self.set_layout()

    def set_layout(self):
        vbox = QVBoxLayout()
        vbox.addWidget(self.quest_list_label)
        vbox.stretch(1)
        vbox.addWidget(self.quest_list)
        self.setLayout(vbox)


class QuestInfoTab(QWidget):
    def __init__(self):
        super().__init__()
        self.width = 700
        self.height = 500

        self.quest_details = QtWidgets.QLabel(self)
        self.quest_details.setAlignment(Qt.AlignCenter)
        self.quest_details.setText("Details of your task")
        self.quest_details.setFont(QFont('Verdana', 10))
        self.quest_details.adjustSize()

        self.quest_text = QtWidgets.QTextBrowser(self)
        self.quest_text.append("Quest info here!")

        self.setFixedWidth(self.width)
        self.setFixedHeight(self.height)
        self.set_layout()

    def set_layout(self):
        vbox = QVBoxLayout()
        vbox.addWidget(self.quest_details)
        vbox.stretch(1)
        vbox.addWidget(self.quest_text)
        self.setLayout(vbox)


class BottomWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.width = 700
        self.height = 50

        self.mot_quote = QtWidgets.QLabel(self)
        self.mot_quote.setAlignment(Qt.AlignCenter)
        self.get_motivational_quote()
        self.mot_quote.setStyleSheet(STYLE_SHEET['mot_quote'])
        self.mot_quote.adjustSize()

        self.close_button = QtWidgets.QPushButton("Close app", self)
        self.close_button.setStyleSheet('font-weight: bold; color:red')
        self.close_button.setFixedWidth(100)
        self.close_button.setFixedHeight(30)
        self.close_button.clicked.connect(self.close_button_clicked)

        self.set_layout()

    def set_layout(self):
        hbox = QHBoxLayout()
        hbox.addWidget(self.mot_quote)
        #hbox.stretch(1)
        hbox.addWidget(self.close_button)
        self.setLayout(hbox)

    def get_motivational_quote(self):
        url = "https://type.fit/api/quotes?fbclid=IwAR066CVqn2qdvUIEBui3J2r-xre3ZcaQrfKJkqJmf4Drj2FH-qgW1DgcD4c"
        response = requests.get(url)
        if response.status_code == 200:
            quote_list = response.json()
            chosen_quote = random.choice(quote_list)
            self.mot_quote.setText(chosen_quote['text'] + " - " + chosen_quote['author'])
        else:
            self.mot_quote.setText("Be better than yesterday and worse than tomorrow! - Daemiac")

    @staticmethod
    def close_button_clicked():
        sys.exit()


if __name__ == '__main__':
    app = QApplication([])
    main_app = AppWindow()
    main_app.show()
    sys.exit(app.exec_())
