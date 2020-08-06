import math
import StarPoints
import sys, pygame

size = width, height = 1920, 1080
Saffron = pygame.Color(255,153,51)
flagGreen = pygame.Color(19,136,8)
flagBlue = pygame.Color(0,0,128)
grey = pygame.Color(112,128,144)
pygame.init()
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
pygame.display.set_caption('Indian Flag')
pygame.mouse.set_visible(True)

background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill(grey)

flagHeight = 1000
flagWidth = flagHeight*1.5

stripeWidth = flagHeight/3
outRadius = int(flagHeight/8)
inRadius = int(outRadius/7)

def drawRect(xLen = 1800,yLen = 1200, centre = (0,0), width = 0, colour = pygame.Color("white")):
    cx = centre[0]
    cy = centre[1]
    
    tl = (cx-xLen/2, cy-yLen/2)
    
    points = pygame.Rect(tl, (xLen, yLen))

    pygame.draw.rect(background, colour, points, width)
    screen.blit(background, (0, 0))

def drawStar(v, r, centre, width, colour = pygame.Color("white"), r2 = 750):
    # Drawing the polygon
    points = StarPoints.star(r, v, centre[0], centre[1], r2)
    pygame.draw.polygon(background, colour, points, width)
    screen.blit(background, (0, 0))

def drawChakra():
        global flagBlue, flagHeight, flagWidth, stripeWidth, background, inRadius, outRadius
        centre = pygame.mouse.get_pos()

        pygame.draw.circle(background,flagBlue,centre,inRadius)
        pygame.draw.circle(background,flagBlue,centre,outRadius,5)
        drawStar(24,outRadius,centre,0,flagBlue,inRadius)

        screen.blit(background, (0, 0))

def drawINDflag():
    global Saffron, flagGreen,flagBlue, flagHeight, flagWidth, stripeWidth, background

    centre = pygame.mouse.get_pos()
    CentreT = (centre[0], centre[1]-stripeWidth)
    CentreD = (centre[0], centre[1]+stripeWidth)

    drawRect(flagWidth, flagHeight, centre)
    drawRect(flagWidth, stripeWidth, CentreT, 0, Saffron)
    drawRect(flagWidth, stripeWidth, CentreD, 0, flagGreen)
    drawChakra()

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
        drawINDflag()

        # Setting the window's FPS
        pygame.display.update()
        # Edit the FPS by changing the input for clock.tick
        clock.tick(300)


# Finally running the program
runShow()