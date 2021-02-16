from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon
import sys


class AppWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = "Reminder alpha ver"
        self.x_position = 600
        self.y_position = 400
        self.width = 600
        self.height = 400
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.x_position, self.y_position, self.width, self.height)
        #self.setWindowIcon(QIcon('python.png'))

        """ initialize buttons"""
        btn1 = QtWidgets.QPushButton("Greet user", self)
        btn1.setGeometry(250, 50, 100, 50)
        btn1.clicked.connect(self.btn1_clicked)
        btn2 = QtWidgets.QPushButton("Exit app", self)
        btn2.setStyleSheet('color:red')
        btn2.setGeometry(250, 300, 100, 50)
        btn2.clicked.connect(self.btn2_clicked)

        """initialize labels"""
        lbl1 = QtWidgets.QLabel(self)
        lbl1.setText("There's nothing interesting here")
        lbl1.adjustSize()
        lbl1.move(200, 120)

    def btn1_clicked(self):
        print("Hello user!")

    def btn2_clicked(self):
        sys.exit()


if __name__ == '__main__':
    app = QApplication([])
    main_app = AppWindow()
    main_app.show()
    sys.exit(app.exec_())
