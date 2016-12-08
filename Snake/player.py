import pygame
from random import randint

# SNAKE HEAD VARIABLES
NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3

# SNAKE VARIABLES
SIZE = 10
HEAD = 0

# SPEED VARIABLES
SCREEN_MODIFIER = 1.5
SNAKE_SIZE = 10
SPEED_MODIFIER = 0.01


class Snake:
    def __init__(self, screen, x, y, color):
        self.__speed = SPEED_MODIFIER * ((screen.get_rect().height / SCREEN_MODIFIER) / SNAKE_SIZE)
        self.__x_pos = x
        self.__y_pos = y
        self.__screen = screen
        self.__direction = NORTH
        self.__color = color
        self.__Snake = [(screen.get_rect().centerx / SNAKE_SIZE, 50), (screen.get_rect().centerx / SNAKE_SIZE, 51), (screen.get_rect().centerx / SNAKE_SIZE, 52), (screen.get_rect().centerx / SNAKE_SIZE, 53), (screen.get_rect().centerx / SNAKE_SIZE, 54), (screen.get_rect().centerx / SNAKE_SIZE, 55), (screen.get_rect().centerx / SNAKE_SIZE, 56), (screen.get_rect().centerx / SNAKE_SIZE, 57)]
        self.__Apple = [screen.get_rect().centerx / SNAKE_SIZE, screen.get_rect().centery / SNAKE_SIZE]
        self.__tail_size = 1
        self.__head_rect = pygame.Rect(SNAKE_SIZE, SNAKE_SIZE, SNAKE_SIZE, SNAKE_SIZE)
        self.__score = 0


    def blit(self):
        count = 0
        for i in self.__Snake:
            rect = pygame.Rect(i[0] * SNAKE_SIZE, i[1] * SNAKE_SIZE, SNAKE_SIZE, SNAKE_SIZE)
            pygame.draw.rect(self.__screen, self.__color, rect)
            if count == 0:
                self.__head_rect = rect
                count = 1

        apple_rect = pygame.Rect(self.__Apple[0] * SNAKE_SIZE, self.__Apple[1] * SNAKE_SIZE, SNAKE_SIZE - 1, SNAKE_SIZE - 1)
        pygame.draw.rect(self.__screen, (0, 255, 0), apple_rect)

        if self.__head_rect.colliderect(apple_rect) == 1:
            wallsize = int(self.__screen.get_rect().height / 1.5)
            large_x = (self.__screen.get_rect().centerx + (wallsize / 2) - 100) / SNAKE_SIZE
            small_x = (self.__screen.get_rect().centerx - (wallsize / 2) + 100) / SNAKE_SIZE
            large_y = (self.__screen.get_rect().centery + (wallsize / 2) - 100) / SNAKE_SIZE
            small_y = (self.__screen.get_rect().centery - (wallsize / 2) + 100) / SNAKE_SIZE
            self.__Apple = [randint(small_x, large_x), randint(small_y, large_y)]
            head = self.__Snake[0]
            head = (head[HEAD] + self.__x_pos, head[1] + self.__y_pos)
            self.__Snake.insert(HEAD, head)
            self.__Snake.insert(HEAD, head)
            self.__score += 1
        return self.__head_rect

    def move(self):
        if self.__direction == NORTH:
            self.__x_pos = 0
            self.__y_pos = -self.__speed
        elif self.__direction == EAST:
            self.__x_pos = self.__speed
            self.__y_pos = 0
        elif self.__direction == SOUTH:
            self.__x_pos = 0
            self.__y_pos = self.__speed
        elif self.__direction == WEST:
            self.__x_pos = -self.__speed
            self.__y_pos = 0

        head = self.__Snake[0]
        head = (head[HEAD] + self.__x_pos, head[1] + self.__y_pos)
        self.__Snake.insert(HEAD, head)
        del self.__Snake[-1]

        if self.__Snake[HEAD] in self.__Snake[1:]:
            Snake.kill_snake(self)

    def direction(self):
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_UP] and self.__direction != SOUTH:
            self.__direction = NORTH
        elif key_pressed[pygame.K_RIGHT] and self.__direction != WEST:
            self.__direction = EAST
        elif key_pressed[pygame.K_DOWN] and self.__direction != NORTH:
            self.__direction = SOUTH
        elif key_pressed[pygame.K_LEFT] and self.__direction != EAST:
            self.__direction = WEST

    def kill_snake(self):
        del self.__Snake[2:]
        self.__score = -1

    def score(self):
        return self.__score



