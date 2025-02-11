#!/usr/bin/python3
"""Student to JSON with filter"""


class Student:
    """Define Class Student"""

    def __init__(self, first_name, last_name, age):
        """
        Public instance attributes

        Args:
            first_name (str): public attribute
            last_name (str): public attribute
            age (int): publlic attribute
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Public method that retrieves a dictionnary representation
        of a Student instance

        Args:
            attrs: A list of strings in which
            only attribute names must be retrieved

        Return:
            dict: A dictionnary representation of the Student instance
        """
        if attrs is None:
            return self.__dict__.copy()
        else:
            student_dict = {}
            for attr in attrs:
                if hasattr(self, attr):
                    student_dict[attr] = getattr(self, attr)
            return student_dict

    def reload_from_json(self, json):
        """
        Function that replaces all attributes of the Student instance

        Args:
            json: A dictionnary
            key: The public attribute name
            value: Value of the public attribute
        """
        for key, value in json.items():
            setattr(self, key, value)
        return self
