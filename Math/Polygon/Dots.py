import math
from Sierpinski import midpoint
from random import randint
import sys,pygame
import time

size = width, height =800, 600
# Setting the background colour (feel free to edit the string to any colour you like)
backgroundColor = "Black"
# Setting the foreground colour (feel free to edit the string to any colour you like)
foregroundColor = "Green"
lineWidth = 1
sideLength = 500
minLength = 50
lengthChange = 50

pygame.init()
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
pygame.display.set_caption('Sierpinski Gasket')
pygame.mouse.set_visible(True)
maxLength = int(screen.get_size()[1]*0.9)
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill(pygame.Color(backgroundColor))

def addDots(points):
    lastPoint = points[len(points)-1]
    randomVertex = points[randint(0,2)]
    newpoint = midpoint(lastPoint, randomVertex)
    points.append(newpoint)
    pygame.draw.circle(background,pygame.Color(foregroundColor),(int(newpoint[0]), int(newpoint[1])),1)
    return points

def removeDots(points):
    if len(points) > 3:
        lastPoint = points.pop(-1)
        pygame.draw.circle(background,pygame.Color(backgroundColor),(int(lastPoint[0]), int(lastPoint[1])),1)
    return points


def main():
    points = [(-2,0),(2,0),(0,2)]
    midx = int(width/2)
    midy = int(height/2)
    points = [
        (midx-sideLength/2,midy+sideLength*math.tan(math.radians(30))/2),
        (midx+sideLength/2,midy+sideLength*math.tan(math.radians(30))/2),
        (midx,midy-sideLength/(2*math.cos(math.radians(30))))
    ]

    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4:
                    points = addDots(points)
                if event.button == 5:
                    points = removeDots(points)
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()  
        screen.blit(background, (0, 0))
        pygame.display.update()      

if __name__ == '__main__':
    main()


