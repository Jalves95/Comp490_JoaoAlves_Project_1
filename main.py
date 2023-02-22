import database_functions
import data_into_gui


def main():
    database_functions.create_wufoo_db()
    data_into_gui.main()


if __name__ == '__main__':
    main()
