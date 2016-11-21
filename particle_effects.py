import pygame
import random
import math

background_colour = (255, 255, 255)
(width, height) = (300, 200)

class Particle:
    def __init__(self, x, y, size):
        self.__x = x
        self.__y = y
        self.__size = size
        self.__color = (0, 0, 0)
        self.__speed = 0.01
        self.__angle = math.pi / 2

    def display(self):
        pygame.draw.circle(screen, self.__color, (int(self.__x), int(self.__y)), self.__size)

    def move(self):
        self.__x += math.sin(self.__angle) * self.__speed
        self.__y -= math.cos(self.__angle) * self.__speed


screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Tutorial 1')
screen.fill(background_colour)

number_of_particles = 10
particles = []

for n in range(number_of_particles):
    size = random.randint(10, 20)
    x = random.randint(size, width - size)
    y = random.randint(size, width - size)
    particles.append(Particle(x, y, size))

for particle in particles:
    particle.move()
    particle.display()

pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
