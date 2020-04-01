import pygame
from pygame.locals import *
import random

class Enemy(pygame.sprite.Sprite):
    enemy_image = None

    def __init__(self):
        super(Enemy, self).__init__()
        if Enemy.enemy_image == None:
            Enemy.enemy_image = pygame.image.load('assets/missile.png').convert()
            Enemy.enemy_image.set_colorkey((255, 255, 255), RLEACCEL)
        self.image = Enemy.enemy_image
        self.rect = self.image.get_rect(
            center=(random.randint(820, 900), random.randint(0, 600)))
        self.speed = random.randint(4, 8)

    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()
