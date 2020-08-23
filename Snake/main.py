import pygame
import sys
import random


class Snake():
    def __init__(self):
        self.length = 1
        self.positions = [((SCREEN_WIDTH/2), (SCREEN_HEIGHT/2))]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        self.color = (17, 24, 47)
        self.score = 0

    def get_head_position(self):
        return self.positions[0]

    def turn(self, point):
        if self.length > 1 and (point[0]*-1, point[1]*-1) == self.direction:
            return
        else:
            self.direction = point


# Constants
SCREEN_HEIGHT = 480
SCREEN_WIDTH = 480

GRIDSIZE = 20
GRID_HEIGHT = SCREEN_WIDTH / GRIDSIZE
GRID_WIDTH = SCREEN_HEIGHT / GRIDSIZE

UP = (0, -1)
RIGHT = (1, 0)
LEFT = (-1, 0)
DOWN = (0, 1)
