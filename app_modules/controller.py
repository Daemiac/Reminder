import sys

from app_modules.views import AppView, AddDialog
from app_modules.models import TaskListModel, MotivationalQuoteModel, ClockModel
from app_modules.db_handler import DatabaseHandler


class AppController:
    """ Mediates between model and view objects """
    def __init__(self, view, model):
        self._view = view
        self._model = model
        self._mot_model = MotivationalQuoteModel()
        self._clock = ClockModel()
        self._dialog = None

        self.clicked_task = None
        self.clicked_task_info = None
        self.clicked_task_deadline = None

        self.update_task_list()
        self.update_motivational_quote()
        self._connect_signals()

    def _connect_signals(self):
        """ Method responsible for connecting main windows' signals with appropriate slot methods """
        self._view.tab_widget.task_list_widget.add_button.clicked.connect(self.add_task_window)
        self._view.tab_widget.task_list_widget.update_button.clicked.connect(self.change_task_details)
        self._view.tab_widget.task_list_widget.arch_button.clicked.connect(self.delete_task)
        self._view.bottom_widget.close_button.clicked.connect(self._close_the_app)
        self._view.tab_widget.task_list_widget.task_list_widget.itemClicked.connect(self.update_task_info)

    def _connect_dialog_signals(self):
        """ Method responsible for connecting dialog window's signals with appropriate slot methods """
        self._dialog.save_button.clicked.connect(self.accept_dialog)
        self._dialog.cancel_button.clicked.connect(self.reject_dialog)

    def update_clock(self):
        self._view.top_widget.update_clock(self._clock.printable_time)

    def update_task_list(self):
        """ Updates task list widget's content with content of model's task list attribute """
        self._model.retrieve_tasks_from_db()
        self._view.tab_widget.task_list_widget.show_tasks(self._model.task_list)

    def update_motivational_quote(self):
        """ Updates motivational quote widget's content with appropriate models' attribute """
        chosen_quote = self._mot_model.quote
        self._view.bottom_widget.set_motivational_quote(chosen_quote)

    @staticmethod
    def obtain_task_list_item(item_clicked):
        """ Returns clicked list widget's element as a string """
        item_clicked = str(item_clicked.text())
        return item_clicked

    def update_task_info(self, item_clicked):
        """ Updates task info widget's content """
        self.clicked_task = self.obtain_task_list_item(item_clicked)
        # searching through list of tuples
        clicked_task_tuple = next(tpl for i, tpl in enumerate(self._model.task_list) if self.clicked_task in tpl)
        self.clicked_task_info = clicked_task_tuple[1]
        self.clicked_task_deadline = clicked_task_tuple[2]
        self._view.tab_widget.task_info_widget.update_quest_info(self.clicked_task_info)
        self._view.tab_widget.task_info_widget.update_deadline_info(self.clicked_task_deadline)

    def add_task_window(self):
        """ Creates a dialog window which can be used to add a task """
        self._dialog = AddDialog.create_add_dialog()
        self._connect_dialog_signals()
        self._dialog.show()

    def change_task_details(self):
        """ Creates a dialog window which can be used to change details of the chosen task"""
        self._dialog = AddDialog.create_change_det_dialog(task_title=self.clicked_task,
                                                          task_details=self.clicked_task_info)
        self._connect_dialog_signals()
        self._dialog.show()

    def accept_dialog(self):
        """ Saves dialog window's entries to model's attribute, updates the view and closes dialog window """
        new_task_name = self._dialog.task_title_edit.text()
        new_task_details = self._dialog.task_details_edit.toPlainText()
        new_task_deadline = self._dialog.task_deadline_edit.text()
        if self._dialog.mode:
            self._model.add_task_to_db(new_task_name, new_task_details, new_task_deadline)
            self.update_task_list()
            self._dialog.close()
            print("Dialog form has been accepted. The task has been added. Closing the dialog window...")
        else:
            self._model.update_task_data(self.clicked_task, new_task_name, new_task_details, new_task_deadline)
            self.update_task_list()
            self._dialog.close()
            print("Dialog form has been accepted. Chosen task details has been changed. Closing the dialog window...")

    def reject_dialog(self):
        """ Closes dialog window without applying changes """
        self._dialog.close()
        print("Dialog form has been rejected. Closing the dialog window...")

    def delete_task(self):
        """ Method responsible for deleting a task from model's task list attribute and updating
            task list widget's view """
        item_to_delete = self.clicked_task
        self._model.archive_task(item_to_delete)
        self.update_task_list()
        self._view.tab_widget.task_info_widget.update_quest_info(f"The '{item_to_delete}' task has been deleted!")

    @staticmethod
    def _close_the_app():
        """ Saves changes into external file and closes the app """
        # with DatabaseHandler() as db:
        #     db.drop_table('archive')
        #     db.drop_table('tasks')
        print("Closing the app...")
        sys.exit()
