#!/usr/bin/env python3

import sys
import logging

from PyQt5.QtWidgets import QApplication

from app_modules.controller import AppController, TaskListModel, AppView


def main():

    logging.basicConfig(format='%(asctime)s || %(levelname)s || %(message)s', filename='data/reminder.log',
                        filemode='w', level=logging.DEBUG, datefmt='%d/%m/%Y %I:%M:%S %p')

    # instance of 'QApplication'
    app = QApplication([])
    # instance of the model
    model = TaskListModel()
    # render the view
    view = AppView()
    view.show()
    # instance of the controller
    ctrl = AppController(view=view, model=model)
    logging.info("Started a reminder app")
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
