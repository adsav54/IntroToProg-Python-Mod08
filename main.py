# ------------------------------------------------------------------------------------------------- #
# Title: main.py
# Description: The application to collect and save employee data
# ChangeLog: (Who, When, What)
# RRoot,1.5.2030,Created Script
# AdamSavage,20241207,Modified script to work with modules
# ------------------------------------------------------------------------------------------------- #

import data_classes as dat
import processing_classes as proc
import presentation_classes as pres


FILE_NAME: str = "EmployeeRatings.json"
menu_choice = ''


# Beginning of the main body of this script
employees = proc.FileProcessor.read_employee_data_from_file(file_name=FILE_NAME,
                                                            employee_data=dat.employees,
                                                            employee_type=dat.Employee)  # Note this is the class name (ignore the warning)

# Repeat the follow tasks
while True:
    pres.IO.output_menu(menu=dat.MENU)

    menu_choice = pres.IO.input_menu_choice()

    if menu_choice == "1":  # Display current data
        try:
            pres.IO.output_employee_data(employee_data=employees)
        except Exception as e:
            pres.IO.output_error_messages(e)
        continue

    elif menu_choice == "2":  # Get new data (and display the change)
        try:
            employees = pres.IO.input_employee_data(employee_data=employees,
                                               employee_type=dat.Employee)  # Note this is the class name (ignore the warning)
            pres.IO.output_employee_data(employee_data=employees)
        except Exception as e:
            pres.IO.output_error_messages(e)
        continue

    elif menu_choice == "3":  # Save data in a file
        try:
            proc.FileProcessor.write_employee_data_to_file(file_name=FILE_NAME, employee_data=employees)
            print(f"Data was saved to the {FILE_NAME} file.")
        except Exception as e:
            pres.IO.output_error_messages(e)
        continue

    elif menu_choice == "4":  # End the program
        break  # out of the while loop
