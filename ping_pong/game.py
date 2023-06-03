# Import the pygame module
import pygame
from ball import Ball
from paddle import Paddle
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

SCREEN_H = 400
SCREEN_W = 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
SCREENRECT = pygame.Rect(0, 0, SCREEN_W, SCREEN_H)

paddle_force_multiplier = 1

# assigning values to X and Y variable
X = 400
Y = 400

# create the display surface object
# of specific dimension..e(X, Y).
display_surface = pygame.display.set_mode((X, Y))

# set the pygame window name
pygame.display.set_caption('Bouncing ball sim')

# create a font object.
# 1st parameter is the font file
# which is present in pygame.
# 2nd parameter is size of the fon
font = pygame.font.Font('freesansbold.ttf', 32)

score_genned = False

state = 0
"""
0 - Ball on top of paddle
1 - Gameplay
"""

alive = True

# Initialize Class Data

#Paddle.screenbound = SCREENRECT
Ball.screenbound = SCREENRECT

# Create the screen object
# The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
screen = pygame.display.set_mode((SCREEN_W, SCREEN_H), pygame.SHOWN)

#paddle = Paddle((SCREEN_W//2, SCREEN_H - 12))
ball = Ball(RED, 10)

ball.rect.centerx = SCREEN_W // 2
ball.rect.centery = SCREEN_H // 2
ball.velocity = [50,20]


# This will be a list that will contain all the sprites we intend to use in our game.
all = pygame.sprite.Group()

# Add the paddles and the ball to the list of objects
#all.add(paddle)
all.add(ball)

# The loop will carry on until the user exits the game (e.g. clicks the close button).
carryOn = True

# The clock will be used to control how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while carryOn:
    # --- Main event loop

    while ball.alive:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                carryOn = False
                break
        keys = pygame.key.get_pressed()

        # paddle.move(keys)
        # if ball.rect.bottom >= paddle.rect.top and paddle.rect.left <= ball.rect.centerx <= paddle.rect.right:
        #     ball.velocity = [ball.velocity[0]+(paddle.velocity[0] - ball.velocity[0])*0.5, paddle.velocity[1]-ball.velocity[1]*ball.bounce_damp]
        #     ball.rect.y -= 1

        all.update()
        # --- Drawing code should go here
        # First, clear the screen to black.

        screen.fill(BLACK)
        # Now let's draw all the sprites in one go. (For now we only have 2 sprites!)
        all.draw(screen)
        pygame.display.update()
        # --- Go ahead and update the screen with what we've drawn.
        clock.tick(60)
        
#    paddle.rect.center = (SCREEN_W//2, SCREEN_H - 12)
    ball.rect.centerx = SCREEN_W//2
    ball.rect.centery = SCREEN_H//2
    ball.alive = True
    ball.velocity = [0, 0]
    state = 0

