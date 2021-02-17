from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
import sys


class AppWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.title = "Reminder alpha ver"
        self.x_position = 600
        self.y_position = 400
        self.width = 600
        self.height = 400
        self.task_list = ["My first task", "My second task", "My third task"]
        self.init_ui()

    def init_ui(self):

        """initialize labels"""
        self.lbl1 = QtWidgets.QLabel(self)
        self.lbl1.setAlignment(Qt.AlignCenter)
        self.lbl1.setText("List of your current tasks")
        self.lbl1.adjustSize()
        #self.lbl1.move(180, 120)

        """initialize text field"""
        #self.text1 = QtWidgets.QLineEdit(self)
        #self.text1.setGeometry(250, 150, 100, 50)
        #self.text1.setAlignment(Qt.AlignCenter)

        """ initialize list widget"""
        self.quest_list = QtWidgets.QListWidget(self)
        for task in self.task_list:
            self.quest_list.addItem(task)
        self.quest_list.adjustSize()

        """ initialize buttons"""
        self.btn1 = QtWidgets.QPushButton("Greet user", self)
        # self.btn1.setGeometry(250, 50, 100, 50)
        self.btn1.clicked.connect(self.btn1_clicked)

        self.btn2 = QtWidgets.QPushButton("Exit app", self)
        self.btn2.setStyleSheet('color:red')
        # self.btn2.setGeometry(250, 300, 100, 50)
        self.btn2.clicked.connect(self.btn2_clicked)

        """ layout objects """
        vbox = QVBoxLayout()
        hbox = QHBoxLayout()
        vbox.addWidget(self.lbl1)
        vbox.addWidget(self.quest_list)
        vbox.addStretch(1)
        hbox.addWidget(self.btn1)
        hbox.addStretch(1)
        hbox.addWidget(self.btn2)
        vbox.addLayout(hbox)
        self.setLayout(vbox)

        self.setWindowTitle(self.title)
        self.setGeometry(self.x_position, self.y_position, self.width, self.height)
        # self.setWindowIcon(QIcon('python.png'))

    def btn1_clicked(self):
        self.text1.setText("Hello user!")

    def btn2_clicked(self):
        sys.exit()


if __name__ == '__main__':
    app = QApplication([])
    main_app = AppWindow()
    main_app.show()
    sys.exit(app.exec_())
