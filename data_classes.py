# ------------------------------------------------------------------------------------------------- #
# Title: data_classes.py
# Description: The module of data classes
# ChangeLog: (Who, When, What)
# AdamSavage,20241208,Created module
# ------------------------------------------------------------------------------------------------- #

from datetime import date

MENU: str = '''
---- Employee Ratings ------------------------------
  Select from the following menu:
    1. Show current employee rating data.
    2. Enter new employee rating data.
    3. Save data to a file.
    4. Exit the program.
--------------------------------------------------
'''

employees: list = []  # a table of employees data


class Person:
    """
    A class representing person data.

    Properties:
    - first_name (str): The person's first name.
    - last_name (str): The person's last name.

    ChangeLog:
    - RRoot, 1.1.2030: Created the class.
    """

    def __init__(self, first_name: str = "", last_name: str = ""):
        """
        Initializes a new Person instance with optional first and last names.

        Args:
            first_name (str): The first name of the person (default is an empty string).
            last_name (str): The last name of the person (default is an empty string).
        """
        self.first_name = first_name
        self.last_name = last_name

    @property
    def first_name(self):
        """
        Gets the first name of the person, capitalized.

        Returns:
            str: The person's first name with the first letter capitalized.
        """
        return self.__first_name.title()

    @first_name.setter
    def first_name(self, value: str):
        """
        Sets the first name of the person after validating that it does not contain numbers.

        Args:
            value (str): The first name to set.

        Raises:
            ValueError: If the first name contains any numeric characters.
        """
        if value.isalpha() or value == "":
            self.__first_name = value
        else:
            raise ValueError("The first name should not contain numbers.")

    @property
    def last_name(self):
        """
        Gets the last name of the person, capitalized.

        Returns:
            str: The person's last name with the first letter capitalized.
        """
        return self.__last_name.title()

    @last_name.setter
    def last_name(self, value: str):
        """
        Sets the last name of the person after validating that it does not contain numbers.

        Args:
            value (str): The last name to set.

        Raises:
            ValueError: If the last name contains any numeric characters.
        """
        if value.isalpha() or value == "":
            self.__last_name = value
        else:
            raise ValueError("The last name should not contain numbers.")

    def __str__(self):
        """
        Returns a string representation of the person.

        Returns:
            str: A string containing the person's first name and last name.
        """
        return f"{self.first_name},{self.last_name}"


class Employee(Person):
    """
    A class representing employee data.

    Properties:
    - first_name (str): The employee's first name.
    - last_name (str): The employee's last name.
    - review_date (date): The data of the employee review.
    - review_rating (int): The review rating of the employee's performance (1-5)

    ChangeLog:
    - RRoot, 1.1.2030: Created the class.
    """

    def __init__(self, first_name: str = "", last_name: str = "", review_date: str = "1900-01-01",
                 review_rating: int = 3):
        """
        Initializes a new Employee instance with optional review date and review rating.

        Args:
            first_name (str): The first name of the employee (default is an empty string).
            last_name (str): The last name of the employee (default is an empty string).
            review_date (str): The date of the employee's review (default is '1900-01-01').
            review_rating (int): The employee's review rating, an integer between 1 and 5 (default is 3).
        """
        super().__init__(first_name=first_name, last_name=last_name)
        self.review_date = review_date
        self.review_rating = review_rating

    @property
    def review_date(self):
        """
        Gets the review date of the employee.

        Returns:
            str: The date of the employee's review, formatted as YYYY-MM-DD.
        """
        return self.__review_date

    @review_date.setter
    def review_date(self, value: str):
        """
        Sets the review date of the employee after validating the date format.

        Args:
            value (str): The review date to set, in the format YYYY-MM-DD.

        Raises:
            ValueError: If the date format is incorrect (not in YYYY-MM-DD format).
        """
        try:
            date.fromisoformat(value)
            self.__review_date = value
        except ValueError:
            raise ValueError("Incorrect data format, should be YYYY-MM-DD")

    @property
    def review_rating(self):
        """
        Gets the review rating of the employee.

        Returns:
            int: The employee's review rating (an integer between 1 and 5).
        """
        return self.__review_rating

    @review_rating.setter
    def review_rating(self, value: str):
        """
        Sets the review rating of the employee after validating it is between 1 and 5.

        Args:
            value (int): The review rating to set, must be between 1 and 5.

        Raises:
            ValueError: If the review rating is not between 1 and 5.
        """
        if value in (1, 2, 3, 4, 5):
            self.__review_rating = value
        else:
            raise ValueError("Please choose only values 1 through 5")

    def __str__(self):
        """
        Returns a string representation of the employee.

        Returns:
            str: A string containing the employee's first name, last name, review date, and review rating.
        """
        return f"{self.first_name},{self.last_name},{self.review_date},{self.__review_rating}"
