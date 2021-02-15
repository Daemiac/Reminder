from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(800, 400, 400, 300)
    win.setWindowTitle("Reminder alpha")

    label = QtWidgets.QLabel(win)
    label.resize(250, 50)
    label.setText("I have much to learn and even more to do!")
    label.move(80, 50)

    win.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    window()
