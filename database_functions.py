import sqlite3
import json
import requests
from secrets import API_FOR_GET_REQUEST
from requests.auth import HTTPBasicAuth


base_url = "https://joaoalves.wufoo.com/api/v3/forms/cubes-project-proposal-submission/entries/json"


def print_red_text(text_str: str):
    """ Prints the incoming string parameter as RED text to the terminal """

    print(f'\033[91m{text_str}\033[00m')


def safe_get_request() -> dict:
    """ This function makes a Get request to the URL passed in as its single parameter.
    If an exception is thrown while trying to execute the GET request, 'None' is returned
    in place of a response object. If the GET request is successful, a response object is returned. """

    try:
        # if request.get() throws an exception, the 'response' variable will remain as 'None'
        response = requests.get(base_url, auth=HTTPBasicAuth(API_FOR_GET_REQUEST, 'pass'))
        if response.status_code != 200:  # if we don't get an ok response we have trouble
            print_red_text(f"Failed to get data, response code:{response.status_code} and error message:"
                           f" {response.reason} ")
        print(f'GET request executed with no errors. Response object created:\n'
              f'Response object: <{hex(id(response))}>\n')
    except requests.exceptions.RequestException as requests_exception:
        print_red_text(f'GET requests FAILED with the following error: {requests_exception}\n')
    finally:
        print(f'The Get request was successful \n{response.status_code}[{response.reason}]\n')
        json_response = response.json()
        return json_response


def establish_database_connection(database_name: str):
    """ This function tries to connect to a database with the name according to the incoming string
    A database connection object is returned if successful
    'None' is returned if a connection was unable to be established """

    db_connection = None
    try:
        db_connection = sqlite3.connect(database_name)
        print(f'Connection to database was \'{database_name}\' was established'
              f' database connection: {db_connection}\n')
    except sqlite3.Error as db_error:
        print_red_text(f'An error occurred while trying to connect to database {database_name}:'
                       f'{db_error}')
    finally:
        return db_connection


def create_db_cursor(db_connection_obj: sqlite3.Connection):
    """ This function creates a sqlite3 Cursor object on the database connection
        incoming as its single parameter. 'None' is returned if the cursor object
        could not be created """

    cursor_obj = None
    if db_connection_obj is None:
        print_red_text(f'Cursor object Not created: No connection object!\n')
        return None
    try:
        cursor_obj = db_connection_obj.cursor()
        print(f'Cursor object created on {db_connection_obj}\n'
              f'Cursor object: {cursor_obj}\n')
    except sqlite3.Error as db_error:
        print_red_text(f'A cursor object could not be created on database connection {db_connection_obj}\n'
                       f'{db_error}\n')
    finally:
        return cursor_obj


def create_database():
    """Creates tables for database"""
    try:
        create_wufoo_db()
    except sqlite3.Error as db_error:
        print_red_text(f'A database error occurred while creating tables: {db_error}\n')
    finally:
        print(f'Tables have been created with no errors\n')


def create_db_connection():
    """Creates database connection and returns that connection"""
    db_name = 'wufoo_data.db'
    db_connection = establish_database_connection(db_name)
    return db_connection


def save_data(data_to_save: list, save_file=None):
    """ Provided by Dr. Santore's sprint 1 solution"""

    for entry in data_to_save:
        for key, value in entry.items():
            print(f"{key}: {value}", file=save_file)
        # now print the spacer
        print("+++++++++++++++++++++++++++++++++++++++++++++\n_______________________________________________",
              file=save_file)


def create_tables(cursor: sqlite3.Cursor, dictionary: dict):
    """ This function creates each tables from the wufoo Database. """

    for key in dictionary:
        create_table_columns(cursor, key)


def create_table_columns(cursor: sqlite3.Cursor, wufoo_data):
    """ This function creates a table in the database to store ALL the wufoo data
     (if it does not already exist) the parentheses following the table name,
     contains a list of column names and the data type of values that will be inserted
     into those columns """

    create_wufoo_table = f'CREATE TABLE IF NOT EXISTS wufoo_data (' \
                         f'Entry TEXT, ' \
                         f'Prefix TEXT,' \
                         f'First_Name TEXT,' \
                         f'Last_Name TEXT,' \
                         f'Title TEXT,' \
                         f'rganization_Name TEXT,' \
                         f'Email TEXT,' \
                         f'Organization_Website TEXT,' \
                         f'Phone_Number TEXT,' \
                         f'Opportunities TEXT,' \
                         f'Opportunities_2 TEXT,' \
                         f'Opportunities_3 TEXT,' \
                         f'Opportunities_4 TEXT,' \
                         f'Opportunities_5 TEXT,' \
                         f'Opportunities_6 TEXT,' \
                         f'Opportunities_7 TEXT,' \
                         f'Collaboration_Date TEXT,' \
                         f'Collaboration_Date_2 TEXT,' \
                         f'Collaboration_Date_3 TEXT,' \
                         f'Collaboration_Date_4 TEXT,' \
                         f'Collaboration_Date_5 TEXT,' \
                         f'Participation TEXT);'
    cursor.execute(create_wufoo_table)


def create_wufoo_db():
    """Creates wufoo table in database"""

    data = safe_get_request()
    data1 = data['Entries']
    file_to_save = open("data_output.txt", 'w')
    save_data(data1, save_file=file_to_save)

    try:
        # Creates database connection
        db_connection = create_db_connection()
        # Creates cursor object
        db_cursor_object = create_db_cursor(db_connection)

        create_tables(db_cursor_object, data1)

        # Clears table if data in it from previous use
        db_cursor_object.execute('DELETE FROM wufoo_data')

        for dict_entry in data1:
            db_cursor_object.execute('''INSERT INTO wufoo_data VALUES(?, ?, ?, ?, ?, ?, ?, ?,
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

    except sqlite3.Error as db_error:
        print_red_text(f'A database error has occurred: {db_error}')

    # 'finally' blocks are useful when behavior in the try/except blocks is not predictable
    # The 'finally' block will run regardless of what happens in the try/except blocks.
    finally:
        # close the database connection whether an error happened or not (if a connection exists)
        if db_connection:
            db_connection.close()
            print('The database has been closed')
