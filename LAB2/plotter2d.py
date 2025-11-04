from matplotlib import pyplot as plt
from matplotlib import patches as patches
from rectangle import Rectangle
from circle import Circle

class Shape2dPlotter():
    def __init__(self, *shapes: Circle|Rectangle):
        if len(shapes) == 0:
            raise ValueError("must be 1 or more shapes")
        
        self.limits = {"min":0.0, "max":0.0}
        self.circles = []
        self.rectangles = []
    
        for shape in shapes:
            if type(shape) == Circle:
                
                if shape.x + shape.radius + 2 > self.limits["max"]: self.limits["max"] = shape.x + shape.radius + 2
                if shape.x - shape.radius - 2 < self.limits["min"]: self.limits["min"] = shape.x - shape.radius - 2
                if shape.y + shape.radius + 2 > self.limits["max"]: self.limits["max"] = shape.y + shape.radius + 2
                if shape.y - shape.radius - 2 < self.limits["min"]: self.limits["min"] = shape.y - shape.radius - 2

                self.circles.append(shape)

            elif type(shape) == Rectangle:
                if shape.x + (shape.width/2) + 2 > self.limits["max"]: self.limits["max"] = shape.x + (shape.width/2) + 2
                if shape.x - (shape.width/2) - 2 < self.limits["min"]: self.limits["min"] = shape.x - (shape.width/2) - 2
                if shape.y + (shape.width/2) + 2 > self.limits["max"]: self.limits["max"] = shape.y + (shape.width/2) + 2
                if shape.y - (shape.width/2) - 2 < self.limits["min"]: self.limits["min"] = shape.y - (shape.width/2) - 2

                self.rectangles.append(shape)
    
    def plot(self):
        limit = round((max([abs(self.limits["min"]),abs(self.limits["max"])]) + 5)/10)*10

        maxlimit = limit
        minlimit = maxlimit*-1

        fig, ax = plt.subplots(1)
        ax.set(
            title=f"{len(self.circles)} circles and {len(self.rectangles)} rectangles",
            xlim=(minlimit, maxlimit),
            ylim=(minlimit, maxlimit)
        )
        ax.spines["left"].set_position("zero")
        ax.spines["right"].set_visible(False)
        ax.spines["bottom"].set_position("zero")
        ax.spines["top"].set_visible(False)
        ax.grid()
        ax.set_aspect("equal", adjustable="box")


        for rectangle in self.rectangles:
            rect_plot = patches.Rectangle(xy=rectangle.corner_position(), width=rectangle.width, height=rectangle.height, edgecolor="red", facecolor="none", linewidth=2)
            fig.gca().add_patch(rect_plot)

        for circle in self.circles:
            circ_plot = patches.Circle(xy=circle.position(), radius=circle.radius, edgecolor="blue", facecolor="none", linewidth=2)
            fig.gca().add_patch(circ_plot)