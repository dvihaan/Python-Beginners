import sys,pygame
import time
import Koch
import math

size = width, height =1280, 1024
# Setting the background colour (feel free to edit the string to any colour you like)
backgroundColor = "Black"
# Setting the foreground colour (feel free to edit the string to any colour you like)
foregroundColor = "Green"
sideLength = 500
angle = 0
level = 0
minLevel = 0
maxLevel = 7
levelChange = 1
minLength = 50
lengthChange = 50
vertices = {}
pygame.init()
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
pygame.display.set_caption('Snowflake')
pygame.mouse.set_visible(True)
maxLength = int(screen.get_size()[1]*0.9)
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill(pygame.Color("white"))

def applyTranslation(point, centre):
    x = point[0]+centre[0]
    y = point[1]+centre[1]
    return (x, y)

def applyRotation(point, centre):
    x = point[0]-centre[0]
    y = point[1]-centre[1]
    return (centre[0]+x*math.cos(math.radians(angle)) - y*math.sin(math.radians(angle)), centre[1]+x*math.sin(math.radians(angle)) + y*math.cos(math.radians(angle)))

def drawKoch(centre=(0,0), drawLevel=0):
    global sideLength, angle, level, backgroundColor, foregroundColor
    if drawLevel == 0:
        drawLevel = level
    background.fill(pygame.Color(backgroundColor))
    if str(sideLength) in vertices and int(vertices[str(sideLength)]["level"]) >= drawLevel:
        points = vertices[str(sideLength)]["points"]
        pointLevel = int(vertices[str(sideLength)]["level"])
        if drawLevel < pointLevel:
            jump = int(math.pow(4, pointLevel - drawLevel))
            levelPoints = []
            for i in range(0, len(points), jump):
                levelPoints.append(points[i])
            points = levelPoints
    else:
        xoff = sideLength/2
        yoff = sideLength*math.tan(math.radians(60))/6
        points = Koch.equalVertex(x1 = 0-xoff,y1 = 0+yoff,x2 = 0+xoff,y2 = 0+yoff)
        points = Koch.Snowflake(points,drawLevel)
        vertices[str(sideLength)] = {"level": str(drawLevel), "points": points}

    if centre[0]==0 and centre[1]==0:
        centre = (pygame.mouse.get_pos())
    points = list(map(lambda p: applyTranslation(p,centre), points))
    points = list(map(lambda p: applyRotation(p,centre), points))
    pygame.draw.lines(background, pygame.Color(foregroundColor), False, points)
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
        background.fill(pygame.Color(backgroundColor))

        # Running the main funtion
        drawKoch()

        # Setting the window's FPS
        # Edit the FPS by changing the input for clock.tick
        clock.tick(60)

#drawKoch((int(screen.get_size()[0]/2), int(screen.get_size()[1]/2)), 7)
run_show()
