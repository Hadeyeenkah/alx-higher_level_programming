#!/usr/bin/python3
"""Define a magicClass matching exactly provided by Alx."""


import math

class MagicClass:
    """Represent a Circle."""

    def __init__(self, radius=0):
        """initialize a MagicClass.
        Arg:
        radius (float or int): Then radius of the new MagicClass.
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.radius = radius

    def area(self):
        """Return the area of the MagicClass."""
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """Return the circumference of the MagicClass."""
        return 2 * math.pi * self.__radius)
