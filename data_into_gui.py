import sys
import PySide6.QtWidgets
import PySide6
import database_functions
import gui_window


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
        guest_sp = current_row[10]
        site_vis = current_row[11]
        job_sh = current_row[12]
        intern = current_row[13]
        car_pan = current_row[14]
        net_event = current_row[15]
        summer_2022 = current_row[16]
        fall_2022 = current_row[17]
        spring_2023 = current_row[18]
        summer_2023 = current_row[19]
        other = current_row[20]
        participation = current_row[21]
        record = {"Entry": entry_collumn, "Prefix": prefix, "First_Name": first_name, "Last_Name": last_name,
                  "Title": title, "Phone_Number": phone_number, "Organization_Name": org_name,
                  "Organization_Website": org_web, "Email": email, "Participation": participation,
                  "Course_Project": crs_pro, "Guest_Speaker": guest_sp, "Site_Visit": site_vis,
                  "Job_Shadow": job_sh, "Internship": intern, "Career_Panel": car_pan, "Networking_Event": net_event,
                  "Summer_2022": summer_2022, "Fall_2022": fall_2022, "Spring_2023": spring_2023,
                  "Summer_2023": summer_2023, "Other": other}
        if current_row in rawdata is None:
            record = "No Entry"
        final_data_list.append(record)
    return final_data_list


def main():
    test_data = get_test_data()
    display_data(test_data)

