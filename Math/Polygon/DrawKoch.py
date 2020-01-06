import sys,pygame
import time
import Koch
import math

size = width, height = 1280,1024
sideLength = 500
angle = 0
level = 0

pygame.init()
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
pygame.display.set_caption('Snowflake')
pygame.mouse.set_visible(True)

background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill(pygame.Color("white"))

def drawEquilateral():
    global sideLength, angle
    centre = (pygame.mouse.get_pos())
    points = Koch.equalVertex(x1 = centre[0]-sideLength/2,y1 = centre[1],x2 = centre[0]+sideLength/2,y2 = centre[1])
    for i in range(len(points)):        
        x = points[i][0]-centre[0]
        y = points[i][1]-centre[1]
        points[i] = (centre[0]+x*math.cos(math.radians(angle)) - y*math.sin(math.radians(angle)), centre[1]+x*math.sin(math.radians(angle)) + y*math.cos(math.radians(angle)))
    pygame.draw.lines(background, pygame.Color("black"), False, points)
    screen.blit(background, (0, 0))

def drawKoch():
    global sideLength, angle, level
    centre = (pygame.mouse.get_pos())
    points = Koch.equalVertex(x1 = centre[0]-sideLength/2,y1 = centre[1]+sideLength/3,x2 = centre[0]+sideLength/2,y2 = centre[1]+sideLength/3)
    '''
    height = points[1][1]
    for i in range(len(points)):
        points[i] = (points[i][0], points[i][1] + height/2)
    print(points)
    '''
    points = Koch.Snowflake(points,level)
    for i in range(len(points)):        
        x = points[i][0]-centre[0]
        y = points[i][1]-centre[1]
        points[i] = (centre[0]+x*math.cos(math.radians(angle)) - y*math.sin(math.radians(angle)), centre[1]+x*math.sin(math.radians(angle)) + y*math.cos(math.radians(angle)))
    pygame.draw.lines(background, pygame.Color("black"), False, points)
    screen.blit(background, (0, 0))

def run_show():
    global sideLength, angle, level
    while True:        
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:

                if event.button == 1:
                    
                    if pygame.mouse.get_pressed() == (1,0,0):
                        if level > 0:
                            level -= 1
                    
                    if pygame.mouse.get_pressed() == (1,1,0):
                        if sideLength > 5:
                            sideLength = sideLength - 5                            
                if event.button == 3:
                    
                    if pygame.mouse.get_pressed() == (0,0,1):
                        if level < 7:
                            level += 1  
                    
                    if pygame.mouse.get_pressed() == (0,1,1):
                        if sideLength < 500:
                            sideLength = sideLength + 5 
                
                if event.button == 4:
                    angle = angle + 10
                if event.button == 5:
                    angle = angle - 10
                

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        # Setting the background colour (feel free to edit the string to any colour you like)
        background.fill(pygame.Color("white"))
        
        # Running the main funtion
        #drawEquilateral()
        drawKoch()

        # Setting the window's FPS
        pygame.display.update()
        # Edit the FPS by changing the input for clock.tick
        clock.tick(250)

run_show()
