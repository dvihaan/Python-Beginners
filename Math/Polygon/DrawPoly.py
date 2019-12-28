import sys, pygame
import time
import Polygon

'''
This is an interactive program which creates a polygon of varying shape, size, and rotation
Controls: 
Right mouse button = increase # of sides
Left mouse button = decrease # of sides
Middle click + Mouse Right = increase side length
Middle click + Mouse left = decrease side length
Scroll wheel = rotate shape
'''

#Initialize PyGame and create a 1280 x 1024 pixel window
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

# The function to actually render the polygon
def renderPolygon():
    # Creating the global variables for the amount of sides, side length, the rotation angle, and the mouse button being pressed 
    global sides, sideLength, mouseEvent, angle
    
    if mouseEvent == False:
        # decreasing the number of sides
        if pygame.mouse.get_pressed() == (1,0,0):
            if sides > 3:
                sides = sides - 1
                print("Number of Sides = {}, Side Length = {}".format(sides, sideLength))
            mouseEvent = True
        # increasing the amount of sides
        if pygame.mouse.get_pressed() == (0,0,1):
            if sides < 1000:
                sides = sides + 1    
                print("Number of Sides = {}, Side Length = {}".format(sides, sideLength))
            mouseEvent = True  
        # Decreasing the side length
        if pygame.mouse.get_pressed() == (1,1,0):
            if sideLength > 10:
                sideLength = sideLength - 10
                print("Number of Sides = {}, Side Length = {}".format(sides, sideLength))
            mouseEvent = True
        # Increasing the side length
        if pygame.mouse.get_pressed() == (0,1,1):
            if sideLength < 100:
                sideLength = sideLength + 10    
                print("Number of Sides = {}, Side Length = {}".format(sides, sideLength))
            mouseEvent = True                   

    # Drawing the polygon
    centre = (pygame.mouse.get_pos())
    points = Polygon.GetPoints(sides,sideLength, centre[0], centre[1], angle)
    pygame.draw.lines(background, pygame.Color("black"), False, points)
    for p in range(len(points)-1):
        pygame.draw.line(background, pygame.Color("black"), (centre[0], centre[1]), points[p])
    screen.blit(background, (0, 0))


# Running the function written before and taking user input
def run_show():
    global mouseEvent, angle
    while True:        
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                print("Button = {}".format(event.button))
                if event.button == 4:
                    angle = angle + 50
                if event.button == 5:
                    angle = angle - 50
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        # Setting the background colour (feel free to edit the string to any colour you like)
        background.fill(pygame.Color("white"))
        
        # Running the main funtion
        renderPolygon()

        # Setting the window's FPS
        pygame.display.update()
        # Edit the FPS by changing the input for clock.tick
        clock.tick(250)
        mouseEvent = False

# Finally running the program
run_show()