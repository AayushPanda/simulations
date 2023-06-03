import pygame
from pygame.locals import *
from random import randint
class Block(pygame.sprite.Sprite):
    screenbound = pygame.Rect(0,0,0,0)
    def __init__(self, origin):
        # Call the parent class (Sprite) constructor
        super().__init__()
        self.image = pygame.Surface([20,20])
        self.color = (randint(127, 255),randint(127, 255),randint(127, 255))
        self.image.fill(self.color)
        pygame.draw.rect(self.image, tuple(map(lambda x: x-40, self.color)), Rect(4, 4, 12, 12))
        self.mask = pygame.mask.from_surface(self.image)

        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect(topleft=origin)
        