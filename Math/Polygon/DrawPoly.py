import sys, pygame
import time
import Polygon

size = width, height = 1280, 1024
sides = 3
sideLength = 10
angle = 0
mouseEvent = False
pygame.init()
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
pygame.display.set_caption('Polygon')
pygame.mouse.set_visible(True)

background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill(pygame.Color("white"))

def renderPolygon():
    global sides, sideLength, mouseEvent, angle
    if mouseEvent == False:
        if pygame.mouse.get_pressed() == (1,0,0):
            if sides > 3:
                sides = sides - 1
                print("Number of Sides = {}, Side Length = {}".format(sides, sideLength))
            mouseEvent = True
        if pygame.mouse.get_pressed() == (0,0,1):
            if sides < 1000:
                sides = sides + 1    
                print("Number of Sides = {}, Side Length = {}".format(sides, sideLength))
            mouseEvent = True  
        if pygame.mouse.get_pressed() == (1,1,0):
            if sideLength > 10:
                sideLength = sideLength - 10
                print("Number of Sides = {}, Side Length = {}".format(sides, sideLength))
            mouseEvent = True
        if pygame.mouse.get_pressed() == (0,1,1):
            if sideLength < 100:
                sideLength = sideLength + 10    
                print("Number of Sides = {}, Side Length = {}".format(sides, sideLength))
            mouseEvent = True                   

    centre = (pygame.mouse.get_pos())
    points = Polygon.GetPoints(sides,sideLength, centre[0], centre[1], angle)
    pygame.draw.lines(background, pygame.Color("black"), False, points)
    for p in range(len(points)-1):
        pygame.draw.line(background, pygame.Color("black"), (centre[0], centre[1]), points[p])
    screen.blit(background, (0, 0))


def run_show():
    global mouseEvent, angle
    while True:        
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                print("Button = {}".format(event.button))
                if event.button == 4:
                    angle = angle + 5
                if event.button == 5:
                    angle = angle - 5
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        background.fill(pygame.Color("white"))

        renderPolygon()

        pygame.display.update()
        clock.tick(10)
        mouseEvent = False

run_show()


