1. Joao Alves
2. In order to run the main program you will need to 'import requests',
'from requests.auth import HTTPBasicAuth', and 'import sqlite3'.
For the test functions; 'import pytest' and 'import sqlite3'. 
To run the GUI application; 'import sys, import PySide6, import PySide6.QtWidgets,
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, 
QListWidget, QLineEdit, QLabel, QCheckBox, QListWidgetItem, from PySide6.QtGui import QCloseEvent'.
3. My program creates a GET request to a dataset provided by Wufoo in a JSON format, with an API key, it is 
authorized to collect the data. The data is then collect and transferred to an output text file that may be 
used as you like. A SQLite database with 22 columns is created. The Wufoo dataset is inserted into the SQLite
database. Each entry has information that pertains to each category from the Wufoo form. When running the
program, there is now a Graphical User Interface (GUI) that will show all the data from the database. The user
is able to select any wufoo entry and another GUI will show all the corresponding data to that entry. The Gui now 
allows the user to select and given entry and claim it, a new window will be displayed asking for the user information.
When done, the user can submit the claim, and update the database through the GUI.
4. My database has 22 columns with each of them containing data from each Wufoo entries. The table for the user entry
has 5 columns, each time a new claim is submitted and updated, the database is also updated.
5. Everything works as intended. All test passes through the command line. All tests for Git Actions pass.
6. Wufoo Link: https://joaoalves.wufoo.com/forms/cubes-project-proposal-submission


