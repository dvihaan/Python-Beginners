import math
def equalVertex(x1=-10,y1=0,x2=10,y2=0):
    x3 = x1/2 + x2/2
    y3 = y1/2 + y2/2
    #print("x3={}, y3={}".format(x3, y3))
    l = math.sqrt((x1-x2)**2 + (y1-y2)**2)
    #print("l={}".format(l))
    m = (y2-y1)/(x2-x1)
    #print("m1={}".format(m1))
    c = m*l*math.sin(math.radians(60))/math.sqrt(m**2 + 1)
    #print("c={}".format(c))
    if x2 == x1:
        x4 = x3 - l*math.sin(math.radians(60))
    else:
        x4 = c+x3

    if m == 0:
        y4 = y3 + l*math.sin(math.radians(60))
    else:
        if x2 == x1:
            y4 = y3
        else:
            y4 = y3 - c/m

    points = [(x1,y1),(x4,y4),(x2,y2),(x1,y1)] 

    return points

def Snowflake(points, level = 0):

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
    return points

def main():
    point = equalVertex(33.33,0, -33.33, 0)

    print(point)

if __name__ == '__main__':
    main()