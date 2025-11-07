from matplotlib import pyplot as plt
from matplotlib import patches as patches
from rectangle import Rectangle
from circle import Circle
from dot import Dot
from cube import Cube
from sphere import Sphere
import matplotlib.ticker as ticker


class Shape2dPlotter():
    """
    A class that takes in shapes and plot them in a coordinate system. If the shape is a 3d-shape it gonna plot it as a 2d-shape

    Colors
    Dots = Blue
    Circles = Orange with no background
    Spheres = Orange with yellow background
    Rectangles = Red with no background
    Cubes = Red with pink background

    Attributes:
    - Shapes = Should be of classes Dot, Circle, Sphere, Rectangle or Cube.
    
    Methods:
    - plot(): Plots all shapes in a coordinate system.

    """
    def __init__(self, *shapes: Dot|Circle|Sphere|Rectangle|Cube) -> None:
        if len(shapes) == 0:
            raise ValueError("must be 1 or more shapes")
        
        self.limits = {"min":0.0, "max":0.0}
        self._dots = []
        self._circles = []
        self._spheres = []
        self._rectangles = []
        self._cubes = []

        # Sorting all shapes into lists and adjusting limits to fit the shapes
        for shape in shapes:
            if type(shape) == Dot:
                if shape.x > self.limits["max"]: self.limits["max"] = shape.x
                if shape.x < self.limits["min"]: self.limits["min"] = shape.x
                if shape.y > self.limits["max"]: self.limits["max"] = shape.y
                if shape.y < self.limits["min"]: self.limits["min"] = shape.y

                self._dots.append(shape)
            
            elif type(shape) == Circle:
                
                if shape.x + shape.radius > self.limits["max"]: self.limits["max"] = shape.x + shape.radius
                if shape.x - shape.radius < self.limits["min"]: self.limits["min"] = shape.x - shape.radius
                if shape.y + shape.radius > self.limits["max"]: self.limits["max"] = shape.y + shape.radius
                if shape.y - shape.radius < self.limits["min"]: self.limits["min"] = shape.y - shape.radius

                self._circles.append(shape)

            elif type(shape) == Sphere:
                
                if shape.x + shape.radius > self.limits["max"]: self.limits["max"] = shape.x + shape.radius
                if shape.x - shape.radius < self.limits["min"]: self.limits["min"] = shape.x - shape.radius
                if shape.y + shape.radius > self.limits["max"]: self.limits["max"] = shape.y + shape.radius
                if shape.y - shape.radius < self.limits["min"]: self.limits["min"] = shape.y - shape.radius

                self._spheres.append(shape.circle)

            elif type(shape) == Rectangle:
                if shape.x + (shape.width/2) > self.limits["max"]: self.limits["max"] = shape.x + (shape.width/2)
                if shape.x - (shape.width/2) < self.limits["min"]: self.limits["min"] = shape.x - (shape.width/2)
                if shape.y + (shape.width/2) > self.limits["max"]: self.limits["max"] = shape.y + (shape.width/2)
                if shape.y - (shape.width/2) < self.limits["min"]: self.limits["min"] = shape.y - (shape.width/2)

                self._rectangles.append(shape)

            elif type(shape) == Cube:
                if shape.x + (shape.width/2) > self.limits["max"]: self.limits["max"] = shape.x + (shape.width/2)
                if shape.x - (shape.width/2) < self.limits["min"]: self.limits["min"] = shape.x - (shape.width/2)
                if shape.y + (shape.width/2) > self.limits["max"]: self.limits["max"] = shape.y + (shape.width/2)
                if shape.y - (shape.width/2) < self.limits["min"]: self.limits["min"] = shape.y - (shape.width/2)

                self._cubes.append(shape.rectangle)

    
    def plot(self):
        # Create limit for coordinate system
        limit = round((max([abs(self.limits["min"]),abs(self.limits["max"])]) + 2)/10)*10
        dot_size = limit/100

        maxlimit = limit
        minlimit = maxlimit*-1

        # Create the coordinate system
        fig, ax = plt.subplots(1)
        ax.set(
            title=f"{len(self._dots)+len(self._circles)+len(self._spheres)+len(self._rectangles)+len(self._cubes)} shapes",
            xlim=(minlimit, maxlimit),
            ylim=(minlimit, maxlimit),
        )
        # Determins the scale for x and y axis
        ax.yaxis.set_major_locator(ticker.MultipleLocator(2))
        ax.xaxis.set_major_locator(ticker.MultipleLocator(2))

        # Move the spines to get a centered 0-position
        ax.spines["left"].set_position("zero")
        ax.spines["right"].set_visible(False)
        ax.spines["bottom"].set_position("zero")
        ax.spines["top"].set_visible(False)

        # Adding grid and adjusting the box to make circles round instead of eliptic
        ax.grid(alpha=0.4)
        ax.set_aspect("equal", adjustable="box")
        
        # Adding the shapes
        for sphere in self._spheres:
            sphere_plot = patches.Circle(xy=sphere.position(), radius=sphere.radius, edgecolor="orange", facecolor="yellow", linewidth=2, alpha=0.5)
            fig.gca().add_patch(sphere_plot)

        for cube in self._cubes:
            cube_plot = patches.Rectangle(xy=cube.corner_position(), width=cube.width, height=cube.height, edgecolor="red", facecolor="pink", linewidth=2, alpha=0.7)
            fig.gca().add_patch(cube_plot)

        for circle in self._circles:
            circ_plot = patches.Circle(xy=circle.position(), radius=circle.radius, edgecolor="orange", facecolor="none", linewidth=2)
            fig.gca().add_patch(circ_plot)

        for rectangle in self._rectangles:
            rect_plot = patches.Rectangle(xy=rectangle.corner_position(), width=rectangle.width, height=rectangle.height, edgecolor="red", facecolor="none", linewidth=2)
            fig.gca().add_patch(rect_plot)

        for dot in self._dots:
            dot_plot = patches.Circle(xy=dot.position(), radius=dot_size, edgecolor="blue", facecolor="blue", linewidth=2 )
            fig.gca().add_patch(dot_plot)

        
