from dot import Dot
from utils import validate_measure

class Rectangle(Dot):
    """
    A class representing a rectangle in a two-dimensional coordinate system.

    Attributes:
    - x (float): The x-coordinate of the centerposition
    - y (float): The y-coordinate of the centerposition
    - width (float): The width of the rectangle
    - height (float): The height of the rectangle
    - area (float): The area of the rectangle created by multipying height and width of the rectangle
    - perimeter (float): The perimeter of the rectangle created by adding all sides together

    Operators
    - '==', '>', '>=', '<', '<='
    - To compare rectangles the operator first checks the area for comparance. If the area are the same it checks perimeter for comparance.
    Only a Rectangle who have the same area and perimeter are equal.
    
    Methods:
    - is_squer(): Checks is the rectangle is a squer
    - position(): Gives the coordinates of the centerposition as a tuple
    - translate(): Moves the rectangles centerposition in the coordinate system.
    - corner_position() Gives the lower left corner-coordinates as a tuple
    
    Example usage:
    >>> rect1 = Rectangle(x=1, y=2, width=4, height=6)
    >>> rect2 = Rectangle(x=3, y=4, width=3, height=8)
    >>> rect1.is_squer()
    False
    >>> rect1 < rect2
    >>> rect1.corner_position()
    (-1, -1)
    >>> rect1.position()
    (1, 2)
    >>> rect1.translate(2, 4)
    (3, 6)
    """
    def __init__(self, x: int|float=0, y: int|float=0, width: int|float=1, height: int|float=1) -> None:
        super().__init__(x, y)
        self.width = width
        self.height = height
    
    # Setters and getters
    @property
    def width(self) -> float:
        return self._width
    
    @width.setter
    def width(self, other_width) -> None:
        validate_measure(other_width)
        self._width = float(other_width)
    
    @property
    def height(self) -> float:
        return self._height

    @height.setter
    def height(self, other_height) -> None:
        validate_measure(other_height)
        self._height = float(other_height)

    @property
    def area(self) -> float:
        return self.width*self.height
    
    @property
    def perimeter(self) -> float:
        return self.width*2+self.height*2
    
    # Dundermethods
    def __repr__(self) -> str:
        return f"x={self.x} y={self.y}, height:{self.height}, width:{self.width}"
    
    def __str__(self) -> str:
        return f"A Rectangle with height {self.height} and width {self.width} and a centerposition at ({self.x}, {self.y})"
    
    # Methods
    def is_squer(self) -> bool: # Determins if all sides are equal and return True or False
        if self.height == self.width:
            return True
        else:
            return False
        
    def corner_position(self) -> tuple: # Calculate the coordinates of the left bottom corner of the rectangle
        corner_x = self.x - (self.width/2)
        corner_y = self.y - (self.height/2)
        return (corner_x, corner_y)
    