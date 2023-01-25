import requests
import json


def print_red_text(text_str: str):
    """ Prints the incoming string parameter as RED text to the terminal """

    print(f'\033[91m{text_str}\033[00m')


def safe_get_request(url: str):
    """ This function makes a Get request to the URL passed in as its single parameter.
    If an exception is thrown while trying to execute the GET request, 'None' is returned
    in place of a response object. If the GET request is successful, a response object is returned. """

    response = None
    try:
        # if request.get() throws an exception, the 'response' variable will remain as 'None'
        response = requests.get(url, headers=HEADER_FOR_GET_REQUEST)
        print(f'GET request executed with no errors. Response object created:\n'
              f'Response object: <{hex(id(response))}>\n')
    except requests.exceptions.RequestException as requests_exception:
        print_red_text(f'GET requests FAILED with the following error: {requests_exception}\n')
    finally:
        return response


def issue_get_request(target_url: str):
    """ This function issues a Get request to the URL passed as its single parameter.
    A response object is returned
    The status code of the request object is also reported. """

    # safe_get_request()returns 'None' if an exception happens while executing its function body
    response_obj = safe_get_request(target_url)
    if response_obj is None:
        print_red_text(f'A GET request error has occurred: No Response Object!\n')
        return None
    if response_obj.status_code != 200:  # 200 status code in get request = successfully
        print_red_text(f'The Get request was NOT successful \n{response_obj.status_code}[{response_obj.reason}]')
        return response_obj
    else:
        print(f'The Get request was successful \n{response_obj.status_code}[{response_obj.reason}]\n')
        return response_obj


HEADER_FOR_GET_REQUEST = (
    {
     }
)


def main():
    base_url = 'https://joaoalves.wufoo.com/api/v3/forms/cubes-project-proposal-submission/entries/json'
    response_obj = issue_get_request(base_url)

    data_out_file = open('data_output.txt', 'w')
    data_out_file.write(response_obj.text)
    data_out_file.close()


if __name__ == '__main__':
    main()
