import pygame
import math
import time

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)

pygame.init()
dis = pygame.display.set_mode((400, 300))
pygame.display.update()
pygame.display.set_caption('Snake game by Edureka')
game_over = False


center = (200, 150)
radius = 100
angle = 0

while not game_over:
    for event in pygame.event.get():
        print(event)  # prints out all the actions that take place on the screen
        if event.type == pygame.QUIT:
            game_over=True
    dis.fill(white)
    pygame.draw.circle(dis, blue, center, radius, 1)
    center2 = ( int(center[0] + radius * math.cos(angle)), int(center[1] + radius * math.sin(angle)))
    pygame.draw.circle(dis, blue, center2, 10, 1)
    #############pygame.draw.rect(dis, blue, [200, 150, 10, 10])
    pygame.display.update()
    angle += 0.01
    time.sleep(0.01)
pygame.quit()
print(math.acos(-1))
quit()