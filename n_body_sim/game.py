# Import the pygame module
import pygame
from body import Body
import math
from random import randint
import pickle
# Import pygame.locals for easier access to key coordinates
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    K_SPACE,
    KEYDOWN,
    QUIT,
    K_RETURN
)

# Initialize pygame
pygame.init()

SCREEN_H = 1080
SCREEN_W = 1920
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
SCREENRECT = pygame.Rect(0, 0, SCREEN_W, SCREEN_H)


# create the display surface object
# of specific dimension..e(X, Y).
display_surface = pygame.display.set_mode((SCREEN_W, SCREEN_H))

# set the pygame window name
pygame.display.set_caption('n body gravity')

screen = pygame.display.set_mode((SCREEN_W, SCREEN_H), pygame.SHOWN)

# This will be a list that will contain all the sprites we intend to use in our game.
all = pygame.sprite.Group()

# Array of bodies in format (mass, x, y, vx, vy) showing the earth and moon
bodies = [[5*10**21, 0, 0, 0, 0],
          [5*10**21, 300*10**6, 0, 0, 0]]

for body in bodies:
    all.add(Body(body[0], body[1], body[2], body[3], body[4]))

# The loop will carry on until the user exits the game (e.g. clicks the close button).
carryOn = True

# The clock will be used to control how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while carryOn:
    
    for body in all:
        Fg = [0, 0]
        for other in all:
            if other!= body:
                r = math.sqrt((body.x-other.x)**2 + (body.y-other.y)**2)
                if r!= 0:
                    mFg = ((6.67408*10**-11)*body.mass*other.mass)/(r**2)
                    theta = math.atan2((other.y-body.y), (other.x-body.x))
                    Fg = [mFg*math.cos(theta), mFg*math.sin(theta)]

        body.velocity[0] += Fg[0]/body.mass
        body.velocity[1] += Fg[1]/body.mass

        if body == all.sprites()[0]:
            print(body.velocity)

    all.update()
    # --- Drawing code should go here
    # First, clear the screen to black.

    screen.fill(BLACK)
    # Now let's draw all the sprites in one go. (For now we only have 2 sprites!)
    all.draw(screen)
    pygame.display.update()
    # --- Go ahead and update the screen with what we've drawn.
    clock.tick(60)


