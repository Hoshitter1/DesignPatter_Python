"""
To understand why we need this, refer to
1. factory_method_bad_practice.py
2. issue_and_solution.md.
"""

from math import *


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Point(x={self.x}, y={self.y})'

    @classmethod
    def new_cartesian_point(cls, x, y):
        return cls(x, y)

    @classmethod
    def new_polar_point(cls, rho, theta):
        return cls(rho * cos(theta), rho * sin(rho))


if __name__ == '__main__':
    p = Point.new_cartesian_point(1, 2)
    p2 = Point.new_polar_point(1, 2)
    print(p)
    print(p2)
