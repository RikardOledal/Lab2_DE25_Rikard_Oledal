from circle import Circle
import math

class Sphere(Circle):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self._area = 4 * math.pi * self.radius**2
        self._volym = (4 * math.pi * self.radius**3)/3
    
    @property
    def volym(self):
        return self._volym
    
    @property
    def perimeter(self) -> None:
        NotImplemented
    
    def is_unitcircle(self) -> None:
        NotImplemented

    def is_unitsphere(self) -> bool:
        if self.x == self.y == 0.0:
            return True
        else:
            return False
        
        
        
        