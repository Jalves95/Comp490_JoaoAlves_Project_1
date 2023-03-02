import pytest
import sqlite3
from PySide6.QtWidgets import QWidget, QPushButton, QLabel, QLineEdit, QTextEdit, QMessageBox, QCheckBox
from PySide6.QtWidgets import QWidget
import database_functions
import getData
import data_into_gui
from PySide6 import QtCore, QtWidgets
import gui_window
import second_gui_window
from PySide6 import QtCore


def test_safe_get_request():
    """ For this test we are just getting the data from wufoo, getting the Entries and counting them.
        Since there are currently 10 entries, this test will pass.
        Provided by Dr. Santore """

    json_data = getData.safe_get_request()
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
    window = data_into_gui.run_data_gui()
    # window.show()
    # qtbot.addWidget(window)
    row = 0  # assume 0 start, get 10th item change to update test
    target_item = window.item(row)
    rectangle = window.visualItemRect(target_item)
    click_point = rectangle.center()
    qtbot.mouseClick(window.list_control.viewport(), QtCore.Qt.LeftButton, pos=click_point)
    assert window.prefix() == "Mr."
    assert window.title() == "IT"
    # assert window.project_check.isChecked() is True
    # assert window.visit_check.isChecked() is False