import pygame, sys, random
from pygame.locals import *

pygame.init()

# Colours
BACKGROUND = (0, 0, 0)

# Game Setup
FPS = 30
fpsClock = pygame.time.Clock()
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('BattleFight')

class Food(object):
    def __init__(self, x , y):
        self.x = x
        self.y = y
        self.size = 10

    def draw(self, surface):
        pygame.draw.circle(surface,(0,128,0), (self.x,self.y), self.size)
    def update(self):
        pass
class PlayerCell (object):
    def __init__(self, x , y):
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 0
        self.size = 20
        self.movespeed = 5

        # self.hitbox = (self.x, self.y, self.size, self.size)

    def draw(self, surface):
        pygame.draw.circle(surface,(128,0,0), (self.x,self.y), self.size)

    def update(self):
        self.x+=self.vx
        self.y+=self.vy
    def move_right(self):
        self.vx=self.movespeed
    def move_left(self):
        self.vx=-self.movespeed
    def move_up(self):
        self.vy=-self.movespeed
    def move_down(self):
        self.vy=self.movespeed
    def stop_vx(self):
        self.vx = 0
    def stop_vy(self):
        self.vy = 0
#The main function that controls the game
def main():
    p = PlayerCell(WINDOW_WIDTH/2, WINDOW_HEIGHT/2)
    f = Food(300,300)
    looping = True
    # The main game loop
    while looping:
        # Get inputs
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == K_RIGHT:
                    p.move_right()
                if event.key == K_LEFT:
                    p.move_left()
                if event.key == K_UP:
                    p.move_up()
                if event.key == K_DOWN:
                    p.move_down()
            if event.type == pygame.KEYUP:
                if event.key in (K_RIGHT,K_LEFT):
                    p.stop_vx()
                if event.key in (K_UP,K_DOWN):
                    p.stop_vy()
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        # Processing
        # This section will be built out later

        # Blank Slate
        WINDOW.fill(BACKGROUND)

        # Render elements of the game
        # Draws the Player
        p.update()
        p.draw(WINDOW)

        # Draws the Food Pellets
        # f.update()
        f.draw(WINDOW)

        pygame.display.update()
        fpsClock.tick(FPS)

main()