#!/usr/bin/python3
"""Defines a square class"""


class Square:
    """Represent a class"""
    def __init__(self, size=0, position=(0, 0)):
        """represent method"""
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """return the position""" 
        return self.__position

    @position.setter
    def position(self, value):
        """to set the position"""
        if not isinstance(self.__position, tuple) or len(self.__position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """represent method"""
        return self.__size ** 2

    def my_print(self):
        """prINTS THE SQUARE"""
        if self.__size == 0:
            print()
            return
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)


my_square_1 = Square(3, (1, 1))
my_square_1.my_print()