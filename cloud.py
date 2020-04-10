import pygame
from pygame.locals import *
import random

class Cloud(pygame.sprite.Sprite):
    cloud_image = None

    def __init__(self):
        super(Cloud, self).__init__()
        if Cloud.cloud_image == None:
            Cloud.cloud_image = pygame.image.load('assets/cloud.png').convert()
            Cloud.cloud_image.set_colorkey((0, 0, 0), RLEACCEL)
        self.image = Cloud.cloud_image
        self.rect = self.image.get_rect(center=(
            random.randint(2000, 2200), random.randint(0, 600))
        )
        self.speed = random.randint(400, 550)/100.0

    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()
