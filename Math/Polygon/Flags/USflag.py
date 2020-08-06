import math
import StarPoints
import sys, pygame

size = width, height = 1920, 1080
flagBlue = pygame.Color(10,49,97)
flagRed = pygame.Color(179,25,66)
grey = pygame.Color(112,128,144)
pygame.init()
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
pygame.display.set_caption('US Flag')
pygame.mouse.set_visible(True)

background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill(grey)


flagHeight = 500
flagWidth = flagHeight*1.9

starVertices = 5
starRadius = flagHeight*0.0308/2
starPent = starRadius*(85/225)
starDistX = 0.063*flagHeight
starDistY = flagHeight*0.054

blueHeight = flagHeight*(7/13)
blueWidth = flagHeight*0.76

stripeWidth = flagHeight/13

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

def drawUSflag():
    global flagHeight, flagWidth, starVertices, starRadius, starPent, starDist, blueHeight, blueWidth, stripeWidth, flagBlue, flagRed

    centre = pygame.mouse.get_pos()

    drawRect(flagWidth, flagHeight, centre, 0, pygame.Color("white"))

    for i in range(-3, 4, 1):
        drawRect(flagWidth, stripeWidth, (centre[0], centre[1]+i*2*stripeWidth), 0, flagRed)
    
    TLx = centre[0]-flagWidth/3.34
    TLy = centre[1]-flagWidth/8.25
    drawRect(blueWidth, blueHeight, (TLx, TLy), 0, flagBlue)


    for r in range (1,10):
        starCY = centre[1]-r*starDistY+starDistY/2
        if r%2 != 0:
            for o in range(1,7):
                starCX = centre[0]-o*2*starDistX - 2*starDistX
                drawStar(starVertices,starRadius,(starCX, starCY),0,pygame.Color("white"),starPent)
        if r%2 == 0:
            for e in range(1,6):
                starCX = centre[0]-e*2*starDistX - 3*starDistX
                drawStar(starVertices,starRadius,(starCX, starCY),0,pygame.Color("white"),starPent)


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