from PySide6.QtWidgets import (
    QWidget,
    QPushButton,
    QListWidget,
    QMessageBox,
    QHBoxLayout,
    QVBoxLayout,
    QLayout,
    QGridLayout,
    QLabel,
    QLineEdit, QApplication,
)


class UserGui(QWidget):

    def save_input(self):
        with open("User_Records.txt", "w") as CurrentFile:
            print(CurrentFile)
            text = self.bsu_email.text()
            text_2 = self.first_name.text()
            text_3 = self.last_name.text()
            text_4 = self.title.text()
            text_5 = self.department.text()
            CurrentFile.write(text + '\t')
            CurrentFile.write(text_2 + '\t')
            CurrentFile.write(text_3 + '\t')
            CurrentFile.write(text_4 + '\t')
            CurrentFile.write(text_5)

    def __init__(self, data_to_show):
        super().__init__()
        self.data = data_to_show
        self.list_control: QListWidget = None
        self.data_window = None
        self.bsu_email: QLineEdit = None
        self.first_name: QLineEdit = None
        self.last_name: QLineEdit = None
        self.title: QLineEdit = None
        self.department: QLineEdit = None
        self.setup_window()

    def setup_window(self):

        self.setWindowTitle("User Records")
        main_layout = QHBoxLayout()
        self.list_control = QListWidget()
        main_window = self.build_right_pane()
        self.list_control.resize(400, 400)
        main_layout.addLayout(main_window)
        self.setLayout(main_layout)
        submit_button = QPushButton('Submit Claim', self)
        submit_button.clicked.connect(self.save_input)
        submit_button.resize(submit_button.sizeHint())
        main_window.addWidget(submit_button)

        quit_button = QPushButton("Quit", self)
        quit_button.clicked.connect(QApplication.instance().quit)
        main_layout.addWidget(quit_button)
        self.show()

    def build_right_pane(self) -> QLayout:
        main_panel = QVBoxLayout()
        one_liners_pane = QGridLayout()
        main_panel.addLayout(one_liners_pane)
        one_liners_pane.addWidget(QLabel("BSU Email :"), 0, 0)
        self.bsu_email = QLineEdit()
        one_liners_pane.addWidget(self.bsu_email, 0, 1)
        one_liners_pane.addWidget(QLabel("First Name:"), 0, 2)
        self.first_name = QLineEdit()
        one_liners_pane.addWidget(self.first_name, 0, 3)
        one_liners_pane.addWidget(QLabel("Last Name:"), 1, 0)
        self.last_name = QLineEdit()
        one_liners_pane.addWidget(self.last_name, 1, 1)
        one_liners_pane.addWidget(QLabel("Title:"), 1, 2)
        self.title = QLineEdit()
        one_liners_pane.addWidget(self.title, 1, 3)
        one_liners_pane.addWidget(QLabel("Department:"), 2, 0)
        self.department = QLineEdit()
        one_liners_pane.addWidget(self.department, 2, 1)
        return main_panel


def save_to_file(self):
    test1 = self.setup_window.text()
    test2 = self.setup_window.text()


    if test1 == "" or test2 == "":
        QMessageBox.information(self, "Please enter network address and number of host before selecting save", QMessageBox.Ok)
        return
    else:
        with open("SubNetSave.txt", "w") as CurrentFile:
            CurrentFile.write(str(test1))
            CurrentFile.write("\n")
            CurrentFile.write(str(test2))
            QMessageBox.information(self, "Your file has been saved under file name SubNetSave.txt", QMessageBox.Ok)
