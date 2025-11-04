from dot import Dot
from utils import validate_measure, validate_class

class Rectangle(Dot):
    def __init__(self, x: int|float, y: int|float, width: int|float, height: int|float) -> None:
        super().__init__(x, y)
        self.width = width
        self.height = height
        self._perimeter = self.width*2+self.height*2

    @property
    def width(self):
        return self._width
    
    @width.setter
    def width(self, other_width):
        validate_measure(other_width)
        self._width = float(other_width)
    
    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, other_height):
        validate_measure(other_height)
        self._height = float(other_height)

    @property
    def area(self):
        return self.width*self.height
    
    @property
    def perimeter(self):
        return self.width*2+self.height*2
    
    def __repr__(self) -> str:
        return f"x={self.x} y={self.y}, height:{self.height}, width:{self.width}"
    
    def __str__(self) -> str:
        return f"A Rectangle with height {self.height} and width {self.width} and a centerposition at ({self.x}, {self.y})"
    
    def __eq__(self, other) -> bool:
        if not isinstance(other, Rectangle):
            return False
        elif other.area == self.area and other.perimeter == self.perimeter:
            return True
        else:
            return False
        
    def __lt__(self, other) -> bool:
        validate_class(self, other)
        if self.area < other.area:
            return True
        elif self.area == other.area and self.perimeter < other.perimeter:
            return True
        else:
            return False
    
    def __le__(self, other) -> bool:
        validate_class(self, other)
        if self.area < other.area:
            return True
        elif self.area == other.area and self.perimeter <= other.perimeter:
            return True
        else:
            return False
        
    def __gt__(self, other) -> bool:
        validate_class(self, other)
        if self.area > other.area:
            return True
        elif self.area == other.area and self.perimeter > other.perimeter:
            return True
        else:
            return False
        
    def __ge__(self, other) -> bool:
        validate_class(self, other)
        if self.area > other.area:
            return True
        elif self.area == other.area and self.perimeter >= other.perimeter:
            return True
        else:
            return False

    def is_squer(self) -> bool:
        if self.height == self.width:
            return True
        else:
            return False
        
    def corner_position(self) -> tuple:
        corner_x = self.x - (self.width/2)
        corner_y = self.y - (self.height/2)
        return (corner_x, corner_y)