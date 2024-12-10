# ------------------------------------------------------------------------------------------------- #
# Title: processing_classes.py
# Description: The module of processing classes
# ChangeLog: (Who, When, What)
# AdamSavage,20241208,Created module
# ------------------------------------------------------------------------------------------------- #

import json
import presentation_classes as pres


class FileProcessor:
    """
    A collection of processing layer functions that work with Json files

    ChangeLog: (Who, When, What)
    RRoot,1.1.2030,Created Class
    """

    @staticmethod
    # def read_employee_data_from_file(file_name: str, employee_data: list, employee_type: dat.Employee):
    def read_employee_data_from_file(file_name: str, employee_data: list, employee_type: object):
        """ This function reads data from a json file and loads it into a list of dictionary rows

        ChangeLog: (Who, When, What)
        RRoot,1.1.2030,Created function

        :param file_name: string data with name of file to read from
        :param employee_data: list of dictionary rows to be filled with file data
        :param employee_type: an reference to the Employee class
        :return: list
        """
        try:
            with open(file_name, "r") as file:
                list_of_dictionary_data = json.load(file)  # the load function returns a list of dictionary rows.
                for employee in list_of_dictionary_data:
                    employee_object = employee_type()
                    employee_object.first_name = employee["FirstName"]
                    employee_object.last_name = employee["LastName"]
                    employee_object.review_date = employee["ReviewDate"]
                    employee_object.review_rating = employee["ReviewRating"]
                    employee_data.append(employee_object)
        except FileNotFoundError as e:
            # raise FileNotFoundError("Text file must exist before running this script!")
            pres.IO.output_error_messages("Text file must exist before running this script!", e)
        except Exception as e:
            # raise Exception("There was a non-specific error!")
            pres.IO.output_error_messages("There was a non-specific error!", e)
        return employee_data

    @staticmethod
    def write_employee_data_to_file(file_name: str, employee_data: list):
        """ This function writes data to a json file with data from a list of dictionary rows

        ChangeLog: (Who, When, What)
        RRoot,1.1.2030,Created function

        :param file_name: string data with name of file to write to
        :param employee_data: list of dictionary rows to be writen to the file

        :return: None
        """
        try:
            list_of_dictionary_data: list = []
            for employee in employee_data:  # Convert List of employee objects to list of dictionary rows.
                employee_json: dict = {"FirstName": employee.first_name,
                                       "LastName": employee.last_name,
                                       "ReviewDate": employee.review_date,
                                       "ReviewRating": employee.review_rating
                                       }
                list_of_dictionary_data.append(employee_json)

            with open(file_name, "w") as file:
                json.dump(list_of_dictionary_data, file)
        except TypeError as e:
            # raise TypeError("Please check that the data is a valid JSON format")
            pres.IO.output_error_messages("Please check that the data is a valid JSON format", e)
        except PermissionError as e:
            # raise PermissionError("Please check the data file's read/write permission")
            pres.IO.output_error_messages("Please check the data file's read/write permission", e)
        except Exception as e:
            # raise Exception("There was a non-specific error!")
            pres.IO.output_error_messages("There was a non-specific error!", e)
