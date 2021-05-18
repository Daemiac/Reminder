import datetime
import logging

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (
    QMainWindow,
    QDialog,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QGroupBox,
    QTabWidget
)
from PyQt5.QtCore import Qt

from app_modules import widget_styles


logger = logging.getLogger(__name__)


class AppView(QMainWindow):
    """ Class responsible for rendering view of the app """
    def __init__(self):
        super().__init__()

        # Set main window's properties
        self.title = "Reminder beta ver"
        self.x_position = 400
        self.y_position = 300
        self.width = 1200  # 1065
        self.height = 800   # 575
        self.setWindowTitle(self.title)
        self.setFixedSize(self.width, self.height)
        # self.setGeometry(self.x_position, self.y_position, self.width, self.height)
        self.setObjectName("main_window")
        self.setStyleSheet(widget_styles.app_window_stylesheet)

        # Creation of the central widget and general layout
        self.generalLayout = QVBoxLayout()
        self._centralWidget = QWidget(self)
        self.setCentralWidget(self._centralWidget)
        self._centralWidget.setLayout(self.generalLayout)

        # Create child widgets
        self.top_widget = TitleClockWidget()
        self.tab_widget = TabWidget()
        self.bottom_widget = BottomWidget()

        self.render_view()

    def render_view(self):
        """ Creates layout of child widgets """
        self.generalLayout.addWidget(self.top_widget)
        self.generalLayout.addWidget(self.tab_widget)
        self.generalLayout.addStretch(1)
        self.generalLayout.addWidget(self.bottom_widget)


class TitleClockWidget(QWidget):
    """ Renders title label and clock widget"""
    def __init__(self):
        super().__init__()
        self.width = 1000
        self.height = 100

        # creation of inner widgets
        self.title_widget = None
        self.clock_widget = None

        self.create_title_widget()
        self.create_clock_widget()

        # setting layout
        self.main_layout = QHBoxLayout()
        self.set_widgets_layout()
        self.setLayout(self.main_layout)

    def create_title_widget(self):
        self.title_widget = QtWidgets.QLabel(self)
        self.title_widget.setAlignment(Qt.AlignCenter)
        self.title_widget.setText("REMINDER - stay disciplined and productive!")
        self.title_widget.setObjectName("title_label")
        self.title_widget.setStyleSheet(widget_styles.title_label_stylesheet)

    def create_clock_widget(self):
        self.clock_widget = QtWidgets.QLabel(self)
        self.clock_widget.setAlignment(Qt.AlignCenter)
        self.clock_widget.setText("01-01-2000 Monday 00:00:00")
        self.clock_widget.setObjectName("clock")
        self.clock_widget.setStyleSheet(widget_styles.clock_stylesheet)

    def set_widgets_layout(self):
        self.main_layout.addWidget(self.title_widget)
        self.main_layout.addStretch(1)
        self.main_layout.addWidget(self.clock_widget)

    def update_clock_label(self, time):
        date = datetime.datetime.now()
        day_of_week = date.strftime("%d-%m-%Y %A")
        self.clock_widget.setText(f"{day_of_week} {time}")


class TabWidget(QWidget):
    """ Content of the app """
    def __init__(self):
        super().__init__()
        # widget's properties
        self.width = 800
        self.height = 500
        self.setObjectName("tab_window")
        self.setStyleSheet(widget_styles.tab_window_stylesheet)

        # list of widget attributes
        self.main_tab = None
        self.overview_tab = None
        self.archive_tab = None
        self.task_list_widget = None
        self.task_info_widget = None
        self.main_tab_layout = None

        # Creating tab widget and setting its tabs
        self.tabs = QTabWidget()
        self.create_main_tab()
        self.create_overview_tab()
        self.create_archive_tab()

        self.main_layout = QHBoxLayout()
        self.set_widgets_layout()

    def create_main_tab(self):
        self.main_tab = QWidget()
        self.tabs.addTab(self.main_tab, "Main page")
        # Creation of child widgets
        self.task_list_widget = TaskListWidget()
        self.task_info_widget = TaskInfoWidget()
        # Setting tabs' layout
        self.set_main_tab_layout()

    def create_overview_tab(self):
        self.overview_tab = QWidget()
        self.tabs.addTab(self.overview_tab, "Details")

    def create_archive_tab(self):
        self.archive_tab = QWidget()
        self.tabs.addTab(self.archive_tab, "Archive")

    def set_main_tab_layout(self):
        self.main_tab_layout = QHBoxLayout()
        self.main_tab_layout.addWidget(self.task_list_widget)
        self.main_tab_layout.addStretch(1)
        self.main_tab_layout.addWidget(self.task_info_widget)
        self.main_tab.setLayout(self.main_tab_layout)

    def set_overview_tab_layout(self):
        pass

    def set_archive_tab_layout(self):
        pass

    def set_widgets_layout(self):
        self.main_layout.addWidget(self.tabs)
        self.setLayout(self.main_layout)


class TaskListWidget(QWidget):
    """ Renders view of task list widget """
    def __init__(self):
        super().__init__()
        self.width = 400
        self.height = 550

        self.task_list = None

        # initializing widgets
        self.task_list_label = None
        self.task_list_widget = None
        self.add_button = None
        self.update_button = None
        self.arch_button = None
        self.buttons_layout = None

        # creation of inner widgets
        self.create_task_list_label()
        self.create_task_list_widget()
        self.create_buttons()

        self.main_layout = QVBoxLayout()
        self.set_widgets_layout()

    def create_task_list_label(self):
        """ Sets up task list label and its properties """
        self.task_list_label = QtWidgets.QLabel(self)
        self.task_list_label.setAlignment(Qt.AlignCenter)
        self.task_list_label.setText("List of your current tasks")
        self.task_list_label.setObjectName("task_list_label")
        self.task_list_label.setStyleSheet(widget_styles.task_list_label_stylesheet)
        self.task_list_label.adjustSize()

    def create_task_list_widget(self):
        """ Sets up task list widget and its properties """
        self.task_list_widget = QtWidgets.QListWidget(self)
        self.task_list_widget.setMinimumSize(250, 450)
        self.task_list_widget.setObjectName("task_list_widget")
        self.task_list_widget.setStyleSheet(widget_styles.task_list_stylesheet)

    def create_buttons(self):
        """ Sets up widget's buttons and their properties """
        self.add_button = QtWidgets.QPushButton("Add task", self)
        self.add_button.setObjectName("add_button")
        self.add_button.setStyleSheet(widget_styles.add_button_stylesheet)
        self.add_button.setFixedWidth(100)
        self.add_button.setFixedHeight(30)

        self.update_button = QtWidgets.QPushButton("Update task", self)
        self.update_button.setObjectName("update_button")
        self.update_button.setStyleSheet(widget_styles.update_button_stylesheet)
        #self.update_button.setEnabled(False)
        self.update_button.setFixedWidth(100)
        self.update_button.setFixedHeight(30)

        self.arch_button = QtWidgets.QPushButton("Archive task", self)
        self.arch_button.setObjectName("arch_button")
        self.arch_button.setStyleSheet(widget_styles.arch_button_stylesheet)
        self.arch_button.setFixedWidth(100)
        self.arch_button.setFixedHeight(30)

        self.set_buttons_layout()

    def set_buttons_layout(self):
        self.buttons_layout = QHBoxLayout()
        self.buttons_layout.addWidget(self.add_button)
        self.buttons_layout.addWidget(self.update_button)
        self.buttons_layout.addWidget(self.arch_button)

    def set_widgets_layout(self):
        self.main_layout.addWidget(self.task_list_label)
        self.main_layout.addWidget(self.task_list_widget)
        self.main_layout.addStretch(1)
        self.main_layout.addLayout(self.buttons_layout)

        self.setLayout(self.main_layout)

    def show_tasks(self, task_list):
        """ Displays all tasks on task_list_widget """
        self.task_list_widget.clear()
        for task in task_list:
            self.task_list_widget.addItem(task[0])


class TaskInfoWidget(QWidget):
    """ Renders view of task info widget """
    def __init__(self):
        super().__init__()
        self.width = 700
        self.height = 550
        self.setFixedWidth(self.width)
        self.setFixedHeight(self.height)

        self.task_details_label = None
        self.task_details_text = None
        self.deadline_label = None
        self.deadline_date = None
        self.task_deadline_group_box = None
        self.deadline_layout = None

        # Create inner widgets
        self.create_task_details_label()
        self.create_task_details_widget()
        self.create_deadline_widget()

        self.main_layout = QVBoxLayout()
        self.set_widgets_layout()

    def create_task_details_label(self):
        """ Sets up task detail widget's label and its properties """
        self.task_details_label = QtWidgets.QLabel(self)
        self.task_details_label.setAlignment(Qt.AlignCenter)
        self.task_details_label.setText("Details of your task")
        self.task_details_label.setObjectName("task_details_label")
        self.task_details_label.setStyleSheet(widget_styles.task_details_label_stylesheet)
        self.task_details_label.adjustSize()

    def create_task_details_widget(self):
        """ Sets up task detail widget and its properties """
        self.task_details_text = QtWidgets.QTextBrowser(self)
        self.task_details_text.setObjectName("task_details_text")
        self.task_details_text.append("Select a task to show its details here!")
        self.task_details_text.setStyleSheet(widget_styles.task_details_text_stylesheet)

    def create_deadline_widget(self):
        """ Sets up deadline widget and its properties """
        # creation and setting deadline_label widget
        self.deadline_label = QtWidgets.QLabel("Deadline of the task:")
        self.deadline_label.setAlignment(Qt.AlignCenter)
        self.deadline_label.setObjectName("task_deadline_label")
        self.deadline_label.setStyleSheet(widget_styles.task_deadline_label_stylesheet)

        # creation and setting deadline_date widget
        self.deadline_date = QtWidgets.QLabel("")
        self.deadline_date.setAlignment(Qt.AlignCenter)
        self.deadline_date.setObjectName("task_deadline_date")
        self.deadline_date.setStyleSheet(widget_styles.task_deadline_date_stylesheet)

        self.set_deadline_widget_layout()

    def set_deadline_widget_layout(self):
        self.deadline_layout = QHBoxLayout()
        self.deadline_layout.addWidget(self.deadline_label)
        self.deadline_layout.addWidget(self.deadline_date)

    def set_widgets_layout(self):
        self.main_layout.addWidget(self.task_details_label)
        self.main_layout.addWidget(self.task_details_text)
        self.main_layout.addLayout(self.deadline_layout)

        self.setLayout(self.main_layout)

    def update_quest_info(self, item_clicked):
        """ Method responsible for updating task detail widget's content """
        self.task_details_text.setText("Details: {}".format(item_clicked))

    def update_deadline_info(self, deadline_date):
        self.deadline_date.setText(deadline_date)


class BottomWidget(QWidget):
    """ Renders view of bottom widget """
    def __init__(self):
        super().__init__()
        self.width = 700
        self.height = 50

        self.mot_quote = None
        self.close_button = None

        self.create_motivational_quote()
        self.create_close_button()

        self.main_layout = QHBoxLayout()
        self.set_widgets_layout()

    def create_motivational_quote(self):
        """ Sets up motivational quote widget and its properties """
        self.mot_quote = QtWidgets.QLabel(self)
        self.mot_quote.setAlignment(Qt.AlignCenter)
        self.mot_quote.setObjectName("mot_quote")
        self.mot_quote.setStyleSheet(widget_styles.mot_quote_stylesheet)
        self.mot_quote.adjustSize()

    def create_close_button(self):
        """ Sets up additional app's close button and its properties """
        self.close_button = QtWidgets.QPushButton("Close app", self)
        self.close_button.setObjectName("close_button")
        self.close_button.setStyleSheet(widget_styles.close_button_stylesheet)
        self.close_button.setFixedWidth(100)
        self.close_button.setFixedHeight(30)

    def set_widgets_layout(self):
        self.main_layout.addWidget(self.mot_quote)
        self.main_layout.addWidget(self.close_button)
        self.setLayout(self.main_layout)

    def set_motivational_quote(self, quote_dic):
        """ Method responsible for updating motivational quote widget's content """
        try:
            self.mot_quote.setText(quote_dic["text"] + " - " + quote_dic["author"])

        except TypeError:
            print(type(quote_dic["text"]))
            print(type(quote_dic["author"]))


class AddDialog(QDialog):
    """ Class used to create dialog window responsible for addition or manipulation of tasks data """
    # TODO update AddDialog window view
    def __init__(self, title, mode, task_title=None, task_details=None, task_deadline=None):
        super(AddDialog, self).__init__()

        self.title = title
        self.mode = mode

        # Window properties
        self.setFixedWidth(550)
        self.setFixedHeight(550)
        self.setWindowTitle(self.title)
        self.setWindowModality(Qt.ApplicationModal)
        self.setObjectName("dialog_window")
        self.setStyleSheet(widget_styles.dialog_style_sheet)

        # Data passed through instantiation
        self.task_title_entry = task_title
        self.task_details_entry = task_details
        self.task_deadline_entry = task_deadline

        # Declaration of widgets
        self.task_title_group_box = None
        self.task_title_label = None
        self.task_title_edit = None
        self.task_title_layout = None
        self.task_details_group_box = None
        self.task_details_label = None
        self.task_details_edit = None
        self.task_details_layout = None
        self.task_deadline_group_box = None
        self.task_deadline_label = None
        self.task_deadline_edit = None
        self.task_deadline_layout = None
        self.save_button = None
        self.cancel_button = None
        self.button_layout = None

        # Creation of child widgets
        self.create_task_title_group_box()
        self.create_task_details_group_box()
        self.create_task_deadline_group_box()
        self.create_dialog_buttons()

        self.main_layout = QVBoxLayout()
        self.set_window_layout()

    def create_task_title_group_box(self):
        """ Creates group box with task title related widgets """
        self.task_title_group_box = QGroupBox()
        self.task_title_group_box.setObjectName("task_title_group_box")

        self.task_title_label = QtWidgets.QLabel("Task title")
        self.task_title_label.setObjectName("task_title_label")

        self.task_title_edit = QtWidgets.QLineEdit(self.task_title_entry)
        self.task_title_edit.setObjectName("task_title_edit")
        self.task_title_edit.setMaxLength(35)

        self.set_task_title_group_box_layout()

    def set_task_title_group_box_layout(self):
        self.task_title_layout = QVBoxLayout()
        self.task_title_layout.addWidget(self.task_title_label)
        self.task_title_layout.addWidget(self.task_title_edit)
        self.task_title_group_box.setLayout(self.task_title_layout)

    def create_task_details_group_box(self):
        """ Creates group box with task details related widgets """
        self.task_details_group_box = QGroupBox()
        self.task_details_group_box.setObjectName("task_details_group_box")

        self.task_details_label = QtWidgets.QLabel("Task details")
        self.task_details_label.setObjectName("task_details_label")

        self.task_details_edit = QtWidgets.QTextEdit(self.task_details_entry)
        self.task_details_edit.setObjectName("task_details_edit")

        self.set_task_details_group_box_layout()

    def set_task_details_group_box_layout(self):
        self.task_details_layout = QVBoxLayout()
        self.task_details_layout.addWidget(self.task_details_label)
        self.task_details_layout.addWidget(self.task_details_edit)
        self.task_details_group_box.setLayout(self.task_details_layout)

    def create_task_deadline_group_box(self):
        """ Creates group box with task details related widgets """
        self.task_deadline_group_box = QGroupBox()
        self.task_deadline_group_box.setObjectName("task_deadline_group_box")

        self.task_deadline_label = QtWidgets.QLabel("Add deadline date")
        self.task_deadline_label.setObjectName("task_deadline_label")

        self.task_deadline_edit = QtWidgets.QLineEdit("Deadline in day-month-year format")
        self.task_deadline_edit.setObjectName("task_deadline_edit")
        self.task_deadline_edit.setMaxLength(35)

        self.set_task_deadline_group_box_layout()

    def set_task_deadline_group_box_layout(self):
        self.task_deadline_layout = QVBoxLayout()
        self.task_deadline_layout.addWidget(self.task_deadline_label)
        self.task_deadline_layout.addWidget(self.task_deadline_edit)
        self.task_deadline_group_box.setLayout(self.task_deadline_layout)

    def create_dialog_buttons(self):
        """ Sets up dialog's window bottom buttons and their properties """
        self.save_button = QtWidgets.QPushButton("Save", self)
        self.save_button.setObjectName("save_button")

        self.cancel_button = QtWidgets.QPushButton("Cancel", self)
        self.cancel_button.setObjectName("cancel_button")

        self.set_dialog_buttons_layout()

    def set_dialog_buttons_layout(self):
        self.button_layout = QHBoxLayout()
        self.button_layout.addWidget(self.save_button)
        self.button_layout.addWidget(self.cancel_button)

    def set_window_layout(self):
        """ Sets layout of child widgets inside dialog window """
        self.main_layout.addWidget(self.task_title_group_box)
        self.main_layout.addWidget(self.task_details_group_box)
        self.main_layout.addWidget(self.task_deadline_group_box)
        self.main_layout.addLayout(self.button_layout)
        self.setLayout(self.main_layout)

    @classmethod
    def create_add_dialog(cls):
        """ Returns add-details type of dialog window object with given arguments """
        return AddDialog("Task addition dialog window", True, 'Write your task title here',
                         'Write your task details here')

    @classmethod
    def create_change_det_dialog(cls, task_title, task_details):
        """ Returns change-details type of dialog window object with given arguments """
        return AddDialog("Task details update dialog window", False, task_title, task_details)
