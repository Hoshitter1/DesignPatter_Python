from enum import Enum
from math import *


class CoordinateSystem(Enum):
    CARTESIAN = 1
    POLAR = 2
    """Issue1 you have to add here every time you want to add something. 
    """


class Point:
    def __init__(self, a, b, system):
        """Issue2 Implementing this way, you have to somehow figure out what are a and b"""
        if system == CoordinateSystem.CARTESIAN:
            self.x = a
            self.y = b
        if system == CoordinateSystem.POLAR:
            self.x = a * cos(a)
            self.y = b * sin(b)
        """Issue3 you have to add here every time you want to add something. 
        """

    def __repr__(self):
        return f'Point(x={self.x}, y={self.y})'


if __name__ == '__main__':
    p = Point(1, 2, CoordinateSystem.CARTESIAN)
    p2 = Point(1, 2, CoordinateSystem.POLAR)
    print(p)
    print(p2)
