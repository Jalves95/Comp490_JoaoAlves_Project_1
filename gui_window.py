import sys
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QListWidget, QLineEdit, QLabel, QCheckBox
from PySide6.QtGui import QCloseEvent


class GuiWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.list_control = None
        self.list_control2 = None

        self.setup()

    def setup(self):
        self.setGeometry(25, 50, 750, 700)
        self.setWindowTitle('Wufoo Data')

        btn_quit = QPushButton('Quit', self)
        btn_quit.clicked.connect(QApplication.instance().quit)
        btn_quit.resize(btn_quit.sizeHint())
        btn_quit.move(630, 650)

        display_list = QListWidget(self)
        self.list_control = display_list
        display_list.resize(300, 600)

        label = QLabel("Prefix:", self)
        label.move(310, 0)
        prefix_display = QLineEdit(self)
        prefix_display.move(375, 0)

        label = QLabel("First_Name:", self)
        label.move(310, 50)
        first_name_display = QLineEdit(self)
        first_name_display.move(375, 50)

        label = QLabel("Last_Name:", self)
        label.move(310, 100)
        title_display = QLineEdit(self)
        title_display.move(375, 100)

        label = QLabel("Phone_Number:", self)
        label.move(310, 150)
        title_display = QLineEdit(self)
        title_display.move(400, 150)

        label = QLabel("Title:", self)
        label.move(520, 0)
        org_display = QLineEdit(self)
        org_display.move(600, 0)

        label = QLabel("Org_Name:", self)
        label.move(520, 50)
        email_display = QLineEdit(self)
        email_display.move(600, 50)

        label = QLabel("Org_Website:", self)
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

        checkbox = QCheckBox("Summer 2022", self)
        checkbox.move(520, 200)
        checkbox = QCheckBox("Fall 2022", self)
        checkbox.move(520, 230)
        checkbox = QCheckBox("Spring 2023", self)
        checkbox.move(520, 260)
        checkbox = QCheckBox("Summer 2023", self)
        checkbox.move(520, 290)
        checkbox = QCheckBox("Other", self)
        checkbox.move(520, 320)

        self.show()

    def closeEvent(self, event: QCloseEvent):
        reply = QMessageBox.question(self, 'Message', 'Are you sure you want to quit?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


def run():
    app = QApplication(sys.argv)

    ex = GuiWindow()

    sys.exit(app.exec())


if __name__ == '__main__':
    run()
