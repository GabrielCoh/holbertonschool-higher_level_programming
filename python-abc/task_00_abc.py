#!/usr/bin/python3
"""Setting up an Abstract Class and implementing its Subclasses"""


from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract class: Animal"""
    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    """Subclass Dog of the Abstract class Animal"""
    def sound(self):
        """Sound for Dog"""
        return "Bark"


class Cat(Animal):
    """Subclass Cat of the Abstract class Animal"""
    def sound(self):
        """Sound for Cat"""
        return "Meow"
