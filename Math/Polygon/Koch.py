import math

def equalVertex(x1=-10,y1=0,x2=10,y2=0):
    x3 = x1/2 + x2/2
    y3 = y1/2 + y2/2
    l = math.sqrt((x1-x2)**2 + (y1-y2)**2)
    m = (y2-y1)/(x2-x1)
    sign = 1 if y2>y1 else -1 if y2<y1 else 1 if x2>x1 else -1 if x2<x1 else 0
    theta = 240 if (m >= 0) ^ (y2 >= y1) else 60
    c = sign*m*l*math.sin(math.radians(theta))/math.sqrt(m**2 + 1)
    x4 = x3 + sign*l*math.sin(math.radians(theta)) if x2==x1 else x3 + sign*c
    y4 = y3 - sign*l*math.sin(math.radians(theta)) if m==0 else y3*sign if x2==x1 else y3 - c*sign/m
    points = [(x1,y1),(x4,y4),(x2,y2),(x1,y1)]
    return points

def Snowflake(points, level = 0):
    print("Level-{} Snowflake drawn for side length {}".format(level, int(math.sqrt(math.pow(points[0][0] - points[1][0], 2) + math.pow(points[0][1] - points[1][1], 2)))))
    n = 1
    print("Level = {}, Points = {}".format(0, len(points)))
    while level > 0:
        newpoints = [points[0]]
        for i in range(len(points)-1):
            pt1 = points[i]
            pt2 = points[i+1]
            pta = (2*pt1[0]/3+pt2[0]/3,2*pt1[1]/3+pt2[1]/3)
            ptb = (pt1[0]/3+2*pt2[0]/3,pt1[1]/3+2*pt2[1]/3)
            calculatedPoints = equalVertex(pta[0],pta[1],ptb[0],ptb[1])
            for j in range(len(calculatedPoints) - 1):
                newpoints.append(calculatedPoints[j])
            newpoints.append(pt2)
        points = newpoints
        level -= 1
        print("Level = {}, Points = {}".format(n, len(newpoints)))
        n +=1
    return points

def main():
    point = equalVertex(33.33,0, -33.33, 0)
    print(point)

if __name__ == '__main__':
    main()
