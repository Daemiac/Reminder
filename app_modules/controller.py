import sys

from app_modules.views import AppView, AddDialog
from app_modules.models import TaskListModel, MotivationalQuoteModel


class AppController:
    """ Mediates between model and view objects """
    def __init__(self, view, model):
        self._view = view
        self._model = model
        self._mot_model = MotivationalQuoteModel()
        self._dialog = None

        self.clicked_task = None
        self.clicked_task_info = None

        self.update_task_list()
        self.update_motivational_quote()
        self._connect_signals()

    def _connect_signals(self):
        """ Method responsible for connecting main windows' signals with appropriate slot methods """
        self._view.first_widget.add_button.clicked.connect(self.add_task_window)
        self._view.first_widget.update_button.clicked.connect(self.change_task_details)
        self._view.first_widget.arch_button.clicked.connect(self.delete_task)
        self._view.third_widget.close_button.clicked.connect(self._close_the_app)
        self._view.first_widget.task_list_widget.itemClicked.connect(self.update_task_info)

    def _connect_dialog_signals(self):
        """ Method responsible for connecting dialog window's signals with appropriate slot methods """
        self._dialog.save_button.clicked.connect(self.accept_dialog)
        self._dialog.cancel_button.clicked.connect(self.reject_dialog)

    def _close_the_app(self):
        """ Saves changes into external file and closes the app """
        # self._model.save_tasks_to_db()
        # self._model.save_tasks()
        print("Closing the app...")
        sys.exit()

    def update_task_list(self):
        """ Updates task list widget's content with content of model's task list attribute """
        self._view.first_widget.show_tasks(self._model.task_list)

    def update_motivational_quote(self):
        """ Updates motivational quote widget's content with appropriate models' attribute """
        chosen_quote = self._mot_model.quote
        self._view.third_widget.set_motivational_quote(chosen_quote)

    @staticmethod
    def obtain_task_list_item(item_clicked):
        """ Returns clicked list widget's element as a string """
        item_clicked = str(item_clicked.text())
        return item_clicked

    def update_task_info(self, item_clicked):
        """ Updates task info widget's content """
        self.clicked_task = self.obtain_task_list_item(item_clicked)
        # searching through list of dictionaries
        task_det_dic = next(d for i, d in enumerate(self._model.task_list) if self.clicked_task in d)
        self.clicked_task_info = task_det_dic[1]
        self._view.second_widget.update_quest_info(self.clicked_task_info)

    def add_task_window(self):
        """ Creates a dialog window which can be used to add a task """
        self._dialog = AddDialog.create_add_dialog()
        self._connect_dialog_signals()
        self._dialog.show()

    def change_task_details(self):
        """ Creates a dialog window which can be used to change details of the chosen task"""
        self._dialog = AddDialog.create_change_det_dialog(label1=self.clicked_task, label2=self.clicked_task_info)
        self._connect_dialog_signals()
        self._dialog.show()

    def accept_dialog(self):
        """ Saves dialog window's entries to model's attribute, updates the view and closes dialog window """
        key = self._dialog.task_title_edit.text()
        value = self._dialog.task_details_edit.toPlainText()
        if self._dialog.mode:
            self._model.add_task_to_list(key, value)
            self._model.add_task_to_db(key, value)
            self.update_task_list()
            self._dialog.close()
            print("Dialog form has been accepted. The task has been added. Closing the dialog window...")
        else:
            self._model.update_task_details(self.clicked_task, self.clicked_task_info, key, value)
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
        self._model.delete_task_from_list(item_to_delete)
        self._model.delete_task_from_db(item_to_delete)
        self.update_task_list()
        self._view.second_widget.update_quest_info("The task has been deleted!")
