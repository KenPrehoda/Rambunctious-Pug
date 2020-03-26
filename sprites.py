import pygame
from pygame.locals import *

class SpriteSheet():
    def __init__(self,image, sprite_width, sprite_height):
        self.image = image
        self.width = sprite_width
        self.height = sprite_height
    
    def get_sprite_image(self,row,column,image):
        image.blit(self.image, (0,0), (column*self.width,row*self.height,self.width,self.height))
        return image

    def __getitem__(self, key):
        image = pygame.Surface((self.width, self.height)).convert()
        _,_,sheet_width,sheet_height = self.image.get_rect()
        columns = width/self.width
        return None #self.get_sprite_image(key % )

    


def load_image_from_file(name):
    pygame.image.load(name).convert_alpha()

class MovingSprite(pygame.sprite.Sprite):
    def __init__(self, image, x, y, x_speed, y_speed):
        super(MovingSprite, self).__init__()
        self._image = image
        self._image.set_colorkey((0, 0, 0), RLEACCEL)
        self._rect = image.get_rect()
        self._rect.move_ip(x,y)
        self._x_speed = x_speed
        self._y_speed = x_speed

    @property
    def x_speed(self):
        return self._x_speed

    @x_speed.setter
    def x_speed(self, value):
        self._x_speed = value

    @property
    def y_speed(self):
        return self._y_speed

    @y_speed.setter
    def y_speed(self, value):
        self._y_speed = value

    def update(self):
        self.rect.move_ip(self._x_speed, self._x_speed)
