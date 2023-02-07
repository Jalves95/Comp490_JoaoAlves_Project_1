import pytest
import requests
import sqlite3
import database_functions
from requests.auth import HTTPBasicAuth
from secrets import API_FOR_GET_REQUEST

""" This file contains all unit tests """


url = "https://joaoalves.wufoo.com/api/v3/forms/cubes-project-proposal-submission/entries/json"


def get_wufoo_data() -> dict:
    response = requests.get(url, auth=HTTPBasicAuth(API_FOR_GET_REQUEST, 'pass'))
    if response.status_code != 200:  # if we don't get an ok response we have trouble
        print(f"Failed to get data, response code:{response.status_code} and error message: {response.reason} ")
    jsonresponse = response.json()
    return jsonresponse


@pytest.fixture
def setup_database():
    """ Fixture to set up the in-memory database with test data """
    data = get_wufoo_data()
    data1 = data['Entries']

    db_connection = sqlite3.connect(':memory:')
    db_cursor = database_functions.create_db_cursor(db_connection)
    database_functions.create_tables(db_cursor, data1)

    db_cursor.execute('''CREATE TABLE IF NOT EXISTS wufoo_data(
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
    # sample_data = [
    #     ('1', 'John', 'Maxwell', 'Internships', 'Yes'),
    #     ('2', 'Tyler', 'Gordon', 'Internships', 'Yes'),
    #     ('3', 'Jordan', 'Torres', 'Internships', 'Yes'),
    #     ('4', 'Jaz', 'Souza', 'Internships', 'Yes'),
    #     ('5', 'Jasmine', 'Morales', 'Internships', 'Yes'),
    #     ('6', 'Deborah', 'Anderson', 'Internships', 'Yes'),
    #     ('7', 'Jessica', 'James', 'Internships', 'Yes'),
    #     ('8', 'Samantha', 'Adams', 'Internships', 'Yes'),
    #     ('9', 'Joe', 'Tyler', 'Internships', 'Yes'),
    #     ('10', 'Paul', ' Kim', 'Internships', 'Yes'),
    # ]

    db_cursor.execute('DELETE FROM wufoo_data')


    for dict_entry in data1:
        db_cursor.execute('''INSERT INTO wufoo_data VALUES(?, ?, ?, ?, ?, ?, ?, ?,
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


def test_connection(setup_database):
    # Test to make sure that there are 24 items in the database

    db_cursor = setup_database
    assert len('SELECT * FROM wufoo_data') == 24

