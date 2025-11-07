from dot import Dot
from utils import validate_measure, validate_class
import math

class Circle(Dot):
    """
    A class representing a circle in a two-dimensional coordinate system.

    Attributes:
    - x (float): The x-coordinate of the centerposition
    - y (float): The y-coordinate of the centerposition
    - radius (float): The radius of the circle
    - area (float): The area of the circle created by formula ( π * radius^2 )
    - perimeter (float): The perimeter of the circle created by formula ( π * 2 * radius )

    Operators
    - '==', '>', '>=', '<', '<='
    - To compare circles the operator checks the radius for comparance
    
    Methods:
    - is_unitcircle(): Checks if the circle has radius 1 and coordinates (0, 0)
    - translate(): Moves the circle centerposition in the coordinate system.
    - position(): Gives the coordinates of the centerposition as a tuple

    Example usage:
    >>> circ1 = Circle(x=0, y=0, radius=1)
    >>> circ2 = Circle(x=2, y=3, radius=3)
    >>> circ1.is_unitcircle()
    True
    >>> circ1 < circ2
    True
    >>> circ2.position()
    (3.0, 4.0)
    >>> circ2.translate(-1, 2)
    (1.0, 5.0)
    """
    def __init__(self, radius: int|float=1, x: int|float =0, y: int|float =0) -> None:
        super().__init__(x, y)
        self.radius = radius
    
    @property
    def radius(self) -> float:
        return self._radius

    @radius.setter
    def radius(self, other_radius) -> None:
        validate_measure(other_radius)
        self._radius = float(other_radius)

    @property
    def area(self) -> float:
        return math.pi * self.radius**2
    
    @property
    def perimeter(self) -> float:
        return self.radius * math.pi * 2
    
    def __repr__(self) -> str:
        return f"x={self.x} y={self.y} radius:{self.radius}"
    
    def __str__(self) -> str:
        return f"A Circle with radius {self.radius} and a centerposition at ({self.x}, {self.y})"
    
    def is_unitcircle(self) -> bool:
        if self.x == self.y == 0.0 and self.radius == float(1):
            return True
        else:
            return False