# ------------------------------------------------------------------------------------------------- #
# Title: test_presentation_classes.py
# Description: The test harness for presentation classes
# ChangeLog: (Who, When, What)
# AdamSavage,20241208,Created script from ChatGPT suggestions
# ------------------------------------------------------------------------------------------------- #

import unittest
from unittest.mock import patch
from data_classes import Employee  # Assuming Employee class is imported from data_classes module
from presentation_classes import IO  # Assuming IO class is in the presentation_classes module


class TestIO(unittest.TestCase):

    # Test output_error_messages method
    @patch("builtins.print")
    def test_output_error_messages(self, mock_print):
        message = "An error occurred!"
        error = Exception("Error details")

        # Call the function with a message and an error
        IO.output_error_messages(message, error)

        # Check that the correct error message was printed
        mock_print.assert_any_call(message)
        mock_print.assert_any_call("-- Technical Error Message --")
        mock_print.assert_any_call(f"{error}\nNone\n{type(error)}")

    # Test output_error_messages method when no error is provided
    @patch("builtins.print")
    def test_output_error_messages_no_error(self, mock_print):
        message = "An error occurred!"

        # Call the function with a message and no error
        IO.output_error_messages(message)

        # Check that the correct message was printed
        mock_print.assert_any_call(message)
        mock_print.assert_any_call("\n")

    # Test output_menu method
    @patch("builtins.print")
    def test_output_menu(self, mock_print):
        menu = "1. Option 1\n2. Option 2\n3. Option 3"

        # Call the function with the menu string
        IO.output_menu(menu)

        # Check that the menu is printed
        mock_print.assert_any_call(menu)

    # Test input_menu_choice method with valid input
    @patch("builtins.input", return_value="2")
    def test_input_menu_choice_valid(self, mock_input):
        # Call the function and get the choice
        choice = IO.input_menu_choice()

        # Check that the choice is correct
        self.assertEqual(choice, "2")

    # Test input_menu_choice method with invalid input
    @patch("builtins.input", return_value="5")  # Invalid choice
    @patch("presentation_classes.IO.output_error_messages")
    def test_input_menu_choice_invalid(self, mock_output, mock_input):
        # Call the function and get the choice
        choice = IO.input_menu_choice()

        # Check that the error message is called
        mock_output.assert_called_once_with("Please, choose only 1, 2, 3, or 4")
        self.assertEqual(choice, "0")  # Default invalid choice

    # Test output_employee_data method
    @patch("builtins.print")
    def test_output_employee_data(self, mock_print):
        # Create mock employee data
        employee_data = [
            Employee("John", "Doe", "2024-01-01", 5),
            Employee("Jane", "Doe", "2024-01-02", 4)
        ]

        # Call the function to output employee data
        IO.output_employee_data(employee_data)

        # Check that the data is printed in the correct format
        mock_print.assert_any_call(" John Doe is rated as 5 (Leading)")
        mock_print.assert_any_call(" Jane Doe is rated as 4 (Strong)")

    # Test input_employee_data method with valid input
    @patch("builtins.input", side_effect=["John", "Doe", "2024-01-01", "5"])
    def test_input_employee_data_valid(self, mock_input):
        employee_data = []

        # Call the function
        result = IO.input_employee_data(employee_data, Employee)

        # Check that the employee data is correctly appended
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].first_name, "John")
        self.assertEqual(result[0].last_name, "Doe")
        self.assertEqual(result[0].review_date, "2024-01-01")
        self.assertEqual(result[0].review_rating, 5)

    # Test input_employee_data method with invalid review rating
    @patch("builtins.input", side_effect=["John", "Doe", "2024-01-01", "invalid"])
    @patch("presentation_classes.IO.output_error_messages")
    def test_input_employee_data_invalid_rating(self, mock_output, mock_input):
        employee_data = []

        # Call the function
        result = IO.input_employee_data(employee_data, Employee)

        # Check that the error message is printed for invalid input
        mock_output.assert_called_once_with('That value is not the correct type of data!', mock_input.side_effect)
        self.assertEqual(len(result), 0)  # No data should be appended due to the error

    # Test input_employee_data method with a general exception
    @patch("builtins.input", side_effect=Exception("Unexpected error"))
    @patch("presentation_classes.IO.output_error_messages")
    def test_input_employee_data_general_exception(self, mock_output, mock_input):
        employee_data = []

        # Call the function
        result = IO.input_employee_data(employee_data, Employee)

        # Check that the non-specific error message is printed
        mock_output.assert_called_once_with("There was a non-specific error!", mock_input.side_effect)
        self.assertEqual(len(result), 0)  # No data should be appended due to the error


if __name__ == '__main__':
    unittest.main()
