import sys,pygame
import time
import math
import Sierpinski

size = width, height =800, 600
# Setting the background colour (feel free to edit the string to any colour you like)
backgroundColor = "Black"
# Setting the foreground colour (feel free to edit the string to any colour you like)
foregroundColor = "Green"
lineWidth = 1
sideLength = 50
angle = 0
level = 0
minLevel = 0
maxLevel = 7
levelChange = 1
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
background.fill(pygame.Color("white"))

def drawPinski(points,currentLevel):
    global level
    gasket = Sierpinski.Sierpinski(points)
    pygame.draw.polygon(background, pygame.Color(foregroundColor), gasket[0], lineWidth)
    if currentLevel <= level:
        for i in range(len(gasket)-1):
            drawPinski(gasket[i+1],currentLevel+1)


def drawGasket():
    global foregroundColor, lineWidth, sideLength
    background.fill(pygame.Color(backgroundColor))
    midx = int(screen.get_size()[0]/2)
    midy = int(screen.get_size()[1]/2)
    points = [(midx-sideLength/2,midy+sideLength/2),(midx+sideLength/2,midy+sideLength/2),(midx,midy-sideLength/2),(midx-sideLength/2,midy+sideLength/2)]
    pygame.draw.polygon(background, pygame.Color(foregroundColor), points, lineWidth)
    drawPinski(points,1)
    screen.blit(background, (0, 0))
    pygame.display.update()

def run_show():
    global sideLength, angle, level, minLevel, maxLevel, levelChange, minLength, maxLength, lengthChange, backgroundColor
    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if pygame.mouse.get_pressed() == (1,0,0):
                        if level > minLevel:
                            level -= levelChange
                    if pygame.mouse.get_pressed() == (1,1,0):
                        if sideLength > minLength:
                            sideLength -= lengthChange
                if event.button == 3:
                    if pygame.mouse.get_pressed() == (0,0,1):
                        if level < maxLevel:
                            level += levelChange
                    if pygame.mouse.get_pressed() == (0,1,1):
                        if sideLength < maxLength:
                            sideLength += lengthChange
                if event.button == 4:
                    angle = angle + 10
                if event.button == 5:
                    angle = angle - 10
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        # Running the main funtion
        drawGasket()
        # Setting the window's FPS
        # Edit the FPS by changing the input for clock.tick
        clock.tick(60)

run_show()

