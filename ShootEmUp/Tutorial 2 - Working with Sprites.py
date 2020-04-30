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
img = pygame.image.load(path.join(img_folder, "kirby.png"))
img = pygame.transform.scale(img, (100, 100))



#Game Classes:
class Player(pygame.sprite.Sprite):
    #Settings for the Player:

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT/2)
        self.speed_x = 5
        self.speed_y = 5

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        
        if self.rect.left > WIDTH:
            self.rect.right = 0
        if self.rect.top < 200:
            self.speed_y = 5
        if self.rect.top > 400:
            self.speed_y = -5
        

#Game Functions:


#Game Sprites:
all_sprites = pygame.sprite.Group()
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




            

























    
