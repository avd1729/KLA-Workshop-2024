'''
Datastructure prefferd : Array

Traversal Algorithm : BFS


for a wafer map without shift , the number of dies can be approximated to the

n = diameter / die size

an 2D array of n x n can be formed to represent the possible dies (complete & partial)

the 2D array is initialized to be true , if all 4 points of the die is outside the wafer , it is modified to False

we find this using circle eqn

x**2 + y**2 = r**2

if x**2 + y**2 > r**2 

    the point (x,y) lies outside the circle

if x**2 + y**2 < r**2 

    the point (x,y) lies inside the circle

if x**2 + y**2 == r**2 

    the point (x,y) lies on the circle

after finding all the possible dies BFS can be used to find the ordering of each dies wrt Reference die

'''

from collections import deque as queue


def initialize_bool_list(diam):
    twod_list = []
    new = []

    for i in range(0, diam//2 + 1):
        for j in range(0, diam//2 + 1):
            new.append(True)
        twod_list.append(new)
        new = []

    return twod_list


lst = initialize_bool_list(300)


def coordinates(die):

    i, j = die[0], die[1]

    (x1, y1) = (i, j)
    (x2, y2) = (i+1, j)
    (x3, y3) = (i, -j)
    (x4, y4) = (i+1, -j)

    return [(x1, y1), (x2, y2), (x3, y3), (x4, y4)]


def valid(die, diam):

    for (i, j) in die:

        if i**2 + j**2 > (diam/2)**2:

            return True

        elif i**2 + j**2 == (diam/2)**2:

            return True

    return False


def block_val(lst):

    for i in range(len(lst)):

        for j in range(len(lst)):

            if not valid(lst[i][j]):

                lst[i][j] == False
    return


dRow = [-1, 0, 1, 0]
dCol = [0, 1, 0, -1]


def isValid(vis, row, col):

    if (row < 0 or col < 0 or row >= 4 or col >= 4):
        return False

    if (vis[row][col]):
        return False

    return True


def BFS(grid, vis, row, col):

    q = queue()

    q.append((row, col))
    vis[row][col] = True

    while (len(q) > 0):
        cell = q.popleft()
        x = cell[0]
        y = cell[1]
        print(grid[x][y], end=" ")

        for i in range(4):
            adjx = x + dRow[i]
            adjy = y + dCol[i]
            if (isValid(vis, adjx, adjy)):
                q.append((adjx, adjy))
                vis[adjx][adjy] = True
