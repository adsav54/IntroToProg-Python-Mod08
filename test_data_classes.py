# ------------------------------------------------------------------------------------------------- #
# Title: test_data_classes.py
# Description: The test harness for data classes
# ChangeLog: (Who, When, What)
# AdamSavage,20241208,Created script from ChatGPT suggestions
# ------------------------------------------------------------------------------------------------- #

import unittest
from datetime import date
from data_classes import Person, Employee

class TestPerson(unittest.TestCase):
    def test_first_name_setter_and_getter_valid(self):
        person = Person()
        person.first_name = "John"
        self.assertEqual(person.first_name, "John")

    def test_last_name_setter_and_getter_valid(self):
        person = Person()
        person.last_name = "Doe"
        self.assertEqual(person.last_name, "Doe")

    def test_first_name_setter_invalid(self):
        person = Person()
        with self.assertRaises(ValueError):
            person.first_name = "John123"  # Invalid first name with numbers

    def test_last_name_setter_invalid(self):
        person = Person()
        with self.assertRaises(ValueError):
            person.last_name = "Doe123"  # Invalid last name with numbers

    def test_str_method(self):
        person = Person("John", "Doe")
        self.assertEqual(str(person), "John,Doe")

class TestEmployee(unittest.TestCase):
    def test_employee_initialization(self):
        employee = Employee("Jane", "Smith", "2024-12-09", 4)
        self.assertEqual(employee.first_name, "Jane")
        self.assertEqual(employee.last_name, "Smith")
        self.assertEqual(employee.review_date, "2024-12-09")
        self.assertEqual(employee.review_rating, 4)

    def test_review_date_setter_valid(self):
        employee = Employee()
        employee.review_date = "2024-12-09"
        self.assertEqual(employee.review_date, "2024-12-09")

    def test_review_date_setter_invalid(self):
        employee = Employee()
        with self.assertRaises(ValueError):
            employee.review_date = "2024/12/09"  # Invalid date format

    def test_review_rating_setter_valid(self):
        employee = Employee()
        employee.review_rating = 5
        self.assertEqual(employee.review_rating, 5)

    def test_review_rating_setter_invalid(self):
        employee = Employee()
        with self.assertRaises(ValueError):
            employee.review_rating = 6  # Invalid rating (greater than 5)

    def test_str_method(self):
        employee = Employee("John", "Doe", "2024-12-09", 3)
        self.assertEqual(str(employee), "John,Doe,2024-12-09,3")

if __name__ == '__main__':
    unittest.main()