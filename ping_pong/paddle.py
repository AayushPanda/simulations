import pygame
from pygame.locals import *
from random import randint

WHITE = (255, 255, 255)
gravity = 0.2


class Paddle(pygame.sprite.Sprite):
    screenbound = pygame.Rect(0,0,0,0)
    def __init__(self, origin):
        # Call the parent class (Sprite) constructor
        super().__init__()
        self.bounce_damp = 1
        self.velocity = [0,0]
        self.width = 80
        self.image = pygame.Surface([self.width,8])
        self.image.fill(WHITE)
        self.mask = pygame.mask.from_surface(self.image)
        self.vdirection = 0

        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect(center=origin)

    def move(self, keystate):
        hdirection = -int(keystate[K_LEFT]) + int(keystate[K_RIGHT])
        self.velocity[0] = hdirection * 10

        if int(keystate[K_UP]):
            self.velocity[1] = self.vdirection * 10

    def update(self):
        #self.velocity[1] -= gravity
        self.rect.x += self.velocity[0]
        self.rect.y -= self.velocity[1]

