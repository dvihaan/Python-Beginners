import sys, pygame
import time
import Polygon

size = width, height = 1280, 1024
pygame.init()
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Polygon')

background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill(pygame.Color("white"))



points = Polygon.GetPoints(100,10, size[0]/2, size[1]/2)
pygame.draw.lines(background, pygame.Color("black"), False, points)
for p in range(len(points)-1):
    pygame.draw.line(background, pygame.Color("black"), (size[0]/2, size[1]/2), points[p])


screen.blit(background, (0, 0))
pygame.display.flip()


time.sleep(10)
