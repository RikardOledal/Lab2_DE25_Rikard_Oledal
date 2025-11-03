from numbers import Number
from utils import validate_xy

class Dot:
    def __init__(self, x: int|float, y: int|float) -> None:
        self.y = y
        self.x = x

    @property
    def x(self):
        return self._x
    
    @x.setter
    def x(self, other_x):
        validate_xy(other_x)
        self._x = float(other_x)

    @property
    def y(self):
        return self._y
    
    @y.setter
    def y(self, other_y):
        validate_xy(other_y)
        self._y = float(other_y)

    def __repr__(self) -> str:
        return f"x={self.x} y={self.y}"
    
    def __str__(self) -> str:
        return f"A dot with position ({self.x}, {self.y})"

    def translate(self, new_x: int|float, new_y: int|float) -> None:
        validate_xy(new_x)
        validate_xy(new_y)
        x_add = float(new_x) + self.x
        y_add = float(new_y) + self.y
        self._x = x_add
        self._y = y_add
        return self.position()

    def position(self) -> tuple:
        position_tp = (self.x, self.y)
        return tuple(position_tp)

