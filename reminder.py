#!/usr/bin/env python3

import sys
import logging
import logging.config

from PyQt5.QtWidgets import QApplication

from app_modules.controller import AppController, TaskListModel, AppView


def main():
    # instance of 'QApplication'
    app = QApplication([])
    # instance of the model
    model = TaskListModel()
    # render the view
    view = AppView()
    view.show()
    # instance of the controller
    ctrl = AppController(view=view, model=model)
    logger.info("Started a reminder app")
    sys.exit(app.exec_())


if __name__ == '__main__':
    # setting logger's config
    logging.config.fileConfig('data/logging.conf', disable_existing_loggers=False)
    # setting up logger
    logger = logging.getLogger(__name__)

    main()
