import math

def GetPoints(n, a, cx = 0, cy = 0):
    points = []
    r = a*math.sin(math.radians(90-180/n))/math.sin(math.radians(360/n))
    for i in range(n+1):
        Vix = r*math.cos(math.radians(i*360/n)) + cx
        Viy = r*math.sin(math.radians(i*360/n)) + cy
        points.append((Vix,Viy))
    return points

def Draw(points):
    for p in range(len(points)-1):
        print("({:.2f},{:.2f}) ---------- ({:.2f},{:.2f})".format(points[p][0],points[p][1],points[p+1][0],points[p+1][1]))
def main():
    points = GetPoints(8,1)

    Draw(points)

    #print(format(math.cos(math.radians(90)), '.2f'))

if __name__ == '__main__':
    main()