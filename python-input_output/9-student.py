#!/usr/bin/python3
"""Student to JSON"""


class Student:
    """Define Class Student"""


    def __init__(self, first_name, last_name, age):
        """
        Public methode that retrieves a dictionnary representation
        of a Student instance

        Args:
            first_name (str): public attribute
            last_name (str): public attribute
            age (int): publlic attribute
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return self.__dict__
