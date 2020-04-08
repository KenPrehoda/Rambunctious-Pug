import pygame
from pygame.locals import *
import random


class GroundTile(pygame.sprite.Sprite):
    def __init__(self,type,rect,speed):
        super(GroundTile, self).__init__()
        self.image = pygame.image.load(f'assets/{type}.png').convert_alpha()
        #self.image.set_colorkey((0, 0, 0), RLEACCEL)
        self.rect = rect
        self.speed = speed

    def update(self):
        self.rect.move_ip(-self.speed, 0)


class Ground(pygame.sprite.Group):
    def __init__(self,rect,speed):
        super(Ground, self).__init__()
        self.screen_rect = rect
        self.speed = speed
        randdirt = ["dirt","dirt2","dirt3"]
        randgrass = ["grass","grass2","grass3"]
        randplant = ["plant","plant 2","plant 3"]
        x_tiles = int((self.screen_rect.width/16) + 2)
        y_tiles = int((self.screen_rect.height/16) + 1)
        self.group_rect = Rect(self.screen_rect.left,self.screen_rect.top,x_tiles*16,y_tiles*16)
        for y in range(y_tiles):
            for x in range(x_tiles):
                if y == 0:
                    if random.randint(1,10) > 8:
                        type = randplant[random.randint(0, len(randplant)-1)]
                    else:
                        type = None
                elif y == 1:
                    type = randgrass[random.randint(0,len(randgrass)-1)]
                else:
                    type = randdirt[random.randint(0, len(randdirt)-1)]
                if type:
                    self.add(GroundTile(type,Rect(16*x+self.screen_rect.left,16*y+self.screen_rect.top,16,16),self.speed))
    
    def update(self):
        self.group_rect.move_ip(-self.speed,0)
        if self.group_rect.right < self.screen_rect.right:
            for ground_tile in self.sprites():
                if ground_tile.rect.right < self.screen_rect.left:
                    ground_tile.rect.move_ip(self.group_rect.width,0)

        super(Ground, self).update()


