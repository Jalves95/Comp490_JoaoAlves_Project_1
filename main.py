import database_functions
import put_data_into_gui
import sys


def show_options():
    """ Provided by Dr. Santore's sprint 3 solution"""

    print("=======================================")
    print("[1] Update the database with wufoo data")
    print("[2] Run the Graphical Program")
    print("[3] Quit")
    print("=======================================")


def main():
    show_options()
    while True:
        answer = input("Please enter your choice:")
        if answer == "1":
            database_functions.create_wufoo_db()
            database_functions.create_user_db()
            break
        elif answer == "2":
            put_data_into_gui.run_data_gui()
            break
        elif answer == "3":
            sys.exit(0)
        else:
            # print("Invalid Entry, ending program...")
            print("Invalid Entry, Choose Again.\n")
            show_options()


if __name__ == '__main__':
    main()
