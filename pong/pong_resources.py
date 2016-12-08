from __future__ import division
import pygame
import operator

PLAYER_ONE = 0
PLAYER_TWO = 1
FILL = 0
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
PADDLE_SHORT = 20
PADDLE_LONG = 165
SCREEN_BUFFER = 75
TOP = 50
MIDDLE = 65


class PongBall:
    def __init__(self, screen):
        self.__radius = 15
        self.__screen = screen
        self.__rect_x = self.__screen.get_rect().centerx
        self.__rect_y = self.__screen.get_rect().centery
        self.__x_position = 11
        self.__y_position = 0

    def display_pong_ball(self):
        pong_ball = pygame.draw.circle(self.__screen, WHITE, (self.__rect_x, self.__rect_y), self.__radius, FILL)
        return pong_ball

    def update_pong_ball(self, paddle_one, paddle_two):

        ball = pygame.Rect(self.__rect_x, self.__rect_y, self.__radius, self.__radius)

        # paddle one collision
        if ball.colliderect(paddle_two.top_rect):
            self.__y_position = self.__x_position
            self.__x_position *= -1
            self.__y_position *= -1
        elif ball.colliderect(paddle_two.mid_rect):
            self.__x_position *= -1
        elif ball.colliderect(paddle_two.bottom_rect):
            self.__y_position = self.__x_position
            self.__x_position *= -1

        # paddle two collision
        if ball.colliderect(paddle_one.top_rect):
            self.__y_position = self.__x_position
            self.__x_position *= -1
        elif ball.colliderect(paddle_one.mid_rect):
            self.__x_position *= -1
        elif ball.colliderect(paddle_one.bottom_rect):
            self.__y_position = self.__x_position
            self.__y_position *= -1
            self.__x_position *= -1

        # screen collision
        if self.__rect_x < self.__screen.get_rect().left:
            self.__rect_x = self.__screen.get_rect().centerx
            self.__rect_y = self.__screen.get_rect().centery
            self.__y_position = 0
            return PLAYER_TWO
        if self.__rect_x > self.__screen.get_rect().right:
            self.__rect_x = self.__screen.get_rect().centerx
            self.__rect_y = self.__screen.get_rect().centery
            self.__y_position = 0
            return PLAYER_ONE
        if self.__rect_y > self.__screen.get_rect().top:
            self.__y_position *= -1
        if self.__rect_y < self.__screen.get_rect().bottom:
            self.__y_position *= -1

        self.__rect_x += self.__x_position
        self.__rect_y += self.__y_position


class Paddle:
    def __init__(self, screen, color, player):
        self.__screen = screen
        self.__color = color
        self.__rect_x = player
        self.__rect_y = self.__screen.get_rect().centery
        self.top_rect = pygame.Rect(self.__rect_x, self.__rect_y, PADDLE_SHORT, TOP)
        self.mid_rect = pygame.Rect(self.__rect_x, self.__rect_y + TOP, PADDLE_SHORT, MIDDLE)
        self.bottom_rect = pygame.Rect(self.__rect_x, self.__rect_y + (TOP + MIDDLE), PADDLE_SHORT, TOP)

    def display_paddle(self):
        paddle = pygame.draw.rect(self.__screen, self.__color, (self.__rect_x, self.__rect_y, PADDLE_SHORT, PADDLE_LONG), FILL)
        return paddle

    def up_paddle(self):
        self.__rect_y -= 7
        self.top_rect = pygame.Rect(self.__rect_x, self.__rect_y, PADDLE_SHORT, TOP)
        self.mid_rect = pygame.Rect(self.__rect_x, self.__rect_y + TOP, PADDLE_SHORT, MIDDLE)
        self.bottom_rect = pygame.Rect(self.__rect_x, self.__rect_y + (TOP + MIDDLE), PADDLE_SHORT, TOP)

    def down_paddle(self):
        self.__rect_y += 7
        self.top_rect = pygame.Rect(self.__rect_x, self.__rect_y, PADDLE_SHORT, TOP)
        self.mid_rect = pygame.Rect(self.__rect_x, self.__rect_y + TOP, PADDLE_SHORT, MIDDLE)
        self.bottom_rect = pygame.Rect(self.__rect_x, self.__rect_y + (TOP + MIDDLE), PADDLE_SHORT, TOP)

