import pygame
from pygame.locals import *
from sprites import SpriteSheet
from itertools import cycle

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        #sheet = SpriteSheet(pygame.image.load('assets/pug_sheet.png').convert(),32,32)
        sheet = pygame.image.load('assets/pug_sheet.png').convert()
        tiles = ((0, 0),(0, 32),(0, 64),(0, 96),(32, 0),(32, 32))
        self.images = []
        for i in range(6):
            image = pygame.Surface((32, 32)).convert()
            image.blit(sheet,(0,0),(*tiles[i],32,32))
            image.set_colorkey((0, 174, 0))
            self.images.append(image)
        self.cur_image = cycle(self.images)
        self.image = next(self.cur_image)
        self.rect = Rect(375,550,32,32)
        self.vertical_movement = None
        self.ticks = pygame.time.get_ticks()

    def update(self, pressed_keys):
        ticks = pygame.time.get_ticks()
        if ticks > self.ticks + 100:
            self.ticks = ticks
            self.image = next(self.cur_image)

        if pressed_keys[K_UP]:
            if not self.vertical_movement:
                self.vertical_movement = -5
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)
        if self.vertical_movement:    
            self.vertical_movement += 0.2
            self.rect.move_ip(0, self.vertical_movement)
            if self.rect.bottom >= 523:
                self.vertical_movement=None
                
        # Keep player on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > 800:
            self.rect.right = 800
        if self.rect.top <= 0:
            self.rect.top = 0
        elif self.rect.bottom >= 523:
            self.rect.bottom = 523
