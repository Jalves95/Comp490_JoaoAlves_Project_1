import pytest
import sqlite3
from PySide6.QtWidgets import QWidget, QPushButton, QLabel, QLineEdit, QTextEdit, QMessageBox, QCheckBox
from PySide6.QtWidgets import QWidget
import database_functions
import get_data
import put_data_into_gui
from PySide6 import QtCore, QtWidgets
import gui_window
import second_gui_window
from PySide6 import QtCore


def test_safe_get_request():
    """ For this test we are just getting the data from wufoo, getting the Entries and counting them.
        Since there are currently 10 entries, this test will pass.
        Provided by Dr. Santore """

    json_data = get_data.safe_get_request()
    entries = json_data['Entries']
    assert len(entries) <= 10


def test_data_into_gui():
    connection = database_functions.create_db_connection()
    cursor = database_functions.create_db_cursor(connection)
    cursor.execute("SELECT Count() FROM SQLITE_MASTER WHERE name = ?", ["wufoo_data"])
    one_record = cursor.fetchone()
    number_of_rows = one_record[0]
    assert number_of_rows <= 1

    all_records = cursor.fetchall()
    for data in all_records:
        assert data == 22
        assert data == all_records
        assert data == one_record


def test_entry_selected(qtbot):  # using qubot requires the pytest-qt plugin (I added it to requirements.txt)
    """this test was built using
    https://stackoverflow.com/questions/58136462/selecting-qlistwidgetitem-with-qtbot-mouseclick
    and
    https://pytest-qt.readthedocs.io/en/latest/tutorial.html"""
    data = put_data_into_gui.get_test_data()
    window = gui_window.GuiWindow(data)
    window.show()
    qtbot.addWidget(window)
    row = 0  # assume 0 start, get 10th item change to update test
    target_item = window.list_control.item(row)
    rectangle = window.list_control.visualItemRect(target_item)
    click_point = rectangle.center()
    qtbot.mouseClick(window.list_control.viewport(), QtCore.Qt.LeftButton, pos=click_point)
    # The data of the first entry matches the data on the GUI
    assert window.data[0] == {'Career_Panel': '',
                              'Course_Project': '',
                              'Email': 'JCablw77@gmail.com',
                              'Entry': '1',
                              'Fall_2022': '',
                              'First_Name': 'John',
                              'Guest_Speaker': '',
                              'Internship': 'Internships',
                              'Job_Shadow': '',
                              'Last_Name': 'Cable',
                              'Networking_Event': '',
                              'Organization_Name': 'IT4US',
                              'Organization_Website': '',
                              'Other': '',
                              'Participation': 'Yes',
                              'Phone_Number': '1255557575',
                              'Prefix': 'Mr.',
                              'Site_Visit': '',
                              'Spring_2023': 'Spring 2023 (January 2023- April 2023)',
                              'Summer_2022': '',
                              'Summer_2023': '',
                              'Title': 'IT'}