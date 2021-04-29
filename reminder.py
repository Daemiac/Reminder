#!/usr/bin/env python3

import sys

from PyQt5.QtWidgets import QApplication

from app_modules.controller import AppController, TaskListModel, AppView


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
