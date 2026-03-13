import pygame, sys, random, math
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

WORLD_WIDTH = 2000
WORLD_HEIGHT = 2000

class Food(object):
    def __init__(self, x , y):
        self.x = x
        self.y = y
        self.size = 10
    def is_colliding(self, player):
        dx = self.x - player.x
        dy = self.y - player.y
        distance = math.hypot(dx, dy)  # sqrt(dx^2 + dy^2)
        return distance < (self.size + player.size)

    def draw(self, surface, player):
        # Offset food position relative to player
        draw_x = self.x - player.x + WINDOW_WIDTH // 2
        draw_y = self.y - player.y + WINDOW_HEIGHT // 2
        pygame.draw.circle(surface,(0,128,0), (int(draw_x),int(draw_y)), self.size)

class PlayerCell (object):
    def __init__(self, x , y):
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 0
        self.size = 20
        self.movespeed = 5

    def draw(self, surface):
        # Player is always in the center
        pygame.draw.circle(surface,(128,0,0), (WINDOW_WIDTH//2, WINDOW_HEIGHT//2), self.size)

    def update(self):
        self.x += self.vx
        self.y += self.vy

    def move_right(self): self.vx = self.movespeed
    def move_left(self): self.vx = -self.movespeed
    def move_up(self): self.vy = -self.movespeed
    def move_down(self): self.vy = self.movespeed
    def stop_vx(self): self.vx = 0
    def stop_vy(self): self.vy = 0

def main():
    player = PlayerCell(WORLD_WIDTH/2, WORLD_HEIGHT/2)

    # Generate lots of food randomly in the world
    foods = []
    for _ in range(100):
        fx = random.randint(0, WORLD_WIDTH)
        fy = random.randint(0, WORLD_HEIGHT)
        foods.append(Food(fx, fy))

    looping = True
    while looping:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE: pygame.quit(); sys.exit()
                if event.key == K_RIGHT: player.move_right()
                if event.key == K_LEFT: player.move_left()
                if event.key == K_UP: player.move_up()
                if event.key == K_DOWN: player.move_down()
            if event.type == KEYUP:
                if event.key in (K_RIGHT, K_LEFT): player.stop_vx()
                if event.key in (K_UP, K_DOWN): player.stop_vy()
            if event.type == QUIT: pygame.quit(); sys.exit()

        # Update player
        player.update()

        # Check collisions
        for pellet in foods[:]:
            if pellet.is_colliding(player):
                foods.remove(pellet)
                player.size += 1

        # Draw everything
        WINDOW.fill(BACKGROUND)

        for f in foods:
            f.draw(WINDOW, player)

        player.draw(WINDOW)

        pygame.display.update()
        fpsClock.tick(FPS)

main()