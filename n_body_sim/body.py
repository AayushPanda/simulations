import pygame
import numpy
import math
from random import randint

scale = 1
BLACK = (0, 0, 0)


class Body(pygame.sprite.Sprite):
    # This class represents a ball. It derives from the "Sprite" class in Pygame.
    screenbound = pygame.Rect(0,0,0,0)
    containers = []
    def __init__(self, mass, x, y, vx, vy):
        # Call the parent class (Sprite) constructor
        super().__init__()
        # Pass in the color of the ball, its width and height.
        # Set the background color and set it to be transparent

        color = (255,255,255)
        self.radius = 10 #0 * math.sqrt(mass)/10**12
        self.image = pygame.Surface([2*self.radius, 2*self.radius])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
        # Draw the ball (a rectangle!)
        pygame.draw.circle(self.image,color,[self.image.get_width()//2,self.image.get_width()//2],self.radius)

        self.mask = pygame.mask.from_surface(self.image.convert_alpha())
        self.mass = mass
        self.velocity = [vx, vy]
        self.x = x
        self.y = y
        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()
        self.rect.centerx = x/scale
        self.rect.centery = y/scale


    def update(self):
        self.x += self.velocity[0]
        self.y += self.velocity[1]

        self.rect.centerx = 600 + (self.x)/scale
        self.rect.centery = 500 + (self.y)/scale
