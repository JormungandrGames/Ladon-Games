import pygame

# SNAKE HEAD VARIABLES
NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3

# SNAKE VARIABLES
SIZE = 10

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
        self.__Snake = [(100, 50), (100, 51), (100, 52), (100, 53), (100, 54), (100, 55), (100, 56), (100, 57)]
        self.__tail_size = 1

    def blit(self):
        for i in self.__Snake:
            rect = (i[0] * SNAKE_SIZE, i[1] * SNAKE_SIZE, SNAKE_SIZE, SNAKE_SIZE)
            pygame.draw.rect(self.__screen, (255, 0, 0), rect)

    def move(self):
        head = self.__Snake[0]
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

        t = self.__Snake[0]
        t = (t[0] + self.__x_pos, t[1] + self.__y_pos)
        self.__Snake.insert(0, t)
        del self.__Snake[-1]
        if self.__Snake[0] in self.__Snake[1:]:
            del self.__Snake[2:]

    def direction(self):
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_UP]:
            self.__direction = NORTH
        elif key_pressed[pygame.K_RIGHT]:
            self.__direction = EAST
        elif key_pressed[pygame.K_DOWN]:
            self.__direction = SOUTH
        elif key_pressed[pygame.K_LEFT]:
            self.__direction = WEST

