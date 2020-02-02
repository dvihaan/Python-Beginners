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

def dots(points):
    lastPoint = points[len(points)-1]
    randomVertex = points[randint(0,2)]
    newpoint = midpoint(lastPoint, randomVertex)
    points.append(newpoint)
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
    for i in range(100000):
        points = dots(points)

    for p in points:
        pygame.draw.circle(background,pygame.Color(foregroundColor),(int(p[0]), int(p[1])),1)
    screen.blit(background, (0, 0))
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()        

if __name__ == '__main__':
    main()

