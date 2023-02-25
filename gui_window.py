from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, \
    QListWidget, QLineEdit, QLabel, QCheckBox, QListWidgetItem
from PySide6.QtGui import QCloseEvent
import second_gui_window


class GuiWindow(QWidget):
    def __init__(self, data_to_show):
        super().__init__()
        self.list_control = None
        self.data = data_to_show
        self.setup()
        self.data_window = None

    def setup(self):
        self.setWindowTitle('Wufoo Data')

        display_list = QListWidget(self)
        self.list_control = display_list
        self.put_data_in_list(self.data)
        display_list.resize(300, 450)
        display_list.currentItemChanged.connect(self.demo_list_item_selected)
        self.setGeometry(25, 50, 300, 500)

        btn_quit = QPushButton('Quit', self)
        btn_quit.clicked.connect(QApplication.instance().quit)
        btn_quit.resize(btn_quit.sizeHint())
        btn_quit.move(115, 465)

        self.show()

    def put_data_in_list(self, data: list[dict]):
        """ Provided from Dr. Santore's GUI DEMO
            Modified for my Project 1 Sprint 3 """

        for item in data:
            display_text = f"{item['Entry']}\t{item['Prefix']}\t{item['First_Name']}\t{item['Last_Name']}"
            list_item = QListWidgetItem(display_text, listview=self.list_control)

    def find_full_data_record(self, entry: str):
        """ Provided from Dr. Santore's GUI DEMO
            Modified for my Project 1 Sprint 3 """

        for entry_record in self.data:
            if entry_record["Entry"] == entry:
                return entry_record

    def demo_list_item_selected(self, current: QListWidgetItem, previous: QListWidgetItem):
        """ Provided from Dr. Santore's GUI DEMO
            Modified for my Project 1 Sprint 3 """

        selected_data = current.data(0)  # the data function has a 'role' choose 0 unless you extended QListWidgetItem
        entry = selected_data.split("\t")[0]  # split on tab and take the first resulting entry
        full_record = self.find_full_data_record(entry)
        # print(full_record)
        self.data_window = second_gui_window.GuiWindow2(full_record)
        self.data_window.show()

    def closeEvent(self, event: QCloseEvent):
        reply = QMessageBox.question(self, 'Message', 'Are you sure you want to quit?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
