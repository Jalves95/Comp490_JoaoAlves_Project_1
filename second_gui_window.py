from PySide6.QtWidgets import QWidget, QPushButton, QLabel, QLineEdit, QTextEdit, QMessageBox, QCheckBox


class GuiWindow2(QWidget):

    def __init__(self, data_to_show:dict):
        super().__init__()
        self.data = data_to_show
        self.setup_window()

    def setup_window(self):
        self.setGeometry(330, 50, 525, 500)
        self.setWindowTitle('Selected Entry Data')

        label = QLabel("Prefix:", self)
        label.move(20, 0)
        prefix_display = QLineEdit(self.data['Prefix'], self)
        prefix_display.move(110, 0)

        label = QLabel("First Name:", self)
        label.move(20, 50)
        first_name_display = QLineEdit(self.data['First_Name'], self)
        first_name_display.move(110, 50)

        label = QLabel("Last Name:", self)
        label.move(20, 100)
        title_display = QLineEdit(self.data['Last_Name'], self)
        title_display.move(110, 100)

        label = QLabel("Phone Number:", self)
        label.move(20, 150)
        title_display = QLineEdit(self.data['Phone_Number'], self)
        title_display.move(110, 150)

        label = QLabel("Title:", self)
        label.move(285, 0)
        org_display = QLineEdit(self.data['Title'], self)
        org_display.move(365, 0)

        label = QLabel("Org Name:", self)
        label.move(285, 50)
        email_display = QLineEdit(self.data['Organization_Name'], self)
        email_display.move(365, 50)

        label = QLabel("Org Website:", self)
        label.move(285, 100)
        last_name_display = QLineEdit(self.data['Organization_Website'], self)
        last_name_display.move(365, 100)

        label = QLabel("Email:", self)
        label.move(285, 150)
        last_name_display = QLineEdit(self.data['Email'], self)
        last_name_display.move(365, 150)

        checkbox = QCheckBox("Course_Project", self)
        checkbox.setChecked(True)
        checkbox.move(20, 200)
        checkbox.toggle()
        checkbox = QCheckBox("Guest Speaker", self)
        checkbox.move(20, 230)
        checkbox = QCheckBox("Site Visit", self)
        checkbox.move(20, 260)
        checkbox = QCheckBox("Job Shadow", self)
        checkbox.move(20, 290)
        checkbox = QCheckBox("Internship", self)
        checkbox.move(20, 320)
        checkbox = QCheckBox("Career Panel", self)
        checkbox.move(20, 350)
        checkbox = QCheckBox("Networking Event", self)
        checkbox.move(20, 380)
        checkbox = QCheckBox("Summer 2022 (June 2022- August 2022)", self)
        checkbox.move(240, 200)
        checkbox = QCheckBox("Fall 2022 (September 2022- December 2022)", self)
        checkbox.move(240, 230)
        checkbox = QCheckBox("Spring 2023 (January 2023- April 2023)", self)
        checkbox.move(240, 260)
        checkbox = QCheckBox("Summer 2023 (June 2023- August 2023)", self)
        checkbox.move(240, 290)
        checkbox = QCheckBox("Other", self)
        checkbox.move(240, 320)

        label = QLabel("Participation:", self)
        label.move(240, 380)
        prefix_display = QLineEdit(self.data['Participation'], self)
        prefix_display.move(320, 380)

        self.show()