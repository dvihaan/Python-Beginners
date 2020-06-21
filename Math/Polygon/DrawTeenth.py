import sys, pygame
import time
import Juneteenth

size = width, height = 1280, 1024
flagBlue = pygame.Color(2,0,102)
flagRed = pygame.Color(202,4,5)
grey = pygame.Color(112,128,144)
pygame.init()
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
pygame.display.set_caption('Juneteenth Flag')
pygame.mouse.set_visible(True)

background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill(grey)

inVertices = 5
inRadius = 100

outVertices = 12
outRadius = 200

flagWidth = 1800
flagHeight = 1200

def drawRect(xLen = 1800,yLen = 600, centre = (0,0)):
    cx = centre[0]
    cy = centre[1]
    
    p1 = (cx-xLen/2, cy+yLen/2)
    p2 = (cx+xLen/2, cy+yLen/2)
    p3 = (cx+xLen/2, cy-yLen/2)
    p4 = (cx-xLen/2, cy-yLen/2)
    
    points = [p1, p2, p3, p4, p1]

    pygame.draw.rect(background, pygame.Color("white"), points, 20)
    screen.blit(background, (0, 0))

def drawStar(v, r, s, centre):
    # Drawing the polygon
    points = Juneteenth.star(r, v, centre[0], centre[1])
    pygame.draw.polygon(background, pygame.Color("white"), points)
    screen.blit(background, (0, 0))

def drawFlag():
    global inVertices, inRadius, outVertices, outRadius, flagHeight, flagWidth



def run_show():
    global inVertices, inRadius
    while True:        
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                print("Button = {}".format(event.button))
                print("Pressed = {}".format(pygame.mouse.get_pressed()))
                if event.button == 1:
                    if pygame.mouse.get_pressed() == (1,0,0):
                        if inVertices > 5:
                            inVertices= inVertices- 1
                    if pygame.mouse.get_pressed() == (1,1,0):
                        if inRadius > 50:
                            inRadius = inRadius - 5                            
                if event.button == 3:
                    if pygame.mouse.get_pressed() == (0,0,1):
                        if inVertices< 12:
                            inVertices= inVertices+ 1  
                    if pygame.mouse.get_pressed() == (0,1,1):
                        if inRadius < 500:
                            inRadius = inRadius + 5 
                '''
                if event.button == 4:
                    angle = angle + 50
                if event.button == 5:
                    angle = angle - 50
                '''
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        # Setting the background colour
        background.fill(grey)
        
        # Running the main funtion
        drawFlag()

        # Setting the window's FPS
        pygame.display.update()
        # Edit the FPS by changing the input for clock.tick
        clock.tick(300)

# Finally running the program
run_show()