import pygame
from pygame.locals import *
import random

dirt_tiles = ["dirt", "dirt2", "dirt3"]
grass_tiles = ["grass", "grass2", "grass3"]
plant_tiles = ["plant", "plant 2", "plant 3"]

tiles = ("dirt", "dirt2", "dirt3", "grass", "grass2", "grass3", "plant", "plant 2", "plant 3")

class GroundTile(pygame.sprite.Sprite):
    ground_tiles = None
    def __init__(self,type,rect,speed):
        super(GroundTile, self).__init__()
        GroudTile.load_tiles()
 
        self.image = GroundTile.ground_tiles[type]
        #self.image.set_colorkey((0, 0, 0), RLEACCEL)
        self.rect = rect
        self.speed = speed

    @staticmethod
    def load_tiles():
        if GroundTile.ground_tiles == None:
            unscaled = {i:
            pygame.transform.scale2x(pygame.image.load(f'assets/{i}.png').convert_alpha()) for i in tiles}
            GroundTile.ground_tiles = unscaled
           #GroundTile.ground_tiles = {k:
            #    pygame.transform.smoothscale(v,(64,64)) for (k, v) in unscaled.items()}

    def update(self):
        self.rect.move_ip(-self.speed, 0)


class FlatChunk(pygame.sprite.Sprite):
    def __init__(self, rect):
        super(FlatChunk, self).__init__()
        self.image = pygame.Surface([rect.width, rect.height])
        self.image.set_colorkey((0, 0, 0), RLEACCEL)
        self.rect = rect
        GroundTile.load_tiles()
        tile_dimension = GroundTile.ground_tiles['dirt'].get_rect().width
        x_tiles = int((self.rect.width/tile_dimension)+1)
        y_tiles = int((self.rect.height/tile_dimension) + 1)
        for y in range(y_tiles):
            for x in range(x_tiles):
                tile = None
                if y == 0:
                    if random.randint(1,10) > 8:
                        tile = GroundTile.ground_tiles[plant_tiles[random.randint(
                            0, len(plant_tiles)-1)]]
                    else:
                        tile = None
                elif y == 1:
                    tile = GroundTile.ground_tiles[grass_tiles[random.randint(
                        0, len(grass_tiles)-1)]]
                else:
                    tile = GroundTile.ground_tiles[dirt_tiles[random.randint(
                        0, len(dirt_tiles)-1)]]
                if tile:
                    self.image.blit(tile, Rect(
                        tile_dimension*x, tile_dimension*y, tile_dimension, tile_dimension))

class Ground(pygame.sprite.Group):
    def __init__(self,screen,ground_surface_bound,speed):
        '''Routine for dynamically generating ground with up and down ramps
        screen:                 the screen rect
        ground_surface_bound:   rect that determines the vertical range the ground should span
        speed:                  speed at which the ground moves''' 
        super(Ground, self).__init__()
        self.screen_rect = screen
        self.surface_bound_rect = ground_surface_bound
        self.speed = speed
        print(screen, ground_surface_bound)
        self.add(FlatChunk(Rect(screen.left, self.surface_bound_rect.top + \
            self.surface_bound_rect.height, screen.width*1.25, \
            screen.top + screen.height-(self.surface_bound_rect.top + \
            self.surface_bound_rect.height))))
    
    def update(self):
        furthest_right = 0
        for s in self.sprites():
            s.rect.move_ip(-self.speed, 0)
            if s.rect.right > furthest_right:
                furthest_right = s.rect.right
            if s.rect.right < 0:
                s.kill()
        if furthest_right < self.screen_rect.right:
            self.add(FlatChunk(Rect(self.screen_rect.right-(self.speed+1), self.surface_bound_rect.top +
                                    self.surface_bound_rect.height, self.screen_rect.width/2,
                                    self.screen_rect.top + self.screen_rect.height-(self.surface_bound_rect.top +
                                                                self.surface_bound_rect.height))))

        super(Ground, self).update()


