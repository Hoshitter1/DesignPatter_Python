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

    class PointFactory:
        """remove class or static method because you may want to use instance variables when initializing"""

        def new_cartesian_point(self, x, y):
            return Point(x, y)

        def new_polar_point(self, rho, theta):
            return Point(rho * cos(theta), rho * sin(rho))

    factory = PointFactory()


if __name__ == '__main__':
    p = Point.factory.new_cartesian_point(1, 2)
    p2 = Point.factory.new_polar_point(1, 2)
    print(p)
    print(p2)
