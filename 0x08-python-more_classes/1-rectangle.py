#!/usr/bin/python3
# 1-rectangle.py
"""Defines a rectangle class"""


class Rectangle:
    """Represent a new rectangle."""

    def __init__(self, width=0, height=0):
      """Initialize a new Rectangle"""
      self.width = width
      self.height = height


    @property
    def width(self):
        """Get/set the width of the rectangle."""
        return self.width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("Width must be an integer")
        
        if values < 0:
            raise ValueError("Width must be >= 0")
        self.__width = value


    @height
    def height(self):
        """Get/set the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("Height must be an integer")

        if value < 0:
            raise ValueError("Height must be >= 0"
        self.__height = value
