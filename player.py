import pygame
from pygame.locals import *
from sprites import SpriteSheet

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        #sheet = SpriteSheet(pygame.image.load('assets/pug_sheet.png').convert(),32,32)
        sheet = pygame.image.load('assets/pug_sheet.png').convert()
        self.image = pygame.Surface((32, 32)).convert()
        self.image.blit(sheet, (0, 0), (0, 0, 32, 32))
        self.image.set_colorkey((0, 255, 0))
        self.rect = self.image.get_rect()

    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)

        # Keep player on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > 800:
            self.rect.right = 800
        if self.rect.top <= 0:
            self.rect.top = 0
        elif self.rect.bottom >= 600:
            self.rect.bottom = 600
