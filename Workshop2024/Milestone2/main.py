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
