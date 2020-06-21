import math

def star (r,p,cx = 0,cy = 0):
    oPoints = []
    inPoints = []
    r2 = r/2

    for i in range(p+1):
        Vix = r*math.cos(math.radians(i*360/p)) + cx
        Viy = r*math.sin(math.radians(i*360/p)) + cy
        oPoints.append((Vix,Viy))

    theta = 360/(2*p)

    for i in range(p+1):
        Vix = r2*math.cos(math.radians(i*360/p+theta)) + cx
        Viy = r2*math.sin(math.radians(i*360/p+theta)) + cy
        inPoints.append((Vix,Viy))

    starPoints = []

    for i in range(p+1):
        starPoints.append(oPoints[i])
        starPoints.append(inPoints[i])

    return starPoints

def Draw(points):
    for i,p in enumerate(range(len(points)-1)):
        print("{:.0f}. ({:.2f},{:.2f}) ---------- ({:.2f},{:.2f})".format(i+1,points[p][0],points[p][1],points[p+1][0],points[p+1][1]))

#running the program
def main():
    points = star(10,5)

    Draw(points)

if __name__ == '__main__':
    main()