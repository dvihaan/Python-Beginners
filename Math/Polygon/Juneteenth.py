import sys, pygame
import time
import StarPoints

size = width, height = 1920, 1080
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

flagHeight = 500
flagWidth = flagHeight*1.8

inVertices = 5
inRadius = flagHeight*0.225
inPent = inRadius*(85/225)

outVertices = 12
outRadius = flagHeight*0.44
outPent = outRadius*(330/440)
outLine = int(flagHeight/100)

def drawRect(xLen = 1800,yLen = 1200, centre = (0,0), width = 0, colour = pygame.Color("white")):
    cx = centre[0]
    cy = centre[1]
    
    tl = (cx-xLen/2, cy+yLen/2)
    
    points = pygame.Rect(tl, (xLen, yLen))

    pygame.draw.rect(background, colour, points, width)
    screen.blit(background, (0, 0))

def drawStar(v, r, centre, width, colour = pygame.Color("white"), r2 = 750):
    # Drawing the polygon
    points = StarPoints.star(r, v, centre[0], centre[1], r2)
    pygame.draw.polygon(background, colour, points, width)
    screen.blit(background, (0, 0))

def drawFlag():
    global inVertices, inRadius, outVertices, outRadius, flagHeight, flagWidth, flagBlue, flagRed, inPent, outPent

    flagWidth = flagHeight*1.8

    inVertices = 5
    inRadius = flagHeight*0.225
    inPent = inRadius*(85/225)

    outVertices = 12
    outRadius = flagHeight*0.44
    outPent = outRadius*(330/440)
    outLine = int(flagHeight/100)

    centre = pygame.mouse.get_pos()
    centreT = (centre[0], centre[1]-flagHeight/1.35)
    centreD = (centre[0], centre[1]-flagHeight/4)
    #centreM = (centre[0], centre[1]+flagHeight/4)
    drawRect(flagWidth, flagHeight/2, centreT, 0, flagBlue)
    drawRect(flagWidth, flagHeight/2, centreD, 0, flagRed)
    drawStar(inVertices, inRadius, centre, 0, pygame.Color("white"), inPent)
    drawStar(outVertices, outRadius, centre, outLine, pygame.Color("white"), outPent)

def run_show():
    global inVertices, inRadius, grey, flagHeight
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4 and flagHeight < 1000:
                    flagHeight += 50
                if event.button == 5 and flagHeight > 100:
                    flagHeight -= 50  
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