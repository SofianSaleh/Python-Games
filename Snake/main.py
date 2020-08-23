import pygame
import sys
import random


class Snake():
    def __init__(self):
        # Initialize the Snake
        self.length = 1
        self.positions = [((SCREEN_WIDTH/2), (SCREEN_HEIGHT/2))]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        self.color = (17, 24, 47)
        self.score = 0
    # Get the snake position

    def get_head_position(self):
        return self.positions[0]

    # Make the snake turn
    def turn(self, point):
        if self.length > 1 and (point[0]*-1, point[1]*-1) == self.direction:
            return
        else:
            self.direction = point

    # Make the snake Move
    def move(self):
        # Current position
        current_position = self.get_head_position()
        # What direction are you going
        x, y = self.direction
        # New Position
        new_position = (((current_position[0]+(x*GRIDSIZE)) % SCREEN_WIDTH),
               (current_position[1]+(y*GRIDSIZE)) % SCREEN_HEIGHT)
        # Reset the game if the snake intersect
        if len(self.positions) > 2 and new_position in self.positions[2:]:
            self.reset()
        else:
            self.positions.insert(0, new_position)
            if len(self.positions) > self.length:
                self.positions.pop()

    def reset(self):
        # Reset the Snake
        self.length = 1
        self.positions = [((SCREEN_WIDTH/2), (SCREEN_HEIGHT/2))]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        self.score = 0

     def draw(self,surface):
        # Draw the snake Snake

        for p in self.positions:
            r = pygame.Rect((p[0], p[1]), (GRIDSIZE,GRIDSIZE))
            pygame.draw.rect(surface, self.color, r)
            pygame.draw.rect(surface, (93,216, 228), r, 1)

      def handle_keys(self):
        # Handels the keys when pressed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.turn(UP)
                elif event.key == pygame.K_DOWN:
                    self.turn(DOWN)
                elif event.key == pygame.K_LEFT:
                    self.turn(LEFT)
                elif event.key == pygame.K_RIGHT:
                    self.turn(RIGHT)


class Food():
        # Initialize the Food
    def __init__(self):
        self.position = (0, 0)
        self.color = (223, 163, 49)
        self.random_position()

        # Making the food appear in random positions
    def random_position(self):
        self.position = (random.randint(0, GRID_WIDTH - 1) * GRIDSIZE,
                         random.randint(0, GRID_HEIGHT - 1) * GRIDSIZE)

    def draw(self, surface):
        r = pygame.Rect((self.position[0], self.position[1]),
                        (GRIDSIZE, GRIDSIZE))
        pygame.draw.rect(surface, self.color, r)
        pygame.draw.rect(surface, (93, 216, 218), r, 1)

    def draw_grid(surface):
    for y in range(0, int(GRID_HEIGHT)):
        for x in range(0, int(GRID_WIDTH)):
            if (x + y) % 2 == 0:
                r = pygame.Rect((x * GRIDSIZE, y * GRIDSIZE),
                                (GRIDSIZE, GRIDSIZE))
                pygame.draw.rect(surface, (93, 216, 228), r)
            else:
                rr = pygame.Rect((x * GRIDSIZE, y * GRIDSIZE),
                                 (GRIDSIZE, GRIDSIZE))
                pygame.draw.rect(surface, (84, 194, 205), rr)



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


def main():
    # Initializing pygame 
    pygame.init()

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)

    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()

    snake = Snake()
    food = Food()

    myfont = pygame.font.SysFont("monospace",16)

    while (True):
        clock.tick(10)
        # Handeling clicks
        snake.handle_keys()
        # Using the draw function to initialize the gird
        draw_grid(surface)
        snake.move()
        # What happens when the snake and the food intersect
        if snake.get_head_position() == food.position:
            # Increment the length, score, and initialize new food
            snake.length += 1
            snake.score += 1
            food.random_position()
        # draw the food and the snke
        snake.draw(surface)
        food.draw(surface)
        screen.blit(surface, (0, 0))
        # Write text
        text = myfont.render("score {0}".format(snake.score), 1, (0, 0, 0))
        screen.blit(text, (5, 10))
        pygame.display.update()

main()
