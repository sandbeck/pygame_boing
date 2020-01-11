import pgzero, pgzrun, pygame
import math, sys, random
from enum import Enum


if sys.version_info < (3,5):
    print("This game requires at least version 3.5 of Python. Please upgrade.")
    sys.exit()

pgzero_version = [int(s) if s.isnumeric() else s
                  for s in pgzero.__version__.split('.')]

if pgzero_version < [1,2]:
    print("This game requires at least version 1.2 of Pygame Zero. Please upgrade")
    sys.exit()


WIDTH = 800
HEIGHT = 480
TITLE = "Boing!"

HALF_WIDTH = WIDTH // 2
HALF_HEIGHT = HEIGHT // 2
PLAYER_SPEED = 6
MAX_AI_SPEED = 6

def normalized(x,y):
    length = math.hypot(x,y)
    return (x / length, y / length)

def sign(x):
    return -1 if x < 0 else 1

class Impact(Actor):
    def __init__(self, pos):
        super().__init__("blank", pos)
        self.time = 0

    def update(self):
        self.image = "impact" + str(self.time // 2)
        self.time += 1

class Ball(Actor):
    def __init__(self, dx):
        super().__init__("ball, (0,0))
        self.x, self.y = HALF_WIDTH, HALF_HEIGHT
        self.dx, self.dy = dx, o
        self.speed = 5

    def update(self)
    