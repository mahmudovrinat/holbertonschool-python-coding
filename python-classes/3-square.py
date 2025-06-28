#!/usr/bin/python3
"""This module defines a Square class with size property and area method.
"""


class Square:
    """Square with size validation, property, and area calculation."""

    def __init__(self, size=0):
        """Initialize the square with an optional size.

        Args:
            size (int): The size of the square (default 0).

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        self.size = size  # Calls the setter to validate size

    @property
    def size(self):
        """Retrieve the size of the square.

        Returns:
            int: The current size.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size with validation.

        Args:
            value (int): The new size value.

        Raises:
            TypeError: If value is not int.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current square area.

        Returns:
            int: Area of the square.
        """
        return self.__size * self.__size
