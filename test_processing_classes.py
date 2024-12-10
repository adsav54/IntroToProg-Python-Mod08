# ------------------------------------------------------------------------------------------------- #
# Title: test_processing_classes.py
# Description: The test harness for processing classes
# ChangeLog: (Who, When, What)
# AdamSavage,20241208,Created script from ChatGPT suggestions
# ------------------------------------------------------------------------------------------------- #

import unittest
from unittest.mock import patch, mock_open
import json
import presentation_classes as pres
from data_classes import Employee
import processing_classes as proc


class TestFileProcessor(unittest.TestCase):

    @patch("builtins.open", new_callable=mock_open,
           read_data='[{"FirstName": "John", "LastName": "Doe", "ReviewDate": "2024-12-09", "ReviewRating": 4}]')
    def test_read_employee_data_from_file_valid(self, mock_file):
        employee_data = []
        result = proc.FileProcessor.read_employee_data_from_file("test_file.json", employee_data, Employee)

        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].first_name, "John")
        self.assertEqual(result[0].last_name, "Doe")
        self.assertEqual(result[0].review_date, "2024-12-09")
        self.assertEqual(result[0].review_rating, 4)
        mock_file.assert_called_once_with("test_file.json", "r")

    @patch("builtins.open", side_effect=FileNotFoundError)
    @patch.object(pres.IO, 'output_error_messages')  # Mock IO error handling
    def test_read_employee_data_from_file_file_not_found(self, mock_output, mock_file):
        employee_data = []
        result = proc.FileProcessor.read_employee_data_from_file("non_existing_file.json", employee_data, Employee)

        self.assertEqual(result, employee_data)  # No data should be added
        mock_output.assert_called_once_with("Text file must exist before running this script!", mock_file.side_effect)

    @patch("builtins.open", side_effect=Exception("Unknown error"))
    @patch.object(pres.IO, 'output_error_messages')  # Mock IO error handling
    def test_read_employee_data_from_file_generic_error(self, mock_output, mock_file):
        employee_data = []
        result = proc.FileProcessor.read_employee_data_from_file("error_file.json", employee_data, Employee)

        self.assertEqual(result, employee_data)  # No data should be added
        mock_output.assert_called_once_with("There was a non-specific error!", mock_file.side_effect)

    @patch("builtins.open", new_callable=mock_open)
    def test_write_employee_data_to_file_valid(self, mock_file):
        employee_data = [Employee("John", "Doe", "2024-12-09", 4)]
        proc.FileProcessor.write_employee_data_to_file("EmployeeRatings.json", employee_data)

        mock_file.assert_called_once_with("EmployeeRatings.json", "w")
        handle = mock_file()
        written_data = json.loads(handle.write.call_args[0][0])  # Extracting written data from the mock
        self.assertEqual(len(written_data), 1)
        self.assertEqual(written_data[0]["FirstName"], "John")
        self.assertEqual(written_data[0]["LastName"], "Doe")
        self.assertEqual(written_data[0]["ReviewDate"], "2024-12-09")
        self.assertEqual(written_data[0]["ReviewRating"], 4)

    @patch("builtins.open", new_callable=mock_open)
    @patch.object(pres.IO, 'output_error_messages')  # Mock IO error handling
    def test_write_employee_data_to_file_type_error(self, mock_output, mock_file):
        # Passing invalid data (for example, passing a string instead of an object)
        employee_data = ["Invalid Data"]

        proc.FileProcessor.write_employee_data_to_file("EmployeeRatings.json", employee_data)

        mock_output.assert_called_once_with("Please check that the data is a valid JSON format", mock_file.side_effect)

    @patch("builtins.open", new_callable=mock_open)
    @patch.object(pres.IO, 'output_error_messages')  # Mock IO error handling
    def test_write_employee_data_to_file_permission_error(self, mock_output, mock_file):
        mock_file.side_effect = PermissionError("Permission denied")
        employee_data = [Employee("John", "Doe", "2024-12-09", 4)]

        proc.FileProcessor.write_employee_data_to_file("EmployeeRatings.json", employee_data)

        mock_output.assert_called_once_with("Please check the data file's read/write permission", mock_file.side_effect)

    @patch("builtins.open", new_callable=mock_open)
    @patch.object(pres.IO, 'output_error_messages')  # Mock IO error handling
    def test_write_employee_data_to_file_generic_error(self, mock_output, mock_file):
        mock_file.side_effect = Exception("Unknown error")
        employee_data = [Employee("John", "Doe", "2024-12-09", 4)]

        proc.FileProcessor.write_employee_data_to_file("EmployeeRatings.json", employee_data)

        mock_output.assert_called_once_with("There was a non-specific error!", mock_file.side_effect)


if __name__ == '__main__':
    unittest.main()
