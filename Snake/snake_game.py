import pygame
from pause_menu import *
from Snake import player
from Snake import walls

# COLORS CONSTANTS
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
SNAKE_COLOR_H = (255, 0, 0)

# SCREEN, FONT AND MUSIC CONSTANTS
ANTI_ANILIASING = 1
LOOP_MUSIC = -1

SPEED = 10


class Snake:
    def __init__(self, screen):
        self.__screen = screen

        # Running game
        self.__running = True

        # Sounds
        self.__music = pygame.mixer.music.load('Snake/resources/music/BushesLove.ogg')

    def game_loop(self):
        # Loads the music, -1 means loop it forever
        pygame.mixer.music.play(LOOP_MUSIC)

        # Call pause
        pause = Pause(self.__screen)
        pause_options = None
        self.__running = True

        # Snake Objects
        snake = player.Snake(self.__screen, self.__screen.get_rect().centerx,
                                  self.__screen.get_rect().centery, SNAKE_COLOR_H)
        game_walls = walls.BuildWalls(self.__screen)

        # snake_head.tail()
        k = 1
        # Game Loop
        while self.__running:
            # Clears the screen and fills it with color (black)
            self.__screen.fill(BLACK)

            # Blit the Snake and walls
            head_rect = snake.blit()
            walls_rect = game_walls.blit()

            # Gets users buttons events
            snake.direction()

            # Moves the snake; Don't change this speed to move faster
            k += 1
            if k % SPEED == 0:
                snake.move()

            for i in walls_rect:
                if i.colliderect(head_rect):
                    snake.kill_snake()

            score = snake.score()

            if score == -1:
                # Snake Objects
                snake_head = player.Snake(self.__screen, self.__screen.get_rect().centerx,
                                          self.__screen.get_rect().centery, SNAKE_COLOR_H)
                game_walls = walls.BuildWalls(self.__screen)

            # Get mouse clicks
            mouse_pos = pygame.mouse.get_pos()
            (on_click1, on_click2, on_click3) = pygame.mouse.get_pressed()

            # On mouse and keyboard events
            for event in pygame.event.get():
                # Hit quit
                if event.type == pygame.QUIT:
                    self.__running = False
                # Get escape key press for menu; COPY THIS BLOCK FOR PAUSE MENU
                elif pygame.key.get_pressed()[pygame.K_ESCAPE]:
                    pause_options = pause.pause_loop()
                    if pause_options == 0:
                        self.__running = False
                        return True
                    elif pause_options == 1:
                        self.__running = False

            # Updates the screen
            pygame.display.update()
