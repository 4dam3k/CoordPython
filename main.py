from sympy import *
from spb import *
import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
axis_size = 16

ticks = np.arange(-axis_size, axis_size + 0.1, axis_size * 0.125)
ax.set_xticks(ticks)
ax.set_yticks(ticks)
ax.axis([-axis_size, axis_size] * 2)
ax.grid()

rectangle_counter = 0


def PolyMaker(vertices, size):
    #   Pass Vertices as list of Point2D
    #   Vertices[0] is always the top left corner
    #   If 2 vertices are passed, first shall be top left and second shall be bottom right
    if len(vertices) == 1 and size == (0, 0):
        raise Exception("Size not passed")

    if type(size) != tuple:
        raise Exception("Size shall be a tuple")

    if len(vertices) == 1:
        vertices.append(Point(vertices[0][0] + size[0], vertices[0][1]))  # TR
        vertices.append(Point(vertices[0][0] + size[0], vertices[0][1] - size[1]))  # BR
        vertices.append(Point(vertices[0][0], vertices[0][1] - size[1]))  # BL
        return vertices

    if len(vertices) == 2:
        size = (abs(vertices[0][0] - vertices[1][0]), abs(vertices[0][1] - vertices[1][1]))
        vertices.insert(1, Point(vertices[0][0] + size[0], vertices[0][1]))  # TR
        vertices.append(Point(vertices[0][0], vertices[0][1] - size[1]))  # BL
        return vertices

    if len(vertices) == 3 or len(vertices) > 4 or len(vertices) == 0:
        raise Exception("Invalid number of points provided")

class Rectangle:
    def __init__(self, *Vertices, name=None, size=(0, 0), color=None, fill=False):
        global rectangle_counter
        # If name is not provided, increment rectangle_counter and assign a default name
        if name is None:
            rectangle_counter += 1
            name = str(rectangle_counter)

        # Make Vertices into Sympy Points
        Vertices = [Point(v) for v in list(Vertices)]

        # Initialize the object properties
        self.Vertices = PolyMaker(list(Vertices), size)
        self.name = name
        self.size = size
        self.color = color
        self.fill = fill

    def Draw(self, ax):
        for i, x in enumerate(self.Vertices):
            ax.plot(*x, "bo")
            ax.annotate(chr(ord('@') + i + 1) + self.name, (x[0] + 0.2, x[1] + 0.2))

        polygon = plt.Polygon([v for v in self.Vertices],
                              fill=self.fill, color=self.color)
        ax.add_patch(polygon)


list_of_polygons = [Rectangle((x*6, 2), size=(2, 2), fill=False, color="orange") for x in range(0, 10)]
for poly in list_of_polygons:
    poly.Draw(ax)

# p1 = Rectangle((0, 0), size=(4, 4), fill=False, color="orange")
# p1.Draw(ax)
# p2 = Rectangle((-2, -4), size=(4,4), fill=False, color="purple")
# p2.Draw(ax)

plt.show()

