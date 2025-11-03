from dot import Dot
from utils import validate_measure, validate_class
import math

class Circle(Dot):
    def __init__(self, radius: int|float, x: int|float =0, y: int|float =0) -> None:
        super().__init__(x, y)
        self.radius = radius
        self._area = math.pi * self.radius**2
        self._perimeter = self.radius * math.pi * 2
    
    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, other_radius):
        validate_measure(other_radius)
        self._radius = float(other_radius)

    @property
    def area(self):
        return self._area
    
    @property
    def perimeter(self):
        return self._perimeter
    
    def __repr__(self) -> str:
        return f"x={self.x} y={self.y} radius:{self.radius}"
    
    def __str__(self) -> str:
        return f"A Circle with radius {self.radius} and a centerposition at ({self.x}, {self.y})"
    
    def __eq__(self, other) -> bool:
        if not isinstance(other, Circle):
            return False
        elif not other.area == self._area:
            return False
        else:
            return True
        
    def __lt__(self, other) -> bool:
        validate_class(self, other)
        if self.area < other.area:
            return True
        else:
            return False
    
    def __le__(self, other) -> bool:
        validate_class(self, other)
        if self.area <= other.area:
            return True
        else:
            return False
        
    def __gt__(self, other) -> bool:
        validate_class(self, other)
        if self.area > other.area:
            return True
        else:
            return False
        
    def __ge__(self, other) -> bool:
        validate_class(self, other)
        if self.area >= other.area:
            return True
        else:
            return False

    def is_unitcircle(self) -> bool:
        if self.x == self.y == 0.0 and self.radius == float(1):
            return True
        else:
            return False