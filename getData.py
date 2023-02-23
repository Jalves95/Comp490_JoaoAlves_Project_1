import requests
import secrets
from requests.auth import HTTPBasicAuth
import sys

base_url = "https://joaoalves.wufoo.com/api/v3/forms/cubes-project-proposal-submission/entries/json"


def print_red_text(text_str: str):
    """ Prints the incoming string parameter as RED text to the terminal """

    print(f'\033[91m{text_str}\033[00m')


# def safe_get_request() -> dict:
#     """ This function makes a Get request to the URL passed in as its single parameter.
#     If an exception is thrown while trying to execute the GET request, 'None' is returned
#     in place of a response object. If the GET request is successful, a response object is returned. """
#
#     try:
#         # if request.get() throws an exception, the 'response' variable will remain as 'None'
#         response = requests.get(base_url, auth=HTTPBasicAuth(secrets.API_FOR_GET_REQUEST, 'pass'))
#         if response.status_code != 200:  # if we don't get an ok response we have trouble
#             print_red_text(f"Failed to get data, response code:{response.status_code} and error message:"
#                            f" {response.reason} ")
#         print(f'GET request executed with no errors. Response object created:\n'
#               f'Response object: <{hex(id(response))}>\n')
#     except requests.exceptions.RequestException as requests_exception:
#         print_red_text(f'GET requests FAILED with the following error: {requests_exception}\n')
#     finally:
#         print(f'The Get request was successful \n{response.status_code}[{response.reason}]\n')
#         json_response = response.json()
#         return json_response

def get_wufoo_data() -> dict:
    """ Provided by Dr. Santore's Sprint 1 Solution """

    response = requests.get(base_url, auth=HTTPBasicAuth(secrets.API_FOR_GET_REQUEST, "pass"))
    if response.status_code != 200:  # if we don't get an ok response we have trouble
        print(
            f"Failed to get data, response code:{response.status_code} and error message: {response.reason} "
        )
        sys.exit(-1)
    jsonresponse = response.json()
    return jsonresponse


def save_data(data_to_save: list, save_file=None):
    """ Provided by Dr. Santore's sprint 1 solution"""

    for entry in data_to_save:
        for key, value in entry.items():
            print(f"{key}: {value}", file=save_file)
        # now print the spacer
        print("+++++++++++++++++++++++++++++++++++++++++++++\n_______________________________________________",
              file=save_file)


def print_data():
    data = get_wufoo_data()
    data1 = data['Entries']
    file_to_save = open("data_output.txt", 'w')
    save_data(data1, save_file=file_to_save)
    print(data1)

