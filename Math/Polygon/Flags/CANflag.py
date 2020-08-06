import math
import StarPoints
import sys, pygame

size = width, height = 1920, 1080
flagRed = pygame.Color(239,51,64)
grey = pygame.Color(112,128,144)
pygame.init()
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
pygame.display.set_caption('Canadian Flag')
pygame.mouse.set_visible(True)

background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill(grey)

flagHeight = 500
flagWidth = flagHeight*2

whiteWidth = flagWidth/2

def drawRect(xLen = 1800,yLen = 1200, centre = (0,0), width = 0, colour = pygame.Color("white")):
    cx = centre[0]
    cy = centre[1]
    
    tl = (cx-xLen/2, cy-yLen/2)
    
    points = pygame.Rect(tl, (xLen, yLen))

    pygame.draw.rect(background, colour, points, width)
    screen.blit(background, (0, 0))

def drawUSflag():
    global flagHeight, flagWidth, flagRed

    centre = pygame.mouse.get_pos()

    drawRect(flagWidth,flagHeight,centre,0,flagRed)
    drawRect(whiteWidth,flagHeight,centre)

def runShow():
    global grey
    
    
    while True:
        
        for event in pygame.event.get():
            '''
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4 and flagHeight < 1000:
                    flagHeight += 50
                if event.button == 5 and flagHeight > 100:
                    flagHeight -= 50 
                    ''' 
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        # Setting the background colour
        background.fill(grey)
        
        # Running the main funtion
        drawUSflag()

        # Setting the window's FPS
        pygame.display.update()
        # Edit the FPS by changing the input for clock.tick
        clock.tick(300)


# Finally running the program
runShow()