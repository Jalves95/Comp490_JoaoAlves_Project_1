import PySide6
from PySide6.QtWidgets import QWidget, QPushButton, QLabel, QLineEdit, QTextEdit, QMessageBox, QCheckBox
from PySide6.QtCore import Qt
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtWidgets import (
    QWidget,
    QPushButton,
    QListWidget,
    QApplication,
    QListWidgetItem,
    QHBoxLayout,
    QVBoxLayout,
    QLayout,
    QGridLayout,
    QPlainTextEdit,
    QLabel,
    QLineEdit,
    QCheckBox,
)

class GuiWindow2(QWidget):

    def __init__(self, data_to_show: dict):
        super().__init__()
        self.data = data_to_show
        self.setup_window()

    def setup_window(self):
        self.setGeometry(341, 50, 525, 500)
        self.setWindowTitle('Selected Entry Data')

        label = QLabel("Prefix:", self)
        label.move(20, 0)
        prefix_display = QLineEdit(self.data['Prefix'], self)
        prefix_display.setReadOnly(True)
        prefix_display.move(110, 0)

        label = QLabel("First Name:", self)
        label.move(20, 50)
        first_name_display = QLineEdit(self.data['First_Name'], self)
        first_name_display.setReadOnly(True)
        first_name_display.move(110, 50)

        label = QLabel("Last Name:", self)
        label.move(20, 100)
        title_display = QLineEdit(self.data['Last_Name'], self)
        title_display.setReadOnly(True)
        title_display.move(110, 100)

        label = QLabel("Phone Number:", self)
        label.move(20, 150)
        phone_display = QLineEdit(self.data['Phone_Number'], self)
        phone_display.setReadOnly(True)
        phone_display.move(110, 150)

        label = QLabel("Title:", self)
        label.move(285, 0)
        title_display = QLineEdit(self.data['Title'], self)
        title_display.setReadOnly(True)
        title_display.move(365, 0)

        label = QLabel("Org Name:", self)
        label.move(285, 50)
        org_name_display = QLineEdit(self.data['Organization_Name'], self)
        org_name_display.setReadOnly(True)
        org_name_display.move(365, 50)

        label = QLabel("Org Website:", self)
        label.move(285, 100)
        org_web_display = QLineEdit(self.data['Organization_Website'], self)
        org_web_display.setReadOnly(True)
        org_web_display.move(365, 100)

        label = QLabel("Email:", self)
        label.move(285, 150)
        email_display = QLineEdit(self.data['Email'], self)
        email_display.setReadOnly(True)
        email_display.move(365, 150)

        course_proj_checkbox = QCheckBox("Course Project", self)
        course_proj_checkbox.setChecked(bool(self.data["Course_Project"]))
        course_proj_checkbox.setAttribute(Qt.WA_TransparentForMouseEvents)  # don't accept editing
        course_proj_checkbox.setFocusPolicy(Qt.NoFocus)  # or keyboard focus
        course_proj_checkbox.move(20, 200)

        guest_speaker_checkbox = QCheckBox("Guest Speaker", self)
        guest_speaker_checkbox.setChecked(bool(self.data["Guest_Speaker"]))
        guest_speaker_checkbox.setAttribute(Qt.WA_TransparentForMouseEvents)
        guest_speaker_checkbox.setFocusPolicy(Qt.NoFocus)
        guest_speaker_checkbox.move(20, 230)

        site_visit_checkbox = QCheckBox("Site Visit", self)
        site_visit_checkbox.setChecked(bool(self.data["Site_Visit"]))
        site_visit_checkbox.setAttribute(Qt.WA_TransparentForMouseEvents)
        site_visit_checkbox.setFocusPolicy(Qt.NoFocus)
        site_visit_checkbox.move(20, 260)

        job_shadow_checkbox = QCheckBox("Job Shadow", self)
        job_shadow_checkbox.setChecked(bool(self.data["Job_Shadow"]))
        job_shadow_checkbox.setAttribute(Qt.WA_TransparentForMouseEvents)
        job_shadow_checkbox.setFocusPolicy(Qt.NoFocus)
        job_shadow_checkbox.move(20, 290)

        intern_checkbox = QCheckBox("Internship", self)
        intern_checkbox.setChecked(bool(self.data["Internship"]))
        intern_checkbox.setAttribute(Qt.WA_TransparentForMouseEvents)
        intern_checkbox.setFocusPolicy(Qt.NoFocus)
        intern_checkbox.move(20, 320)

        career_checkbox = QCheckBox("Career Panel", self)
        career_checkbox.setChecked(bool(self.data["Career_Panel"]))
        career_checkbox.setAttribute(Qt.WA_TransparentForMouseEvents)
        career_checkbox.setFocusPolicy(Qt.NoFocus)
        career_checkbox.move(20, 350)

        networking_checkbox = QCheckBox("Networking Event", self)
        networking_checkbox.setChecked(bool(self.data["Networking_Event"]))
        networking_checkbox.setAttribute(Qt.WA_TransparentForMouseEvents)
        networking_checkbox.setFocusPolicy(Qt.NoFocus)
        networking_checkbox.move(20, 380)

        summer_2022_checkbox = QCheckBox("Summer 2022 (June 2022- August 2022)", self)
        summer_2022_checkbox.setChecked(bool(self.data["Summer_2022"]))
        summer_2022_checkbox.setAttribute(Qt.WA_TransparentForMouseEvents)
        summer_2022_checkbox.setFocusPolicy(Qt.NoFocus)
        summer_2022_checkbox.move(240, 200)

        fall_2022_checkbox = QCheckBox("Fall 2022 (September 2022- December 2022)", self)
        fall_2022_checkbox.setChecked(bool(self.data["Fall_2022"]))
        fall_2022_checkbox.setAttribute(Qt.WA_TransparentForMouseEvents)
        fall_2022_checkbox.setFocusPolicy(Qt.NoFocus)
        fall_2022_checkbox.move(240, 230)

        spring_2023_checkbox = QCheckBox("Spring 2023 (January 2023- April 2023)", self)
        spring_2023_checkbox.setChecked(bool(self.data["Spring_2023"]))
        spring_2023_checkbox.setAttribute(Qt.WA_TransparentForMouseEvents)
        spring_2023_checkbox.setFocusPolicy(Qt.NoFocus)
        spring_2023_checkbox.move(240, 260)

        summer_2023_checkbox = QCheckBox("Summer 2023 (June 2023- August 2023)", self)
        summer_2023_checkbox.setChecked(bool(self.data["Summer_2023"]))
        summer_2023_checkbox.setAttribute(Qt.WA_TransparentForMouseEvents)
        summer_2023_checkbox.setFocusPolicy(Qt.NoFocus)
        summer_2023_checkbox.move(240, 290)

        other_checkbox = QCheckBox("Other", self)
        other_checkbox.setChecked(bool(self.data["Other"]))
        other_checkbox.setAttribute(Qt.WA_TransparentForMouseEvents)
        other_checkbox.setFocusPolicy(Qt.NoFocus)
        other_checkbox.move(240, 320)

        label = QLabel("Participation:", self)
        label.move(240, 380)
        part_display = QLineEdit(self.data['Participation'], self)
        part_display.setReadOnly(True)
        part_display.move(320, 380)
