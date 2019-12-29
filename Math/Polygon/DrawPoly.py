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
    global sides, sideLength, angle
    # Drawing the polygon
    centre = (pygame.mouse.get_pos())
    points = Polygon.GetPoints(sides,sideLength, centre[0], centre[1], angle)
    pygame.draw.lines(background, pygame.Color("black"), False, points)
    for p in range(len(points)-1):
        pygame.draw.line(background, pygame.Color("black"), (centre[0], centre[1]), points[p])
    screen.blit(background, (0, 0))


# Running the function written before and taking user input
def run_show():
    global angle, sides, sideLength
    while True:        
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                print("Button = {}".format(event.button))
                print("Pressed = {}".format(pygame.mouse.get_pressed()))
                if event.button == 1:
                    if pygame.mouse.get_pressed() == (1,0,0):
                        if sides > 3:
                            sides = sides - 1
                    if pygame.mouse.get_pressed() == (1,1,0):
                        if sideLength > 5:
                            sideLength = sideLength - 5                            
                if event.button == 3:
                    if pygame.mouse.get_pressed() == (0,0,1):
                        if sides < 1000:
                            sides = sides + 1  
                    if pygame.mouse.get_pressed() == (0,1,1):
                        if sideLength < 500:
                            sideLength = sideLength + 5 
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

# Finally running the program
run_show()