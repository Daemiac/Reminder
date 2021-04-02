from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (
    QMainWindow,
    QDialog,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QGroupBox
)
from PyQt5.QtCore import Qt

from Reminder import widget_styles


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
        self.setFixedSize(self.width, self.height)
        # self.setGeometry(self.x_position, self.y_position, self.width, self.height)
        self.setObjectName("app_window")
        self.setStyleSheet(widget_styles.app_window_stylesheet)

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

        # initializing widgets
        self.task_list_label = None
        self.task_list_widget = None
        self.add_button = None
        self.update_button = None
        self.arch_button = None

        # create inner widgets
        self.create_task_list_label()
        self.create_task_list_widget()
        self.create_buttons()

        self.setLayout(self.main_layout)

    def create_task_list_label(self):
        """ Sets up task list label and its properties """
        self.task_list_label = QtWidgets.QLabel(self)
        self.task_list_label.setAlignment(Qt.AlignCenter)
        self.task_list_label.setText("List of your current tasks")
        self.task_list_label.setObjectName("task_list_label")
        self.task_list_label.setStyleSheet(widget_styles.task_list_label_stylesheet)
        self.task_list_label.adjustSize()
        self.main_layout.addWidget(self.task_list_label)

    def create_task_list_widget(self):
        """ Sets up task list widget and its properties """
        self.task_list_widget = QtWidgets.QListWidget(self)
        self.task_list_widget.setMinimumSize(250, 400)
        self.task_list_widget.setObjectName("task_list_widget")
        self.task_list_widget.setStyleSheet(widget_styles.task_list_stylesheet)
        self.main_layout.addWidget(self.task_list_widget)

    def create_buttons(self):
        """ Sets up widget's buttons and their properties """
        button_layout = QHBoxLayout()
        self.add_button = QtWidgets.QPushButton("Add task", self)
        self.add_button.setObjectName("add_button")
        self.add_button.setStyleSheet(widget_styles.add_button_stylesheet)
        self.add_button.setFixedWidth(100)
        self.add_button.setFixedHeight(30)
        button_layout.addWidget(self.add_button)

        self.update_button = QtWidgets.QPushButton("Update task", self)
        self.update_button.setObjectName("update_button")
        self.update_button.setStyleSheet(widget_styles.update_button_stylesheet)
        self.update_button.setFixedWidth(100)
        self.update_button.setFixedHeight(30)
        button_layout.addWidget(self.update_button)

        self.arch_button = QtWidgets.QPushButton("Archive task", self)
        self.arch_button.setObjectName("arch_button")
        self.arch_button.setStyleSheet(widget_styles.arch_button_stylesheet)
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

        self.task_details_label = None
        self.task_details_text = None

        # Create inner widgets
        self.create_task_details_label()
        self.create_task_details_widget()

        self.setLayout(self.main_layout)

    def create_task_details_label(self):
        """ Sets up task detail widget's label and its properties """
        self.task_details_label = QtWidgets.QLabel(self)
        self.task_details_label.setAlignment(Qt.AlignCenter)
        self.task_details_label.setText("Details of your task")
        self.task_details_label.setObjectName("task_details_label")
        self.task_details_label.setStyleSheet(widget_styles.task_details_label_stylesheet)
        self.task_details_label.adjustSize()

        self.main_layout.addWidget(self.task_details_label)

    def create_task_details_widget(self):
        """ Sets up task detail widget and its properties """
        self.task_details_text = QtWidgets.QTextBrowser(self)
        self.task_details_text.setObjectName("task_details_text")
        self.task_details_text.append("Select a task to show its details here!")
        self.task_details_text.setStyleSheet(widget_styles.task_details_text_stylesheet)

        self.main_layout.addWidget(self.task_details_text)

    def update_quest_info(self, item_clicked):
        """ Method responsible for updating task detail widget's content """
        self.task_details_text.setText("Details: {}".format(item_clicked))


class BottomWidget(QWidget):
    """ Renders view of bottom widget """
    def __init__(self):
        super().__init__()
        self.width = 700
        self.height = 50

        self.mot_quote = None
        self.close_button = None

        self.main_layout = QHBoxLayout()
        self.create_motivational_quote()
        self.create_close_button()

        self.setLayout(self.main_layout)

    def create_motivational_quote(self):
        """ Sets up motivational quote widget and its properties """
        self.mot_quote = QtWidgets.QLabel(self)
        self.mot_quote.setAlignment(Qt.AlignCenter)
        self.mot_quote.setObjectName("mot_quote")
        self.mot_quote.setStyleSheet(widget_styles.mot_quote_stylesheet)
        self.mot_quote.adjustSize()

        self.main_layout.addWidget(self.mot_quote)

    def create_close_button(self):
        """ Sets up additional app's close button and its properties """
        self.close_button = QtWidgets.QPushButton("Close app", self)
        self.close_button.setObjectName("close_button")
        self.close_button.setStyleSheet(widget_styles.close_button_stylesheet)
        self.close_button.setFixedWidth(100)
        self.close_button.setFixedHeight(30)

        self.main_layout.addWidget(self.close_button)

    def set_motivational_quote(self, quote_dic):
        """ Method responsible for updating motivational quote widget's content """
        self.mot_quote.setText(quote_dic["text"] + " - " + quote_dic["author"])


class AddDialog(QDialog):
    """ Class used to create dialog window widgets """
    def __init__(self, label1='Write your task title here', label2='Write your task details here', add=False):
        super(AddDialog, self).__init__()
        self.text1 = label1
        self.text2 = label2
        self.add_mode = add
        self.add_title = "Task addition dialog window"
        self.change_title = "Task details update dialog window"
        self.title = self.add_title if self.add_mode is True else self.change_title

        self.setFixedWidth(500)
        self.setFixedHeight(400)
        self.setWindowTitle(self.title)
        self.setWindowModality(Qt.ApplicationModal)
        self.setObjectName("dialog_window")

        self.task_title_group_box = None
        self.task_title_label = None
        self.task_title_edit = None
        self.task_details_group_box = None
        self.task_details_label = None
        self.task_details_edit = None
        self.save_button = None
        self.cancel_button = None

        self.main_layout = QVBoxLayout()
        self.create_task_title_group_box()
        self.create_task_details_group_box()
        self.create_dialog_buttons()
        self.setLayout(self.main_layout)

        self.setStyleSheet(widget_styles.dialog_style_sheet)

    def create_task_title_group_box(self):
        """ Creates group box with task title related widgets """
        self.task_title_group_box = QGroupBox()
        self.task_title_group_box.setObjectName("task_title_group_box")

        self.task_title_label = QtWidgets.QLabel("Task title")
        self.task_title_label.setObjectName("task_title_label")

        self.task_title_edit = QtWidgets.QLineEdit(self.text1)
        self.task_title_edit.setObjectName("task_title_edit")
        self.task_title_edit.setMaxLength(35)

        task_title_layout = QVBoxLayout()
        task_title_layout.addWidget(self.task_title_label)
        task_title_layout.addWidget(self.task_title_edit)
        self.task_title_group_box.setLayout(task_title_layout)

        self.main_layout.addWidget(self.task_title_group_box)

    def create_task_details_group_box(self):
        """ Creates group box with task details related widgets """
        self.task_details_group_box = QGroupBox()
        self.task_details_group_box.setObjectName("task_details_group_box")

        self.task_details_label = QtWidgets.QLabel("Task details")
        self.task_details_label.setObjectName("task_details_label")

        self.task_details_edit = QtWidgets.QTextEdit(self.text2)
        self.task_details_edit.setObjectName("task_details_edit")

        task_details_layout = QVBoxLayout()
        task_details_layout.addWidget(self.task_details_label)
        task_details_layout.addWidget(self.task_details_edit)
        self.task_details_group_box.setLayout(task_details_layout)

        self.main_layout.addWidget(self.task_details_group_box)

    def create_dialog_buttons(self):
        """ Sets up dialog's window bottom buttons and their properties """
        button_layout = QHBoxLayout()

        self.save_button = QtWidgets.QPushButton("Save", self)
        self.save_button.setObjectName("save_button")
        button_layout.addWidget(self.save_button)

        self.cancel_button = QtWidgets.QPushButton("Cancel", self)
        self.cancel_button.setObjectName("cancel_button")
        button_layout.addWidget(self.cancel_button)

        self.main_layout.addLayout(button_layout)
