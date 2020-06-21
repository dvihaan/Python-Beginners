import sys, pygame
import time
import Juneteenth

size = width, height = 1280, 1024
pygame.init()
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
pygame.display.set_caption('Juneteenth Flag')
pygame.mouse.set_visible(True)

background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill(pygame.Color("white"))

vertices = 5
radius = 50

def drawStar():
    # Creating the global variables for the amount of sides, side length, the rotation angle, and the mouse button being pressed 
    global vertices, radius
    # Drawing the polygon
    centre = (pygame.mouse.get_pos())
    points = Juneteenth.star(radius,vertices, centre[0], centre[1])
    pygame.draw.lines(background, pygame.Color("black"), False, points)
    for p in range(len(points)-1):
        pygame.draw.line(background, pygame.Color("black"), points[p], points[p+1])
    screen.blit(background, (0, 0))

def run_show():
    global vertices, radius
    while True:        
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                print("Button = {}".format(event.button))
                print("Pressed = {}".format(pygame.mouse.get_pressed()))
                if event.button == 1:
                    if pygame.mouse.get_pressed() == (1,0,0):
                        if vertices > 5:
                            vertices = vertices - 1
                    if pygame.mouse.get_pressed() == (1,1,0):
                        if radius > 50:
                            radius = radius - 5                            
                if event.button == 3:
                    if pygame.mouse.get_pressed() == (0,0,1):
                        if vertices < 12:
                            vertices = vertices + 1  
                    if pygame.mouse.get_pressed() == (0,1,1):
                        if radius < 500:
                            radius = radius + 5 
                '''
                if event.button == 4:
                    angle = angle + 50
                if event.button == 5:
                    angle = angle - 50
                '''
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        # Setting the background colour (feel free to edit the string to any colour you like)
        background.fill(pygame.Color("white"))
        
        # Running the main funtion
        drawStar()

        # Setting the window's FPS
        pygame.display.update()
        # Edit the FPS by changing the input for clock.tick
        clock.tick(250)

# Finally running the program
run_show()