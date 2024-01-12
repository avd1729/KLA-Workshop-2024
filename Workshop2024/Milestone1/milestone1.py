import math
import numpy as np


def create_line_segment(angle, diam):

    rad = diam / 2

    x1 = math.cos(math.radians(angle))*rad
    y1 = math.sin(math.radians(angle))*rad

    return [(x1, y1), (-x1, -y1)]


def generate_points(lst, no_of_points):

    x = np.linspace(lst[0][0], lst[1][0], no_of_points, endpoint=True)
    y = np.linspace(lst[0][1], lst[1][1], no_of_points, endpoint=True)
    mapped = zip(x, y)
    return mapped

# main

# case 1


WaferDiameter: 300
NumberOfPoints: 30
Angle: 0

result = create_line_segment(Angle, WaferDiameter)

ans = generate_points(result, NumberOfPoints)
