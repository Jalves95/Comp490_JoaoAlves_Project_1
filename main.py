import sys
import PySide6.QtWidgets
import PySide6
import database_functions
import getData
import gui_window


# add comment to test workflow

def display_data(data: list):
    qt_app = PySide6.QtWidgets.QApplication(sys.argv)  # sys.argv is the list of command line arguments
    my_window = gui_window.GuiWindow(data)
    sys.exit(qt_app.exec())


def get_test_data() -> list[dict]:
    workbook_file = database_functions.create_wufoo_db()
    cnn = database_functions.create_db_connection()
    cursor = cnn.cursor()
    cursor.execute("select * from wufoo_data")  # DataTable is a table in Data.mdb
    rawdata = cursor.fetchall()
    final_data_list = []
    for current_row in rawdata:
        entry_collumn = current_row[0]
        prefix = current_row[1]
        first_name = current_row[2]
        last_name = current_row[3]
        record = {"Entry": entry_collumn, "Prefix": prefix, "First_Name": first_name, "Last_Name": last_name}
        final_data_list.append(record)
    return final_data_list


# def get_key(value:dict):
#     return value["median_income"]


def main():
    # database_functions.create_wufoo_db()
    # gui_window.run()
    # getData.print_data()
    test_data = get_test_data()
    # test_data.sort(key=get_key)
    display_data(test_data)


if __name__ == '__main__':
    main()
