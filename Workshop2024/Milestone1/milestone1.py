import math


def create_line_segment(angle, diam):

    rad = diam / 2

    x1 = math.cos(math.radians(angle))*rad
    y1 = math.sin(math.radians(angle))*rad

    return [(x1, y1), (-x1, -y1)]

# test cases


testcase1 = create_line_segment(0, 300)
testcase2 = create_line_segment(45, 300)
testcase3 = create_line_segment(250, 200)
testcase4 = create_line_segment(200, 150)

print(testcase1)
print(testcase2)
print(testcase3)
print(testcase4)
