import pygame
import random

#Colors:
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

#Settings:
pygame.init()
pygame.mixer.init() #sounds
WIDTH = 600
HEIGHT = 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Shoot em up!")
clock = pygame.time.Clock()
FPS = 60


#Game Classes:


#Game Functions:


#Game Sprites:


#Main Game:
running = True
while running:
    clock.tick(FPS)
    
    #Check for events:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False #exit the game loop


    #Update:
            

    #Draw/Render:
    screen.fill(BLACK)


    #Display the new screen after drawing/updating
    pygame.display.update()

pygame.quit()




            

























    
