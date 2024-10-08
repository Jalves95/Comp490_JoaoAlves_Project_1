import pytest
import sqlite3
import database_functions

""" This file contains all unit tests """

# 10 manual data for testing
sample_data = {'EntryId': '1', 'Field3': 'Mr.', 'Field4': 'John', 'Field5': 'Cable', 'Field218': 'IT',
               'Field12': 'IT4US'}, \
    {'EntryId': '2', 'Field3': 'Mrs.', 'Field4': 'Hella', 'Field5': 'Jones',
     'Field218': 'Front Desk',
     'Field12': 'IPOrganization'}, \
    {'EntryId': '3', 'Field3': 'Mr.', 'Field4': 'James', 'Field5': 'Sousa', 'Field218': 'Manager',
     'Field12': 'Walmart'}, \
    {'EntryId': '4', 'Field3': 'Mrs.', 'Field4': 'Morgan', 'Field5': 'Tall', 'Field218': 'Student',
     'Field12': 'BSU'}, \
    {'EntryId': '5', 'Field3': 'Dr.', 'Field4': 'Matt', 'Field5': 'Alex', 'Field218': 'Professor',
     'Field12': 'Computer Science'}, \
    {'EntryId': '6', 'Field3': 'Dr.', 'Field4': 'Grand', 'Field5': 'Poobah', 'Field218': 'Super Dude',
     'Field12': 'Kalel.com'}, \
    {'EntryId': '7', 'Field3': 'Dr.', 'Field4': 'Tyler', 'Field5': 'Soares', 'Field218': 'President',
     'Field12': 'Amazon'}, \
    {'EntryId': '8', 'Field3': 'Dr.', 'Field4': 'Joao', 'Field5': 'All', 'Field218': 'Vice President',
     'Field12': 'Facebook'}, \
    {'EntryId': '9', 'Field3': 'Dr.', 'Field4': 'David', 'Field5': 'Roach', 'Field218': 'IT',
     'Field12': 'Bestbuy'}, \
    {'EntryId': '10', 'Field3': 'Dr.', 'Field4': 'Sean', 'Field5': 'Miley', 'Field218': 'Front Desk',
     'Field12': 'Target'}


@pytest.fixture
def test_setup_database():
    """ Fixture to set up the in-memory database with test data """
    data = sample_data

    db_connection = sqlite3.connect(':memory:')
    cursor = database_functions.create_db_cursor(db_connection)
    database_functions.create_tables(cursor, data)

    cursor.execute('''CREATE TABLE IF NOT EXISTS test_data(
                                    Entry TEXT,
                                    Prefix TEXT,
                                    First_Name TEXT,
                                    Last_Name TEXT,
                                    Title TEXT,
                                    Organization_Name TEXT,
                                    Email TEXT,
                                    Organization_Website TEXT,
                                    Phone_Number TEXT,
                                    Opportunities TEXT,
                                    Opportunities_2 TEXT,
                                    Opportunities_3 TEXT,
                                    Opportunities_4 TEXT,
                                    Opportunities_5 TEXT,
                                    Opportunities_6 TEXT,
                                    Opportunities_7 TEXT,
                                    Collaboration_Date TEXT,
                                    Collaboration_Date_2 TEXT,
                                    Collaboration_Date_3 TEXT,
                                    Collaboration_Date_4 TEXT,
                                    Collaboration_Date_5 TEXT,
                                    Participation TEXT)''')

    cursor.execute('DELETE FROM test_data')

    for dict_entry in data:
        cursor.execute('''INSERT INTO test_data VALUES(?, ?, ?, ?, ?, ?, ?, ?,
            ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                       (dict_entry.get('EntryId', None),
                        dict_entry.get('Field3', None),
                        dict_entry.get('Field4', None),
                        dict_entry.get('Field5', None),
                        dict_entry.get('Field218', None),
                        dict_entry.get('Field12', None),
                        dict_entry.get('Field13', None),
                        dict_entry.get('Field14', None),
                        dict_entry.get('Field15', None),
                        dict_entry.get('Field16', None),
                        dict_entry.get('Field17', None),
                        dict_entry.get('Field18', None),
                        dict_entry.get('Field19', None),
                        dict_entry.get('Field20', None),
                        dict_entry.get('Field21', None),
                        dict_entry.get('Field22', None),
                        dict_entry.get('Field116', None),
                        dict_entry.get('Field117', None),
                        dict_entry.get('Field118', None),
                        dict_entry.get('Field119', None),
                        dict_entry.get('Field120', None),
                        dict_entry.get('Field216', None)))

    db_connection.commit()


def test_database_functions():
    connection = database_functions.create_db_connection()
    cursor = database_functions.create_db_cursor(connection)
    cursor.execute("SELECT Prefix, First_Name, Last_Name FROM wufoo_data WHERE Entry = 5")
    record = cursor.fetchone()
    assert record[0] == "Dr."
    assert record[1] == "Matt"
    assert record[2] == "Alex"


def test_database(test_setup_database):
    # Test to make sure that there are 24 items in the database
    assert len('SELECT * FROM wufoo_data') == 24


def test_entries():
    with pytest.raises(ValueError) as exception_info:
        assert dict(sample_data) is ValueError

    with pytest.raises(AssertionError) as exception_info:
        assert str(sample_data) is AssertionError
