import pygame
import random
from os import path

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

#Sounds and Images:
game_folder = path.dirname(__file__)
img_folder = path.join(game_folder, "img")




#Game Classes:
class Player(pygame.sprite.Sprite):
    #Settings for the Player:

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((70, 50)) #dimension (width, height)
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH/2
        self.rect.bottom = HEIGHT - 20
        self.speed_x = 8

    def movement(self):
        #Movement of the ship to the left and right
        self.speed_x = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_RIGHT]:
            self.speed_x = 8
        if keystate[pygame.K_LEFT]:
            self.speed_x = -8
        self.rect.x += self.speed_x

    def boundary(self):
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

    def update(self):
        self.movement()
        self.boundary()
        
        

#Game Functions:



#Game Sprites:
all_sprites = pygame.sprite.Group() #group to contain all the sprites
player = Player()
all_sprites.add(player)


#Main Game:
running = True
while running:
    clock.tick(FPS)
    
    #Check for events:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False #exit the game loop

    #Update:
    all_sprites.update()     

    #Draw/Render:
    screen.fill(BLACK)
    all_sprites.draw(screen)


    #Display the new screen after drawing/updating
    pygame.display.update()

pygame.quit()




            

























    
