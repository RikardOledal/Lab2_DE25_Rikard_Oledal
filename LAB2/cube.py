from dot import Dot
from utils import validate_measure, validate_class, validate_cube

class Cube(Dot):
    def __init__(self, x: int|float, y: int|float, size: int|float):
        super().__init__(x, y)
        self.size = size

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, other_size):
        validate_measure(other_size)
        self._size = float(other_size)
        self._depth = float(other_size)
        self._height = float(other_size)
        self._width = float(other_size)
    
    @property
    def width(self):
        return self._width
    
    @width.setter
    def width(self, other_width):
        validate_cube(self.size, other_width)
        self._width = float(other_width)

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, other_height):
        validate_cube(self.size, other_height)
        self._height = float(other_height)

    @property
    def depth(self):
        return self._depth

    @depth.setter
    def depth(self, other_depth):
        validate_cube(self.size, other_depth)
        self._depth = float(other_depth)

    @property
    def area(self):
        return 6 * self.size**2
    
    @property
    def perimeter(self):
        return 12 * self.size
        
    @property
    def volume(self):
        return self.size**3
    
    def __repr__(self) -> str:
        return f"x={self.x} y={self.y}, height:{self.height}, width:{self.width}, depth:{self.width}"
    
    def __str__(self) -> str:
        return f"A Cube with height, width and depth of {self.size} and a centerposition at ({self.x}, {self.y})"
    
    def __eq__(self, other) -> bool:
        if not isinstance(other, Cube):
            return False
        elif self.size == other.size:
            return True
        else:
            return False
        
    def __lt__(self, other) -> bool:
        validate_class(self, other)
        if self.size < other.size:
            return True
        else:
            return False
    
    def __le__(self, other) -> bool:
        validate_class(self, other)
        if self.size <= other.size:
            return True
        else:
            return False
        
    def __gt__(self, other) -> bool:
        validate_class(self, other)
        if self.size > other.size:
            return True
        else:
            return False
        
    def __ge__(self, other) -> bool:
        validate_class(self, other)
        if self.size >= other.size:
            return True
        else:
            return False