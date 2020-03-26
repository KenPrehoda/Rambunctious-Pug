# import the pygame module
import pygame
from player import Player
from cloud import Cloud
from enemy import Enemy
from ground import Ground
# import pygame.locals for easier access to key coordinates
from pygame.locals import *
framelock = pygame.time.Clock()

# initialize pygame
pygame.init()
SCREEN_SIZE = (800,600)
# create the screen object
# here we pass it a size of 800x600
screen = pygame.display.set_mode(SCREEN_SIZE)

# Create a custom event for adding a new enemy.
ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 250)
ADDCLOUD = pygame.USEREVENT + 2
pygame.time.set_timer(ADDCLOUD, 1000)

# create our 'player', right now he's just a rectangle
player = Player()

background = pygame.Surface(
    screen.get_size(), pygame.DOUBLEBUF | pygame.HWSURFACE,32)
background.fill((135, 206, 250))

enemies = pygame.sprite.Group()
clouds = pygame.sprite.Group()
ground = Ground(Rect(0,500,800,300),5)
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

running = True

while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False
        elif event.type == ADDENEMY:
            new_enemy = Enemy()
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)
        elif event.type == ADDCLOUD:
            new_cloud = Cloud()
            all_sprites.add(new_cloud)
            clouds.add(new_cloud)
    screen.blit(background, (0, 0))
    pressed_keys = pygame.key.get_pressed()
    player.update(pressed_keys)
    enemies.update()
    clouds.update()
    ground.update()
    ground.draw(screen)
    all_sprites.draw(screen)

    if pygame.sprite.spritecollideany(player, enemies):
        player.kill()

    
    

    pygame.display.flip()
    framelock.tick(60)
