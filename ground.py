import pygame
from pygame.locals import *
import random


class GroundTile(pygame.sprite.Sprite):
    def __init__(self,type,rect,speed):
        super(GroundTile, self).__init__()
        self.image = pygame.image.load(f'assets/{type}.png').convert()
        self.image.set_colorkey((0, 0, 0), RLEACCEL)
        self.rect = rect
        self.speed = speed

    def update(self):
        self.rect.move_ip(-self.speed, 0)
        #if self.rect.right < 0:
            #self.kill()


class Ground(pygame.sprite.Group):
    def __init__(self,rect,speed):
        super(Ground, self).__init__()
        self.screen_rect = rect
        self.speed = speed
        x_tiles = int((self.screen_rect.width/16) + 2)
        y_tiles = int((self.screen_rect.height/16) + 1)
        self.group_rect = Rect(self.screen_rect.left,self.screen_rect.top,x_tiles*16,y_tiles*16)
        for y in range(y_tiles):
            for x in range(x_tiles):
                if y == 0:
                    type = 'plant'
                elif y == 1:
                    type = 'grass'
                else:
                    type = 'dirt'
                self.add(GroundTile(type,Rect(16*x+self.screen_rect.left,16*y+self.screen_rect.top,16,16),self.speed))
    
    def update(self):
        self.group_rect.move_ip(-self.speed,0)
        if self.group_rect.right < self.screen_rect.right:
            for ground_tile in self.sprites():
                if ground_tile.rect.right < self.screen_rect.left:
                    ground_tile.rect.move_ip(self.group_rect.width,0)

        super(Ground, self).update()


