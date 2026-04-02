#!/usr/bin/python3
"""Defines a square class"""


class Square:
    """Represent a class"""
    def __init__(self, size=0):
        """represent method"""
        self.__size = size

    @property
    def size(self):
        """retrieve size"""
        return self.__size

    @size.setter
    def size(self, value):
        """to set value instead of size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """represent method"""
        return self.__size ** 2
