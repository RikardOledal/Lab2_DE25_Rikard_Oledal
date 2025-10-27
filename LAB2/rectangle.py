from dot import Dot
from utils import validate_measure

class Rectangle(Dot):
    def __init__(self, x: int|float, y: int|float, width: int|float, height: int|float) -> None:
        super().__init__(x, y)
        self.width = width
        self.height = height
        self.area = self.width*self.height
        self.perimeter = self.width*2+self.height*2

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