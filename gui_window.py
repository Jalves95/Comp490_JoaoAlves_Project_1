from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, \
    QListWidget, QListWidgetItem
from PySide6.QtGui import QCloseEvent
import second_gui_window
import user_record_gui
import database_functions


class GuiWindow(QWidget):
    def __init__(self, data_to_show):
        super().__init__()
        self.list_control = None
        self.data = data_to_show
        self.setup()
        self.data_window = None

    def setup(self):
        self.setGeometry(25, 50, 315, 500)

        btn_update = QPushButton('Update Wufoo Data', self)
        btn_update.clicked.connect(self.update_gui_data)
        btn_update.resize(btn_update.sizeHint())
        btn_update.move(10, 465)

        btn_quit = QPushButton('Quit', self)
        btn_quit.clicked.connect(QApplication.instance().quit)
        btn_quit.resize(btn_quit.sizeHint())
        btn_quit.move(230, 465)

        display_list = QListWidget(self)
        self.list_control = display_list
        self.put_data_in_list(self.data)
        display_list.resize(315, 450)
        display_list.currentItemChanged.connect(self.demo_list_item_selected)

        btn_claim = QPushButton('Claim Entry', self)
        btn_claim.clicked.connect(self.demo_user_record)
        btn_claim.resize(btn_claim.sizeHint())
        btn_claim.move(140, 465)

        self.show()

    def put_data_in_list(self, data: list[dict]):
        """ Provided from Dr. Santore's GUI DEMO
            Modified for my Project 1 Sprint 3 """

        for item in data:
            display_text = f"{item['Entry']}\t{item['Prefix']}\t{item['First_Name']}\t{item['Last_Name']}"
            list_item = QListWidgetItem(display_text, listview=self.list_control)
            list_item.setData(1, item)  # lets put the dictionary for later use

    def find_full_data_record(self, entry: str):
        """ Provided from Dr. Santore's GUI DEMO
            Modified for my Project 1 Sprint 3 """

        for entry_record in self.data:
            if entry_record["Entry"] == entry:
                return entry_record

    def demo_list_item_selected(self, current: QListWidgetItem, previous: QListWidgetItem):
        """ Provided from Dr. Santore's GUI DEMO
            Modified for my Project 1 Sprint 3
            Allows the user to select an entry to claim, showing another GUI when prompt"""

        selected_data = current.data(0)  # the data function has a 'role' choose 0 unless you extended QListWidgetItem
        entry = selected_data.split("\t")[0]  # split on tab and take the first resulting entry
        full_record = self.find_full_data_record(entry)
        # print(full_record)
        self.data_window = second_gui_window.GuiWindow2(full_record)
        self.data_window.show()

    def demo_user_record(self, event: QCloseEvent):
        """ Provided from Dr. Santore's GUI DEMO
            Modified for my Project 1 Sprint 3 """

        reply = QMessageBox.question(self, 'Message', 'You want to claim this entry?',
                                     QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            full_record = self.find_full_data_record(str(0))
            print(full_record)
            self.data_window = user_record_gui.UserGui(full_record)
            self.data_window.show()
        else:
            pass

    def update_gui_data(self, event: QCloseEvent):
        """ Function to update the GUI window with the wufoo data"""

        reply = QMessageBox.question(self, 'Message', 'You want to update the data?',
                                     QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            database_functions.create_wufoo_db()
        else:
            pass

    def closeEvent(self, event: QCloseEvent):
        """ Function to allow the user to quit the GUI when selected """
        reply = QMessageBox.question(self, 'Message', 'Are you sure you want to quit?',
                                     QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
