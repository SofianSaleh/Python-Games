import pygame
import sys
import random


class Snake():
    def __init__(self):
        self.length = 1
        self.positions = [((SCREEN_WIDTH/2), (SCREEN_HEIGHT/2))]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        self.color = (17, 24, 47)
        # Special thanks to YouTubers Mini - Cafetos and Knivens Beast for raising this issue!
        # Code adjustment courtesy of YouTuber Elija de Hoog
        self.score = 0


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
