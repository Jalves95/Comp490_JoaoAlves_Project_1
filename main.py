import numbers
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
        title = current_row[4]
        org_name = current_row[5]
        org_web = current_row[7]
        email = current_row[6]
        phone_number = current_row[8]
        crs_pro = current_row[9]
        participation = current_row[21]
        record = {"Entry": entry_collumn, "Prefix": prefix, "First_Name": first_name, "Last_Name": last_name,
                  "Title": title, "Phone_Number": phone_number, "Organization_Name": org_name,
                  "Organization_Website": org_web, "Email": email, "Participation": participation,
                  "Course_Project": crs_pro}
        if current_row in rawdata is None:
            record = "No Entry"
        final_data_list.append(record)
    return final_data_list


# def get_key(value:dict):
#     return value["median_income"]


def main():
    # database_functions.create_wufoo_db()
    test_data = get_test_data()
    # test_data.sort(key=get_key)
    display_data(test_data)


if __name__ == '__main__':
    main()
