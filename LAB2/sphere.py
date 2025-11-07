from circle import Circle
import math
from utils import validate_xy

class Sphere(Circle):
    """
    A class representing a sphere in a three-dimensional coordinate system.

    Attributes:
    - x (float): The x-coordinate of the centerposition
    - y (float): The y-coordinate of the centerposition
    - z (float): The z-coordinate of the centerposition
    - radius (float): The radius of the sphere
    - area (float): The area of the sphere created by formula ( 4 * π * radius^2 )
    - volume (float): The volume of the sphere created by formula ( π * 2 * radius )
    - perimeter (float): The perimeter/circumference of the sphere created by formula ( π * 2 * radius )

    Operators
    - '==', '>', '>=', '<', '<='
    - To compare sphere the operator checks the radius for comparance
    
    Methods:
    - is_unitsphere(): Checks if the sphere has radius 1 and coordinates (0, 0)
    - translate(): Moves the sphere centerposition in the coordinate system.
    - position(): Gives the coordinates of the centerposition as a tuple

    Example usage:
    >>> sph1 = Sphere(x=0, y=0, z=0, radius=1)
    >>> sph2 = Sphere(x=2, y=3, radius=3)
    >>> sph1.is_unitsphere()
    True
    >>> sph1 < sph2
    True
    >>> sph2.position()
    (2.0, 3.0, 0.0)
    >>> sph2.translate(-1, 2, 4)
    (1.0, 5.0, 4.0)
    """
    def __init__(self, radius: int|float=1, x: int|float =0, y: int|float =0, z: int|float =0) -> None:
        super().__init__(radius, x, y)
        self.z = z
        self.circle = Circle(x=self.x,y=self.y, radius=self.radius)
    
    # Setters and getters
    @property
    def z(self) -> float:
        return self._z
    
    @z.setter
    def z(self, other_z) -> None:
        validate_xy(other_z)
        self._z = float(other_z)

    @property
    def volume(self) -> float:
        return (4 * math.pi * self.radius**3)/3
    
    @property
    def area(self) -> float:
        return 4 * math.pi * self.radius**2
    
    # Dundermethods
    def __repr__(self) -> str:
        return f"x={self.x} y={self.y} z={self.z}, radius:{self.radius}"
    
    def __str__(self) -> str:
        return f"A Sphere with radius {self.radius} and a centerposition at ({self.x}, {self.y}, {self.z})"
    
    # Methods
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

    def is_unitcircle(self) -> None: # Since its not a circle a Sphere is going to return False
        return False

    def is_unitsphere(self) -> bool: # Determins if coordinates are (0, 0, 0) and radius is 1 and returns True or False
        if self.x == self.y == self.z == 0.0 and self.radius == float(1):
            return True
        else:
            return False
        
    
        
        
        
        