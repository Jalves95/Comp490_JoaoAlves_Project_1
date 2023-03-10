import database_functions
import get_data
import put_data_into_gui
import gui_window
from PySide6 import QtCore


def test_safe_get_request():
    json_data = get_data.safe_get_request()
    entries = json_data['Entries']
    assert len(entries) > 10


def test_data_into_user_gui():
    connection = database_functions.create_db_connection()
    cursor = database_functions.create_db_cursor(connection)
    cursor.execute("SELECT First_Name, Last_Name, Title FROM user_records WHERE BSU_Email = 'Heather'")
    record = cursor.fetchone()
    assert record[0] == "Jones"
    assert record[1] == "cool"
    assert record[2] == "guy"
