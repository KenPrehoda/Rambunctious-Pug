import pygame
from pygame.locals import *
import random

class Enemy(pygame.sprite.Sprite):
    enemy_image = None

    def __init__(self):
        super(Enemy, self).__init__()
        if Enemy.enemy_image == None:
            Enemy.enemy_image = pygame.image.load('assets/lilkid.png').convert()
            Enemy.enemy_image.set_colorkey((0, 0, 0), RLEACCEL)
        self.image = pygame.transform.scale2x(Enemy.enemy_image)
        self.rect = Rect(2000,830,64,64)
        self.speed = 6.5
        

    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()
