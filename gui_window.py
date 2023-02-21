import sys
import PySide6
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, \
    QListWidget, QLineEdit, QLabel, QCheckBox, QListWidgetItem
from PySide6.QtGui import QCloseEvent

import getData


class GuiWindow(QWidget):
    def __init__(self, data_to_show):
        super().__init__()
        self.list_control = None
        self.list_control2 = None
        self.data = data_to_show
        self.setup()
        self.data_window = None

    def setup(self):
        self.setGeometry(25, 50, 790, 650)
        self.setWindowTitle('Wufoo Data')

        btn_quit = QPushButton('Quit', self)
        btn_quit.clicked.connect(QApplication.instance().quit)
        btn_quit.resize(btn_quit.sizeHint())
        btn_quit.move(575, 575)

        display_list = QListWidget(self)
        self.list_control = display_list
        self.put_data_in_list(self.data)
        display_list.resize(300, 600)
        # display_list.currentItemChanged.connect(self.demo_list_item_selected)

        label = QLabel("Prefix:", self)
        label.move(310, 0)
        prefix_display = QLineEdit(self)
        prefix_display.move(375, 0)

        label = QLabel("First Name:", self)
        label.move(310, 50)
        first_name_display = QLineEdit(self)
        first_name_display.move(375, 50)

        label = QLabel("Last Name:", self)
        label.move(310, 100)
        title_display = QLineEdit(self)
        title_display.move(375, 100)

        label = QLabel("Phone Number:", self)
        label.move(310, 150)
        title_display = QLineEdit(self)
        title_display.move(400, 150)

        label = QLabel("Title:", self)
        label.move(520, 0)
        org_display = QLineEdit(self)
        org_display.move(600, 0)

        label = QLabel("Org Name:", self)
        label.move(520, 50)
        email_display = QLineEdit(self)
        email_display.move(600, 50)

        label = QLabel("Org Website:", self)
        label.move(520, 100)
        last_name_display = QLineEdit(self)
        last_name_display.move(600, 100)

        label = QLabel("Email:", self)
        label.move(550, 150)
        last_name_display = QLineEdit(self)
        last_name_display.move(600, 150)

        checkbox = QCheckBox("Course_Project", self)
        checkbox.move(310, 200)
        checkbox = QCheckBox("Guest Speaker", self)
        checkbox.move(310, 230)
        checkbox = QCheckBox("Site Visit", self)
        checkbox.move(310, 260)
        checkbox = QCheckBox("Job Shadow", self)
        checkbox.move(310, 290)
        checkbox = QCheckBox("Internship", self)
        checkbox.move(310, 320)
        checkbox = QCheckBox("Career Panel", self)
        checkbox.move(310, 350)
        checkbox = QCheckBox("Networking Event", self)
        checkbox.move(310, 380)
        checkbox = QCheckBox("Summer 2022 (June 2022- August 2022)", self)
        checkbox.move(520, 200)
        checkbox = QCheckBox("Fall 2022 (September 2022- December 2022)", self)
        checkbox.move(520, 230)
        checkbox = QCheckBox("Spring 2023 (January 2023- April 2023)", self)
        checkbox.move(520, 260)
        checkbox = QCheckBox("Summer 2023 (June 2023- August 2023)", self)
        checkbox.move(520, 290)
        checkbox = QCheckBox("Other", self)
        checkbox.move(520, 320)
        # checkbox = QCheckBox("Participation", self)
        # checkbox.move(520, 380)

        label = QLabel("Participation:", self)
        label.move(520, 380)
        prefix_display = QLineEdit(self)
        prefix_display.move(600, 380)

        self.show()

    # def put_data_in_list(self, data: list[dict]):
    #     for item in data:
    #         display_text = f"{item[0]}"
    #         list_item = QListWidgetItem(display_text, listview=self.list_control)
    def put_data_in_list(self, data: list[dict]):
        for item in data:
            display_text = f"{item['Entry']}\t{item['Prefix']}\t{item['First_Name']}\t{item['Last_Name']}"
            list_item = QListWidgetItem(display_text, listview=self.list_control)

    # def find_full_data_record(self, stateName:str):
    #     for state_record in self.data:
    #         if state_record["state_name"] == stateName:
    #             return state_record

    # def demo_list_item_selected(self, current:QListWidgetItem, previous:QListWidgetItem):
    #     selected_data = current.data(0)  # the data function has a 'role' choose 0 unless you extended QListWidgetItem
    #     state_name = selected_data.split("\t")[0]  # split on tab and take the first resulting entry
    #     # full_record = self.find_full_data_record(state_name)
    #     # print(full_record)
    #     # self.data_window = GuiWindow(full_record)
    #     self.data_window.show()

    def closeEvent(self, event: QCloseEvent):
        reply = QMessageBox.question(self, 'Message', 'Are you sure you want to quit?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


# def run():
#     app = PySide6.QtWidgets.QApplication(sys.argv)
#     my_window = GuiWindow(getData.safe_get_request())
#     sys.exit(app.exec())

#
# if __name__ == '__main__':
#     run()
