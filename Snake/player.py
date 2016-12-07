import pygame

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
        
        self.__tail_size = 1

    def blit(self):
        for i in self.__Snake:
            rect = (i[0] * SNAKE_SIZE, i[1] * SNAKE_SIZE, SNAKE_SIZE, SNAKE_SIZE)
            pygame.draw.rect(self.__screen, self.__color, rect)

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

        t = self.__Snake[HEAD]
        t = (t[HEAD] + self.__x_pos, t[1] + self.__y_pos)
        self.__Snake.insert(HEAD, t)
        del self.__Snake[-1]
        if self.__Snake[HEAD] in self.__Snake[1:]:
            del self.__Snake[2:]

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

    def generateApple(self):
        for i in self.__Snake:
            i = self.__Apple.index(Snake[HEAD])

