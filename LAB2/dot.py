from numbers import Number

class Dot:
    def __init__(self, x: int|float, y: int|float) -> None:
        self.x = x
        self.y = y

    @property
    def x(self):
        return self._x
    
    @x.setter
    def x(self, other_x):
        if not isinstance(other_x, Number):
            raise TypeError(f"x should be int or float. Not {type(other_x)}")
        self._x = float(other_x)

    @property
    def y(self):
        return self._y
    
    @y.setter
    def y(self, other_y):
        if not isinstance(other_y, Number):
            raise TypeError(f"y should be int or float. Not {type(other_y)}")
        self._y = float(other_y)

    def __repr__(self) -> str:
        return f"x={self.x} y={self.y}"
    
    def __str__(self) -> str:
        return f"A dot with position ({self.x}, {self.y})"

    def translate(self, new_x: int|float, new_y: int|float) -> None:
        self.x = float(new_x)
        self.y = float(new_y)

    def position(self):
        position_tp = (self.x, self.y)
        return position_tp

