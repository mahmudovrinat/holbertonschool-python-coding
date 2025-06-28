#!/usr/bin/python3
"""This module defines a Square class with size validation and area method."""


class Square:
    """Represents a square with size validation and area calculation."""

    def __init__(self, size=0):
        """Initialize the square with an optional size.

        Args:
            size (int): Size of the square. Must be >= 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """Calculate and return the current square area.

        Returns:
            int: The area of the square (size squared).
        """
        return self.__size * self.__size
