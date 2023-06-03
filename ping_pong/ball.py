import pygame
import numpy
import math
from random import randint

BLACK = (0, 0, 0)
gravity = 0.5


class Ball(pygame.sprite.Sprite):
    # This class represents a ball. It derives from the "Sprite" class in Pygame.
    screenbound = pygame.Rect(0,0,0,0)
    containers = []
    def __init__(self, color, radius):
        # Call the parent class (Sprite) constructor
        super().__init__()
        # Pass in the color of the ball, its width and height.
        # Set the background color and set it to be transparent

        self.bounce_damp = 0.8
        self.image = pygame.Surface([2*radius, 2*radius])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
        # Draw the ball (a rectangle!)
        pygame.draw.circle(self.image,color,[self.image.get_width()//2,self.image.get_width()//2],radius)
        self.mask = pygame.mask.from_surface(self.image.convert_alpha())
        self.radius = radius
        self.velocity = [0, 0]
        self.alive = True
        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()

    def update(self):
        self.velocity[1] -= gravity
        self.rect.x += self.velocity[0]
        self.rect.y -= self.velocity[1]

        if self.rect.right >= self.screenbound.width:
            self.rect.right = self.screenbound.width
            self.velocity[0] *= -1*self.bounce_damp
        if self.rect.left <= 0:
            self.rect.left = 0
            self.velocity[0] *= -1*self.bounce_damp
        if self.rect.top <= 0:
            self.rect.top = 0
            self.velocity[1] *= -1*self.bounce_damp
        if self.rect.bottom > 400:
            self.rect.bottom = 400
            self.velocity[1] *= -1*self.bounce_damp

        self.velocity=math.floor(self.velocity[1])