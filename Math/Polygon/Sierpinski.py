import math

def midpoint(p1,p2):
    midx = p1[0]/2 + p2[0]/2
    midy = p1[1]/2 + p2[1]/2

    midp = (midx,midy)

    return midp


def Sierpinski(tri1):
    nextTriangles = []
    tri2 = []
    for i in range(len(tri1)-1):
        tri2.append(midpoint(tri1[i],tri1[i+1]))
    tri2.append(tri2[0])
    tri2.append(tri2[1])
    nextTriangles.append(tri2)

    '''
        tri3 = [tri1[0],tri2[0],tri2[2],tri1[0]]
        tri4 = [tri1[1],tri2[1],tri2[3],tri1[1]]
        tri5 = [tri1[2],tri2[2],tri2[4],tri1[2]]
        nextTriangles.append(tri3)
        nextTriangles.append(tri4)
        nextTriangles.append(tri5)
    '''
    for i in range(len(tri1)-1):
        newTri = [tri1[i],tri2[i],tri2[i+2],tri1[i]]
        nextTriangles.append(newTri)

    return nextTriangles

def main():
    listA = [(-2,0),(2,0),(0,2),(-2,0)]
    gasket = Sierpinski(listA)
    for g in gasket:
        print(g)

if __name__ == '__main__':
    main()

