1. Joao Alves
2. In order to run the main program you will need to 'import requests',
'from requests.auth import HTTPBasicAuth', and 'import sqlite3'.
For the test functions; 'import pytest' and 'import sqlite3'
3. My program creates a GET request to a dataset provided by Wufoo in a JSON format, with an API key, it is 
authorized to collect the data. The data is then collect and transferred to an output text file that may be 
used as you like. A SQLite database with 22 columns is created. The Wufoo dataset is inserted into the SQLite
database. Each entry has information that pertains to each category from the Wufoo form.
4. My database has 22 columns with each of them containing data from each Wufoo entries.
5. Everything works as intended
6. Wufoo Link: https://joaoalves.wufoo.com/forms/cubes-project-proposal-submission


