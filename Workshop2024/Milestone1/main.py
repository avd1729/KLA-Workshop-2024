# Modules

import math
import numpy as np

# Reading input from text file


def reading_input(input_file_path):

    with open(input_file_path, 'r') as file:

        lines = file.readlines()

        WaferDiameter = None
        NumberOfPoints = None
        Angle = None

        for line in lines:
            key, value = line.split(':')

            if 'WaferDiameter' in key:
                WaferDiameter = int(value.strip())
            elif 'NumberOfPoints' in key:
                NumberOfPoints = int(value.strip())
            elif 'Angle' in key:
                Angle = int(value.strip())

        return [WaferDiameter, NumberOfPoints, Angle]

# Calculating diameter end points


def diameter_endpoints(Angle, WaferDiameter):

    Radius = WaferDiameter / 2

    x1 = math.cos(math.radians(Angle))*Radius
    y1 = math.sin(math.radians(Angle))*Radius

    return [(x1, y1), (-x1, -y1)]

# Point generation


def generate_points(lst, NumberOfPoints):

    x = np.linspace(lst[0][0], lst[1][0], NumberOfPoints, endpoint=True)
    y = np.linspace(lst[0][1], lst[1][1], NumberOfPoints, endpoint=True)
    mapped = zip(x, y)
    return mapped

# Writing to text file


def write_file(output_file_path, result):

    with open(output_file_path, 'w') as f:
        f.write(list(result))

# Main function


def main():

    input_file_path = input("Enter input file path (without '')")

    # output_file_path = input("Enter output file path (without '')")

    input_params = reading_input(input_file_path)

    WaferDiameter = input_params[0]
    NumberOfPoints = input_params[1]
    Angle = input_params[2]

    end_points = diameter_endpoints(Angle, WaferDiameter)

    result = generate_points(end_points, NumberOfPoints)

    # write_file(output_file_path, result)

    print(result)


if __name__ == "__main__":

    main()
