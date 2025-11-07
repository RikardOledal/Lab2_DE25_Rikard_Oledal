from numbers import Number
from utils import validate_xy, validate_class

class Dot:
    """
    A class representing a dot in a two-dimensional coordinate system.

    Attributes:
    - x (float): The x-coordinate
    - y (float): The y-coordinate

    Methods:
    - translate(): Moves the dot in the coordinate system.
    - position(): Gives the coordinates as a tuple

    Example usage:
    >>> dot1 = Dot(1, 2)
    >>> dot1.position()
    (1, 2)
    >>> dot1.translate(2, 4)
    (3, 6)
    """
    def __init__(self, x: int|float=0, y: int|float=0) -> None:
        self.y = y
        self.x = x

    # Setters and getters
    @property
    def x(self) -> float:
        return self._x
    
    @x.setter
    def x(self, other_x) -> None:
        validate_xy(other_x)
        self._x = float(other_x)

    @property
    def y(self) -> float:
        return self._y
    
    @y.setter
    def y(self, other_y) -> None:
        validate_xy(other_y)
        self._y = float(other_y)

    @property
    def area(self) -> float:
        return 0

    @property
    def perimeter(self):
        return 0

    # Dundermethods   
    def __repr__(self) -> str:
        return f"x={self.x} y={self.y}"
    
    def __str__(self) -> str:
        return f"A dot with position ({self.x}, {self.y})"
    
    # Operators overload   
    def __eq__(self, other) -> bool:
        if not isinstance(other, type(self)):
            return False
        elif other.area == self.area and other.perimeter == self.perimeter:
            return True
        else:
            return False
        
    def __lt__(self, other) -> bool:
        validate_class(other)
        if self.area < other.area:
            return True
        elif self.area == other.area and self.perimeter < other.perimeter:
            return True
        else:
            return False
    
    def __le__(self, other) -> bool:
        validate_class(other)
        if self.area < other.area:
            return True
        elif self.area == other.area and self.perimeter <= other.perimeter:
            return True
        else:
            return False
        
    def __gt__(self, other) -> bool:
        validate_class(other)
        if self.area > other.area:
            return True
        elif self.area == other.area and self.perimeter > other.perimeter:
            return True
        else:
            return False
        
    def __ge__(self, other) -> bool:
        validate_class(other)
        if self.area > other.area:
            return True
        elif self.area == other.area and self.perimeter >= other.perimeter:
            return True
        else:
            return False
    
    # Methods
    def translate(self, new_x: int|float=0, new_y: int|float=0) -> tuple: # Moves centerposition and return new centerposition as a Tuple
        validate_xy(new_x)
        validate_xy(new_y)
        x_add = float(new_x) + self.x
        y_add = float(new_y) + self.y
        self._x = x_add
        self._y = y_add
        return self.position()

    def position(self) -> tuple: # Return centerposition as a Tuple
        position_tp = (self.x, self.y)
        return tuple(position_tp)

