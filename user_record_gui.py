import PySide6
from PySide6.QtWidgets import QWidget, QPushButton, QLabel, QLineEdit, QTextEdit, QMessageBox, QCheckBox


class UserGui(QWidget):
    def __init__(self, data_to_show):
        super().__init__()
        self.data = data_to_show
        self.setup_window()

    def setup_window(self):
        self.setGeometry(341, 50, 525, 200)
        self.setWindowTitle('User Records')

        label = QLabel("BSU Email:", self)
        label.move(20, 0)
        bsu_email_display = QLineEdit(self)
        bsu_email_display.move(110, 0)

        label = QLabel("First Name:", self)
        label.move(20, 50)
        first_name_display = QLineEdit(self)
        first_name_display.move(110, 50)

        label = QLabel("Last Name:", self)
        label.move(20, 100)
        last_name_display = QLineEdit(self)
        last_name_display.move(110, 100)

        label = QLabel("Title:", self)
        label.move(285, 0)
        title_display = QLineEdit(self)
        title_display.move(365, 0)

        label = QLabel("Department:", self)
        label.move(285, 50)
        depart_display = QLineEdit(self)
        depart_display.move(365, 50)

