import sys
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QListWidget, QLineEdit, QLabel
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
        btn_quit.move(600, 650)

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

        label = QLabel("Title:", self)
        label.move(520, 0)
        org_display = QLineEdit(self)
        org_display.move(600, 0)

        label = QLabel("Organization:", self)
        label.move(520, 50)
        email_display = QLineEdit(self)
        email_display.move(600, 50)

        label = QLabel("Email:", self)
        label.move(520, 100)
        last_name_display = QLineEdit(self)
        last_name_display.move(600, 100)

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
