from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
import sys


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

        self.lbl1 = QtWidgets.QLabel(self)
        self.lbl1.setAlignment(Qt.AlignCenter)
        self.lbl1.setText("Details of your quest")
        self.lbl1.adjustSize()

        self.quest_text = QtWidgets.QTextBrowser(self)
        self.quest_text.append("Quest info here!")

        self.setFixedWidth(self.width)
        self.setFixedHeight(self.height)
        self.set_layout()

    def set_layout(self):
        vbox = QVBoxLayout()
        vbox.addWidget(self.lbl1)
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
        self.mot_quote.setText("Motivational quote")
        self.mot_quote.adjustSize()

        self.close_button = QtWidgets.QPushButton("Close app", self)
        self.close_button.setStyleSheet('color:red')
        # self.btn2.setGeometry(250, 300, 100, 50)
        self.close_button.clicked.connect(self.close_button_clicked)

        self.set_layout()

    def set_layout(self):
        hbox = QHBoxLayout()
        hbox.addWidget(self.mot_quote)
        hbox.stretch(1)
        hbox.addWidget(self.close_button)
        self.setLayout(hbox)

    def close_button_clicked(self):
        sys.exit()


if __name__ == '__main__':
    app = QApplication([])
    main_app = AppWindow()
    main_app.show()
    sys.exit(app.exec_())
