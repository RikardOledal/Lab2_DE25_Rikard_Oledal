from dot import Dot
from rectangle import Rectangle
from utils import validate_measure, validate_class, validate_cube, validate_xy

class Cube(Dot):
    """
    A class representing a cube in a three-dimensional coordinate system.

    Attributes:
    - x (float): The x-coordinate of the centerposition
    - y (float): The y-coordinate of the centerposition
    - z (float): The z-coordinate of the centerposition
    - size (float): Representing the size of width, height and depth since they should be the same in a cube
    - width (float): The width of the cube
    - height (float): The height of the cube
    - depth (float): The depth of the cube
    - area (float): The area of all 6 sides of the cube.
    - perimeter (float): The perimeter of the cube by adding all 12 edges.
    - volume (float): The volume of the cube by multiplying width, depth and height

    Operators
    - '==', '>', '>=', '<', '<='
    - To compare cube the operator checks the size for comparance
    
    Methods:
    - translate(): Moves the cube centerposition in the coordinate system.
    - position(): Gives the coordinates of the centerposition as a tuple

    Example usage:
    >>> cube1 = Cube(size=1,x=2,z=3)
    >>> cube2 = Cube(x=3, y=4, size=2, z=1)
    >>> cube1 < cube2
    True
    >>> cube1.position()
    (2.0, 0.0, 3.0)
    >>> cube1.translate(-1, 2, 4)
    (1.0, 2.0, 7.0)
    """
    def __init__(self, size: int|float=1, x: int|float=0, y: int|float=0, z: int|float=0,):
        super().__init__(x, y)
        self.size = size
        self.z = z
        self.rectangle = Rectangle(self.x,self.y,self.width,self.height)

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
    def z(self) -> float:
        return self._z
    
    @z.setter
    def z(self, other_z) -> None:
        validate_xy(other_z)
        self._z = float(other_z)

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
        return f"x={self.x} y={self.y} z={self.z}, height:{self.height}, width:{self.width}, depth:{self.width}"
    
    def __str__(self) -> str:
        return f"A Cube with height, width and depth of {self.size} and a centerposition at ({self.x}, {self.y}, {self.z})"
        
    def position(self) -> tuple:
        position_tp = (self.x, self.y, self.z)
        return tuple(position_tp)
    
    def translate(self, new_x: int|float=0, new_y: int|float=0, new_z: int|float=0) -> tuple:
        validate_xy(new_x)
        validate_xy(new_y)
        validate_xy(new_z)
        x_add = float(new_x) + self.x
        y_add = float(new_y) + self.y
        z_add = float(new_z) + self.z
        self._x = x_add
        self._y = y_add
        self._z = z_add
        return self.position()
