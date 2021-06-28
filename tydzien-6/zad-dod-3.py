from math import sqrt

class Point:
    def __init__(self, x, y):
        self._y = y
        self._x = x

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

class Section:
    def __init__(self, begin: Point, end: Point):
        self.end = end
        self.begin = begin

    def get_length(self):
        return sqrt((self.begin.get_x() - self.end.get_x() ) ** 2 + (self.begin.get_y() - self.end.get_y()) ** 2)

