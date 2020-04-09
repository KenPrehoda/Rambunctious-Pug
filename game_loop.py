# import the pygame module
import pygame
from player import Player
from cloud import Cloud
from ground import Ground
# import pygame.locals for easier access to key coordinates
from pygame.locals import *
framelock = pygame.time.Clock()

# initialize pygame
pygame.init()
SCREEN_SIZE = (1920,1080)
screen = pygame.display.set_mode(SCREEN_SIZE,
                                 flags=pygame.FULLSCREEN | pygame.DOUBLEBUF | pygame.HWSURFACE)

# Create a custom event for adding a new (anything)_
ADDCLOUD = pygame.USEREVENT + 2
pygame.time.set_timer(ADDCLOUD, 1000)

# create our 'player', right now he's just a rectangle
player = Player()

background = pygame.Surface(
    screen.get_size(), pygame.DOUBLEBUF | pygame.HWSURFACE,32)
background.fill((135, 206, 250))

clouds = pygame.sprite.Group()
ground = Ground(screen.get_rect(), Rect(0,660,1920,300),5)
player_group = pygame.sprite.Group()
player_group.add(player)
running = True

while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False
        elif event.type == ADDCLOUD:
            new_cloud = Cloud()
            clouds.add(new_cloud)
    screen.blit(background, (0, 0))
    pressed_keys = pygame.key.get_pressed()
    player.update(pressed_keys)
    clouds.update()
    ground.update()
    ground.draw(screen)
    clouds.draw(screen)
    player_group.draw(screen)


    
    

    pygame.display.flip()
    framelock.tick(60)
