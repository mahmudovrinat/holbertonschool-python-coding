#!/usr/bin/python3
"""This module defines a class Square that represents a square."""


class Square:
    """This class defines a square with a private size attribute."""

    def __init__(self, size):
        """Initialize the square with a given size.

        Args:
            size (any): The size of the square (no type or value check).
        """
        self.__size = size
