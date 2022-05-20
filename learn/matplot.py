import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse

figure, axes = plt.subplots()
def ellipse():
    ellipse = Ellipse((2, 5), 4, 5)

    axes.add_patch(ellipse)
    plt.xlim(0, 10)
    plt.ylim(0, 10)
    plt.title('Ellipse')
    plt.show()
def Rectangle():
    rectangle = plt.Rectangle((1, 3), 5, 6)
    axes.add_patch(rectangle)
    plt.xlim(0, 10)
    plt.ylim(0, 10)
    plt.title('Rectangle')
    plt.show()
def Circle():
    circle = plt.Circle((0.6, 0.6), 0.2)
    axes.add_patch(circle)
    plt.xlim(0, 10)
    plt.ylim(0, 10)
    plt.title('Circle')
    plt.show()
def polygon():
    xy = [[2, 3], [2, 1], [2, 2], [1, 2]]
    polygon = plt.Polygon(xy)
    x, y=polygon.exterior.xy
    axes.add_patch(polygon)
    plt.xlim(0, 10)
    plt.ylim(0, 10)
    plt.title('Circle')
    plt.plot(x,y)
    plt.show()

ellipse()
Rectangle()
# polygon()
# Circle()