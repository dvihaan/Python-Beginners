import math

'''
This is a function to get the points that  you are supposed to plot, given a certain side length and amount of sides.
This function and code only prints the points you would need to plot the shape that you have decided on.
'''
#The inputs, in order from left to right are: number of sides, side length, centre x position, centre y position, and the angle the shape is rotated
#By default, the shape is centered at the origin and has no rotation from its original shape
def GetPoints(n, a, cx = 0, cy = 0, theta = 0):
    #the list of tuples that will contain the points
    points = []
    # r = the distance from the centre to any vertex
    r = a*math.sin(math.radians(90-180/n))/math.sin(math.radians(360/n))
    #creating the tuples containing the points
    for i in range(n+1):
        Vix = r*math.cos(math.radians(i*360/n+theta)) + cx
        Viy = r*math.sin(math.radians(i*360/n+theta)) + cy
        points.append((Vix,Viy))
    return points
#printing the points that should be connected in a drawing
def Draw(points):
    for p in range(len(points)-1):
        print("({:.2f},{:.2f}) ---------- ({:.2f},{:.2f})".format(points[p][0],points[p][1],points[p+1][0],points[p+1][1]))
#running the program
def main():
    points = GetPoints(8,1)

    Draw(points)

if __name__ == '__main__':
    main()